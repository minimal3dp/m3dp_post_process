# Phase 2 ACO Optimization Roadmap

**Target**: Additional 40-60% speedup + 50-70% memory reduction
**Timeline**: 2-4 weeks implementation + validation
**Research Foundation**: Fok et al. (2019), Skinderowicz (2012, 2022), Lin et al. (2024)

---

## Executive Summary

Phase 1 delivered 66% speedup (5m 12s → 1m 45s) through:
- ✅ MMAS pheromone bounds
- ✅ Candidate lists
- ✅ Early termination
- ✅ ACS pseudo-random rule

Phase 2 will implement **3D printing-specific optimizations** from the Fok et al. paper (our original research basis) that we didn't include in Phase 1. The centerpiece is **Segment Integration**, which dynamically shrinks the graph as the algorithm learns which segments are always traversed together.

### Expected Phase 2 Results

| Metric | Current (Phase 1) | Phase 2 Target | Total Improvement |
|--------|-------------------|----------------|-------------------|
| **Processing Time** | 1m 45s | **40-60s** | **87% faster than baseline** |
| **Memory Usage** | ~200MB (45K nodes) | **60-100MB** | 50-70% reduction |
| **Max File Size** | ~50K segments | **100K+ segments** | 2x capacity increase |
| **Quality** | 33.8% travel reduction | 34-36% | Maintained or improved |

---

## Phase 2 Priorities

### Tier 1: Core Optimizations (Implement First)

#### 1. 🔥 Segment Integration (HIGHEST PRIORITY)

**Research Basis**: Fok et al. (2019) Section IV.C - "Modified ACO with Segment Integration"

##### Problem Statement
G-code for curved surfaces is tessellated into hundreds of tiny connected line segments. For example, a circular arc might be 50 segments of 0.1mm each. Standard ACO treats these as 50 independent decisions, wasting computation on "should I print segment 23 or 24 next?" when they're always printed together.

##### Solution: Dynamic Graph Shrinkage
1. **Identify STS Patterns**: After each iteration, detect "Segment-Transition-Segment" groups that are frequently traversed together (high pheromone on both segments and their transition).
2. **Probabilistic Merging**: With probability proportional to pheromone strength, merge STS into a single "super-segment".
3. **Graph Reduction**: Problem size N shrinks from (e.g.) 5000 → 2000 → 800 over iterations.
4. **Accelerating Returns**: As N decreases, each iteration becomes faster, creating positive feedback.

##### Implementation Strategy

**New Data Structures**:
```python
@dataclass
class SuperSegment:
    """A merged group of segments that are always traversed together."""
    id: str  # e.g., "SS_123"
    original_segments: List[Segment]  # The constituent segments
    start: Point  # Start of first segment
    end: Point    # End of last segment
    length: float  # Total length of all segments

@dataclass
class SegmentGraph:
    """Manages both raw segments and super-segments."""
    segments: List[Segment]
    super_segments: Dict[str, SuperSegment]
    segment_to_super: Dict[int, str]  # Map segment index to super-segment ID
```

**New ACOConfig Parameters**:
```python
@dataclass
class ACOConfig:
    # ... existing parameters ...

    # Segment Integration parameters
    enable_segment_integration: bool = True
    """Enable dynamic segment merging"""

    integration_threshold: float = 0.7
    """Pheromone threshold for considering STS merge (0-1)"""

    integration_probability: float = 0.3
    """Probability of merging qualifying STS (theta parameter)"""

    min_integration_iteration: int = 2
    """Don't integrate before this iteration (let pheromone stabilize)"""
```

**Algorithm Flow**:
```python
def optimize(self) -> OptimizationResult:
    """Main ACO loop with segment integration."""

    # Initialize with raw segments
    graph = SegmentGraph(segments=self.segments)

    for iteration in range(self.config.num_iterations):
        # Build ant solutions on current graph
        solutions = self._run_ants(graph)

        # Update pheromones
        self._update_pheromones(graph, solutions)

        # Integrate segments (after warmup iterations)
        if (self.config.enable_segment_integration and
            iteration >= self.config.min_integration_iteration):
            graph = self._integrate_segments(graph)
            logger.info(f"Graph reduced to {len(graph.active_nodes)} nodes")

        # Early termination check
        if self._check_early_termination():
            break

    # Expand super-segments back to raw segments for output
    return self._expand_solution(best_solution, graph)
```

**Core Integration Logic**:
```python
def _integrate_segments(self, graph: SegmentGraph) -> SegmentGraph:
    """Identify and merge high-pheromone STS patterns."""

    candidates = []

    # Find STS patterns: seg1 -> transition -> seg2
    for seg1_id in graph.active_segments:
        for seg2_id in graph.active_segments:
            if seg1_id == seg2_id:
                continue

            # Check if seg1.end connects to seg2.start (spatial adjacency)
            if not self._are_spatially_adjacent(graph[seg1_id], graph[seg2_id]):
                continue

            # Check pheromone strength on both segments
            tau1 = self.pheromone[seg1_id, next_of_seg1]
            tau2 = self.pheromone[prev_of_seg2, seg2_id]

            if (tau1 > self.config.integration_threshold * self.tau_max and
                tau2 > self.config.integration_threshold * self.tau_max):
                candidates.append((seg1_id, seg2_id, min(tau1, tau2)))

    # Sort by pheromone strength (merge strongest patterns first)
    candidates.sort(key=lambda x: x[2], reverse=True)

    # Probabilistically merge
    for seg1_id, seg2_id, strength in candidates:
        if random.random() < self.config.integration_probability:
            graph.merge_segments(seg1_id, seg2_id)

    return graph
```

##### Expected Impact
- **Time**: 30-40% faster (Fok et al. measured 34.9%)
- **Memory**: Pheromone matrix size ∝ N², so 50% node reduction = 75% memory reduction
- **Quality**: Same or better (fewer decision points = less noise)

##### Testing Strategy
1. **Unit test**: Verify merge logic on simple 4-segment square
2. **Integration test**: Run on real Benchy file, validate graph size reduction
3. **Regression test**: Ensure output G-code is functionally identical
4. **Performance test**: Measure time improvement on 3 file sizes (small/medium/large)

##### Success Criteria
- [ ] Graph size reduces by 40-60% over iterations
- [ ] Total processing time reduces by 30-40%
- [ ] Output travel distance within 1% of non-integrated result
- [ ] All existing tests pass

##### Implementation Complexity: **Medium** (2-3 days)

---

#### 2. Selective Pheromone Memory

**Research Basis**: Skinderowicz (2012, 2022) - Sparse pheromone storage

##### Problem Statement
For a 45K-node problem, full pheromone matrix is:
- **Size**: 45,000 × 45,000 = 2.025 billion floats
- **Memory**: 2.025B × 8 bytes = 16.2 GB (!!!!)

Current implementation uses NumPy matrices which pre-allocate this space. Even with candidate lists limiting *computation*, we still store the full matrix.

##### Solution: Sparse Storage
Only store pheromone values for:
1. Edges in candidate lists (k × N edges, where k=25)
2. Edges with pheromone > τ₀ + ε (significantly above baseline)
3. All others assumed to have default value τ₀

##### Implementation Strategy

**Replace NumPy matrix with sparse structure**:
```python
from scipy.sparse import lil_matrix, csr_matrix
from collections import defaultdict

class SparsePheromoneMatrix:
    """Memory-efficient pheromone storage."""

    def __init__(self, n: int, tau0: float):
        self.n = n
        self.tau0 = tau0  # Default value for unstored edges

        # Use lil_matrix for construction, csr_matrix for access
        self._matrix = lil_matrix((n, n), dtype=np.float32)
        self._initialized = False

    def set(self, i: int, j: int, value: float):
        """Set pheromone value."""
        # Only store if significantly different from tau0
        if abs(value - self.tau0) > 1e-6:
            self._matrix[i, j] = value
        elif self._initialized:
            # Evaporated back to baseline, remove from storage
            self._matrix[i, j] = 0  # sparse matrices auto-delete zeros

    def get(self, i: int, j: int) -> float:
        """Get pheromone value (returns tau0 if not stored)."""
        value = self._matrix[i, j]
        return value if value != 0 else self.tau0

    def finalize_construction(self):
        """Convert to CSR for fast row-based access."""
        self._matrix = self._matrix.tocsr()
        self._initialized = True

    def memory_usage_mb(self) -> float:
        """Actual memory consumption."""
        return self._matrix.data.nbytes / (1024**2)
```

**Update ACOOptimizer to use sparse matrices**:
```python
class ACOOptimizer:
    def __init__(self, segments: List[Segment], config: Optional[ACOConfig] = None):
        self.segments = segments
        self.config = config or ACOConfig()

        # Use sparse matrix if enabled
        if self.config.use_sparse_pheromone:
            self.pheromone = SparsePheromoneMatrix(
                n=len(segments),
                tau0=self.config.initial_pheromone
            )
        else:
            # Legacy full matrix
            self.pheromone = np.full(
                (len(segments), len(segments)),
                self.config.initial_pheromone
            )
```

##### Expected Impact
- **Memory**: 200MB → 60-80MB (60-70% reduction)
- **Time**: 0-5% faster (better cache locality)
- **Capacity**: Can handle 100K+ segment files

##### Testing Strategy
1. **Unit test**: Verify sparse matrix get/set behavior matches dense
2. **Memory test**: Measure actual RAM usage with profiler
3. **Performance test**: Ensure no speed regression
4. **Large file test**: Process 100K segment synthetic file

##### Success Criteria
- [ ] Memory usage < 100MB for 45K-node problem
- [ ] Processing time within 5% of dense matrix version
- [ ] Can process 100K-segment file without OOM

##### Implementation Complexity: **Medium** (2-3 days)

---

### Tier 2: Advanced Optimizations (After Tier 1)

#### 3. K-means Pre-Clustering (For Very Large Files)

**Research Basis**: Lin et al. (2024)

##### When to Apply
Only for layers with >5,000 segments. Below that, standard ACO is efficient enough.

##### Strategy
```python
def _optimize_large_layer(self, segments: List[Segment]) -> List[Segment]:
    """Use hierarchical clustering for large layers."""

    # 1. Cluster segments spatially (K-means)
    n_clusters = max(5, len(segments) // 1000)  # ~1000 segments/cluster
    clusters = self._kmeans_cluster(segments, n_clusters)

    # 2. Optimize cluster visiting order (TSP with cluster centroids)
    cluster_order = self._aco_tsp([c.centroid for c in clusters])

    # 3. Optimize within each cluster (URPP)
    optimized_segments = []
    for cluster_id in cluster_order:
        cluster_segs = self._aco_urpp(clusters[cluster_id].segments)
        optimized_segments.extend(cluster_segs)

    return optimized_segments
```

##### Expected Impact
- **Time**: 40-60% faster for >10K segment layers
- **Quality**: 95-98% as good as full ACO (slight loss due to cluster boundaries)

##### Implementation Complexity: **High** (4-5 days)

---

#### 4. Multi-Population Strategy

**Research Basis**: Deng et al. (2019)

##### Strategy
Split ants into two populations:
- **Elite ants** (30%): Start from best-known solution, do local optimization (2-opt moves)
- **Common ants** (70%): Standard ACO exploration

##### Expected Impact
- **Time**: 20-30% faster due to better exploitation
- **Quality**: Improved by 5-10%

##### Implementation Complexity: **Low** (1-2 days)

---

#### 5. Local Pheromone Decay (Full ACS)

**Research Basis**: Dorigo & Gambardella (1997) - ACS variant

##### Current State
We use ACS pseudo-random-proportional rule (q0 parameter) but NOT local pheromone decay.

##### Full ACS Implementation
```python
def _construct_tour(self, ...):
    """Build tour with local pheromone decay."""

    for step in range(n):
        next_node = self._choose_next(current, ...)
        tour.append(next_node)

        # LOCAL PHEROMONE DECAY (new)
        # Immediately reduce pheromone on traversed edge
        edge = (current, next_node)
        self.pheromone[edge] = (1 - self.config.xi) * self.pheromone[edge]

        current = next_node
```

##### Expected Impact
- **Quality**: 10-15% improvement (less "follow the leader")
- **Time**: Neutral or slight improvement

##### Implementation Complexity: **Low** (1 day)

---

## Implementation Timeline

### Week 1-2: Tier 1 Implementation
- **Days 1-3**: Segment Integration
  - [ ] Implement `SegmentGraph` and `SuperSegment` classes
  - [ ] Implement `_integrate_segments()` method
  - [ ] Implement `_expand_solution()` for output conversion
  - [ ] Unit tests for merge logic

- **Days 4-6**: Selective Pheromone Memory
  - [ ] Implement `SparsePheromoneMatrix` class
  - [ ] Refactor ACOOptimizer to use sparse matrices
  - [ ] Memory profiling and validation
  - [ ] Unit tests for sparse operations

- **Days 7-10**: Integration Testing & Validation
  - [ ] Run full test suite (must pass 51/51 tests)
  - [ ] Benchmark on 3 file sizes (small/medium/large)
  - [ ] Profile memory usage
  - [ ] Document performance improvements

### Week 3-4: Tier 2 (Optional)
- **Days 11-15**: K-means Clustering (if needed for large files)
- **Days 16-18**: Multi-Population Strategy
- **Days 19-20**: Local Pheromone Decay

---

## Testing & Validation Plan

### Unit Tests (New)
```python
# tests/test_segment_integration.py
def test_sts_detection():
    """Verify STS pattern detection."""

def test_segment_merge():
    """Verify merge creates correct super-segment."""

def test_graph_reduction():
    """Verify graph size shrinks over iterations."""

def test_solution_expansion():
    """Verify super-segments expand to original segments."""

# tests/test_sparse_pheromone.py
def test_sparse_get_set():
    """Verify sparse matrix matches dense behavior."""

def test_memory_usage():
    """Verify memory reduction."""
```

### Integration Tests (Enhanced)
```python
# tests/test_aco_optimizer.py (add to existing)
def test_segment_integration_benchy():
    """Test integration on real Benchy file."""
    # Should reduce graph size by 40-60%
    # Should maintain solution quality within 1%

def test_sparse_pheromone_performance():
    """Ensure sparse matrix doesn't slow down optimization."""
    # Time difference should be < 5%
```

### Performance Benchmarks
```python
# tests/benchmark_phase2.py (new)
def benchmark_segment_integration():
    """Measure time improvement from integration."""

def benchmark_memory_usage():
    """Measure RAM reduction from sparse matrices."""

def benchmark_large_file():
    """Test 100K-segment file (synthetic)."""
```

---

## Success Metrics

### Performance Targets

| Metric | Phase 1 Baseline | Phase 2 Target | Measurement Method |
|--------|------------------|----------------|-------------------|
| **Time (3.3MB Benchy)** | 1m 45s | **40-60s** | `time` command |
| **Memory (45K nodes)** | ~200MB | **60-100MB** | `memory_profiler` |
| **Graph Size Reduction** | N/A | **40-60%** | Log output |
| **Solution Quality** | 33.8% travel reduction | **33-36%** | Compare output distances |

### Quality Assurance

- [ ] **Zero Regressions**: All 51 existing tests pass
- [ ] **Functional Equivalence**: Output G-code produces same physical result (visual inspection)
- [ ] **Backward Compatible**: Phase 2 features can be disabled via config flags
- [ ] **Documentation**: Code comments explain Segment Integration algorithm
- [ ] **Research Citations**: Fok et al. (2019) cited in docstrings

---

## Risk Assessment & Mitigation

### Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Segment Integration breaks output** | Medium | High | Extensive unit tests, visual validation of prints |
| **Sparse matrices slower than dense** | Low | Medium | Benchmark before full integration, keep dense option |
| **Graph reduction too aggressive** | Medium | Medium | Tunable θ parameter, conservative defaults |
| **Memory savings less than expected** | Low | Low | Profile early, adjust approach if needed |

### Schedule Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Integration logic more complex** | Medium | Medium | Start with simple merge rules, iterate |
| **Testing takes longer than expected** | High | Low | Parallelize test execution, automate benchmarks |

---

## Configuration Interface

Users will control Phase 2 features via expanded `ACOConfig`:

```python
@dataclass
class ACOConfig:
    # Phase 1 parameters (existing)
    num_ants: int = 8
    num_iterations: int = 8
    use_mmas: bool = True
    use_candidate_lists: bool = True
    candidate_list_size: int = 25
    enable_early_termination: bool = True
    stagnation_limit: int = 15

    # PHASE 2: Segment Integration
    enable_segment_integration: bool = True
    integration_threshold: float = 0.7  # Pheromone threshold for merge
    integration_probability: float = 0.3  # Theta parameter
    min_integration_iteration: int = 2  # Warmup period

    # PHASE 2: Sparse Pheromone Memory
    use_sparse_pheromone: bool = True
    sparse_threshold: float = 1e-6  # Only store if |τ - τ₀| > threshold

    # PHASE 2: K-means Clustering (optional)
    enable_clustering: bool = False  # Only for very large layers
    clustering_threshold: int = 5000  # Min segments to trigger clustering
    cluster_size_target: int = 1000  # Target segments per cluster
```

### User-Facing Presets

```python
# Conservative (maximum quality, slower)
ACOConfig.conservative_preset()  # All Phase 2 disabled

# Balanced (default)
ACOConfig.balanced_preset()  # Segment Integration + Sparse Memory

# Aggressive (maximum speed, slight quality loss)
ACOConfig.aggressive_preset()  # All Phase 2 enabled including clustering
```

---

## Documentation Updates

### Files to Update

1. **`ACO_PERFORMANCE_IMPROVEMENTS.md`** (✅ Already updated)
   - Added Phase 2 references
   - Added Segment Integration as priority

2. **`README.md`**
   - Update feature list to mention Phase 2 optimizations
   - Update performance metrics to reflect new targets

3. **`m3dp_post_process/aco_optimizer.py`** (docstrings)
   - Explain Segment Integration algorithm
   - Document sparse pheromone matrix rationale
   - Add Fok et al. citations

4. **`.github/copilot-instructions.md`**
   - Update with Phase 2 architecture details
   - Document SegmentGraph and SuperSegment data structures

---

## Expected Deliverables

### Code
- [ ] `SegmentGraph` class in `aco_optimizer.py`
- [ ] `SuperSegment` dataclass
- [ ] `SparsePheromoneMatrix` class
- [ ] `_integrate_segments()` method
- [ ] `_expand_solution()` method
- [ ] Updated `ACOConfig` with Phase 2 parameters

### Tests
- [ ] `tests/test_segment_integration.py` (8-10 tests)
- [ ] `tests/test_sparse_pheromone.py` (5-8 tests)
- [ ] Updated `tests/test_aco_optimizer.py` (add 5 integration tests)
- [ ] `tests/benchmark_phase2.py` (performance measurement)

### Documentation
- [x] `PHASE_2_ROADMAP.md` (this document)
- [x] Updated `ACO_PERFORMANCE_IMPROVEMENTS.md`
- [ ] Updated `README.md` with Phase 2 performance metrics
- [ ] Code comments and docstrings

### Validation
- [ ] Benchmark report (Markdown table with times/memory)
- [ ] Memory profiling results (before/after charts)
- [ ] Visual validation photos (printed test parts)

---

## Conclusion

Phase 2 focuses on **3D printing-specific optimizations** from the original Fok et al. research. By implementing Segment Integration and Selective Pheromone Memory, we expect to:

- **Reduce processing time** from 1m 45s to 40-60s (additional 40-60% improvement)
- **Reduce memory usage** by 50-70% (200MB → 60-100MB)
- **Enable larger files** (support 100K+ segments)
- **Maintain quality** (within 1% of current results)

The implementation is well-researched, proven by peer-reviewed papers, and designed with backward compatibility and incremental deployment in mind. Success will position m3dp_post_process as the leading open-source G-code optimizer for 3D printing.

---

**Document Version**: 1.0
**Date**: November 24, 2025
**Author**: Minimal3DP Development Team
**Status**: Planning - Ready for Implementation
**Repository**: [github.com/minimal3dp/m3dp_post_process](https://github.com/minimal3dp/m3dp_post_process)

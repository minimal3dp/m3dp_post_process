# 

**Source:** `An_effective_ant_colony_optimization_alg.pdf`
---

## Page 1

An eﬀective ant colony optimization algorithm (ACO) for
multi-objective resource allocation problem (MORAP)
S.K. Chaharsooghi *, Amir H. Meimand Kermani
Department of Industrial Engineering, School of Engineering, Tarbiat Modares University, Iran
Abstract
The multi-objective resource allocation problem (MORAP) addresses the important issue which seeks to ﬁnd the
expected objectives by allocating the limited amount of resource to various activates. Resources may be manpower, assets,
raw material or anything else in limited supply which can be used to accomplish the goals. The goals may be objectives (i.e.,
minimizing costs, or maximizing eﬃciency) usually driven by speciﬁc future needs. In this paper, in order to obtain a set of
Pareto solution eﬃciently, we proposed a modiﬁed version of ant colony optimization (ACO), in this algorithm we try to
increase the eﬃciency of algorithm by increasing the learning of ants. Eﬀectiveness and eﬃciency of proposed algorithm
was validated by comparing the result of ACO with hybrid genetic algorithm (hGA) which was applied to MORAP later.
 2007 Elsevier Inc. All rights reserved.
Keywords: Ant colony optimization; Multi-objective optimization model; Multi-objective resources allocation problem (MORAP)
1. Introduction
Multi-objective optimization problems have received increased interest from researchers with various back-
grounds since early 1960. In a multi-objective optimization problem, multiple-objective functions need to be
optimized simultaneously. In the case of multiple objectives, there may not necessarily existence a solution that
is best with respect to all objectives because of conﬂiction among objectives. A solution may be best in one
objective but worst in another. Therefore, there usually exist a set of solutions for the multiple-objective case
which cannot simply be compared with each other. For such solutions, called no-dominated solutions or Par-
eto optimal solutions, no improvement is possible in any objective function without scarifying at least one of
the other objective functions [1].
Resource allocation problem (RAP) is the process of allocating resources among the various activities, pro-
jects or business units for maximization of proﬁt or minimization of cost. The process of the RAP seeks to ﬁnd
an optimal allocation of a limited amount of resource to a number of tasks for optimizing their objectives sub-
ject to the given resource constraint. Resource may be a person, asset, material, or capital which can be used to
accomplish a goal. A goal may be objective or target, usually driven by speciﬁc future ﬁnancial needs. The best
or optimal solution may mean maximizing proﬁts, minimizing costs, or achieving the best possible quality.
0096-3003/$ - see front matter  2007 Elsevier Inc. All rights reserved.
doi:10.1016/j.amc.2007.09.070
* Corresponding author.
E-mail addresses: SKCH@Modares.ac.ir (S.K. Chaharsooghi), amirhosein.meimand@gmail.com (A.H. Meimand Kermani).
Available online at www.sciencedirect.com
Applied Mathematics and Computation 200 (2008) 167–177
www.elsevier.com/locate/amc


## Page 2

The RAP has a variety of applications, including ‘‘product allocation” [2] for allocating a limited number of
products among plants such that the incurred cost is minimized; ‘‘portfolio optimization” [3] for creating eﬃ-
cient portfolios on allocating funds to stocks or bonds to maximize return for a given level of risk, or to min-
imize risk for a target rate of return; ‘‘capital or project budgeting” [4] for allocating funds to projects that
initially consume cash but later generate cash, to maximize a ﬁrm’s return on capital; ‘‘software testing” [5]
for optimal testing-resource allocation of modular software systems their eﬃcacy in solving computationally
intensive problems; ‘‘health care resource allocation” [6] to the cost-eﬀectiveness analysis for the health care
resource allocation; ‘‘processor allocation or job shop scheduling” [7] for allocating time for work orders
on diﬀerent types of production equipment, to minimize delivery time or maximize equipment utilization, just
to name a few. An almost inﬁnite variety of problems can be tackled this way.
The development of meta-heuristic optimization theory has been ﬂourishing. Many meta-heuristic para-
digms such as genetic algorithm [8], simulated annealing [9], and tabu search [10] have shown their eﬃcacy
in solving computationally intensive problems. Among them, Abo-Sinna [11] proposed a genetic algorithm
for multi-objective resource allocation problem. The chromosome is resource allocated job and the objective
is to maximize the eﬃciency with the minimum cost. Lin and Gen [12] presented a hybrid genetic algorithm for
the same problem. It is seen that compared to mathematical programming approaches only few MORAP
researches based on meta-heuristic algorithms have been conducted.
This paper intends to present a new algorithm for solving MORAP based on the ant colony optimization
(ACO) which was recently developed by Dorigo [13]. We also propose to use adaptive resource bounds to
ensure that the resource constraint is satisﬁed. Experimental results manifest that the proposed ACO-based
method outperforms the genetic algorithm on a set of simulated MORAP problems. The convergence behav-
ior of the proposed method is analyzed by observing the variations of node transition entropy. Section 2
describes the deﬁnition of Pareto-optimal solutions or non-dominated solutions. Section 3 formulates the
MORAP that will be addressed in this paper. Section 4 presents the ACO-based algorithm for tackling the
MORAP in details. Section 5 reports the comparative performance of proposed ACO with Hybrid genetic
algorithm and also convergence analysis. Finally, Section 6 concludes this work.
2. Pareto-optimal solutions
For a problem having more than one objective function, any two solutions X(1) and X(2) can have one of
two possibilities – one dominates the other or none dominates the other. A solution X(1) is said to dominate
the other solution X(2), if both the following conditions are true:
1. The solution X(1) is no worse (say the operator  denotes worse and  denotes better) than X(2) in all objec-
tives, or fj(X(1)) § fj(X(2)) for all j = 1,2,. . .,M objectives.
2. The solution X(1) is strictly better than X(2) in at least one objective, or fj(X(1))  fj(X(2)) for at least one j
{1,2,. . .,M}.
If any of the above condition is violated, the solution X(1) does not dominate the solution X(2). If X(1) dom-
inates the solution X(2), it is also customary to write X(2) is dominated by X(1), or X(1) is non-dominated by X(2),
or, simply, among the two solutions, X(1) is the non-dominated solution.
The above concept can also be extended to ﬁnd a non-dominated set of solutions in a set of solutions. Con-
sider a set of N solutions, each having M(M > 1) objective function values. The following procedure can be
used to ﬁnd the non-dominated set of solutions [14]:
Step 0: Begin with i = 1.
Step 1: For all j 6¼ i, compare solutions X(i) and X(j) for domination using the above two conditions for all M
objectives.
Step 2: If for any j, X(i) is dominated by X(j), mark X(i) as ‘dominated’.
Step 3: If all solutions (that is, when i = N is reached) in the set are considered, Go to Step 4, else increment i by
one and Go to Step 1.
Step 4 : All solutions that are not marked ‘dominated’ are non-dominated solutions.
168
S.K. Chaharsooghi, A.H. Meimand Kermani / Applied Mathematics and Computation 200 (2008) 167–177


## Page 3

A population of solutions can be classiﬁed into groups of diﬀerent non-domination levels [15]. When the
above procedure is applied for the ﬁrst time in a population, the resulting set is the non-dominated set of ﬁrst
level. In order to have further classiﬁcations, these non-dominated solutions can be temporarily counted out
from the original set and the above procedure can be applied once more. What results is a set of non-domi-
nated solutions of second level. These new set of non-dominated solutions can be counted out and the proce-
dure may be applied again to ﬁnd the third level non-dominated solutions. This procedure can be continued
till all members are classiﬁed into a non-dominated level. It is important to realize that the number of non-
domination levels in a set of N solutions is bound to lie within [1, N]. The minimum case of one non-domi-
nation level occurs when no solution dominates any other solution in the set, thereby classifying all solutions
of the original population into one non-dominated level. The maximum case of N non-domination levels
occurs, when there is hierarchy of domination of each solution by exactly one other solution in the set. In most
interesting multi-objective optimization problem that objectives are ‘conﬂicting’ to each other, the main goal is
achieving the ﬁrst (or the best) non-dominated level.
3. Mathematical formulation
In this paper, we focus on the multi-stage decision making model for multi-objective human resource allo-
cation problem. Optimization deals with the problem of seeking solution over a set of possible choices to
optimize certain criteria [12], without loss of generality. The mathematical model can be formulated as
follows:
Notations
Indices:
i
index of job, i = 1, 2, . . ., N,
j
number of worker, j = 0,1, 2, . . ., M.
Parameters:
N
total number of jobs,
M
total number of workers,
cij
cost of job i when j workers are assigned,
eij
eﬃciency of job i when j workers are assigned.
Decision variables:
X ij
1;
if j amounts of resource are assigned to the project i;
0;
otherwise;
(
max
X
N
i¼1
X
M
J¼0
eijX ij;
ð1Þ
min
X
N
i¼1
X
M
j¼0
cijX ij;
ð2Þ
s:t:
X
N
i¼1
X
M
j¼0
jX ij 6 M;
ð3Þ
X
M
j¼0
X ij ¼ 1
8i;
ð4Þ
X ij ¼ 0 or 1
8i; j:
ð5Þ
S.K. Chaharsooghi, A.H. Meimand Kermani / Applied Mathematics and Computation 200 (2008) 167–177
169


## Page 4

The objective function (1) is to maximizing the total eﬃciencies for all the jobs. And the objective (2) is to
minimizing the total costs for all the workers. Constraint (3) ensures that we cannot assign the workers more
than the total numbers of workers. Constraint (4) ensures that for each job i we just can only assign workers
for it one time. The Pareto optimal solutions are usually characterized as solutions of the multi-objective pro-
gramming problem. Therefore, in implementation of ACO algorithms, a module for handling Pareto optimal
solutions is added. It consists of two steps:
Step 1: Evaluate transmitted by the objective functions.
Step 2: Select Pareto solutions based on the procedure described in Section 2.
4. Ant colony optimization for MORAPS
The ant colony optimization (ACO) paradigm was ﬁrst proposed by Dorigo [13] and has encouraged many
researchers to develop ACO variants for tackling well-known NP-hard problems, such as the traveling sales-
man problem [16], quadratic assignment problem [17], scheduling problem [18], minimum weight vertex cover
problem [19], and curve segmentation problem [20], just to name a few. The ACO is inspired by the research
on the real ant foraging behavior. Ethnologists observed that ants can construct the shortest path from their
colony to the feeding source through the use of pheromone trails.
The ant colony approach imitates the behavior shown by real ants when searching for food. They commu-
nicate information about food source via pheromone, which they secrete as they move along. When an ant
ﬁnds a food source it returns to the nest. As ants on short (i.e. objective function) path will return to the nest
faster, more pheromone will be deposited on the shorter paths. Moving ants accordingly choose their path
with a probability that depend on the amount of pheromone detected and consequently, paths that are more
frequently traveled become more attractive and, by means of that self-strengthen behavior, will be used more
often. Further, the pheromone ‘‘evaporates” over time, so that pheromone trails of infrequently traveled
become weaker while attractive paths are reinforced. And ﬁnally, artiﬁcial ants not only imitate the learning
behavior described above, but often apply additional, problem-speciﬁc heuristic information. While such arti-
ﬁcial ant colony system have been successfully applied to various single-objective problems, several extensions
have been necessary in order to be able to tackle the multi-objective problems. Generally any ant algorithm
must specify the following elements:
1. Construction of solutions.
2. Heuristic information.
3. Pheromone updating rule.
4. Selection probability.
5. Termination condition.
Speciﬁc implementation of these elements results in distinct ant algorithms with varying degrees of success.
In the following subsections we describe our proposed methods for these elements.
4.1. Construction of solutions
A feasible and complete solution of the formulated multi-objective resource allocation problem is consid-
ered as a permutation of resource allocation. Each part of this solution is termed state. Assignment of j
amount of resource to the ith project is called a move and represented by V(i,j). A move Vk takes ant k from
state S1 to state S2 and thus the partial solution is gradually completed. Once j amount of resource is assigned
to the ith project in the solution of ant k, the available amount of resource must be updated and according to
the new amount of resource, all infeasible moved must be stored into a Tabu list denoted by Tabuk. This list is
the memory of ant k saving the index of infeasible allocations. In addition to the list Tabuk, all the moves
selected by ant k are stored in a memory represented by Vk. In the next step in which ant k moves from current
state to the next state, the list Tabuk is used to avoid assignment of project whose needed resource is not
170
S.K. Chaharsooghi, A.H. Meimand Kermani / Applied Mathematics and Computation 200 (2008) 167–177


## Page 5

available. The memory Vk is used at the end of iteration to update the pheromones of moves selected by ants.
It is assumed that allocations of resource are pre-ordered in an ascending manner. In other words, each ant
initially assigns a resource to project 1, then assigns to project 2 and so on till a complete solution is obtained.
In each assignment, the infeasible assignments are added to the Tabu list of that ant. Thus, the constraints
Eqs. (3)–(5) are satisﬁed. This leads each ant to generate feasible solution.
4.2. Heuristic information
Unlike the real ants that are almost blind creatures, artiﬁcial ants can include some heuristic information
while assigning resource at diﬀerent projects. The heuristic information pertaining to move V(i,j) is denoted
by gij. This information indicates the desirability of assigning j amount of resource to project i and is cal-
culated using a heuristic approach. There are several methods to estimate the desirability of each move. Since
the heuristic information is calculated for all moves in all ants, it may signiﬁcantly reduce the eﬃciency of
the algorithm and thus it should be computed in an eﬃcient manner. Let us consider the complexity of this
element in the ant algorithms. From the beginning of constructing a solution to the end, each ant has a pos-
sibility to assign M amounts of resource to all projects without considering the feasibility, so in total, each
ant should calculate the heuristic information M  N times in each iteration of the algorithm. Thus, the
complexity of this element for the entire algorithm becomes O (I  A  M  N) where, I is the number
of iterations and A is the number of ants in each iteration. According to our observation describe in Section
4, the number of ants is a multiplication of the number of projects, it is concluded that providing heuristic
information for each move is computationally crucial for the eﬃciency of the algorithm. In the earlier imple-
mentations of ant algorithms, the heuristic information is calculated either a priori [22] or a posteriori [21].
In the ﬁrst category of implementations, the heuristic information is computed ﬁrst at the beginning and
remains unchanged during the running of algorithm. In the second category, the heuristic information is
dynamic and depends upon the current state of the ant. Two confecting aspects are to be considered in
the calculation of heuristic information. These are: (1) the eﬃciency of calculation, and (2) the quality of
information. The implementations with a priori heuristic information are eﬃcient but not thoroughly indi-
cating the desirability of moves. On the contrary, in the second category of implementations, a precise esti-
mation of the desirability of each move is obtained, though the eﬃciency of computation is not satisfactory.
An attempt has been made in this paper to develop a method for calculating heuristic information by a ratio-
nale combination of these aspects. The proposed method to calculate the heuristic information falls in the
second category, i.e. implementation with a posteriori information. However, the computational complexity
of our proposed approach is less than that of some methods falling in this category such as [21]. The pro-
posed formula considers the partial contribution of each move to the objective function value. Let p denote a
permutation of assignment under construction. Since, while calculating the desirability of move V(l,j) the
permutation of projects till l, i.e. p(1),p(2),. . .,p(l) is known, the partial contribution of move V(l,j) can
therefore be calculated as follows:
Partial contribution of move V(l,j) for the ﬁrst objective function:
glj1 ¼
1
e þ Pl1
i¼1
PM
j¼0cijX ij
:
ð6Þ
In this formula e is the small positive number; the reason due to which e is added in the denominator of (6)
is for avoiding division by 0.
As well as the ﬁrst objective function, Partial contribution of move V(l,j) for the second one can be calcu-
lated as follows:
glj2 ¼
X
l1
i¼1
X
M
j¼0
eijX ij:
ð7Þ
Heuristic information given by Eqs. (6) and (7) can be obtained in O(L  N). There are several way for
combining desirability in multi-objective problem to achieve total desirability of each move, In this paper
we propose the following formula to calculate the total desirability of V(l,j):
S.K. Chaharsooghi, A.H. Meimand Kermani / Applied Mathematics and Computation 200 (2008) 167–177
171


## Page 6

glj ¼ g1lj  g2lj:
ð8Þ
4.3. Pheromone updating rule
ACO relies on the synergy among a population of ant agents. At each iteration, every ant moves from stage
to stage by iteratively applying the node transition rule until it enters the sink-node upon which a candidate
solution to the problem has been constructed. Before activating the next iteration, the quantity of pheromone
on each edge is updated by the pheromone updating rule, according to the original ACO algorithm in the sin-
gle objective function problems the Eq. (9) applied to update quantity of pheromone on each edge:
sijðtÞ ¼ ð1  qÞsijðt  1Þ þ Dsðt  1Þ
8i; j;
ð9Þ
where q, (0,1] is the evaporation rate of pheromone, sij(t) is the updated quantity of pheromone on the edge ij
– which means assignment of j amount of resource to the job i – and sij(t  1) is the later quantity of phero-
mone on this edge. Ds(t  1) is the quantity of pheromone laid on edge ij by the ant during the current iter-
ation. Clearly, if the ant did not traverse edge ij during the current iteration, then Ds(t  1) = 0. Otherwise,
Ds(t  1) must be calculated. In the real world almost all ants deposit the constant amount of pheromone
on each traversed edge but laid pheromone by artiﬁcial ant are related to the quality of constructed solution,
in the original ACO algorithm for single objective function problem the following formula is used to calculate
Ds(t  1):
rsðt  1Þ ¼
1
f ðX t1Þ ;
ð10Þ
where Xt is the candidate solution constructed by the ant. There are several ways for calculating Ds in the lit-
erature [22,23]. In this paper we proposed another diﬀerent way for calculating Ds more eﬀectively. According
to this fact that there does not existence an exact optimal solution with respect to all objective functions, all
non-dominated or Pareto solutions are considered as optimal or best solutions for a multi-objective function
problems. It can be assumed that all non-dominated solutions have the same and highest quality and all dom-
inated solutions must be omitted, So the following rule is proposed to calculating Ds(t  1):
Dsðt þ 1Þ ¼
þðt  dÞ
if X t is a non-dominated solution
ðt  dÞ
Otherwise;

ð11Þ
where d is a small positive number and t is number of current iteration. In this formula each constructed solu-
tion in the current iteration is compared with all former non-dominated solutions, if it is a non-dominated
solution, the quantity of pheromone in all edge which constructed it will be increased by t  d. The reason
for multiply d by t is this fact that by increasing the set of feasible solution, which is corresponded to t, found
non-dominated solutions are more approached to the ﬁrst (or best) non-dominated level which was described
in the Section 2, i.e. some non-dominated solution in Nth interaction can be dominated by some solutions of
(N + 1)th iteration. This rule tries to increasing the learning of ants.
4.4. Selection probability
In all the implementations of ant algorithms, an ant chooses a move to go from current state, S1, to the next
adjacent state, S2, based on a rationale combination of two factors, namely the desirability of that move and
the quantity of pheromone on the edge which is to be traversed. There are diﬀerent methods in literature to
combine these factors. We have modiﬁed the method proposed in [24] to calculate the selection probability.
There are two reasons for adopting and modifying this method. The ﬁrst is the simplicity of the approach pro-
posed in [24] as only one control parameter, i.e. a, is used to map the relative importance of quantity of pher-
omone and the desirability of each move. In other methods, however, one parameter is considered for each
factor. The second reason is the computational eﬃciency of this method as multiplication operations are used
instead of exponentiations. We explain the genesis of this approach as follows. According to the method pro-
posed by [24], ant k chooses edge ij for traversing by the following probability:
172
S.K. Chaharsooghi, A.H. Meimand Kermani / Applied Mathematics and Computation 200 (2008) 167–177


## Page 7

pij ¼
a  sij þ ð1  aÞgij
P
i62Tabukða  sij þ ð1  aÞgijÞ
8i 62 Tabuk:
ð12Þ
Application of Eq. (11) may result in negative probability of some move. We investigated the performance
of two policies in tackling the moves with negative probability. These are as follows:
(1) Moves with negative probability are avoided and the selection is only done amongst the moves with posi-
tive ones. Moves are chosen with equal chances if there is no move with positive probability.
(2) The absolute value of the most negative probability is added to the probabilities of other moves and then
new probabilities are calculated based on cumulative, therefore all the probabilities become positive.
It must be noted that the search space in the ﬁrst policy is more limited than that of in the second [23]. This
fact is in agreement with our experimental observations signifying that the second policy functions better than
the ﬁrst. Our proposed method performs as follows: after applying the Eq. (12) for calculating the probability
of each resource assigning, In case of any negative probability, the second policy is employed.
4.5. The ant algorithm
In this subsection, the elements discussed above are synthesized to evolve the proposed ant algorithm. The
pseudo code of the proposed ant algorithm is given below:
Initialize
1. Set values of parameter q, d, a, t0, A (number of ants) and Max_Iter (number of iteration)
2. Initialize the quantity of pheromone of all edges Iteration
3. for k = 1 to A
4. for i=1 to works
4.1 Select all impossible moves
4.2 Calculate the desirability of all possible moves for all objective functions (Eqs. (7), (8) and (9)).
4.3 Calculate the probability of all possible moves based on the second policy (Eq. (12)).
4.4 Assign
4.5 Update available resource.
Evaluation
5. Calculate objective functions corresponded to the constructed solution.
6. Compare the constructed solution with other solution of Ant k to speciﬁcation if it is Pareto or non-
dominate solution.
Pheromone updating
7. Compare all solutions of all A ants which are marked as non-dominated and select ﬁnal non-dominate
solutions.
8. Update the pheromone quantity. (Eqs. (9) and (11))
9. if total iteration < max_Iter got to step 3 otherwise stop.
5. Computational results
The proposed ant algorithm had been coded in Borland Delphi 7 and executed on a 1.80 GHz centrino. The
proposed algorithm contains four parameters A as number of ants, number of iterations, q, d, a and t0. These
parameters aﬀect the performance of the proposed ant algorithm. Extensive experimental tests were conducted
to see the eﬀect of diﬀerent values on the performance of the proposed algorithm. Based upon these observa-
tions, the following experimentally derived rules are proposed to set the value of parameters:
S.K. Chaharsooghi, A.H. Meimand Kermani / Applied Mathematics and Computation 200 (2008) 167–177
173


## Page 8

A = 5  M, max_iteration = N, a = 0.5, d = 0.05/N, t0 = 0.01, q = 0.3
Consider the following problem which was extract from [12] and was solved with Hybrid Genetic Algo-
rithm, this problem is allocating 10 workers to a certain set of four jobs. Tables 1 and 2 provide the expected
eﬃciency and cost. The following Tables 3 and 4 as shows an example of the non-dominated (Pareto) solution
by hGA and proposed ACO.
Chart 1 shows that proposed ACO dominates 50% of Pareto solutions constructed by hGA (Solutions 2, 4
and 6 of Table 3) and also none of the Pareto solutions generated by proposed ACO was dominated by hGA.
This result can approve that proposed ACO approximately outperform the hGA in solving multi-objective
resource allocation problem.
5.1. Convergence analysis
To analyze the convergence behavior of the proposed algorithm, we testify whether the entire ant colony
evolves to a consensus goal and the ﬁnal high quality solution is a consequence of the collective intelligence
Table 1
Excepted Cost Cij
Number of jobs
Number of workers
0
1
2
3
4
5
6
7
8
9
10
1
41
38
46
32
78
76
72
84
80
92
96
2
45
54
36
55
87
82
90
132
97
121
134
3
36
43
68
56
72
59
32
67
86
88
100
4
46
78
88
64
90
80
120
104
96
86
120
Table 3
The non-dominated (Pareto) solutions by hGA
Solution k
jX1j
jX2j
jX3j
jX4j
Overall cost
Overall eﬃciency
1
3
2
1
4
201
229
2
0
2
6
2
197
210
3
3
2
5
0
173
182
4
3
1
6
0
164
175
5
1
1
6
2
212
241
6
0
1
6
3
191
209
Table 4
The non-dominated (Pareto) solutions by proposed ACO
Solution k
jX1j
jX2j
jX3j
jX4j
Overall cost
Overall eﬃciency
1
3
2
1
3
175
222
2
1
2
6
0
152
180
3
3
2
0
0
150
105
4
1
1
6
1
202
234
Table 2
Excepted eﬃciency Eij
Number of jobs
Number of workers
0
1
2
3
4
5
6
7
8
9
10
1
1
37
42
50
54
56
58
65
72
80
95
2
1
49
55
59
62
67
73
80
87
95
102
3
1
45
49
57
64
77
88
92
100
105
110
4
1
60
67
72
79
83
88
97
102
110
120
174
S.K. Chaharsooghi, A.H. Meimand Kermani / Applied Mathematics and Computation 200 (2008) 167–177


## Page 9

instead of the wandering of a lucky ant. We use the entropy for measuring the information purity about the
distributions of node transition probability Pij Eq. (12). We deﬁne the node transition entropy Eij for the jth
node of the ith layer in the ACO representation graph as follows:
0
50
100
150
200
250
300
0.0000
0.0010
0.0020
0.0030
0.0040
0.0050
0.0060
0.0070
1/Overall Cost
Overall Efficiency
Feasible Solutions
Pareto Solutions by hGA
Pareto Solutions by Proposed ACO
Chart 1. Comparing hGA by proposed ACO.
0.000000
0.000500
0.001000
0.001500
0.002000
0.002500
0.003000
0.003500
0.004000
0.004500
0
100
200
300
400
500
600
Number of Iteration
Average Entropy
Chart 2. Convergence analysis.
S.K. Chaharsooghi, A.H. Meimand Kermani / Applied Mathematics and Computation 200 (2008) 167–177
175


## Page 10

Eij ¼ 
X
for all nodes
pij ln pij:
ð13Þ
The node transition rule becomes more deterministic when the node transition entropy approaches 0 [25].
We then compute the average entropy E over all node transition entropy values. Chart 2 shows the variations
of E as the number of ACO iterations increases. It is seen that the value of E decreases gradually from
3.94  103 to 8.8  104, which manifests that, as the evolution becomes mature, the dominant path with
the highest node transition probabilities stands out and the probability distributions become more stable.
Hence, the ACO colony converges to the same solution corresponding to the dominant path which is learned
through the pheromone updating.
6. Conclusion
The multi-objective allocation problem (MORAP) addresses the important issue which seeks to ﬁnd the
expected objectives by allocating the limited amount of resource to various activates. Resources may be man-
power, assets, raw material or anything else in limited supply which can be used to accomplish the goals. The
resource allocation problem (RAP) has a wide range of applications, including product allocation, resource
distribution, project budgeting, software testing, health care resource allocation, etc. Many versions of
RAP formulations have been provided in accordance with various applications. In this paper we proposed
a modiﬁed version of ant colony optimization for MORAP, in this algorithm we tries to increase both eﬃ-
ciency and eﬀectiveness of algorithm by increasing the learning of ants in updating pheromone rule, and also
by simplifying of probability calculation. In the last Section of paper we compare the result of hGA with pro-
posed ACO which were applied in the same problem, this comparing manifest that proposed ACO outperform
hGA in 50% of non-dominated solution. Finally the convergence of the ACO-based algorithm is analyzed
using node transition entropy which validates that the obtained quality solution is due to the consensus knowl-
edge possessed by the whole ant colony instead of the wandering of a lucky ant.
References
[1] C.M. Fonseca, P.J. Fleming, An overview of evolutionary algorithms in multi-objective optimization, Evolutionary Computation 3
(1) (1995) 1–16.
[2] Y.C. Hou, Y.H. Chang, A new eﬃcient encoding mode of genetic algorithms for the generalized plant allocation problem, Journal of
Information Science and Engineering 20 (2004) 1019–1034.
[3] Matthias Ehrgott, Kathrin Klamroth, Christian Schwehm, An MCDM approach to portfolio optimization, European Journal of
Operational Research 155 (3) (2004) 752–770, June.
[4] H. Luss, S.K. Gupta, Allocation of eﬀort resource among competing activities, Operations Research 23 (1975) 360–366.
[5] Y.S. Dai, M. Xie, K.L. Poh, B. Yang, Optimal testing-resource allocation with genetic algorithm for modular software systems,
Journal of Systems and Software 66 (2003) 47–55.
[6] M. Johannesson, M.C. Weinstein, On the decision rules of cost-eﬀectiveness analysis, Journal of Health Economics 12 (1993) 459–
467.
[7] A. Ernst, H. Hiang, M. Krishnamoorthy, Mathematical programming approaches for solving task allocation problems, in:
Proceedings of the 16th National Conference of Australian Society of Operations Research, 2001.
[8] D.E. Goldberg, Genetic Algorithms in Search, Optimization, and Machine Learning, Addison Wesley, Reading, Massachusetts, 1997.
[9] S. Kirkpatrick, C. Gelatt Jr., M. Vecchi, Optimization by simulated annealing, Science 220 (1983) 671–680.
[10] F. Glover, Tabu search – Part I, ORSA Journal of Computing 1 (1989) 190–206.
[11] M.S. Osman, M.A. Abo-Sinna, A.A. Mousa, An eﬀective genetic algorithm approach to multi-objective resource allocation problems,
Applied Mathematics and Computation 163 (2005) 755–768.
[12] Chi-Ming Lin, Mitsuo Gen, Multi-objective resource allocation problem by multistage decision-based hybrid genetic algorithm,
Applied Mathematics and Computation 187 (2007) 574–583.
[13] M. Dorigo, Optimization, learning, and natural algorithms, Ph.D. Thesis, Dip. Elettronica e Informazione, Politecnico di Milano,
Italy, 1992.
[14] Kalyanmoy Deb. Multi-Objective Genetic Algorithms: Problem Diﬃculties and Construction of Test Problems, Technical Report CI-
49/98, Dortmund: Department of Computer Science/LS11, University of Dortmund, Germany, 1998.
[15] D.E. Goldberg, J. Richardson, Genetic algorithms with sharing for multimodal function optimization, in: Proceedings of the First
International Conference on Genetic Algorithms and Their Applications, 1987, p. 41.
[16] M. Dorigo, L. Gambardella, Ant colony system: a cooperative learning approach to the traveling salesman problem, IEEE
Transaction on Evolutionary Computation 1 (1997) 53–66.
176
S.K. Chaharsooghi, A.H. Meimand Kermani / Applied Mathematics and Computation 200 (2008) 167–177


## Page 11

[17] V. Maniezzo, A. Colorni, M. Dorigo, The ant system applied to the quadratic assignment problem, Universite Libre de Bruxelles,
Belgium, Technical Report IRIDIA/94-28, 1994.
[18] S.J. Shyu, B.M.T. Lin, P.Y. Yin, Application of ant colony optimization for no-wait ﬂow shop scheduling problem to minimize the
total completion time, Computer and Industrial Engineering 47 (2004) 181–193.
[19] S.J. Shyu, P.Y. Yin, B.M.T. Lin, T.S. Hsiao, An ant colony optimization algorithm for the minimum weight vertex cover problem,
Annals of Operations Research 131 (2004) 283–304.
[20] P.Y. Yin, Ant colony search algorithm for optimal polygonal approximation of plane curves, Pattern Recognition 36 (2003) 1783–
1797.
[21] V. Maniezzo, A. Colorni, The ant system applied to the quadratic assignment problem, IEEE Transactions on Knowledge and Data
Engineering 11 (5) (1999) 769–778.
[22] M. Dorigo, L.M. Gambardella, Ant colony system: A cooperative learning approach to the traveling salesman problem, IEEE
Transactions on Evolutionary Computation 1 (1) (1997) 53–66.
[23] M. Solimanpur, P. Vrat, R. Shankar, Ant colony optimization algorithm to the inter-cell layout problem in cellular manufacturing,
European Journal of Operational Research 157 (2004) 592–606.
[24] V. Maniezzo, Exact and approximate nondeterministic tree-search procedures for the quadratic assignment problem, INFORMS
Journal on Computing 11 (1999) 358–369.
[25] Peng-Yeng Yin, Jing-Yu Wang, Ant colony optimization for the nonlinear resource allocation problem, Applied Mathematics and
Computation 174 (2006) 1438–1453.
S.K. Chaharsooghi, A.H. Meimand Kermani / Applied Mathematics and Computation 200 (2008) 167–177
177



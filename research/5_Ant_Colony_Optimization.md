# 

**Source:** `5_Ant_Colony_Optimization.pdf`
---

## Page 1

 5. Ant Colony Optimization 
Vittorio Maniezzo, Luca Maria Gambardella, Fabio de Luigi  
5.1 Introduction 
Ant Colony Optimization (ACO) is a paradigm for designing metaheuristic algo-
rithms for combinatorial optimization problems. The first algorithm which can be 
classified within this framework was presented in 1991 [21, 13] and, since then, 
many diverse variants of the basic principle have been reported in the literature. 
The essential trait of ACO algorithms is the combination of a priori information 
about the structure of a promising solution with a posteriori information about the 
structure of previously obtained good solutions.  
Metaheuristic algorithms are algorithms which, in order to escape from local 
optima, drive some basic heuristic: either a constructive heuristic starting from a 
null solution and adding elements to build a good complete one, or a local search 
heuristic starting from a complete solution and iteratively modifying some of its 
elements in order to achieve a better one. The metaheuristic part permits the low-
level heuristic to obtain solutions better than those it could have achieved alone, 
even if iterated. Usually, the controlling mechanism is achieved either by con-
straining or by randomizing the set of local neighbor solutions to consider in local 
search (as is the case of simulated annealing [46] or tabu search [33]), or by com-
bining elements taken by different solutions (as is the case of evolution strategies 
[11] and genetic [40] or bionomic [56] algorithms). 
The characteristic of ACO algorithms is their explicit use of elements of previ-
ous solutions. In fact, they drive a constructive low-level solution, as GRASP [30] 
does, but including it in a population framework and randomizing the construction 
in a Monte Carlo way. A Monte Carlo combination of different solution elements 
is suggested also by Genetic Algorithms [40], but in the case of ACO the probabil-
ity distribution is explicitly defined by previously obtained solution components. 
The particular way of defining components and associated probabilities is prob-
lem-specific, and can be designed in different ways, facing a trade-off between the 
specificity of the information used for the conditioning and the number of solu-
tions which need to be constructed before effectively biasing the probability dis-
                                                          
  This work was partially supported by the Future & Emerging Technologies  
unit of the European Commission through Project BISON (IST-2001-38923).  


## Page 2

 
2 
tribution to favor the emergence of good solutions. Different applications have fa-
vored either the use of conditioning at the level of decision variables, thus requir-
ing a huge number of iterations before getting a precise distribution, or the compu-
tational efficiency, thus using very coarse conditioning information. 
The chapter is structured as follows. Section 2 describes the common elements 
of the heuristics following the ACO paradigm and outlines some of the variants 
proposed. Section 3 presents the application of ACO algorithms to a number of 
different combinatorial optimization problems and it ends with a wider overview 
of the problem attacked by means of ACO up to now. Section 4 outlines the most 
significant theoretical results so far published about convergence properties of 
ACO variants. 
5.2 Ant Colony Optimization 
ACO [1, 24] is a class of algorithms, whose first member, called Ant System, was 
initially proposed by Colorni, Dorigo and Maniezzo [13, 21, 18]. The main under-
lying idea, loosely inspired by the behavior of real ants, is that of a parallel search 
over several constructive computational threads based on local problem data and 
on a dynamic memory structure containing information on the quality of previ-
ously obtained result. The collective behavior emerging from the interaction of the 
different search threads has proved effective in solving combinatorial optimization 
(CO) problems.  
Following [50], we use the following notation. A combinatorial optimization 
problem is a problem defined over a set C = c1, ... , cn of basic components. A 
subset S of components represents a solution of the problem; F ⊆ 2C is the subset 
of feasible solutions, thus a solution S is feasible if and only if S ∈ F. A cost func-
tion z is defined over the solution domain, z : 2C å R, the objective being to find 
a minimum cost feasible solution S*, i.e., to find S*: S* ∈ F and z(S*) ≤ z(S), 
∀S∈F. 
Given this, the functioning of an ACO algorithm can be summarized as follows 
(see also [27]). A set of computational concurrent and asynchronous agents (a col-
ony of ants) moves through states of the problem corresponding to partial solu-
tions of the problem to solve. They move by applying a stochastic local decision 
policy based on two parameters, called trails and attractiveness. By moving, each 
ant incrementally constructs a solution to the problem. When an ant completes a 
solution, or during the construction phase, the ant evaluates the solution and modi-
fies the trail value on the components used in its solution. This pheromone infor-
mation will direct the search of the future ants. 
Furthermore, an ACO algorithm includes two more mechanisms: trail evapora-
tion and, optionally, daemon actions. Trail evaporation decreases all trail values 
over time, in order to avoid unlimited accumulation of trails over some compo-
nent. Daemon actions can be used to implement centralized actions which cannot 
be performed by single ants, such as the invocation of a local optimization proce-


## Page 3

 
3 
dure, or the update of global information to be used to decide whether to bias the 
search process from a non-local perspective [27].  
More specifically, an ant is a simple computational agent, which iteratively 
constructs a solution for the instance to solve. Partial problem solutions are seen as 
states. At the core of the ACO algorithm lies a loop, where at each iteration, each 
ant moves (performs a step) from a state ι to another one ψ, corresponding to a 
more complete partial solution. That is, at each step σ, each ant k computes a set 
Akσ(ι) of feasible expansions to its current state, and moves to one of these in 
probability. The probability distribution is specified as follows. For ant k, the 
probability pιψk of moving from state ι to state ψ depends on the combination of 
two values: 
• the attractiveness ηιψ of the move, as computed by some heuristic indicating 
the a priori desirability of that move;  
• the trail level τιψ of the move, indicating how proficient it has been in the past 
to make that particular move: it represents therefore an a posteriori indication 
of the desirability of that move. 
Trails are updated usually when all ants have completed their solution, increas-
ing or decreasing the level of trails corresponding to moves that were part of 
"good" or "bad" solutions, respectively. 
The general framework just presented has been specified in different ways by 
the authors working on the ACO approach. The remainder of Section 2 will out-
line some of these contributions. 
5.2.1 Ant System 
The importance of the original Ant System (AS) [13, 21, 18] resides mainly in be-
ing the prototype of a number of ant algorithms which collectively implement the 
ACO paradigm. AS already follows the outline presented in the previous subsec-
tion, specifying its elements as follows. 
The move probability distribution defines probabilities pιψk to be equal to 0 for 
all moves which are infeasible (i.e., they are in the tabu list of ant k, that is a list 
containing all moves which are infeasible for ants k starting from state ι), other-
wise they are computed by means of formula (5.1), where α and β are user-
defined parameters (0 ≤ α,β ≤ 1): 








∉




⋅
+
+
=
∑
∉
otherwise
0
tabu
)
( 
if
       
p
k
)
(
k
ιψ
η
τ
η
τ
ιζ
β
ιζ
α
ιζ
β
ιψ
αιψ
ιψ
k
tabu
 
(5.1) 


## Page 4

 
4 
 
In formula 5.1, tabuk is the tabu list of ant k, while parameters α and β specify 
the impact of trail and attractiveness, respectively. 
After each iteration t of the algorithm, i.e., when all ants have completed a solu-
tion, trails are updated by means of formula (5.2): 
 
τιψ (τ) = ρ τιψ (τ − 1) + ∆τιψ   
(5.2) 
 
where ∆τιψ represents the sum of the contributions of all ants that used move 
(ιψ) to construct their solution, ρ, 0 ≤ ρ ≤ 1, is a user-defined parameter called 
evaporation coefficient, and ∆τιψ represents the sum of the contributions of all 
ants that used move (ιψ) to construct their solution. The ants’ contributions are 
proportional to the quality of the solutions achieved, i.e., the better solution is, the 
higher will be the trail contributions added to the moves it used.  
For example, in the case of the TSP, moves correspond to arcs of the graph, 
thus state ι could correspond to a path ending in node i, the state ψ to the same 
path but with the arc (ij) added at the end and the move would be the traversal of 
arc (ij). The quality of the solution of ant k would be the length Lk of the tour 
found by the ant and formula (5.2) would become τij(t)=ρ τij(t-1)+∆τij , with  
∑
=
∆
=
∆
m
k
k
ij
ij
1
τ
τ
 
(5.3) 
where m is the number of ants and 
kij
τ
∆
 is the amount of trail laid on edge (ij) 
by ant k, which can be computed as 



=
∆
otherwise
    
0 
 tour
its
in 
 
(ij)
 
arc
 
uses
 
ant 
 
if
 
L
Q
k
k
ij
k
τ
 
(5.4) 
Q being a constant parameter.  
The ant system simply iterates a main loop where m ants construct in parallel 
their solutions, thereafter updating the trail levels. The performance of the algo-
rithm depends on the correct tuning of several parameters, namely: α, β, relative 
importance of trail and attractiveness, ρ, trail persistence, τij(0), initial trail level, 
m, number of ants, and Q, used for defining to be of high quality solutions with 
low cost. The algorithm is the following. 
 
1. {Initialization} 
 
Initialize τιψ and ηιψ, ∀(ιψ).  
2. {Construction} 
  For each ant k (currently in state ι) do 
 
 
repeat 
 
 
 
choose in probability the state to move into. 


## Page 5

 
5 
 
 
 
append the chosen move to the k-th ant's set tabuk. 
 
 
until ant k has completed its solution. 
  end for  
3. {Trail update} 
 
For each ant move (ιψ) do 
 
 
compute ∆τιψ 
 
 
update the trail matrix. 
 
end for 
4. {Terminating condition} 
 
If not(end test) go to step 2 
5.2.2 Ant Colony System 
AS was the first algorithm inspired by real ants behavior. AS was initially applied 
to the solution of the traveling salesman problem but was not able to compete 
against the state-of-the art algorithms in the field. On the other hand he has the 
merit to introduce ACO algorithms and to show the potentiality of using artificial 
pheromone and artificial ants to drive the search of always better solutions for 
complex optimization problems. The next researches were motivated by two 
goals: the first was to improve the performance of the algorithm and the second 
was to investigate and better explain its behavior. Gambardella and Dorigo pro-
posed in 1995 the Ant-Q algorithm [35], an extension of AS which integrates 
some ideas from Q-learning [76], and in 1996 Ant Colony System (ACS) [36, 25] 
a simplified version of Ant-Q which maintained approximately the same level of 
performance, measured by algorithm complexity and by computational results. 
Since ACS is the base of many algorithms defined in the following years we focus 
the attention on ACS other than Ant-Q. ACS differs from the previous AS because 
of three main aspects:  
Pheromone 
In ACS once all ants have computed their tour (i.e. at the end of each iteration) AS 
updates the pheromone trail using all the solutions produced by the ant colony. 
Each edge belonging to one of the computed solutions is modified by an amount 
of pheromone proportional to its solution value. At the end of this phase the 
pheromone of the entire system evaporates and the process of construction and 
update is iterated. On the contrary, in ACS only the best solution computed since 
the beginning of the computation is used to globally update the pheromone. As 
was the case in AS, global updating is intended to increase the attractiveness of 
promising route but ACS mechanism is more effective since it avoids long con-
vergence time by directly concentrate the search in a neighborhood of the best tour 
found up to the current iteration of the algorithm.   


## Page 6

 
6 
In ACS, the final evaporation phase is substituted by a local updating of the 
pheromone applied during the construction phase. Each time an ant moves from 
the current city to the next the pheromone associated to the edge is modified in the 
following way: 
( )
(
)
0
)
1(
τ
ρ
τ
ρ
τ
⋅
−
+
⋅
=
1
-
t
t
ij
ij
 where 0 ≤ ρ ≤ 1 is a parameter 
(usually set at 0.9) and τ0 is the initial pheromone value. τ0 is defined as 
τ0=(n·Lnn)-1, where Lnn is the tour length produced by the execution of one ACS 
iteration without the pheromone component (this is equivalent to a probabilistic 
nearest neighbor heuristic). The effect of local-updating is to make the desirability 
of edges change dynamically:  every time an ant uses an edge this becomes 
slightly less desirable and only for the edges which never belonged to a global best 
tour the pheromone remains τ0. An interesting property of these local and global 
updating mechanisms is that the pheromone τij(t) of each edge is inferior limited 
by τ0. A similar approach was proposed with the Max-Min-AS (MMAS, [70]) that 
explicitly introduces lower and upper bounds to the value of the pheromone trials.  
State Transition Rule 
During the construction of a new solution the state transition rule is the phase 
where each ant decides which is the next state to move to. In ACS a new state 
transition rule called pseudo-random-proportional is introduced. The pseudo-
random-proportional rule is a compromise between the pseudo-random state 
choice rule typically used in Q-learning [76] and the random-proportional action 
choice rule typically used in Ant System. With the pseudo-random rule the chosen 
state is the best with probability q0 (exploitation) while a random state is chosen 
with probability 1-q0 (exploration). Using the AS random-proportional rule the 
next state is chosen randomly with a probability distribution depending on ηij and 
τij. The ACS pseudo-random-proportional state transition rule provides a direct 
way to balance between exploration of new states and exploitation of a priori and 
accumulated knowledge. The best state is chosen with probability q0 (that is a pa-
rameter 0 ≤ q0 ≤ 1  usually fixed to 0.9) and with probability (1-q0) the next state 
is chosen randomly with a probability distribution based on ηij and τ ij weighted by 
α  (usually equal to 1) and β  (usually equal to 2) . 
 
{
}







≤
⋅
∉
       
on)
(explorati
   
otherwise
        
          
5.1
 
rule
 
AS
        
          
ion)
(exploitat
  
 
if
  
          
max
arg
=
 
 
)
(
0
q
q
s
ij
ij
k
tabu
ij
β
α η
τ
 
(5.5) 


## Page 7

 
7 
Hybridization and performance improvement 
ACS was applied to the solution of big symmetric and asymmetric traveling 
salesman problems (TSP/ATSP) [36],[25]. For these purpose ACS incorporates an 
advanced data structure known as candidate list [60]. A candidate list is a static 
data structure of length cl which contains, for a given city i, the cl preferred cities 
to be visited. An ant in ACS first uses candidate list with the state transition rules 
to choose the city to move to. If none of the cities in the candidate list can be vis-
ited the ant chooses the nearest available city only using the heuristic value ηij. 
ACS for TSP/ATSP has been improved by incorporating local optimization heu-
ristic (hybridization): the idea is that each time a solution is generated by the ant it 
is taken to its local minimum by the application of a local optimization heuristic 
based on an edge exchange strategy, like 2-opt, 3-opt or Lin-Kernighan [48]. The 
new optimized solutions are considered as the final solutions produced in the cur-
rent iteration by ants and are used to globally update the pheromone trails.  
This ACS implementation combining a new pheromone management policy, a 
new state transition strategy and local search procedures was finally competitive 
with state-of-the-art algorithm for the solution of TSP/ATSP problems [5]. This 
opened a new frontier for ACO based algorithm. Following the same approach 
that combines a constructive phase driven by the pheromone and a local search 
phase that optimizes the computed solution, ACO algorithms were able to break 
several optimization records, including those for routing and scheduling problems 
that will be presented in the following paragraphs. 
5.2.3 ANTS  
ANTS is an extension of the AS proposed in [50], which specifies some underde-
fined elements of the general algorithm, such as the attractiveness function to use 
or the initialization of the trail distribution. This turns out to be a variation of the 
general ACO framework that makes the resulting algorithm similar in structure to 
tree search algorithms. In fact, the essential trait which distinguishes ANTS from a 
tree search algorithm is the lack of a complete backtracking mechanism, which is 
substituted by a probabilistic (Non-deterministic) choice of the state to move into 
and by an incomplete (Approximate) exploration of the search tree: this is the ra-
tionale behind the name ANTS, which is an acronym of Approximated Non-
deterministic Tree Search. In the following, we will outline two distinctive ele-
ments of the ANTS algorithm within the ACO framework, namely the attractive-
ness function and the trail updating mechanism. 
Attractiveness 
The attractiveness of a move can be effectively estimated by means of lower 
bounds (upper bounds in the case of maximization problems) on the cost of the 
completion of a partial solution. In fact, if a state ι corresponds to a partial prob-
lem solution it is possible to compute a lower bound on the cost of a complete so-


## Page 8

 
8 
lution containing ι. Therefore, for each feasible move ι,ψ, it is possible to compute 
the lower bound on the cost of a complete solution containing ψ: the lower the 
bound the better the move. Since a large part of research in ACO is devoted to the 
identification of tight lower bounds for the different problems of interest, good 
lower bounds are usually available. 
When the bound value becomes greater than the current upper bound, it is ob-
vious that the considered move leads to a partial solution which cannot be com-
pleted into a solution better than the current best one. The move can therefore be 
discarded from further analysis. A further advantage of lower bounds is that in 
many cases the values of the decision variables, as appearing in the bound solu-
tion, can be used as an indication of whether each variable will appear in good so-
lutions. This provides an effective way of initializing the trail values. For more de-
tails see [50]. 
Trail update 
A good trail updating mechanism avoids stagnation, the undesirable situation in 
which all ants repeatedly construct the same solutions making any further explora-
tion in the search process impossible. Stagnation derives from an excessive trail 
level on the moves of one solution, and can be observed in advanced phases of the 
search process, if parameters are not well tuned to the problem. 
The trail updating procedure evaluates each solution against the last k solutions 
globally constructed by ANTS. As soon as k solutions are available, their moving 
average z  is computed; each new solution zcurr is compared with z  (and then 
used to compute the new moving average value). If zcurr is lower than z , the trail 
level of the last solution's moves is increased, otherwise it is decreased. Formula 
(5.6) specifies how this is implemented: 






−
−
−
⋅
=
∆
LB
z
LB
zcurr
ij
1
0
τ
τ
 
(5.6) 
where z  is the average of the last k solutions and LB is a lower bound on the 
optimal problem solution cost. The use of a dynamic scaling procedure permits 
discrimination of a small achievement in the latest stage of search, while avoiding 
focusing the search only around good achievement in the earliest stages. 
One of the most difficult aspects to be considered in metaheuristic algorithms is 
the trade-off between exploration and exploitation. To obtain good results, an 
agent should prefer actions that it has tried in the past and found to be effective in 
producing desirable solutions (exploitation); but to discover them, it has to try ac-
tions not previously selected (exploration). Neither exploration nor exploitation 
can be pursued exclusively without failing in the task: for this reason, the ANTS 
algorithm integrates the stagnation avoidance procedure to facilitate exploration 
with the probability definition mechanism based on attractiveness and trails to de-
termine the desirability of moves. 


## Page 9

 
9 
Based on the elements described, the ANTS algorithm is as follows. 
1. 
Compute a (linear) lower bound LB to the problem 
  
Initialize τιψ (∀ι,ψ) with the primal variable values 
2. 
For k=1,m (m= number of ants) do 
  
  repeat 
2.1   
compute ηιψ ∀(ιψ)      
2.2  
choose in probability the state to move into 
2.3  
append the chosen move to the k-th ant’s tabu list  
  
  until ant k has completed its solution 
2.4   carry the solution to its local optimum 
  
end for 
3. 
For each ant move (ιψ),  
  
compute ∆τιψ and update trails by means of (5.6) 
4. 
If not(end_test) goto step 2. 
It can be noted that the general structure of the ANTS algorithm is closely akin 
to that of a standard tree search procedure. At each stage we have in fact a partial 
solution which is expanded by branching on all possible offspring; a bound is then 
computed for each offspring, possibly fathoming dominated ones, and the current 
partial solution is selected from among those associated to the surviving offspring 
on the basis of lower bound considerations. By simply adding backtracking and 
eliminating the MonteCarlo choice of the node to move to, we revert to a standard 
branch and bound procedure. An ANTS code can therefore be easily turned into 
an exact procedure. 
5.3 Significant problems 
In the following of this section we will present applications of ACO algorithms to 
some significant combinatorial optimization problems. This is to give the reader 
an idea of what is involved by the use of an ACO algorithm for a problem: even 
though the last subsection presents an overview of recent application the list is by 
no means exhaustive, as it becomes readily evident by searching the web under the 
keywords “ant colony optimization”. 


## Page 10

 
10
5.3.1 Sequential ordering problem 
The first ACO applications were devoted to solve the symmetric and the asymmet-
ric traveling salesman problem. Given a set of cities V = {v1, ...  , vn}, a set of 
edges A = {(i,j) : i,j ∈V} and a cost dij = dji associated with edge (i,j) ∈ A, the TSP 
is the problem of finding a minimal length closed tour that visits each city once. In 
case dij ≠ dji for at least one edge (i,j) than the TSP becomes an Asymmetric TSP 
(ATSP).  The first algorithm that applies an ACO based algorithm to a more gen-
eral version of the ATSP problem is Hybrid Ant System for the Sequential Order-
ing Problem (HAS-SOP, [34]). HAS-SOP was intended to solve the sequential or-
dering problem with precedence constraints (SOP). The SOP in an NP-hard 
combinatorial optimization problem first formulated by Escudero [29] to design 
heuristics for a production planning system. The SOP models real-world problems 
like production planning [29], single-vehicle routing problems with pick-up and 
delivery constraints [64], and transportation problems in flexible manufacturing 
systems [2]. The SOP can be seen as a general case of both the ATSP and the 
pick-up and delivery problem [47]. It differs from ATSP because the first and the 
last nodes are fixed, and in the additional set of precedence constraints on the or-
der in which nodes must be visited. It differs from the pick-up and delivery prob-
lem because this is usually based on symmetric TSPs, and because the pick-up and 
delivery problem includes a set of constraints between nodes with a unique prede-
cessor defined for each node, in contrast to the SOP where multiple precedences 
can be defined.  
HAS-SOP combines a constructive phase (ACS-SOP) based on the ACS algo-
rithm [36] with a new local search procedure called SOP-3-exchange. SOP-3-
exchange is based on a lexicographic search heuristic due to [64], on a new label-
ing procedure and on a new data structure called don’t push stack inspired by the 
don’t look bit [6] both introduced by the authors. SOP-3-exchange is the first local 
search able to handle multiple precedence constraints in constant time. 
ACS-SOP implements the constructive phase of HAS-SOP but differs from 
ACS in the way the set of feasible nodes is computed and in the setting of one of 
the algorithm’s parameters that is made dependent on the problem dimensions. 
ACS-SOP generates feasible solutions that does not violate the precedence con-
straints with a computational cost of order O(n2) like the traditional ACS heuris-
tic.  
A set of experiments based on the TSPLIB data shows that HAS-SOP algo-
rithm is more effective than other existing methods for the SOP. HAS-SOP was 
compared against the two previous most effective algorithms: a branch-and-cut al-
gorithm [2] that proposed a new class of valid inequalities and Maximum Partial 
Order/Arbitrary Insertion (MPO/AI), a genetic algorithm by Chen and Smith [17].  
To better understand the role of the constructive ACS-SOP phase and the role 
of the SOP-3-exchange local search MPO/AI was also coupled with the SOP-3-
exchange local search. Experimental results shows that MPO/AI alone is better 
than ACS-SOP due to the use of a simple local search embedded in its crossover 
operator. On the contrary, the combination between constructive phase and local 


## Page 11

 
11
search shows that HAS-SOP is better than both MPO/AI alone and MPO/AI + 
SOP-3-exchange. This is probably due to the fact that MPO/AI generates solutions 
that are already optimized and therefore the SOP-3-exchange procedure quickly 
gets stuck. On the contrary, ACS-SOP solution is a very effective starting point 
for the SOP-3-exchange local search therefore the HAS-SOP hybridization is very 
effective. Currently HAS-SOP is the best known method to solve the SOP and was 
able to improve 14 over 22 best known results in the TSPLIB data set. 
5.3.2 Vehicle routing problems 
A direct extension of the TSP, the first problem AS was applied to, are Vehicle 
routing problems (VRPs). These are problems where a set of vehicles stationed at 
a depot has to serve a set of customers before returning to the depot, and the ob-
jective is to minimize the number of vehicles used and the total distance traveled 
by the vehicles. Capacity constraints are imposed on vehicle trips, as well as pos-
sibly a number of other constraints deriving from real-world applications, such as 
time windows, backhauling, rear loading, vehicle objections, maximum tour 
length, etc. The basic VRP problem is the Capacitated VRP (CVRP): ASrank, the 
rank-based version of AS, was applied to this problem by Bullnheimer, Hartl and 
Strauss [7, 8] with good results. These authors used various standard heuristics to 
improve the quality of VRP solutions and modified the construction of the tabu 
list considering constraints on the maximum total tour length of a vehicle and on 
its capacity.  
Following these results, and the excellent ones obtained by ACS with TSP, 
SOP and QAP problems, ACS was applied to a VRP version more close to actual 
logistic practice, called VRPTW. VRPTW is defined as the problem of minimiz-
ing time and costs in case a fleet of vehicles has to distribute goods from a depot 
to a set of customers. The VRPTW minimizes a multiple, hierarchical objective 
function: the first objective is to minimize the number of tours (or vehicles) and 
the second objective is to minimize the total travel time. A solution with a lower 
number of tours is always preferred to a solution with a higher number of tours 
even if the travel time is higher. This hierarchical objectives VRPTW is very 
common in the literature and in case problem constraints are very tight (for exam-
ple when the total capacity of the minimum number of vehicles is very close to the 
total volume to deliver or when customers time windows are narrow), both objec-
tives can be antagonistic: the minimum travel time solution can include a number 
of vehicles higher than the solution with minimum number of vehicles (see e.g. 
Kohl et al., [45]).  
To adapt ACS to a multiple objectives the Multiple Ant Colony System for the 
VRPTW (MACS-VRPTW [38]) has been defined. MACS-VRPTW is organized 
with a hierarchy of artificial ACS colonies designed to hierarchically optimize a 
multiple objective function: the first ACS colony (ACS-VEI) minimizes the num-
ber of vehicles while the second ACS colony (ACS-TIME) minimizes the traveled 
distances. Both colonies use independent pheromone trails but they collaborate by 
exchanging information through mutual pheromone updating. In the MACS-


## Page 12

 
12
VRPTW algorithm both objective functions are optimized simultaneously: ACS-
VEI tries to diminish the number of vehicles searching for a feasible solution with 
always one vehicle less than the previous feasible solution.  
ACS-VEI is therefore different from the traditional ACS applied to the TSP. In 
ACS-VEI the current best solution is the solution (usually unfeasible) with the 
highest number of visited customers, while in ACS the current best solution is the 
shortest one. On the contrary, ACS-TIME is a more traditional ACS colony: ACS-
TIME, optimizes the travel time of the feasible solutions found by ACS-VEI. As 
in HAS-SOP, ACS-TIME is coupled with a local search procedure that improves 
the quality of the computed solutions. The local search uses data structure similar 
to the data structure implemented in HAS-SOP [36] and is based on the exchange 
of two sub-chains of customers. One of this sub-chain may eventually be empty, 
implementing a more traditional customer insertion. 
 
0. MACS-VRPTW algorithm 
1. {Initialization} 
 
Initialize 
gb
ψ
the best feasible solution: lowest number 
of vehicles and shortest travel time.  
2. {Main loop} 
 
Repeat  
 2.1 Vehicles ← #active_vehicles(
gb
ψ
)/*  The number of used 
vehicles is computed */ 
 
 
2.3 Activate ACS-VEI(Vehicles - 1) /* ACS-VEI searches for a 
feasible solution with always one    
vehicle less by maximising the num. 
of visited customers */ 
 
 
2.4 Activate ACS-TIME(Vehicles)/* ACS-TIME is a traditional 
ACS colony that minimises the travel 
time*/ 
 
 
While ACS-VEI and ACS-TIME are active  
 
 
 
Wait for an improved solution ψ  from ACS-VEI or     
ACS-TIME 
 
 
 
2.5 
gb
ψ
 ← ψ  
 
 
 
if #active_vehicles(
gb
ψ
) < Vehicles then 
 
 
 
   
2.6 kill ACS-TIME and ACS-VEI  
 
 
End While 
 
until a stopping criterion is met 
 


## Page 13

 
13
 
Experimentally has been shown that the performance of the system increases in 
case the best solution 
gb
ψ
calculated in ACS-TIME is used, in combination with 
the ACS-VEI best solution 
VEI
ACS −
ψ
, to update the pheromone in ACS-VEI equa-
tion (5.7).  
 
 
 
(
)
VEI
-
ACS
VEI
-
ACS
)
,
(
1
)1
(
)
(
ψ
ρ
τ
ρ
τ
ψ
∈
∀
−
+
−
⋅
=
j
i
L
t
ij
t
ij
 
(5.7) 
(
)
gb
gb
j
i
L
t
ij
t
ij
ψ
ρ
τ
ρ
τ
ψ
∈
∀
−
+
−
⋅
=
)
,
(
          
1
)1
(
)
(
 
 
 
 
MACS-VRPTW has been experimentally proved to be most effective than the 
best known algorithms in the field such as the the tabu search of Rochat and Tail-
lard [61], the large neighbourhood search of Shaw [71] and the genetic algorithm 
of Potvin and Bengio [58]. MACS-VRPTW was also able to improve many results 
in the Solomon problem set both decreasing the number of vehicle or the travelled 
time. 
MACS-VRPTW introduces a new methodology for optimising multiple objec-
tive functions. The basic idea is to coordinate the activity of different ant colonies, 
each of them optimizing a different objective. These colonies work by using inde-
pendent pheromone trails but they collaborate by exchanging information. This is 
the first time a multi-objective function minimization problem is solved with a 
multiple ant colony optimization algorithm. 
5.3.3 Quadratic Assignment Problem  
The quadratic assignment problem (QAP) is the problem of assigning n facilities 
to n locations so that the assignment cost is minimized, where the cost is defined 
by a quadratic function. The QAP is considered one of the hardest CO problems, 
and can be solved to optimality only for small instances. Several ACO applica-
tions dealt with the QAP, starting using AS and then by means of several of the 
more advanced versions [54], [66]. The limited effectiveness of AS was in fact 
improved using a well-tuned local optimizer [53], but several other systems previ-
ously introduced were also adapted to the QAP. For example, two efficient tech-
niques are the MMAS-QAP algorithm [69] and HAS-QAP [39]. For the testing of 
QAP solution algorithms, Taillard [74] proposed to categorize instances into four 
groups: (i) unstructured, uniform random (ii) unstructured, grid distance, (iii) real-
world and (iv) real-world-like. Both MMAS-QAP and HAS-QAP have been ap-
plied to problem instances of type i and iii. The performances of these two heuris-
tic approaches are strongly dependent on the type of problem. Comparisons with 
some of the best heuristics for the QAP have shown that HAS-QAP performs well 
as far as real-world, irregular and structured problems are concerned. On the other 


## Page 14

 
14
hand, on random, regular and unstructured problems the performance of this tech-
nique is less competitive.  
This problem-dependency was not shown by ANTS, which was also applied to 
QAP. In order to apply ANTS to QAP (or any other problem), it is necessary to 
specify the lower bound to use and what is a move in the problem context (step 
2.2). The application described in [50] made the following choices.  
As for the lower bound, since there is currently no lower bound for QAP, which 
is both tight and efficient to compute, the LBD bound was used, which can be 
computed in O(n) but which is unfortunately on the average quite far from the op-
timal solution.  
As for the moves, it was declared that a move corresponds to the assignment of 
a facility to a location, thus adding a new component to the partial solution corre-
sponding to the state from which the move originated. Some considerations on the 
move structure were used to improve the computational effectiveness of the result-
ing algorithm. 
ANTS was tested on instances up to n=40 and showed to be effective on all in-
stance types; moreover its direct transposition into an exact branch and bound was 
also effective when compared to other exact algorithms. 
5.3.4 Other problems 
This section outlines some of the more recent applications of ACO approaches to 
problems other than those listed in the previous ones. This variety is well repre-
sented in the many diverse conference with tracks entirely dedicated to ACO and 
most notably in ANTS conference series, entirely dedicated to algorithms inspired 
by the observation of ants' behavior (ANTS'98, ANTS'2000 and ANTS'2002). 
Many different applications have been presented: from plan merging to routing 
problems, from driver scheduling to search space sharing, from set covering to 
nurse scheduling, from graph coloring to dynamic multiple criteria balancing 
problems. A large part of the relevant literature can be accessed online from [1]. 
Moreover, several introductory overviews have been published. We refer the 
reader to [23], [24] and [52] for other overviews on ACO. 
Among the problems not in the list above, a prominent role is played by the 
TSP. In fact, TSP has been and in many cases still is the first testbed for ACO 
variants, and more in general for most combinatorial optimization metaheuristics 
[68]. It was already on this problem that the limited effectiveness of the first vari-
ants emerged, and this fostered the design of improved approaches modifying 
some algorithm element and possibly hybridizing the framework with greedy local 
search or with other approaches, such as genetic algorithms or tabu seach [69], 
[42], [72]. These variants were then applied to other problems, for example MAX-
MIN ant system was applied to the flow shop problem in [63], a problem then 
faced also with other ACO modifications [10], whereas in [8] a rank-based ap-
proach for the TSP is described or in [14] a so-called best-worst variant. 
More recently, different authors ([75], [44]) have tackled the TSP with hybrid 
variants, mainly using tabu search, but also, in the case of large TSP instances, 


## Page 15

 
15
also with genetic evolution and nearest neighbor search, in order to improve both 
efficiency and efficacy. Moreover, variations of the basic TSP, such as the orien-
teering problem [49] or the probabilistic TSP where clients have to be visited with 
a certain probability [4] have also been studied.  
Scheduling problems provide another common area for testing the effectiveness 
of ACO algorithms. An ACO approach for the job-shop scheduling is presented in 
[12], whereas applications to real-world scheduling cases have been recently de-
scribed in [3] and [62].  
More recently, the maturity of the field is showed by the fact that ACO ap-
proaches began to be proposed also for problems which are not standard combina-
torial optimization testbed, but which are more directly connected to actual prac-
tice. For example, the problem of searching and clustering records of large 
databases is faced by means of ACO in [59], while an algorithm for document 
clustering is described in [78]. Even more theoretical problems linked to spatial 
data analysis were tackled with ACO techniques in [73] and [37]. 
Finally, a recent interesting research branch of ACO, not directly related to 
combinatorial optimization, is about telecommunication. In fact, the area of packet 
switching communications appear to be a promising field for ACO-related routing 
approaches [19, 20]. Whereas a standard optimization version of the frequency as-
signment problem was described in [51], an application to wavelength allocation 
was presented in [57], while techniques for path adaptive search are described in 
[77], [22], [9], [79] and an application to a satellite network in [67]. Moreover, 
applications directly related to communication Quality of Service (QoS) have been 
presented in [28], and more recently in [15], while an application which optimizes 
communication systems with GPS techniques is described in [16]. 
5.4 Convergence proofs  
Recently, some works appeared which provide theoretical insight into the conver-
gence properties of ant colony algorithms. All proofs refer to simplified versions 
of actually used systems, and do not provide direct guidelines for real-world us-
age, but they are of interest for the ascertainment of general properties of the sys-
tems used. 
The first such proofs was proposed by Gutjahr [31], who worked on an ACO 
variant called Graph-Based Ant System (GBAS). The name derives from the 
analysis being carried on a so-called construction graph, which is a graph as-
signed to an instance of the optimization problem under consideration, encoding 
feasible solutions by “walks” on the graph. The objective function value of the 
walk is equal to the objective function value of the corresponding feasible solution 
of the original problem. It is always possible to design a construction graph for 
any given combinatorial optimization problem instance, with a number of nodes 
linear in the number of bits needed for the representation of a solution, and a num-
ber of arcs quadratic in this number of bits. Gutjahr proved that, under the condi-
tions listed below, the solutions generated in each iteration of this Graph-based 


## Page 16

 
16
Ant System converge with a probability that can be made arbitrarily close to 1 to 
the optimal solution of the given problem instance. Essential conditions are: (i) 
there is only one optimal walk in W, i.e., the optimal solution is unique, and it is 
encoded by only one walk in W; (ii) along the optimal walk w*, the desirability 
values satisfy ηkl.(u) > 0 for all arcs (k,l) of w* and the corresponding partial 
walks u of w*; (iii) a version of what is called elitist strategy is used, where only 
the best walks are rewarded: walks that are dominated by another already trav-
ersed walk do not get pheromone increments anymore. Especially the first of these 
conditions is quite restrictive. 
Stützle and Dorigo [65] propose another convergence proof. They consider 
both the MAX-MIN Ant System and the ACS outlined in Section 3, and they 
show that in this case it is possible to prove that allowing more and more iterations 
the cost of the best solution found converges with probability equal to 1 to the op-
timal cost. This a property already guaranteed by random search alone, and it does 
not get lost imposing a minimum trail value. Moreover, the authors show that it is 
possible to compute a lower bound for the probability of the current best solution 
to be optimal.  
Finally, Gutjahr [32] in a recent paper builds upon these results context of ACO 
and shows that for a particular ACO algorithm, a time-dependent modification of 
GBAS, the current solutions converge to an optimal solution with probability ex-
actly one. More specifically, he shows that by using suitable parameter schemes, it 
can be guaranteed that the optimal paths get attractors of the stochastic dynamic 
process realized by the algorithm. This improves all previous results and proves a 
property of the same strength of the tightest one so far obtained in the whole 
metaheuristic area, which was that obtained by Hajek [41] for Simulated Anneal-
ing.  
5.5 Conclusions 
Ant Colony Optimization has been and continues to be a fruitful paradigm for de-
signing effective combinatorial optimization solution algorithms. After more than 
ten years of studies, both its application effectiveness and its theoretical ground-
ings have been demonstrated, making ACO one of the most successful paradigm 
in the metaheuristic area.  
This overview tries to propose the reader both introductory elements and point-
ers to recent results, obtained in the different directions pursued by current re-
search on ACO.  
No doubt new results will both improve those outlined here and widen the area 
of applicability of the ACO paradigm.  
 


## Page 17

 
17
References 
1. 
M. Dorigo, Ant colony optimization web page, 
 
http://iridia.ulb.ac.be/mdorigo/ACO/ACO.html. 
2. 
N. Ascheuer (1995) Hamiltonian path problems in the on-line optimization of flexible 
manufacturing systems. Ph.D.Thesis, Technische Universität Berlin, Germany 
3. 
M. E. Bergen P.van Beek, T. Carchrae (2001) Constraint-based assembly line sequenc-
ing, Lecture Notes in Computer Science, 2056:88-99 
4. 
L. Bianchi, L.M. Gambardella, M. Dorigo (2002) An ant colony optimization approach 
to the probabilistic traveling salesman problem. In Proceedings of PPSN-VII, Seventh 
International Conference on Parallel Problem Solving from Nature, Lecture Notes in 
Computer Science. Springer Verlag, Berlin, Germany, pp 883-892  
5. 
E. Bonabeau, M. Dorigo, G. Theraulaz (2000) Nature, 406(6791):39-42 
6. 
J.L. Bentley (1992) Fast algorithms for geometric traveling salesman problem, ORSA 
Journal on Computing, 4:387-411 
7. 
B. Bullnheimer, R.F. Hartl, C. Strauss (1999) Applying the ant system to the vehicle 
routing problem, In: Voss S., Martello S., Osman I.H., Roucairol C. (eds.) Meta-
Heuristics: Advances and Trends in Local Search Paradigms for Optimization, Klu-
wer, Boston, pp 285-296 
8. 
B. Bullnheimer, R.F. Hartl, C. Strauss (1999) A new rank-based version of the ant sys-
tem: a computational study, Central European Journal of Operations Research 
7(1):25-38 
9.  C. N. Bendtsen, T. Krink (2002) Phone routing using the dynamic memory model, In 
Proceedings of the 2002 congress on Evolutionary Computation, Honolulu, USA, pp 
992-997 
10. C. Blum, M. Sampels (2002) Ant colony optimization for FOP shop scheduling: a case 
study on different pheromone representations, In Proceedings of the 2002 congress on 
Evolutionary Computation, Honolulu, USA, pp 1558-1563 
11. T. Bäck, H.-P. Schwefel (1993) An overview of evolutionary algorithms for parameter 
optimization, Evolutionary Computation 1(1):1-23 
12. M. den Besten, T. Stützle, M. Dorigo (2000) Ant colony optimization for the total 
weighted tardiness problem, In Proceedings Parallel Problem Solving from Nature: 
6th international conference, Lecture Notes in Computer Science. Springer Verlag, 
Berlin, Germany, pp 611-620 
13. A. Colorni, M. Dorigo, V. Maniezzo (1991) Distributed optimization by ant colonies, 
In Proceedings of ECAL'91 European Conference on Artificial Life, Elsevier Publish-
ing, Amsterdam, The Netherlands, pp 134-142 
14.  O. Cordon, I. Fernandez de Viana, F. Herrera, L. Moreno (2000) A new ACO model 
integrating evolutionary computation concepts: the best-worst ant system, In Proceed-
ings of ANTS'2000 - From Ant Colonies to Artificial Ants: Second International Work-
shop on Ant Algorithms, Brussels, Belgium, pp 22-29 
15.  C. Chao-Hsien, G. JunHua, H. Xiang Dan, G. Qijun (2002) A heuristic ant algorithm 
for solving QoS multicast routing problem, in Proceedings of the 2002 congress on 
Evolutionary Computation, Honolulu, USA, pp 1630-1635 
16. D. Camara, A.A.F. Loureiro (2000) A GPS/ant-like routing algorithm for ad hoc net-
works, In Proceeding of 2000 IEEE Wireless Communications and Networking Con-
ference, Chicago, USA, 3:1232-1236 


## Page 18

 
18
17. S. Chen, S. Smith (1996) Commonality and genetic algorithms. Technical Report 
CMU-RI-TR-96-27, The Robotic Institute, Carnegie Mellon University, Pittsburgh, 
PA, USA 
18. M. Dorigo (1992) Optimization, learning and natural algorithms, Ph.D. Thesis, Politec-
nico di Milano, Milano 
19. G. di Caro, M. Dorigo (1998) Antnet: distributed stigmergetic control for communica-
tions networks, Journal of Artificial Intelligence Research, 9:317-365 
20. G. di Caro, M. Dorigo (1998) Mobile agents for adaptive routing, In Proceedings of 
the 31st Hawaii International Conference on System, IEEE Computer Society Press, 
Los Alamitos, CA, pp 74-83 
21. M. Dorigo, V. Maniezzo, A. Colorni (1991) The ant system: an autocatalytic optimiz-
ing process, Technical Report TR91-016, Politecnico di Milano 
22. G. di Caro, M. Dorigo (1998) AntNet: distributed stigmergetic control for communica-
tions network, JAIR, Journal of Artificial Intelligence Research, 9:317-365 
23. M. Dorigo, G. Di Caro (1999) The Ant Colony Optimization Meta-Heuristic. In D. 
Corne, M. Dorigo, F. Glover (eds) New Ideas in Optimization, McGraw-Hill, London, 
UK, pp 11-32 
24. M. Dorigo, G. Di Caro, L.M. Gambardella (1999) Ant Algorithms for Discrete 
Optimization. Artificial Life, 5(2):137-172 
25. M. Dorigo, L.M. Gambardella (1997) Ant colony system: a cooperative learning ap-
proach to the traveling salesman problem, IEEE Transaction on Evolutionary Compu-
tation 1:53-66 
26. M. Dorigo, V. Maniezzo, A. Colorni (1996) The ant system: optimization by a colony 
of cooperating agents, IEEE Transactions on Systems, Man, and Cybernetics-Part B 
26(1):29-41 
27. M. Dorigo, T. Stützle (2002) The ant colony optimization metaheuristic: Algorithms, 
applications and advances. In F. Glover, G. Kochenberger (eds) Handbook of Meta-
heuristics. Kluwer Academic Publishers, Norwell, MA, pp 251-285 
28. G. Di Caro, T. Vasilakos (2000) Ant-SELA: Ant-agents and stochastic automata learn 
adaptive routing tables for QoS routing in ATM networks, In Proceedings of 
ANTS'2000 - From Ant Colonies to Artificial Ants: Second International Workshop on 
Ant Algorithms, Brussels, Belgium, pp 43-46  
29. L.F. Escudero (1988) An inexact algorithm for the sequential ordering problem. Euro-
pean Journal of Operational Research 37:232-253 
30. T.A. Feo, M.G.C. Resende (1995) Greedy randomized adaptive search procedures, 
Journal of Global Optimization 6:109-133 
31. W.J. Gutjahr (2000) A graph-based Ant System and its convergence. Future Genera-
tion Computer Systems. 16:873-888 
32. W.J. Gutjahr (2002) ACO algorithms with guaranteed convergence to the optimal so-
lution. Information Processing Letters 82(3):145-153 
33. F. Glover (1989) Tabu search, ORSA Journal on Computing 1:190-206 
34. L.M. Gambardella, M. Dorigo (2000) An ant colony system hybridized with a new lo-
cal search for the sequential ordering problem, INFORMS Journal on Computing 
12(3):237-255 
35. L.M. Gambardella, M. Dorigo (1995) Ant-Q: a reinforcement learning approach to the 
travelling salesman problem, In Proceedings of the Twelfth International Conference 
on Machine Learning, Morgan Kaufmann, Palo Alto, California, USA, pp 252-260 


## Page 19

 
19
36. L.M. Gambardella, M. Dorigo (1996) Solving Symmetric and Asymmetric TSPs by 
Ant Colonies, In Proceedings of the IEEE Conference on Evolutionary Computation, 
ICEC96, Nagoya, Japan, pp 622-627 
37. Y. Gabriely, E. Rimon (2001) Spanning-tree based coverage of continuous areas by a 
mobile robot, Annals of Mathematics and Artificial Intelligence 31(1-4):77-98  
38. L.M. Gambardella, E. Taillard, G. Agazzi (1999) MACS-VRPTW: A Multiple Ant 
Colony System for Vehicle Routing Problems with Time Windows, In D. Corne, M. 
Dorigo, F. Glover (eds) New Ideas in Optimization, McGraw-Hill, London, UK, pp 63-
76  
39. L.M. Gambardella, E. Taillard, M. Dorigo (1999) Ant colonies for the quadratic as-
signment problem, Journal of the Operational Research Society 50:167-176. 
40. J.H. Holland (1975) Adaptation in natural and artificial systems, University of Michi-
gan Press 
41. B. Hajek (1988) Cooling schedules for optimal annealing, Math. of OR, 13:311-329 
42. H.M. Botee, E. Bonabeau (1999) Evolving ant colony optimization, (SFI Working Pa-
per Abstract) 
43. C. Hurkens, S. Tiourine (1995) Upper and lower bounding techniques for frequency 
assignment problems, Technical Report 95-34, T.U. Eindhoven 
44.  T. Kaji (2001) Approach by ant tabu agents for Traveling Salesman Problem, In Pro-
ceedings of the IEEE International Conference on System, Man and Cybernetics 
45. N. Kohl, J. Desrosiers, O. B. G. Madsen, M. M. Solomon, F. Soumis (1997) K-Path 
Cuts for the Vehicle Routing Problem with Time Windows, Technical Report IMM-
REP-1997-12, Technical University of Denmark 
46. S. Kirkpatrik, C.D. Gelatt, M.P. Vecchi (1983) Optimization by simulated annealing, 
Science 220:671-680 
47. G.A.P. Kindervater, M.W.P. Savelsbergh (1997) Vehicle routing: handling edge ex-
changes, E. H. Aarts, J. K. Lenstra (eds) Local Search in Combinatorial Optimization.  
John Wiley & Sons, Chichester, UK, pp 311-336 
48. S. Lin, B.W. Kernighan, (1973) An effective heuristic algorithm for the traveling 
salesman problem, Operations Research, 21:498–516 
49.  Yun-Chia Liang, S. Kulturel-Konak, A.E. Smith (2002) Meta heuristic for the 
orienteering problem, In Proceedings of the 2002 Congress on Evolutionary 
Computation, Honolulu, USA, pp 384-389 
50. V. Maniezzo (1999) Exact and approximate nondeterministic tree-search procedures 
for the quadratic assignment problem, INFORMS Journal of Computing 11(4):358-369 
51. V. Maniezzo, A. Carbonaro (2000) An ANTS Heuristic for the Frequency Assignment 
Problem, Future Generation Computer Systems; 16, North-Holland/Elsevier, Amster-
dam, 927-935. 
52. V. Maniezzo, A.Carbonaro (2001) Ant Colony Optimization: an overview, in C. 
Ribeiro (ed) Essays and Surveys in Metaheuristics, Kluwer, 21-44 
53. V. Maniezzo, A. Colorni (1999) The ant system applied to the quadratic assignment 
problem, IEEE Transactions on Knowledge and Data Engineering 11(5):769-778 
54. V. Maniezzo, A. Carbonaro (2000) A bionomic approach to the capacitated p-median 
problem, Future Generation Computer Systems 16(8):927-935 
55. V. Maniezzo, R. Montemanni (1999) An exact algorithm for the radio link frequency 
assignment problem, Technical Report CSR99-02 
56. V. Maniezzo, A. Mingozzi, R. Baldacci (1998) A bionomic approach to the capacitated 
p-median problem, Journal of Heuristics 4(3):263-280 


## Page 20

 
20
57. G. Navarro Varela, M. C. Sinclair (1999) Ant Colony Optimization for virtual wave-
length path routing and wavelength allocations, In Proceeding of the Congress on Evo-
lutionary Computation, Washington DC, USA, pp 1809-1816 
58. J.Y. Potvin, S. Bengio (1996) The vehicle routing problem with time windows – part 
II: genetic search, Informs Journal of Computing 8:165-172 
59. R.S. Parpinelli, H.S. Lopes, A.A. Freitas (2002) Data mining with ant colony optimiza-
tion algorithm, in IEEE Transactions on Evolutionary Computation, 6(4):321-332 
60. G. Reinelt (1994) The traveling salesman: computational solutions for TSP applica-
tions. Springer-Verlag 
61. Y. Rochat, E.D. Taillard (1995) Probabilistic diversification and intensification in local 
search for vehicle routing, Journal of Heuristics 1:147-167 
62. H. Shyh-Jier (2001) Enhancement of hydroelectric generation scheduling using ant 
colony system based organization approach, in IEEE Transactions of Energy Conver-
sion, Volume 16(3):296-301 
63. T. Stützle (1998) An Ant Approach to the Flow Shop Problem, In Proceedings of 
EUFIT'98 , Aachen, Germany, pp 1560-1564 
64. M.W.P. Savelsbergh (1990) An efficient implementation of local search algorithms for 
constrained routing problems. European Journal of Operational Research 47:75-85 
65. T. Stützle, M. Dorigo (2002) A Short Convergence Proof for a Class of ACO Algo-
rithms,  IEEE Transactions on Evolutionary Computation,  6(4):358-365 
66. T. Stützle, M. Dorigo (1999) Aco algorithms for the quadratic assignment problem, In 
D. Corne, M. Dorigo, F. Glover (eds) New Ideas in Optimization, McGraw-Hill, Lon-
don, pp 3-50 
67. E. Siegel, B. Denby, S. Le Hégarat-Mascle (2000) Application of ant colony optimiza-
tio to adaptive routing in a telecommunications satellite network, submitted to IEEE 
Trasactions on Networks 
68. T. Stützle, A .Grün, S. Linke, M. Rüttger (2000) A comparison of nature inspired heu-
ristic on the traveling salesman problem, In Deb et al. (eds) In Proceeding of PPSN-
VI, Sixth International Conference on Parallel Problem Solving from Nature, 
1917:661-670 
69. T. Stützle, H. Hoos (2000) MAX-MIN ant system, Future Generation Computer Sys-
tems, Vol. 16(8):889-914 
70. T. Stützle, H. Hoos (1997) Improvements on the ant system: Introducing MAX-MIN 
ant system, In Proceeding of ICANNGA'97, International Conference on Artificial 
Neural Networks and Genetic Algorithms, Springer Verlag, pp 245-249 
71. P. Shaw (1998) Using Constraint Programming and Local Search Methods to Solve 
Vehicle Routing Problems, In Proceeding of Proceedings of the Fourth International 
Conference on Principles and Practice of Constraint Programming, M. Maher, J.-F. 
Puget (eds.), Springer-Verlag, pp 417-43 
72. T. Stützle, H. Hoos (1998) The MAX-MIN Ant System and Local Search for Combi-
natorial Optimization Problems: Towards Adaptive Tools for Combinatorial Global 
Optimization In S. Voss, S. Martello, I.H. Osman, C. Roucairol (eds) Meta-Heuristics: 
Advances and Trends in Local Search Paradigms for Optimization, Kluwer Academic 
Publishers, Boston, pp 313-329 
73. M. Schreyer, G. R. Raidl, (2002) Letting ants labeling point feature, in Proceedings of 
the 2002 congress on Evolutionary Computation, Honolulu, USA, pp 1564-1569 
74. E.D. Taillard (1995) Comparison of iterative searches for the quadratic assignment 
problem, Location Science, 3:87-105 


## Page 21

 
21
75. C. Tsai, C. Tsai, C. Tseng (2002) A new approach for solving large traveling salesman 
problem, In Proceeding of the 2002 Congress of Evolutionary Computation, Honolulu, 
USA, pp 1636-1641 
76. C.J. Watkins, P. Dayan (1992) Q-learning, Machine Learning, 8:279-292 
77. O. Wittnr, B. E. Helvik, (2002) Cross-entropy guided ant-like agents finding depend-
able primary/backup path patterns in networks, In Proceedings of the 2002 congress 
on Evolutionary Computation, Honolulu, USA, pp 1528-1533 
78. B. Wu, Y. Zheng, S. Liu, Z. Shi, (2002) CSIM: a document clustering algorithm based 
on swarm intelligence, In Proceedings of the 2002 congress on Evolutionary Computa-
tion, Honolulu, USA, pp 477-482 
79 . W. Ying, X. Jianying (2000) Ant colony optimization for multicast routing, In Pro-
ceeding of the 2000 IEEE Asia-Pacific Conference on Circuits and Systems, Tianjin, 
China 



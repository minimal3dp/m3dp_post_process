# 

**Source:** `Ant_Colony_Optimization_An_Overview.pdf`
---

## Page 1

Ant Colony Optimization:
an overview
Vittorio Maniezzo
University of Bologna, Italy


## Page 2

Vittorio Maniezzo - University of Bologna
2/52
Metaheuristics
Metaheuristics include:
• Simulated Annealing
• Tabu Search
• GRASP
• Genetic Algorithms
• Variable Neighborhood Search
• …
• ACO


## Page 3

Vittorio Maniezzo - University of Bologna
3/52
Ant System
Ant System (AS) was the first ACO algorithm 
presented [CDM91]. 
The idea it was to modify a constructive heuristic so 
that the ordering of the components could be
recalculated at each iteration taking into account
•
the a priori expectation, ηi, of the usefulness of a 
particular component ci as in standard 
constructive approaches, 
•
but also an a posteriori measure, τi, of the 
goodness of solutions constructed using that 
particular component.


## Page 4

Vittorio Maniezzo - University of Bologna
4/52
Ant System
•
general purpose heuristic inspired by nature;
•
parallel distributed search effort;
• combines a problem-specific constructive
heuristic (visibility) and a general-purpose 
adaptive problem representation


## Page 5

Vittorio Maniezzo - University of Bologna
5/52
ACO
Ant Colony Optimization is the name given by 
M.Dorigo [D98] to a class of algorithms whose first 
member was AS. 
The main underlying idea is that of parallelizing
search over several constructive computational 
threads, all based on a dynamic memory structure
with information on the effectiveness of previously
obtained results and in which the behavior of each 
single agent is inspired by the behavior of real ants.
Web page: 
http:/ / iridia.ulb.ac.be/ ~mdorigo/ ACO/ ACO.html


## Page 6

Vittorio Maniezzo - University of Bologna
6/52
The biological metaphor
A
E
A
E
Obstacle
C
H
D
B
Obstacle
A
E
B
D
C
H
B
D
C
H
d=1
d=1
d=0.5
d=0.5
E
A
B
D
C
H
15 ants
t=0
E
A
15 ants
15 ants
15 ants
30 ants
30 ants
B
D
C
H
10 ants
t=1
E
A
20 ants
20 ants
10 ants
30 ants
30 ants
τ=15
τ=15
τ=30
τ=30


## Page 7

Vittorio Maniezzo - University of Bologna
7/52
Ant agents
An ant is defined to be a simple computational
agent, which iteratively constructs a solution for the 
problem to solve. 
Partial problem solutions are seen as states; each 
ant moves from a state ι to another one ψ, 
corresponding to a more complete partial solution. 
At each step σ, each ant k computes a set of 
feasible expansions to its current state, and moves 
to one of these in probability, according to a 
probability distribution specified as follows. 


## Page 8

Vittorio Maniezzo - University of Bologna
8/52
Probability of a move
The formula for defining the probability distribution 
at each move makes use of a set tabuk which 
indicates a set of infeasible moves for ant k. 
Probabilities are computed as follows:
Parameter α defines the relative importance of trail 
with respect to attractiveness. 
(
)





∉
ιψ
η
⋅
α
−
+
τ
⋅
α
η
⋅
α
−
+
τ
⋅
α
=
∑
∉
ιν
ιν
ιν
ιψ
ιψ
ιψ
otherwise
0
tabu
)
( 
if
)
1(
)
1(
p
k
tabu
)
(
k
k


## Page 9

Vittorio Maniezzo - University of Bologna
9/52
Trail update
Trails are updated at each iteration, increasing the 
level of those related to moves that were part of 
"good" solutions, while decreasing all others. 
After each iteration t of the algorithm, trails are 
updated using the following formula.
where ρ is a user-defined coefficient and ∆τιψ
represents the sum of the contributions of all ants 
that used move (ιψ) to construct their solution.
ιψ
ιψ
ιψ
τ
ρτ
τ
∆
+
−
=
)1
(
)
(
t
t


## Page 10

Vittorio Maniezzo - University of Bologna
10/52
Attractiveness and trail
For ant k, the probability pιψ of moving from state ι
to state ψ depends on the combination of two 
values:
•
the attractiveness η of the move, as computed by 
some heuristic indicating the a priori desirability 
of that move;
•
the trail level τ of the move, indicating how 
proficient it has been in the past to make that 
particular move, the a posteriori the 
desirability of that move.


## Page 11

Vittorio Maniezzo - University of Bologna
11/52
CCA0 example
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
2
3
4
5
6
7
8
9
10


## Page 12

Vittorio Maniezzo - University of Bologna
12/52
ACO pseudo code
1
(Initialization)
Initialize τιψ, ∀ι,ψ
2
(Construction)
For each ant k do
repeat
compute ηιψ ∀ι,ψ
choose in probability the state to move into 
append the chosen move to the k-th ant’s set tabuk
until ant k has completed its solution
[apply a local optimization procedure]
enddo
3. (Trail update)
For each ant move (ι,ψ) do
compute ∆τιψ and update the trail values 
4. (Terminating condition)
If not(end_condition) go to step 2.


## Page 13

Vittorio Maniezzo - University of Bologna
13/52
Ant System
1. Initialize a set A of partial solutions
ai=∅, i=1, … , m.
2. For i=1 to m
choose a component cj to append to solution ai with 
probability given as a function of ai, ηj, τj.
3. If the solutions in A are not complete, go to step 2.
4. Evaluate z(ai), i=1, … , m and update τj, j=1, … , n
accordingly.
5. If not (end condition) go to step 1.


## Page 14

Vittorio Maniezzo - University of Bologna
14/52
ANTS conferences
The ACO has been specified in different ways by 
different authors. 
This variety was represented in the ANTS series of 
international workshops (ANTS'98, ANTS‘2000 and 
ANTS'2002), conferences entirely devoted to
algorithms inspired by the observation of ants 
behavior. 
Many applications: from plan merging to routing
problems, from driver scheduling to search space 
sharing, from set covering to nurse scheduling, from 
graph coloring to dynamic multiple criteria 
balancing problems, etc.


## Page 15

Vittorio Maniezzo - University of Bologna
15/52
ACO approaches
ABC    
Bonabeau et al. [B98], van der Put, Rothkrantz 
[vdPR98] 
 network routing
ACS    
Dorigo, Ganbardella [DG97]  
 TSP, VRP
AntNet Di Caro, Dorigo [DCD97], [DCD98] 
 network routing
ANTS   Maniezzo [M98] , Maniezzo, Carbonaro [MC99] 
 QAP, FAP
AS     
Colorni, Dorigo, Maniezzo [CDM91], [D92], 
[CDMT94], [DMC96] 
 TSP, QAP, JSP
ASrank Bullnheimer, Hartl, Strauss [BHS97] 
 TSP, VRP
HAS    
Gambardella, Taillard, Dorigo [GTD99]  
 QAP, VRP, SOP
MMAS   Stuetzle, Hoos [SH98,SD99] 
 TSP, QAP
AS-SCS Michel, Middendorf [MM98] 
 SCS
- 
Costa, Hertz [CH97] 
 GCP
- 
Merkle, Middendorf, Schmeck [MM00,MMS00] 
 Scheduling Problems
- 
Gambardella, Dorigo [GD00] 
 SOP
- 
Kawamura et al. [KYSO00] 
 TSP


## Page 16

Vittorio Maniezzo - University of Bologna
16/52
Max-min ant system
Stuetzle and Hoos  [SH97] introduced Max-Min Ant 
System (MMAS), a modification of AS. 
They use two parameters, a maximum and minimum 
trail levels, in order to restrict possible trail values to 
the interval [τmin, τmax]. 
Moreover, MMAS controls the trail levels (initialized to 
their maximum value τmax, only allowing the best ant 
at each iteration to update trails. 
Trails that receive very rare reinforcements will lower 
their strength and will be selected more and more 
rarely by the ants, until they reach the τmin value. 


## Page 17

Vittorio Maniezzo - University of Bologna
17/52
AS-rank
Bullnheimer, Hartl and Strauss [BHS97] proposed yet 
another modification of AS, called AS-rank, 
introducing a rank-based version of the probability 
distribution to limit the danger of over-emphasized 
trails caused by many ants using sub-optimal
solutions. 
At each iteration the ants are sorted by solution 
quality and the contribution of an ant to the trail 
level update is weighted according to the rank of 
the ant, considering only the Ωbest ants.


## Page 18

Vittorio Maniezzo - University of Bologna
18/52
Ant Colony System
Gambardella and Dorigo [GD95, 97] proposed ACS, 
where trails are updated with (constant) values which 
predict the quality of solution using the relative edges. 
Trail values are added offline only to the arcs 
belonging to the best tour so far, while ants perform 
online step-by-step trail updates to favor the
emergence of other solutions. 
Each ant uses a pseudo-random proportional rule to 
choose the next node to move to based on a q0 ∈[0,1]
parameter that modulates the exploration inclinacy. 
ACS also uses a data structure associated to vertices 
called candidate list, as in GRASP.


## Page 19

Vittorio Maniezzo - University of Bologna
19/52
ANTS
1
(Initialization)
Compute a (linear) lower bound LB to the problem to solve
Initialize τιψ, ∀ι,ψ with the primal variable values
2
(Construction)
For each ant k do
repeat
compute ηιψ ∀ι,ψ, as a lower bound to the cost of 
completing a solution containing ι,ψ
choose in probability the state to move into 
append the chosen move to the k-th ant’s set tabuk
until ant k has completed its solution
apply a local optimization procedure
enddo
3. (Trail update)
For each ant move (ι,ψ) do
compute ∆τιψ and update the trail values 
4. (Terminating condition)
If not(end_test) go to step 2.


## Page 20

Vittorio Maniezzo - University of Bologna
20/52
Convergence
W.Gutjahr [W00] proposed a convergence proof for 
AS.
For a restricted version of AS and using suitable 
parameter values (many ants or little evaporation), 
the propobability of AS achieving an optimal 
solution can be made arbitrarily close to 1.


## Page 21

Vittorio Maniezzo - University of Bologna
21/52
Current applications …
Applications are listed by class of problems and in 
chronological order (from Dorigo, Gambardella, 2003).
Problem name
Authors
Algorithm name Year
Traveling salesman
Dorigo, Maniezzo, Colorni
AS
1991
Gambardella, Dorigo
Ant-Q
1995
Dorigo, Gambardella
ACS, ACS-3-opt 1996
Stuetzle, Hoos
MMAS
1997
Bullnheimer, Hartl, Strauss
ASrank
1997
Cordòn, et al.
BWAS
2000
Quadratic assignment Maniezzo, Colorni, Dorigo
AS-QAP
1994
Gambardella, Taillard, Dorigo HAS-QAP
1997
Stuetzle, Hoos
MMAS-QAP
1997
Maniezzo
ANTS
1998
Maniezzo, Colorni
AS-QAP
1999
Scheduling problems
Colorni, Dorigo, Maniezzo
AS-JSP
1994
Stuetzle
AS-FSP
1997
Bauer et al.
ACS-SMTTP
1999
den Besten, Stuetzle, Dorigo
ACS-SMTWTP
1999
Merkle, Middendorf, Schmeck ACO-RCPS
2000


## Page 22

Vittorio Maniezzo - University of Bologna
22/52
Current applications (cont.)
Problem name
Authors
Algorithm name
Year
Vehicle routing
Bullnheimer, Hartl, Strauss
AS-VRP
1997
Gambardella, Taillard, Agazzi HAS-VRP
1999
Connection-oriented
Schoonderwoerd et al.
ABC
1996
network routing
White, Pagurek, Oppacher
ASGA
1998
Di Caro, Dorigo
AntNet-FS
1998
Bonabeau et al.
ABC-smart ants
1998
Connection-less
Di Caro, Dorigo
AntNet, AntNet-FA
1997
network routing
Subramanian, Druschel, Chen  Regular ants
1997
Heusse et al.
CAF
1998
van der Put, Rothkrantz
ABC-backward
1998
Sequential ordering
Gambardella, Dorigo
HAS-SOP
1997
Graph coloring
Costa, Hertz
ANTCOL
1997
Shortest common supersequence Michel, Middendorf AS-SCS
1998
Frequency assignment
Maniezzo, Carbonaro
ANTS-FAP
1998
Generalized assignment Ramalhinho Lourenco, Serra MMAS-GAP
1998
Multiple knapsack
Leguizamòn, Michalewicz
AS-MKP
1999
Optical networks routing Navarro Varela, Sinclair
ACO-VWP
1999
Redundancy allocation
Liang, Smith
ACO-RAP 
1999
Constraint satisf.
Solnon
Ant-P-solver 
2000


## Page 23

Reality bites
Real-world ACO applications


## Page 24

Vittorio Maniezzo - University of Bologna
24/52
An ACO-based company!


## Page 25

Vittorio Maniezzo - University of Bologna
25/52
Car pooling


## Page 26

Vittorio Maniezzo - University of Bologna
26/52
Stochastic VRP


## Page 27

Vittorio Maniezzo - University of Bologna
27/52
Urban solid waste collection


## Page 28

Vittorio Maniezzo - University of Bologna
28/52
Civil protection


## Page 29

Vittorio Maniezzo - University of Bologna
29/52
Traffic flow optimization



# Dynamic Path Optimization Based on Improved Ant Colony Algorithm
**Subject:** Journal of Advanced Transportation 2023.2023:7651100

**Source:** `Journal of Advanced Transportation - 2023 - Cheng - Dynamic Path Optimization Based on Improved Ant Colony Algorithm.pdf`
---

## Page 1

Research Article
Dynamic Path Optimization Based on Improved Ant
Colony Algorithm
Juan Cheng
Jinling Institute of Technology, Nanjing 211169, China
Correspondence should be addressed to Juan Cheng; apriljj@163.com
Received 20 June 2022; Revised 19 December 2022; Accepted 18 March 2023; Published 17 April 2023
Academic Editor: Wen Liu
Copyright © 2023 Juan Cheng. Tis is an open access article distributed under the Creative Commons Attribution License, which
permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.
Dynamic path optimization is an important part of intelligent transportation systems (ITSs). Aiming at the shortcomings of the
current dynamic path optimization method, the improved ant colony algorithm was used to optimize the dynamic path. Trough
the actual investigation and analysis, the infuencing factors of the multiobjective planning model were determined. Te ant
colony algorithm was improved by using the analytic hierarchy process (AHP) to transform path length, travel time, and trafc
fow into the comprehensive weight-infuencing factor. Meanwhile, directional guidance and dynamic optimization were in-
troduced to the improved ant colony algorithm. In the simulated road network, the length of the optimal path obtained by the
improved ant colony algorithm in the simulation road network is 3.015, which is longer than the length of the optimal path
obtained by the basic ant colony algorithm (2.902). Te travel time of the optimal path obtained by the improved ant colony
algorithm (376 s) is signifcantly shorter than that of the basic ant colony algorithm (416.3 s). Te number of iterations of the
improved ant colony algorithm (45) is less than that of the basic ant colony algorithm (58). In the instance network, the number of
iterations of the improved ant colony algorithm (18) is less than that of the basic ant colony algorithm (26). Te travel time of the
optimal path obtained by the improved ant colony algorithm (377.1 s) is signifcantly shorter than that of the basic ant colony
algorithm (426 s) and the spatial shortest distance algorithm (424 s). Compared with the basic ant colony algorithm and the spatial
shortest distance algorithm, the results of the optimal path obtained by the improved ant colony algorithm were more accurate,
and the efectiveness of the improved ant colony algorithm was verifed.
1. Introduction
In intelligent transportation systems, path optimization is an
essential part. Obtaining real-time and accurate trafc in-
formation is important for estimating the trafc conditions at
the next moment and has a signifcant position in trafc
guidance. Path optimization helps the traveler to constantly
adjust his driving route according to the actual trafc condi-
tions during driving, and reach the destination quickly and
efciently. Te ultimate goal of path optimization is to optimize
the distribution of trafc fow throughout the road network,
thus solving urban trafc congestion problems fundamentally,
improving road capacity and travel comfort, and alleviating
environmental pollution caused by automobile exhaust.
To solve the trafc congestion, trafc accidents, trafc
pollution, and other problems existing in the current road
trafc, it is impossible to rely on trafc demand management
alone. It is urgent to implement an intelligent transportation
system to improve the utilization rate of the existing road
network. In the face of increasingly serious trafc problems,
trafc managers and trafc participants need to obtain real-
time and accurate trafc information of road sections in time
to provide basis for dynamic management decisions and
travel decisions. Because link travel time and dynamic path
optimization can efectively improve travel efciency in the
driving process, travel time estimation and prediction and
dynamic path optimization have become one of the issues in
the trafc feld.
Trough investigation and analysis, the dynamic road
multiobjective planning model is established with the path
length, travel time, and trafc fow as the targets. Te analytic
hierarchy process (AHP) is used to transform the path
Hindawi
Journal of Advanced Transportation
Volume 2023, Article ID 7651100, 11 pages
https://doi.org/10.1155/2023/7651100


## Page 2

length, travel time, and trafc fow into the comprehensive
weight-infuencing factor, and then the ant colony algorithm
is improved. Te improved ant colony algorithm is used to
optimize the dynamic path.
Te rest of the paper is structured as follows: a brief
review is given in the next section. Section 3 discussed the
dynamic path multiobjective programming model followed
by Section 4, which describes the improved ant colony al-
gorithm. Results and discussion are presented in Section 5.
Finally, the conclusions are outlined in Section 6.
2. Literature Review
Dynamic path optimization can not only integrate real-time
trafc information, but also accurately predict trafc fow
parameters in future time based on detected real-time trafc
information. Te dynamic path optimization algorithm
provides path planning to the driver, which can be planned
before travel or during travel. Researchers have carried out
a lot of study on dynamic path optimization algorithms and
achieved fruitful results. Bauer et al. [1] introduced layering
technology and target acceleration technology in the Dijk-
stra algorithm, which improved the data storage capacity of
the road network and the efciency of the algorithm. Wei
and Meng [2] optimized the dynamic path using the im-
proved Dijkstra algorithm, a weight function was introduced
to the improved algorithm, and the weight was determined
according to the degree of trafc congestion. Te A∗al-
gorithm for the unbalanced search was proposed by Pijls and
Post [3]. Te proposed algorithm improved the path search
ability and narrowed the search range. However, the stability
of the solution obtained by this method was poor. Atila et al.
[4] applied the improved genetic algorithms for route
guidance with the shortest travel time, which introduced
a genetic search method in the crossover operation of genetic
algorithms. Te experimental results showed that the im-
proved genetic algorithm enhanced the computational ef-
fciency compared with the traditional genetic algorithm. An
improved ant colony algorithm was developed by D’Acierno
et al. [5]. Te algorithm divided ants into two categories, one
for path selection and one for setting signals at intersections.
Te improved ant colony algorithm solved the problem of
asymmetric trafc assignment. Yu et al. [6] presented an
improved ant colony algorithm. In this algorithm, the path
length, road slope, and trafc condition were equivalent to
the weight of the path, and the improved ant colony algo-
rithm was applied to the TSP problem. Experimental results
showed that the improved ant colony algorithm was feasible.
Kobayashi et al. [7] studied the dynamic path optimization
algorithm of the trafc network. Taking the shortest distance
and the shortest travel time as constraints, a road network
with 12 light-controlled intersections was simulated. Che
et al. [8] proposed an improved ant colony optimization
algorithm based on the particle swarm optimization algo-
rithm. Experiment results demonstrate that improved ant
colony optimization algorithm is more efective and feasible
in path planning for autonomous underwater vehicles than
the traditional ant colony algorithm. Research on trajectory
optimization to realize real-time collision avoidance under
complex driving conditions, a hierarchical three-layer tra-
jectory planning framework was presented by Zhang et al.
[9]. Te simulation results showed that the proposed scheme
is efective in various scenarios. In order to avoid subsequent
collisions and stabilize vehicles, Wang et al. [10] proposed
a postcollision motion planning and stability control
method for autonomous vehicles. Trough the hardware in
the loop test, the proposed scheme is verifed in the in-
tegrated driving scenario. Zhang et al. [11] made a com-
prehensive and systematic review of chassis-coordinated
control methods for full-line control vehicles, summarized
the research progress in recent years, and introduced the
identifcation methods of diferent working conditions
under steering and braking conditions.
In summary, the application of dynamic path optimi-
zation in the trafc feld is more and more mature. Te
dynamic path optimization algorithms include Dijkstra al-
gorithm, heuristic algorithm [12], genetic algorithm, ant
colony algorithm, and so on. Te algorithm used in the
existing literature employed the path length as the weight,
the dynamic travel time calculation generally used the BPR
function, and the data obtained from the fxed detector data
or trafc simulation data. However, the path optimization
under a dynamic road network not only requires the optimal
path search based on real-time trafc information, but also
requires stability, fast convergence, and low complexity of
the algorithms. Terefore, artifcial intelligence algorithms
that can realize dynamic characteristics are the development
trend of dynamic path optimization algorithms.
Te ant colony algorithm has the characteristics of
parallelism, positive feedback, and self-organization ability.
Terefore, the ant colony algorithm is introduced to opti-
mize the dynamic path. To make the ant colony algorithm
more suitable for dynamic path optimization, the ant colony
algorithm is improved in this paper. Te novelties in this
paper are as follows: (1) path length conversion, (2) add
directional guidance, and (3) dynamic optimization.
3. Dynamic Path Multiobjective
Programming Model
At present, most of the path optimization has a single se-
lection criterion, which is the minimum travel time or the
shortest travel distance. However, surveys have shown that
in London and Paris, 42% of travelers use the combination of
the minimum travel time and the shortest travel distance to
select the optimal path, and 56% of travelers use the min-
imum travel time as the standard for the optimal path. In
Munich, 71% of travelers use the combined standard with
the minimum travel time and the shortest travel distance to
select the path, and only 27% of travelers use the minimum
travel time as the path selection criterion [13]. It can be seen
that travelers prefer multiple criteria rather than a single
criterion when optimizing travel routes.
3.1. Dynamic Path Multiobjective Programming Model. In
the dynamic trafc network, the factors afecting the trav-
elers should be considered comprehensively to fnd the
2
Journal of Advanced Transportation
 1409, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2023/7651100, Wiley Online Library on [23/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## Page 3

optimal path. In order to understand the factors afecting
travelers, questionnaires were used to investigate the factors
that infuence path optimization. In the questionnaire, the
factors that afect path optimization were path length, road
width, travel time, trafc fow, road slope, road performance,
trafc speed, number of intersections, weather, and so on.
Te questionnaires issued in the survey were 890. In addition
to the survey conducted by the conventional method, the
survey was conducted using QQ and WeChat. Finally, 543
valid questionnaires were collected. Trough the analysis of
the recovered questionnaire, it was found that the path
length, travel time, and trafc fow were the three main
factors afecting path optimization. Terefore, the infuence
of path length, travel time, and trafc fow on path opti-
mization should be considered comprehensively in the
process of path optimization. Te statistical distribution of
various infuencing factors is shown in Figure 1.
Te traveler will choose the path with the shortest travel
distance and the minimum travel time in the trafc state of
free-fow. While in the trafc state of transition and con-
gestion, the traveler will choose the path with less travel time
and travel distance relatively short and try to avoid
crowded paths.
3.1.1. Optimal Path Based on the Shortest Travel Distance.
Te shortest travel distance refers to the shortest path chosen
from the starting point O to the ending point D, as shown in
the following equation:
W1  min Lod
k
􏽮
􏽯,
s.t.
Lod
k  􏽘
i
liδod
i,k,
i ∈A, k ∈Kod,
⎧
⎪
⎨
⎪
⎩
(1)
where li is the geometric length of road i. δod
i,k is 1 if road i is
on the feasible path k connecting the OD, otherwise δod
i,k is 0.
3.1.2. Optimal Path Based on the Minimum Travel Time.
Te minimum travel time indicates the path with the least
travel time from the starting point O to the ending point D,
which is shown in the following equation:
W2  min Tod
k
􏽮
􏽯,
s.t.
Tod
k  􏽘
i
ti(t)δod
i,k,
i ∈A, k ∈Kod,
⎧
⎪
⎨
⎪
⎩
(2)
where ti(t) is the average travel time of road i at time t. δod
i,k is
1 if road i is on the feasible path k connecting the OD,
otherwise δod
i,k is 0.
3.1.3. Optimal Path Based on the Least Trafc Flow.
Trafc fow is an indicator of congestion. Te least trafc
fow is the path with the minimum trafc fow from the
starting point O to the ending point D, that is, the path with
the least congestion is selected, as indicated in the following
equation:
W3  min Qod
k
􏽮
􏽯,
s.t.
Qod
k  􏽘
i
qi(t)δod
i,k,
i ∈A, k ∈Kod,
⎧
⎪
⎨
⎪
⎩
(3)
where qi(t) is the average trafc fow of road i at time t. δod
i,k is
1 if road i is on the feasible path k connecting the OD,
otherwise δod
i,k is 0.
Trough the abovementioned analysis, the infuence of
path length, travel time, and trafc fow should be consid-
ered in the dynamic path optimization process. Consistent
with the method used by Yu et al. [6], the AHP is also used to
calculate the weight of each infuencing factor, and then
transforms the factors afecting the path optimization into
a comprehensive weighting infuencing factor.
3.2. Analytic Hierarchy Process. Te AHP was proposed by
the American operations researcher Professor Saaty in the
mid 1970 s. AHP can classify various factors that afect the
problem, determine the relationship between the various
factors, and establish a multilevel structural model of the
infuencing factors [6].
3.2.1. Establishing the Hierarchy Model. In this paper, the
structure of the model is divided into two layers, namely, the
target layer A and the criterion layer B. Te weight of the
path optimization in the target layer is wij, and the weights of
the path length, travel time, and trafc fow in the criterion
layer are w1, w2, and w3, respectively, as shown in Figure 2.
3.2.2. Constructing the Judgment Matrix. Te uniform
matrix method was proposed to determine the weight be-
tween each infuencing factor. aij is the comparison result of
the importance between element i and element j. Table 1 is
the nine important levels and assignments given by Saaty.
3.2.3. Hierarchical Single Arrangement. Te eigenvector
corresponding to the maximum eigenvalue λmax of the
judgment matrix is denoted as W after normalization
(making the sum of all elements in the vector equal to 1). Te
element of W is the ranking weight of the same level factor
for the relative importance of the previous level factor. Tis
process is called hierarchical single arrangement. Te cal-
culation steps are presented as follows:
Step (1): multiplying element of each row in the
judgment matrix A, that is, Mi  􏽑n
j1aij, i  1, 2 · · · n
Step (2): calculating the n −th root of Mi, wi
−


Mi
n􏽰
Step (3): if wi
−
is normalized to wi  wi
−/􏽐n
j1wj
−, then
wi is the eigenvector
Step
(4):
calculating
the
maximum
eigenvalue,
λmax ≈􏽐n
i1(AW)i/nwi
3.2.4. Consistency Test. Te consistency test is to determine
the allowable range of inconsistency in the judgment matrix
Journal of Advanced Transportation
3
 1409, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2023/7651100, Wiley Online Library on [23/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## Page 4

A, which the test standard is indicated in the following
equation:
CR  CI
RI ,
(4)
where CR is the conformance ratio. When its value is less
than 0.1, the judgment matrix passes the consistency test;
otherwise, it needs to be corrected. CI is the consistency
index, CI  λmax −n/n −1. RI is the random consistency
index, determined by the order of the judgment matrix,
which is shown in Table 2.
Among the 543 valid questionnaires, 291 questionnaires
were selected with the path length, travel time, and trafc
fow as the top three infuencing factors. Te judgment
matrix of this paper is determined by 291 questionnaires and
the scale method of Table 1. Te constructed judgment
matrix is shown in Table 3.
Te weight of the criterion layer is determined by the
eigenvalue method mentioned above.
Te maximum eigenvalue is λmax  3.0385. Te con-
sistency
test
result
is
CR  CI/RI  0.0193
/0.58  0.0333 < 0.1, indicating that the constructed judg-
ment matrix passes the consistency test. Te eigenvalue of
the criteria layer is w1  0.637, w2  0.258, and w3  0.105.
3.3. Quantifcation of Infuencing Factors. Te factors af-
fecting path optimization in this paper are path length, travel
time, and trafc fow, but the dimensions of the three
infuencing factors are inconsistent. In order to apply the
infuence of diferent factors on path optimization, di-
mensionless processing of diferent infuencing factors is
required. Te extremum method is used to perform di-
mensionless processing infuencing factors [14], and the
variables are transformed into (0, 1]. Te transformation
equation is indicated as follows:
xi′ 
xi
max xi
,
(5)
where xi′ is the dimensionless value of xi. max xi is the
maximum value of xi.
Te weights of the infuencing factors in the criterion
layer are obtained through Section 3.2. Ten, the compre-
hensive weight-infuencing factor of the path is calculated
considering the three factors of path length, travel time, and
trafc fow as follows:
sij  w1 · dij + w2 · tij + w3 · nij,
(6)
where sij is the comprehensive weight-infuencing factor
considering path length, travel time, and trafc fow. dij is
the
dimensionless
value
of
path
length.
tij
is
the
0
100
200
300
400
500
600
path length
travel time
traffic flow
traffic speed
number of intersections
road width
road performance
road slope
weather
other factor
Figure 1: Statistical distribution diagram of various infuencing factors afecting path optimization.
path optimization wij
path length w1
travel time w2
traffic flow w3
target layer A
criterion layer B
Figure 2: Te layering diagram of path optimization.
4
Journal of Advanced Transportation
 1409, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2023/7651100, Wiley Online Library on [23/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## Page 5

dimensionless value of travel time. nij is the dimensionless
value of travel fow. w1, w2, andw3 are the weights of each
infuencing
factor
in
the
criteria
layer,
w1  0.637,
w2  0.258, and w3  0.105.
4. The Improved Ant Colony Algorithm
Te classic application of the ant colony algorithm is the TSP
problem. In order to make the ant colony algorithm more
suitable for dynamic path optimization, the ant colony al-
gorithm is improved.
4.1. Te Improved Ant Colony Algorithm
4.1.1. Path Length Conversion. Based on Section 3.2, path
length, travel time, and trafc fow are comprehensively
considered, and the comprehensive weight-infuencing
factors of each infuencing factor are taken as path length,
which is shown in equation (4).
4.1.2. Adding Directional Guidance. In the ant colony al-
gorithm, ηij(t) is a heuristic function, representing the
expectation between city i and city. Among them, ηij(t) 
1/dij is the reciprocal of the distance between adjacent
nodes. Te smaller the dij is, the greater the pk
ij(t) is. Te
smaller the distance is, the more likely the ant is to select the
next node. Tis defnition is applicable to unordered TSP
problems, but for ordered path optimization problems, this
search method will reduce the search efciency. Te A∗
algorithm is introduced to improve ηij(t). In order to be
consistent with the abovementioned, equation (7) is di-
mensionless according to the method of Section 3.3 as
follows:
ηij(t) 
1
dij + djD
,
(7)
where ηij(t) is the heuristic function, djD is the di-
mensionless value of the length between node j and the
ending point D, and dij is the dimensionless value of the
length between adjacent nodes i and j.
Te visibility function is improved comprehensively
considering equations (1) and (2) as follows:
ηij(t) 
1
sij + djD
.
(8)
4.1.3. Dynamic Optimization. When the information in the
road network changes, the path should be reoptimized
according to the changed information. Terefore, when the
ant selects the next node, it checks whether the information
in the road network changes. If the change occurs, the
pheromone concentration needs to be updated, as shown in
the following equation:
τ(t + 1)  tt+1
tt
· τ(t),
(9)
where τ(t + 1) is the pheromone concentration on path ij at
time t + 1, tt+1 is the travel time on path ij at time t + 1, tt is
the travel time on path ij at time t, and τ(t) is the pher-
omone concentration on path ij at time t.
4.2. Design of the Improved Ant Colony Algorithm. Te
improved
ant
colony
algorithm
is
applied
to
path
optimization.
4.2.1. Ant Transfer Rule. Te ant moves from node i to node
j according to the following equation:
j 
argmax
τij(t)
􏽨
􏽩
α · ηij(t)
􏽨
􏽩
β
􏼚
,
q < q0,
Pk
ij(t),
q ≥q0,
⎧
⎪
⎪
⎨
⎪
⎪
⎩
(10)
where q is a random variable uniformly distributed on [0,1].
q0 is the parameter that controls the movement rule,
q0 ∈[0, 1]. Te value of q0 can be divided into three types
according to the scale of the road network, which is generally
large, medium, and small, and the values are 0.7, 0.5, and 0.2
[15]. ηij is shown in equation (8). pk
ij(t) is indicated in the
following equation:
Table 1: Important scale.
Important scale
Meaning
1
Te two factors are equally important
3
Te former is slightly more important than the latter
5
Te former is more important than the latter
7
Te former is obviously important than the latter
9
Te former is extremely important than the latter
2, 4, 6, 8
Intermediate value of two adjacent judgments
Reciprocal
If the ratio of the importance between element i and element j is aij, the ratio of
element j and element i is aji  1/aij
Table 2: Average random consistency index.
Matrix
order
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
RI
0
0
0.58
0.90
1.12
1.24
1.32
1.41
1.45
1.49
Table 3: Te judgment matrix.
A
C1
C2
C3
C1
1
3
5
C2
1/3
1
3
C3
1/5
1/3
1
Journal of Advanced Transportation
5
 1409, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2023/7651100, Wiley Online Library on [23/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## Page 6

pk
ij(t) 
τij(t)
􏽨
􏽩
α · ηij(t)
􏽨
􏽩
β
􏽐s∈allowk τis(t)
􏼂
􏼃α · ηis(t)
􏼂
􏼃β ,
j ∈allowk,
0,
j ∉allowk.
⎧
⎪
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎪
⎩
(11)
Te variables in equation (11) are shown in Table 4.
It can be seen from equation (8), when q < q0, the ant
temporarily ignores the existence of the better next node,
and accumulates the pheromone on the path of node i to all
the nodes j to be selected. When q ≥q0, the ant will select the
next node according to pk
ij(t), preventing the ant from
selecting the path with large pheromone concentration at the
beginning, which is benefcial to the global search and avoids
local convergence.
4.2.2. Pheromone Update. Tere are two ways to update
the pheromone, namely, local pheromone updates and
global pheromone updates. Local pheromone update
means that when the ant completes a path search, the
pheromone is updated on the path. While global pher-
omone update means that the pheromone is updated of
the optimal path in all paths when all ants complete a path
search.
Te local pheromone update rule is as follows:
τij(t + 1)  (1 −ρ) · τij(t) + ∆τij(t),
∆τij(t)  􏽘
m
k1
∆τk
ij(t),
(12)
where ∆τk
ij is the concentration of pheromone left between
node i and node j by ant k. ∆τij is the pheromone con-
centration that all ants increase between node i and node j
due to the release of pheromones. Te ant cycle model is
used for calculating ∆τk
ij as follows [16]:
∆τk
ij 
Q
Lk
,
If the ant visits node i to node j,
0,
otherwise,
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎩
(13)
where Q is the pheromone constant released by the ant
during the whole path optimization. Lk is the total length
traveled by ant k.
Te global pheromone update rule is as follows:
τij(t + 1) (1 −ζ) · τij(t) + ∆τij(t),
∆τij(t)  􏽘
m
k1
∆τk
ij(t),
∆τk
ij 
Q
Lk
,
The optimal path of ants in this circle,
0,
otherwise,
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎩
(14)
where ξ is the pheromone volatile factor, ξ ∈(0, 1). Lk is the
sum of the lengths selected by the ants in this circle.
4.2.3. Dynamic Optimization. Trafc information on the
road network is updated every 5–15 minutes. When the
vehicle reaches the next node of the road network, it is
checked whether the pheromone on the road has changed
according to equation (9). If the pheromone has changed,
the path is searched according to the changed pheromone,
and the path is dynamically optimized.
Te fow of the improved ant colony algorithm is as
follows:
Step 1: initializing each parameter, set the number of
iterations to NC  0, and place m ants on the
starting point.
Step 2: the number of iterations set to NC  NC + 1.
Step 3: the ant performs a path search according to
equation (10).
Step 4: when an ant reaches the end point, the pher-
omone is updated to the path searched by the ant
according to the local pheromone update rule.
Step 5: repeat Step 2–Step 4. When all the ants have
reached the end point, the path that all ants passed is
the optimal path.
Table 4: Constants and variables in ant colony algorithm.
Symbol
Meaning
n
Number of nodes
m
Number of ants
ηij(t)
A heuristic function that represents the expectation between node i and node j
dij
Te distance between node i and node j
τij(t)
Te pheromone concentration between node i and node j at time t
∆τk
ij
Te pheromone concentration of ant k released between node i and node j
Q
Pheromone constant
α
Pheromone importance factor, or pheromone factor for short
β
Te importance factor of heuristic function is referred to as heuristic function factor
ρ
Pheromone volatile factor, where 0 < ρ < 1
pk
ij(t)
Te probability of ant k moving from node i to node j at time t
allowk
Search table, representing ant k is looking forward to visiting the node
tabuk
Search tabu table, representing ant k have visited the node
6
Journal of Advanced Transportation
 1409, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2023/7651100, Wiley Online Library on [23/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## Page 7

Step 6: select an optimal path from all paths and
perform global pheromone update on the optimal path.
Step 7: if NC > NCmax, the search ends and outputs the
current optimal path, otherwise return to step 2.
Step 8: check whether the road network has been
updated. If updated, the pheromone is updated
according to equation (9).
Step 9: if the vehicle has reached the end point at this
time, the search is fnished, otherwise return to step 2.
5. Results and Discussion
Using the improved ant colony algorithm, the path opti-
mization is carried out for the simulated road network and
the instance network.
5.1. Simulated Road Network
5.1.1. Road Network Data. In order to verify the efective-
ness of the improved ant colony algorithm proposed in this
paper, some sections of Chaoyang Zhou South Road in
Nanchang City were selected as the study area. A road
network with 15 nodes is designed, and the road network
contains 21 road segments. Te road network to be opti-
mized in this paper is shown in Figure 3, where node O is the
starting point of the road section, and node D is the ending
point of the road section. Te goal of path optimization is to
fnd the optimal path from node O to node D. Vehicle
arrivals follow the normal distribution. In the road network,
the update interval of trafc information is 5 minutes.
Te length, the travel time at a certain time, and the
trafc fow are shown in Tables 5–7, respectively. Te table
only shows the results of nondimensionalization according
to the abovementioned method.
5.1.2. Parameter Settings. Te parameters in the improved
ant colony algorithm are shown in Table 4, and the main
parameters are set as follows:
(1) m represents the number of ants. m afects the
calculation results of MATLAB. Te literature re-
search and simulation results showed that when the
number of ants is 1.5 times the number of nodes, the
efect is better. In this paper, the number of nodes is
15, so the number of ants is set to 23.
(2) n indicates the number of nodes. n  15.
(3) α denotes the pheromone heuristic factor, which
describes the infuence of the pheromone released by
the ant during the path fnding process on the ant
path selection. Trough literature research and
simulation results, it is known that the efect is better
when α is 0 to 5, and α  1 selected in this paper.
(4) β refers to the expected value heuristic factor, in-
dicating the degree of action expected in the path
selection. Te larger the β, the easier to fall into the
local optimal solution. Te smaller the β, the smaller
the efect of the expected value, the harder to fnd the
optimal solution. Te simulation results showed that
β is 0–5, the efect is better, and this paper takes
β  5.
(5) ρ is the pheromone volatilization factor, indicating
the level of disappearance of the pheromone. 1 −ρ is
the pheromone residual factor, describing the re-
tention level of the pheromone. Trough simulation
results, it is shown that ρ is 0.2–0.5; the simulation
efect is better, so ρ is set to 0.3 in this paper.
5.1.3. Results and Analysis. Using the data in Section 5.1.1
and the parameters determined in Section 5.1.2, the results
were inputted into the MATLAB simulation platform to
verify the improved ant colony algorithm proposed in
this paper.
After the optimized processing of the improved ant
colony algorithm, the optimal path is shown in Figure 4, and
O
3
4
5
6
2
9
8
7
10
11
12
13
D
1
Figure 3: Road network diagram.
Table 5: Table of path length.
Node-node
Path length (m)
O-1
0.549
1–4
0.704
3–10
1.000
5-6
0.282
7-8
0.268
8–13
0.394
11-12
0.282
O–3
0.718
2–6
0.746
4-5
0.282
5–7
0.423
7–12
0.437
9-D
0.423
12-13
0.310
1-2
0.676
3-4
0.563
4–11
0.972
6–8
0.451
8-9
0.282
10-11
0.563
13-D
0.282
Journal of Advanced Transportation
7
 1409, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2023/7651100, Wiley Online Library on [23/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## Page 8

the convergence curve is shown in Figure 5. In the improved
ant colony algorithm, the comprehensive weight-infuencing
factors are used for calculation, and after the optimal path is
obtained, the optimal path is described in the actual road
network.
As can be seen from Figure 4, the optimal path from
node O to node D is O-3-4-5-7-12-13-D, and the optimal
path length (comprehensive weight-infuencing factor)
is 2.885.
Meantime, the basic ant colony algorithm is used to
calculate the optimal path, which is compared with the
improved ant colony algorithm proposed in this paper.
Figure 6 shows the optimal path of the ant colony algorithm,
and Figure 7 shows the convergence curve of the ant colony
algorithm.
As indicated in Figure 6, the optimal path from node O
to node D obtained by the ant colony algorithm is O-1-4-5-
7-8-13-D, and the optimal path length (comprehensive
weight-infuencing factor) is 2.902.
A comparison of the improved ant colony algorithm, the
basic ant colony algorithm, and the spatial shortest distance
algorithm is shown in Table 8.
From Figures 4–7 and Table 8, the following conclusions
can be drawn:
(1) Te length of the optimal path obtained by the
improved ant colony algorithm (3.015) is longer than
the length obtained by the basic ant colony algorithm
(2.092). Tis is because the improved ant colony
algorithm comprehensively considers the infuence
of path length, travel time, and trafc fow on the
optimal path. Terefore, when choosing the optimal
path, the road with a shorter travel time and less
trafc fow will be considered, which may lead to the
selection of the longer path length. However, when
the optimal path is simultaneously expressed by the
comprehensive weight-infuencing factor, the opti-
mal path selected by the basic ant colony algorithms
is longer than the optimal path obtained by the
improved ant colony algorithm, since the two al-
gorithms do not consider the real-time trafc con-
ditions of the road segment (such as the delay time
caused by trafc congestion).
(2) Te number of iterations of the improved ant colony
algorithm is reduced compared with the basic ant
colony algorithm. Because of the directional guid-
ance introduced in the improved ant colony algo-
rithm, the ant’s search always points to the ending
point, and the convergence speed is accelerated.
Table 6: Table of travel time at a certain time.
Node-node
Travel time (s)
O-1
0.659
1–4
0.634
3–10
1.000
5-6
0.254
7-8
0.241
8–13
0.245
11-12
0.338
O–3
0.462
2–6
0.987
4-5
0.298
5–7
0.634
7–12
0.357
9-D
0.585
12-13
0.254
1-2
0.704
3-4
0.423
4–11
0.921
6–8
0.272
8-9
0.241
10-11
0.441
13-D
0.220
Table 7: Table of trafc fow.
Node-node
Trafc fow (vehicle)
O-1
0.533
1–4
0.615
3–10
0.770
5-6
0.256
7-8
0.304
8–13
0.488
11-12
0.450
O–3
0.347
2–6
1.000
4-5
0.254
5–7
0.464
7–12
0.687
9-D
0.411
12-13
0.251
1-2
0.507
3-4
0.450
4–11
0.758
6–8
0.303
8-9
0.258
10-11
0.488
13-D
0.256
Optimal path
15
10
5
0
0
5
10
15
Coordinate X
Coordinate Y
Figure 4: Te optimal path of the improved ant colony algorithm.
8
Journal of Advanced Transportation
 1409, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2023/7651100, Wiley Online Library on [23/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## Page 9

Trend of convergence curve
3
2.5
2
1.5
1
0.5
0
0
20
40
60
80
100
Iterations
Length of optimal path
Figure 5: Te convergence curve of the improved ant colony algorithm.
Optimal path
15
10
5
0
0
5
10
15
Coordinate X
Coordinate Y
Figure 6: Te optimal path of the ant colony algorithm.
Trend of convergence curve
3
2.5
2
1.5
1
0.5
0
0
20
40
60
80
100
Iterations
Length of optimal path
Figure 7: Te convergence curve of the ant colony algorithm.
Journal of Advanced Transportation
9
 1409, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2023/7651100, Wiley Online Library on [23/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## Page 10

(3) Te travel time of the optimal path obtained by the
improved ant colony algorithm is signifcantly
shorter than that of the basic ant colony algorithm
and the spatial shortest distance algorithm, in-
dicating that the improved ant colony algorithm
improves the accuracy when optimizing the path.
Although the length of the optimal path obtained by
the improved ant colony algorithm is not the
shortest, the improved ant colony algorithm will
bypass relatively congested roads while driving and
can reach the destination more quickly.
5.2. Instance Network. In order to verify the efectiveness of
the proposed method, the road network of [17] is selected for
verifcation. Te purpose of path optimization is to fnd the
optimal path from node 1 to node 16.
Te comparisons of the optimal paths obtained by the
improved ant colony algorithm, the basic ant colony algo-
rithm and the space shortest distance algorithm, the length
of the path, the travel time, and the number of iterations are
shown in Table 9.
It can also be seen from Table 9 that the length of the
optimal path obtained by the improved ant colony al-
gorithm is longer than that obtained by the basic ant
colony algorithm. However, when the optimal path is
simultaneously expressed by the comprehensive weight-
infuencing factors at the same time, the optimal path
length selected by the basic ant colony algorithm and the
spatial shortest distance algorithm is obviously longer
than the optimal path obtained by the improved ant
colony algorithm. Te number of iterations of the im-
proved ant colony algorithm is less than that of the basic
ant colony algorithm. Te travel time of the optimal path
obtained by the improved ant colony algorithm is sig-
nifcantly shorter than that of the basic ant colony al-
gorithm and the spatial shortest distance algorithm,
indicating that the improved ant colony algorithm has
improved accuracy in optimizing the path compared with
the basic ant colony algorithm and the spatial shortest
distance algorithm. Te efectiveness of the improved ant
colony algorithm in path optimization is further verifed.
6. Conclusion
Te dynamic path optimization method was studied, and the
application of the dynamic path multiobjective pro-
gramming model and ant colony algorithm in TSP problem
were analyzed in this paper. Trough the actual investigation
and analysis, the section length, travel time, and trafc fow
are converted into comprehensive weight-infuencing fac-
tors by using the AHP. At the same time, directional
guidance and dynamic optimization are added. Te im-
proved ant colony algorithm is proposed, which is verifed
by the simulation road network and the example road
network. Te travel time comparison results of the optimal
path showed that the accuracy of the optimal path obtained
by the improved ant colony algorithm is improved com-
pared with the basic ant colony algorithm and the space
shortest distance algorithm, which verifed the efectiveness
of the improved ant colony algorithm. Meanwhile, di-
rectional guidance is introduced to reduce the number of
iterations.
Because of the time and the lack of appropriate data, the
paper is verifed with simulation data. Te author hopes to
use real data in future research to verify the accuracy of the
model. Besides, in the future research, the author uses PSO,
SSO, WOA [18–20], and other methods to establish a dy-
namic path optimization model.
Data Availability
Te data used to support the fndings of the study are
available from the corresponding author upon request.
Conflicts of Interest
Te authors declare that there are no conficts of interest
regarding the publication of this paper.
Table 8: Comparison of various algorithms in Simulated Road Network.
Path optimization algorithm
Optimal path
Path length
Travel time (s)
Actual length of the
path
Comprehensive
weight-infuencing factor
Improved ant colony algorithm
O-3-4-5-7-12-13-D
3.015
2.  5
376
Ant colony algorithm
O-1-4-5-7-8-13-D
2.902
2.911
416.3
Bold valuers represent the optimal values of various path optimization algorithms.
Table 9: Comparison of various algorithms in Instance network.
Path optimization algorithm
Optimal path
Path length
Travel time (s)
Number of
iterations
Actual length of the
path (m)
Comprehensive
weight-infuencing factor
Improved ant colony algorithm
1-2-17-7-11-12-16
2666
4.109
377.1
1 
Ant colony algorithm
1-5-6-10-11-15-16
2662
4.240
426
26
Spatial shortest distance algorithm
1-5-9-10-11-12-16
2680
4.243
424
—
Bold valuers represent the optimal values of various path optimization algorithms.
10
Journal of Advanced Transportation
 1409, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2023/7651100, Wiley Online Library on [23/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


## Page 11

Acknowledgments
Tis study was supported by the Jiangsu University Phi-
losophy
and
Social
Science
Research
Project
(no.
2021SJA0518).
References
[1] R.
Bauer,
D.
Delling,
P.
Sanders,
D.
Schieferdecker,
D. Schultes, and D. Wagner, “Combining hierarchical and
goal-directedspeed-up techniques for dijkstra’s algorithm,”
Journal of Experimental Algorithmics, vol. 15, 2010.
[2] M. Wei and Y. Meng, “Research on the optimal route choice
based on improved Dijkstra,” in Proceedings of the Advanced
Research & Technology in Industry Applications, IEEE, Ot-
tawa, ON, September 2014.
[3] W. Pijls and H. Post, “A new bidirectional search algorithm
with shortened postprocessing,” European Journal of Oper-
ational Research, vol. 198, no. 2, pp. 363–369, 2009.
[4] U. Atila, I. R. Karas, C. Gologlu, B. Yaman, and I. M. Orak,
“Design of a route guidance system with shortest driving time
based on genetic algorithm,” in Proceedings of the 10th
WSEAS international conference on Applied computer and
applied computational science. World Scientifc and Engi-
neering Academy and Society (WSEAS), pp. 61–66, Beijing
China, July 2011.
[5] L. D’Acierno, M. Gallo, and B. Montella, “An Ant Colony
Optimisation algorithm for solving the asymmetric trafc
assignment problem,” European Journal of Operational Re-
search, vol. 217, no. 2, pp. 459–469, 2012.
[6] M. Yu, G. Yue, Z. Lu, and X. Pang, “Logistics terminal dis-
tribution mode and path optimization based on ant colony
algorithm,” Wireless Personal Communications, vol.102, 2018.
[7] M. A. Kobayashi, H. Shimizu, and Y. Yonezawa, “Dynamic
route search algorithms of a trafc network,” in Proceedings of
the 36th SICE Annual Conference. International Session Pa-
pers, IEEE, Tokushima, Japan, July 2002.
[8] G. Che, L. Liu, and Z. Yu, “An improved ant colony opti-
mization algorithm based on particle swarm optimization
algorithm for path planning of autonomous underwater ve-
hicle,” Journal of Ambient Intelligence and Humanized
Computing, vol. 11, no. 8, pp. 3349–3354, 2020.
[9] Z. Zhang, L. Zhang, J. Deng, M. Wang, Z. Wang, and D. Cao,
“An enabling trajectory planning scheme for lane change
collision avoidance on highways,” IEEE Transactions on In-
telligent Vehicles, vol. 12, 2021.
[10] C. Wang, Z. Wang, L. Zhang, and T. Chen, “Post-impact
motion planning and tracking control for autonomous ve-
hicles[J],” Chinese Journal of Mechanical Engineering, vol. 35,
no. 1, pp. 1–18, 2022.
[11] L. Zhang, Z. Zhang, Z. Wang, J. Deng, and D. G. Dorrell,
“Chassis coordinated control for full X-by-wire vehicles-A
review,” Chinese Journal of Mechanical Engineering, vol. 34,
no. 1, pp. 42–25, 2021.
[12] N. Rivera, J. A. Baier, and C. Hern´andez, “Incorporating
weights into real-time heuristic search,” Artifcial Intelligence,
vol. 225, no. 225, pp. 1–23, 2015.
[13] G. K. H. Pang, K. Takabashi, T. Yokota, and H. Takenaga,
“Adaptive route selection for dynamic route guidance system
based on fuzzy-neural approaches,” IEEE Transactions on
Vehicular Technology, vol. 48, no. 6, pp. 2028–2041, 1999.
[14] C. L. Zong, X. Y. Li, and Y. T. Wang, “A multi-objective
programming model of route choice before travel [J],”
JOURNAL
OF
TRANSPORTATION
SYSTEMS
ENGINEERING
AND
INFORMATION
TECHNOLOGY,
vol. 5, no. 6, pp. 58–61, 2005.
[15] M. Dorigo and L. M. Gambardella, “Ant colony system:
a cooperative learning approach to the traveling salesman
problem,” IEEE Transactions on Evolutionary Computation,
vol. 1, no. 1, pp. 53–66, 1997.
[16] Y. C. Chang, V. C. Li, and C. J. Chiang, “An ant colony
optimization heuristic for an integrated production and
distribution scheduling problem [J],” Engineering Optimiza-
tion, vol. 46, no. 4, p. 18, 2014.
[17] N. Li, A Research in Dynamic Trafc Assignment and Route
Guide System Based on Ant colony Algorithm [D], Changsha
University of Science & Technology, Hu Nan Sheng, China,
2008.
[18] A. J. Humaidi and H. M. Badir, “Linear and nonlinear active
rejection controllers for single-link fexible joint robot ma-
nipulator based on PSO tuner,” JOURNAL OF ENGINEER-
ING SCIENCE AND TECHNOLOGY REVIEW, vol. 13, no. 6,
pp. 2272–2278, 2018.
[19] T. Ghanim, A. R. Ajel, and A. J. Humaidi, “Optimal fuzzy logic
control for temperature control based on social spider opti-
mization,” IOP Conference Series: Materials Science and En-
gineering, vol. 745, no. 1, Article ID 012099, 2020.
[20] A. J. Humaidi, H. M. Badr, and A. H. Hameed, “PSO-based
active disturbance rejection control for position control of
magnetic levitation system,” in Proceedings of the 2018 5th
International Conference on Control, Decision and In-
formation Technologies (CoDIT), Tessaloniki, Greece, April
2018.
Journal of Advanced Transportation
11
 1409, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2023/7651100, Wiley Online Library on [23/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License



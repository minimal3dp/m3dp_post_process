# A New Fast Ant Colony Optimization Algorithm: The Saltatory Evolution Ant Colony Optimization Algorithm
**Author:** Shugang Li, Yanfang Wei, Xin Liu, He Zhu and Zhaoxu Yu
**Subject:** Various studies have shown that the ant colony optimization (ACO) algorithm has a good performance in approximating complex combinatorial optimization problems such as traveling salesman problem (TSP) for real-world applications. However, disadvantages such as long running time and easy stagnation still restrict its further wide application in many fields. In this study, a saltatory evolution ant colony optimization (SEACO) algorithm is proposed to increase the optimization speed. Different from the past research, this study innovatively starts from the perspective of near-optimal path identification and refines the domain knowledge of near-optimal path identification by quantitative analysis model using the pheromone matrix evolution data of the traditional ACO algorithm. Based on the domain knowledge, a near-optimal path prediction model is built to predict the evolutionary trend of the path pheromone matrix so as to fundamentally save the running time. Extensive experiment results on a traveling salesman problem library (TSPLIB) database demonstrate that the solution quality of the SEACO algorithm is better than that of the ACO algorithm, and it is more suitable for large-scale data sets within the specified time window. This means it can provide a promising direction to deal with the problem about slow optimization speed and low accuracy of the ACO algorithm.

**Source:** `mathematics-10-00925-v2.pdf`
---

## Page 1



Citation: Li, S.; Wei, Y.; Liu, X.; Zhu,
H.; Yu, Z. A New Fast Ant Colony
Optimization Algorithm: The
Saltatory Evolution Ant Colony
Optimization Algorithm. Mathematics
2022, 10, 925. https://doi.org/
10.3390/math10060925
Received: 15 January 2022
Accepted: 10 March 2022
Published: 14 March 2022
Publisher’s Note: MDPI stays neutral
with regard to jurisdictional claims in
published maps and institutional afﬁl-
iations.
Copyright:
© 2022 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
mathematics
Article
A New Fast Ant Colony Optimization Algorithm: The Saltatory
Evolution Ant Colony Optimization Algorithm
Shugang Li 1
, Yanfang Wei 1
, Xin Liu 1,*
, He Zhu 1,*
and Zhaoxu Yu 2
1
School of Management, Shanghai University, Shanghai 200444, China; luck_li@shu.edu.cn (S.L.);
weiyanfang@shu.edu.cn (Y.W.)
2
Department of Automation, East China University of Science and Technology, Shanghai 200237, China;
yyzx@ecust.edu.cn
*
Correspondence: liuxin007@shu.edu.cn (X.L.); zh19720582@shu.edu.cn (H.Z.)
Abstract: Various studies have shown that the ant colony optimization (ACO) algorithm has a
good performance in approximating complex combinatorial optimization problems such as trav-
eling salesman problem (TSP) for real-world applications. However, disadvantages such as long
running time and easy stagnation still restrict its further wide application in many ﬁelds. In this
study, a saltatory evolution ant colony optimization (SEACO) algorithm is proposed to increase
the optimization speed. Different from the past research, this study innovatively starts from the
perspective of near-optimal path identiﬁcation and reﬁnes the domain knowledge of near-optimal
path identiﬁcation by quantitative analysis model using the pheromone matrix evolution data of the
traditional ACO algorithm. Based on the domain knowledge, a near-optimal path prediction model
is built to predict the evolutionary trend of the path pheromone matrix so as to fundamentally save
the running time. Extensive experiment results on a traveling salesman problem library (TSPLIB)
database demonstrate that the solution quality of the SEACO algorithm is better than that of the ACO
algorithm, and it is more suitable for large-scale data sets within the speciﬁed time window. This
means it can provide a promising direction to deal with the problem about slow optimization speed
and low accuracy of the ACO algorithm.
Keywords: ant colony algorithm; traveling salesman problem; near-optimal path identiﬁcation;
optimization speed
MSC: 05A17; 68R05; 68W50
1. Introduction
The ant colony optimization (ACO) algorithm was proposed by M. Dorigo and his
assistants in 1991 [1]. It is a meta-heuristic algorithm that simulates ants looking for food in
nature and is used to approximate the NP-hard combinatorial optimization problems. It
has been veriﬁed to have the advantages of distributed computation and robustness. In
addition, it has a good performance in approximating complex combinatorial optimization
problems such as the Traveling Salesman Problem (TSP), so its application prospects are
very broad. However, the ACO algorithm has the shortcomings of long running time and
easy stagnation [2], which has restricted its wide application in many ﬁelds. Now in the era
of data interconnection, path planning in autonomous driving [3,4] and task scheduling
in cloud computing and fog computing [5,6] as well as the large-scale combinatorial
optimization problems such as service node mining in the ﬁeld of Internet of Things [7]
increasingly require fast calculations to obtain a near-optimal solution in a limited time.
Therefore, it is of great importance to design a fast ACO algorithm to better solve or
approximate the practical application problems of combinatorial optimization, to beneﬁt
work efﬁciency and to optimize service experience.
Mathematics 2022, 10, 925. https://doi.org/10.3390/math10060925
https://www.mdpi.com/journal/mathematics


## Page 2

Mathematics 2022, 10, 925
2 of 22
It is known that the fundamental reason for the long running time and slow con-
vergence speed of the ACO algorithm is that the running mechanism includes a random
selection of paths [8,9]. However, the difﬁculty in dealing with this problem is that this
kind of stochastic uncertainty is a necessary part in the ACO algorithm because it can
prevent the ACO algorithm from prematurely converging to the local optimal solution
to some extent. In order to overcome this difﬁculty, some improvement methods such as
algorithm parameter self-adjustment, multi-ant colony collaborative optimization, multi-
algorithm or multi-strategy and other methods are proposed to improve the optimization
speed [3,10–12]. However, all of these methods need to look for improvement opportu-
nities from the components of optimization system constructed by the traditional ACO
algorithm. The overall acceleration is not very satisfactory, and the slow approximating
speed still hinders the wide application of the ACO algorithm, especially for the large-scale
combinatorial optimization problems. Unlike the past research, this study innovatively
starts from the perspective of near-optimal path identiﬁcation. Take the TSP as an example,
the saltatory evolution ant colony optimization (SEACO) algorithm uses the quantitative
analysis model to mine the domain knowledge of near-optimal path identiﬁcation and
constructs the optimal path prediction model based on the domain knowledge. The opti-
mization speed of ant colony algorithm is greatly improved by predicting the evolutionary
trend of pheromone matrix and updating pheromone matrix based on the prediction results.
Then, the saltatory evolution mechanism of SEACO algorithm is constructed so as to greatly
and fundamentally save the running time and improve the convergence speed.
The SEACO algorithm is constructed in three stages in this study. Firstly, in the ﬁrst
stage, the TSP and the operating characteristics of the ACO algorithm are deeply analyzed,
and an index system for evaluating the path performance of the ACO algorithm is innova-
tively proposed. Then in the second stage, the key domain knowledge of the near-optimal
path identiﬁcation is extracted from the evolution data of the traditional ACO algorithm
pheromone matrix using the quantitative analysis model. Finally, in the third stage, a
model of near-optimal path identiﬁcation is constructed gathering the domain knowledge
to realize the saltatory evolution of the ACO algorithm. In addition, 79 international TSP
data sets are used to test the SEACO algorithm, and the experimental results are compared
with the traditional ACO algorithm and other improved ACO algorithms. According to
the experimental results, the solution quality of SEACO algorithm is better than that of
ACO algorithm, and it is more suitable for large-scale data sets within the speciﬁed time
window.
The rest of the study is organized as follows. The related work about improving
the speed of the ACO algorithm is presented in Section 2.
The model of the quick-
approximating TSP is presented in Section 3. The traditional ACO algorithm model is
described in Section 4. The SEACO algorithm model is showed in Section 5. The results of
the experiments and comparison are provided in Section 6. Finally, Section 7 concludes the
study.
2. Research Status
This section will further introduce the current researchers’ efforts about improving the
optimization speed of the ACO algorithm. Related improvement strategies can be roughly
divided into three types.
The ﬁrst one is designing algorithm parameter adaptive rules to realize self-repair of
the ACO algorithm and accelerate the convergence. For example, F. Zheng et al. proposed
an algorithm parameter adaptive strategy to control the convergence trajectory of the
algorithm in the decision space so as to ensure that the algorithm could complete the
convergence within the given time [10]. In order to improve the running speed, S. Zhang
et al. not only constructed a non-uniformly distributed initial pheromone matrix but also
proposed an adaptive parameter adjustment strategy based on population entropy to
balance the speed and quality of the algorithm during the operation [13]. W. Deng et al.


## Page 3

Mathematics 2022, 10, 925
3 of 22
set up a parameter adaptive pseudo-random transfer strategy and increased the adaptive
obstacle removal factor and angle guidance factor to improve the convergence speed [14].
The second one is setting multiple ant groups for collaborative optimization to improve
the optimization speed of the ACO algorithm. For example, J. Yu et al. proposed a parallel
sorting ACO algorithm by multi-ant colony information interaction and multi-subgroup
joint growth and realized the fast convergence when generating paths with different
complexity mapping [3]. W. Deng et al. added the algorithm parameter adjustment on the
basis of multi-subgroup coordination and constructed a co-evolutionary ACO algorithm to
realize the simultaneous improvement of the optimization speed and quality. However,
the author also proposed that the algorithm still faced a problem of slow convergence
rate [14]. H. Pan et al. further proposed a pheromone reconstruction mechanism based on
Pearson’s correlation coefﬁcient for efﬁcient information interaction during collaborative
optimization of multiple ant groups [15].
The third one is improving the pheromone updating rule to increase the evolution
efﬁciency of the pheromone matrix. For example, X. Wei introduced the reward and punish-
ment coefﬁcient into the pheromone updating rule of the ACO algorithm to accelerate the
running speed, and the ﬂuctuation coefﬁcient was used to dynamically update the perfor-
mance of the overall strategy [16]. J. Li et al. optimized the negative feedback mechanism,
simultaneously updated the pheromone concentration on the worst and optimal path and
enhanced the weight of the pheromone concentration on the optimal path to increase the
running speed of the algorithm [17]. W. Gao merged the paths of the two ants that met
after half of the journey into one solution to update the pheromone, which not only saved
the search time of the TSP but also expanded the diversity of the search, but the number of
ants met during the actual calculation process was very limited [18].
In addition to the main improvement strategies mentioned above, some researchers
try to add other algorithms to make up for the shortcoming of the ACO algorithm [11],
and more and more researchers tend to mix up with multiple improvement strategies to
maximally improve the operating efﬁciency of the ACO algorithm [12].
In summary, whether it is the ACO algorithm parameter self-adjustment, multi-ant
colony collaborative optimization, or pheromone updating rules improvement, all of these
improvement strategies are based on the components of the optimization system built by
the traditional ACO algorithm. Thus, the effect is relatively limited, and the improvement
strategy is getting more and more complicated. Different from the above research, this study
innovatively incorporates the idea of pheromone evolutionary trend prediction, starting
from the perspective of predicting the near-optimal path, mining domain knowledge that
can be widely used in the prediction of the near-optimal path of the TSP and constructing a
new type of fast ACO algorithm: the SEACO algorithm. It can predict the evolutionary
trend of the pheromone matrix and directly realize the saltatory evolution of the ACO
algorithm which can be able to save lots of running time.
3. TSP with a Solving Time Window
The TSP is a realistic problem that simulates a salesman visiting customers at different
locations and ﬁnally returning to the original location. Among them, the symmetric TSP
refers to the situation where the travel cost or distance between any given location is
the same in back and forward directions. Effective solutions to this type of TSP can be
applied to many practical problems, such as online and ofﬂine route planning, cargo
distribution, artiﬁcial intelligence algorithm parameter adjustment, and so on, which have
a wide range of application value. TSP is a typical complex combinatorial optimization
problem, the research of TSP with a solving time window has important theoretical value
of approximating NP-hard problems. In addition, ACO algorithm is more suitable for the
application of large-scale cities, and the time complexity is lower. Using TSP to test the
performance of proposed ACO algorithm is also the most typical in theory. Therefore, this
study mainly concentrates on applying the SEACO algorithm to typical symmetric TSP.


## Page 4

Mathematics 2022, 10, 925
4 of 22
The typical symmetric TSP is marked as a complete weighted graph G = (V, E), V is
the vertex set, E represents the edge set, and the distance between the vertices dij is known.
The TSP with a solving time window can be modiﬁed to the following mathematical model
on the basis of 0–1 programming model:
minZ =
n
∑
i=1
n
∑
j=1
dijxijs.t























n
∑
i=1
xij = 1, ∀j ∈V, i ̸= j
n
∑
j=1
xij = 1, ∀i ∈V, i ̸= j
∑
i∈S
∑
j∈S
xij < |S| −1, ∀S ⊂V, 2 ≤|S| ≤n −1
Zt ≤Tmax
xij ∈{0, 1}, ∀i, j ∈V
In the model, n represents the number of cities, dij stands for the city distance from
city i to city j, V is the set of n city labels, and S denotes any subset of the V set. Xij
is a 0–1 variable, indicating whether the path (i, j) has been selected. Zt stands for the
running time in the approximating process, and Tmax refers to the longest time permitted to
approximate the TSP. The objective function describes the shortest combined path. Among
the constraints, the ﬁrst two constraints are used to restrict each city node to have only
one edge in and one edge out. Constraint (3) is used as the prevention of the Hamiltonian
sub-loop, which means in any set of nodes, the sum of Xij is less than the number of nodes.
Constraint (4) is deﬁned as the limitation on the approximating time in the TSP with solving
time window.
4. Traditional Ant Colony Optimization Algorithm
The traditional ACO algorithm [2] made the following marks in order to simulate the
foraging process of ant groups, where N refers to the number of city nodes, m stands for the
number of ants, and D is an N ∗N matrix representing the path distance matrix. dij denotes
the distance from city i to city j, τij(t) describes the pheromone amounts accumulated on the
path from city i to city j at time t. Γ is an N ∗N matrix, which is deﬁned as the pheromone
matrix composed of all paths. Each row of the matrix stands for the set of pheromone values
of possible paths starting from a certain city node i, and ρ is the pheromone volatilization
factor.
At the initial moment, m ants are randomly placed in N different cities. At this time,
the initial concentration of the pheromone on each path is the same, namely c. After that,
each ant uses the roulette method [19] to choose a city that has not been visited according
to the selection rule, until it traverses all the cities and returns to the starting point. The
path selection rule is a heuristic rule determined by the speciﬁc problem. In the TSP, the
heuristic function ηij is generally the reciprocal of the path distance dij from city i to j, as
shown in Formula (1).
ηij = 1
dij
(1)
At time t, ant k located in city i will choose the next new city j according to the
probability calculated by Formula (2).
pk
ij(t) =
τα
ij(t)ηβ
ij
∑jNk
i τα
ij(t)ηβ
ij
i f j ∈Nk
i
(2)
where τij(t) stands for the accumulated path pheromone of path (i, j) at time t. α and β are
two parameters that respectively determine the mutual inﬂuence degree of pheromone and
heuristic information. Nk
i represents the list of cities that ant k has not yet arrived from city
i, which is to prevent the ant from visiting a city more than one time. And tabu(k) denotes
a list of the cities that the ant k has visited. Finally, when all the ants visit all the cities and


## Page 5

Mathematics 2022, 10, 925
5 of 22
complete a cycle, the path pheromone will be updated according to the results of each ant’s
solution, as Formula (3) shows:
τij(t + 1) = ρτij(t) + ∑
m
k=1 ∆τk
ij
(3)
where ρ refers to the pheromone volatilization factor. ∆τk
ij stands for the pheromone
increment because of the ant k moving from city i to j. Generally, the pheromone increment
adopts the global updating method as shown in Formula (4):
∆τk
ij =
(
Q
Tk , if ant k moves through path (i, j)
0, other situations
(4)
where Q stands for the constant amount of pheromone that an ant can release in a cycle,
and Tk describes the path distance of the solution found by the ant k during this iteration.
After updating the pheromone matrix, the ant groups will continue the next iteration cycle
until reaching the termination condition and then output the near-optimal result.
5. Saltatory Evolution Ant Colony Optimization Algorithm
5.1. Algorithm Mechanism and Structure
The SEACO algorithm is based on the iterative principle of the traditional ACO
algorithm, starting from the perspective of near-optimal path identiﬁcation, reﬁning and
integrating domain knowledge for the near-optimal path identiﬁcation of TSP to construct
a near-optimal path prediction model that can accurately predict the evolutionary trend
of the pheromone matrix, which can help traditional ACO algorithm achieve saltatory
evolution and accelerate the convergence process. The mechanism of the SEACO algorithm
includes three main stages: the path performance evaluation stage, the near-optimal path
identiﬁcation rules generation stage, and the near-optimal path identiﬁcation stage. The
algorithm structure is shown in Figure 1.
5.1.1. The Path Performance Evaluation
The near-optimal paths in TSP refer to those paths that appear in the near-optimal solu-
tion. The continuous iterative optimization process of the ACO algorithm can be regarded
as a process in which many ants constantly evaluate and adjust the path performance
based on the past search experience to ﬁnd the near-optimal paths. In this process, the path
pheromone acts as a communication medium among ants, carrying and disseminating the
path performance information shown in the past. Therefore, the cumulative pheromone of
the path when the overall-optimal or near-optimal solution is found, is used to represent
the path performance in this study.
Next, based on the traditional ACO algorithm mechanism, an index system for evalu-
ating the path performance is proposed. As shown in Figure 2, the index system includes
three aspects: (1) dij, the distance of the path (i, j). It represents the cost could be paid
when ants moving through the given path, which is generally determined by the speciﬁc
problem. (2) fij(T), the selected frequency of path (i, j) in the ﬁrst T generations. It is the
frequency with which the given path is selected into the solution during the algorithm
running process. (3) Zij(T), the average value of solution containing the path (i, j) in the
ﬁrst T generations. It describes the capability of the given path to be compatible with other
paths to form a near-optimal solution. The speciﬁc calculation methods of index (2) and (3)
are respectively shown in Formulas (5) and (6).
Zij(T) =
∑m ∑T Zkt
ij
Cij
(5)
fij(T) =
Cij
m ∗T
(6)


## Page 6

Mathematics 2022, 10, 925
6 of 22
where Cij denotes the selected number of the path (i, j) during the ﬁrst T iterations, and Zkt
ij
refers to the solution value containing the path (i, j) of ant k at the t iteration. The larger the
value of Zij(T), the weaker the capability of path (i, j) to be compatible with other paths to
form a near-optimal solution, as the objective function of the TSP is to ﬁnd the minimum
value.
Initialize the algorithm
Run the traditional ACO
algorithm continuously
Extract the  performance
indices of paths
The path distance
The average value of
the solution containing
a given path
The near-optimal path
identification model
Update the pheromone matrix of
the saltatory evolution algorithm
Output the result of the SEACO
Run for T generations
Judge whether T ≤Tmax
or not
No
Judge whether to conduct
the saltatory evolution at T
Yes
Yes
No
Figure 1. The SEACO algorithm ﬂow chart.


## Page 7

Mathematics 2022, 10, 925
7 of 22
The average value of the
solution containing a
given path in the first T
generations
The path distance
The selected frequency of
the path in the first T
generations
 The path pheromone
value in the near-optimal
pheromone matrix
The dispersion degree of the
path distance
The main influence factors
H2
H0
H1
The adjustment variables
The pheromone
importance factor α
The heuristic
function degree
factor β
The control variables
The extreme value influence
of the path distance
H3
H4
H5
H6

Figure 2. The conceptual diagram of the hypothesis test.
5.1.2. The Generation of the Near-Optimal Path Identiﬁcation Rules
In this section, based on the path performance evaluation indicators proposed in
Section 5.1.1, the quantitative analysis model is used to reﬁne the TSP near-optimal path
identiﬁcation rule working as the domain knowledge to support the construction of the
SEACO algorithm from the pheromone matrix evolution data of the traditional ACO
algorithm.
At the initial moment of ACO, the pheromone of each path is the same, and the
pheromone matrix is uniformly distributed. With the continuous iteration of the algorithm,
the distribution of the pheromone matrix changes based on the search results and only
one path is selected in each row of the pheromone matrix during each iteration of the
TSP. In order to reﬂect the evolutionary trend of the pheromone matrix more clearly, the
path pheromone is normalized in each row after each iteration. It is obvious that the total
amount of path pheromones in each row of the pheromone matrix will converge to the
near-optimal path when the algorithm achieves the global optimal solution. This matrix is
deﬁned as the near-optimal pheromone matrix in this study. In conclusion, the evolutionary
process of the pheromone matrix is a process in which the path pheromone continuously
converges from a uniform distribution to the near-optimal path. If the near-optimal path
prediction rules can be found based on historical iterative data and be used to predict
the future evolutionary trend of the pheromone matrix reasonably, it will greatly save the
search time of the ACO algorithm and increase the convergence speed in this process.
Next, the quantitative analysis model will be used to test hypotheses, which is to
mine the near-optimal path prediction rules from the pheromone matrix evolution data
of the traditional ACO algorithm. First of all, each path pheromone in the near-optimal
pheromone matrix is set as an explanatory variable Y, which describes the path performance,
and then, three key assumptions that could affect the path pheromone in the near-optimal
pheromone matrix are proposed based on the path performance evaluation indexes.
Hypothesis 0 (H0). The larger the path distance, the smaller the path pheromone in the near-
optimal pheromone matrix.
Hypothesis 1 (H1). The larger the average value of the solution containing a given path, the
smaller the path pheromone in the near-optimal pheromone matrix.


## Page 8

Mathematics 2022, 10, 925
8 of 22
Hypothesis 2 (H2). The higher the selected frequency of a given path, the larger the path pheromone
in the near-optimal pheromone matrix.
It can be seen from Formula (2) that the pheromone importance factor α and the
important factor of heuristic function β in the ACO algorithm affect the value of the path
selection probability. Therefore, in the hypothesis test model, α and β are deﬁned as the
adjustment variables for the average value of the path solution and the frequency of path
selection. The following four hypotheses are proposed based on the above algorithm
mechanism:
Hypothesis 3 (H3). The pheromone importance factor α can enhance the negative inﬂuence of
the average value of the solution containing a given path on the path pheromone value in the
near-optimal pheromone matrix.
Hypothesis 4 (H4). The heuristic function degree factor β can weaken the negative inﬂuence
of the average value of the solution containing a given path on the path pheromone value in the
near-optimal pheromone matrix.
Hypothesis 5 (H5). The pheromone importance factor α can enhance the positive inﬂuence of
the selected frequency of a given path on the path pheromone value in the near-optimal pheromone
matrix.
Hypothesis 6 (H6). The heuristic function degree factor β can weaken the positive inﬂuence of
the selected frequency of a given path on the path pheromone value in the near-optimal pheromone
matrix.
Finally, the variance S2 reﬂecting the dispersion degree of the paths distance in the
TSP data sets and the index ∆E reﬂecting the inﬂuence of the extreme value of the path
distance on the average value are added as control variables in the hypothesis test model
as shown in Figure 2. The control variable ∆E is calculated with Formula (7), where Vs
refers to the vertex set of the graph G when removed top 10 edges with minimum distance,
and Vb denotes the vertex set of the graph G when removed top 10 edges with maximum
distance.
∆E = ∑i,j∈Vs dij −∑i,j∈Vb dij
N ∗N −10
(7)
In order to verify the above hypotheses, 60% of the 79 data sets in international
traveling salesman problem library (TSPLIB) database [20] were randomly selected as the
training data sets, and the traditional ACO algorithm pheromone matrix evolution data
in 200 generations were used to test the quantitative analysis model. The parameters of
the traditional ACO algorithm according to previous research [21–23] were set as follows:
the number of ants m was 50, the pheromone volatilization factor ρ was 0.1, the constant
coefﬁcient Q was 1, the maximum number of iterations was 200, and the running node
T was 20. In addition, the pheromone value of the path (i, j) at the 200th generation
was regarded as the estimated value of the path pheromone amount in the near-optimal
pheromone matrix, so the regression equation is constructed as Formula (8).
y = b0 + b1x1 + b2x2 + b3x3 + b4x4 + b5x5 + b6x2x4 + b7x3x4 + b8x2x5 + b9x3x5 + b10x6 + b11x7
(8)
where x1 represents dij, x2 stands for Zij(T), x3 denotes fij(T), x4 is α (the value is 1 or 5),
x5 refers to β (the value is 2 or 5), S2 is deﬁned as x6, and x7 stands for ∆E.
The results of quantitative analysis model test are shown in Table 1. The p-value of the
regression equation is 0, which passes the signiﬁcance test. The variance inﬂation factor
(VIF) value of the regression equation without cross terms is equal to 6.3, indicating that
there is no serious multicollinearity between variables. The regression coefﬁcient of x1 is
negative, and the p-value is 0, indicating that the larger the path distance, the smaller the


## Page 9

Mathematics 2022, 10, 925
9 of 22
pheromone value of the path (i, j) in the near-optimal pheromone matrix. Therefore, the
hypothesis H0 is supported. The regression coefﬁcient of x2 is positive indicating that the
larger the average value of the solutions containing the path (i, j), the larger the pheromone
value of path (i, j) in the near-optimal pheromone matrix, which is contrary to the original
hypothesis H1. The evolutionary strategies in ACO algorithm to avoid the prematurity
of pheromone matrix may be the reason, such as pheromone volatilization mechanism
and roulette random selection strategy. The regression coefﬁcient of x3 is 0, indicating that
the selected frequency of path (i, j) in the ﬁrst T generations has no correlation with the
pheromone value of path (i, j) in the near-optimal pheromone matrix. The hypothesis H2
is not supported, and thus, the hypothesis H5 and H6 about the adjustment variables are
also not supported. What is more, the regression coefﬁcient of the adjustment variable α is
negative, and the regression coefﬁcient of the cross term of α is also negative, indicating
that α can weaken the positive effect of the average value of the solutions containing
path (i, j) on the path pheromone value in the near-optimal pheromone matrix. Therefore,
H3 is supported. The regression coefﬁcient of the adjustment variable β is positive, but
the regression coefﬁcient of the cross term of β is negative, indicating that β can weaken
the positive effect of the average value of the solutions containing path (i, j) on the path
pheromone value in the near-optimal pheromone matrix, so H4 is supported. Finally, four
near-optimal path identiﬁcation rules are obtained, and the hypothesis test results are
shown in Figure 3.
Table 1. The results of quantitative analysis model test.
Variable
Coefﬁcient
p-Value
constant term
0.0018975
0 *
x1
−4.442 × 108
0 *
x2
8.1777 × 10−10
5.0679 × 10−275 *
x3
0
0 *
x4
−6.471 × 10−6
0.00017177 *
x5
1.9936 × 10−5
3.4768 × 10−13 *
x2x4
−4.7122 × 10−12
0.0015371 *
x3x4
0
0 *
x2x5
−6.3676 × 10−10
0 *
x3x5
0
0 *
x6
2.248 × 10−12
0.19642
x7
0.0017948
0 *
R2 = 0.00474, p-value = 0
Notes: * represents p-value < 0.05. If p-value is under 0.05, the coefﬁcient is statistically signiﬁcant.
5.1.3. The Near-Optimal Path Identiﬁcation
In this section, the adjustment variables α and β are ﬁxed. The supported H0 and H2
are used to make a qualitative identiﬁcation of the near-optimal path ﬁrstly, and then a
model for predicting the near-optimal path is constructed to realize the saltatory evolution
of the pheromone matrix of the traditional ACO algorithm and speed up the process of
optimizing.
The qualitative identiﬁcation process of the near-optimal path is as follows:
(a)
Discretizing variables.
All possible paths starting from i are considered as an analysis unit. Then variable dij and
variable Zij(T) are mapped to one of the low value interval [min(i), 1
3(max(i) + 2 min(i))], the
median interval

1
3(max(i) + 2min(i)), 1
3(2max(i) + min(i))
i
, and the high value interval

1
3(2max(i) + min(i)), max(i)
i
and are converted to the low, medium, and high value
accordingly to be the discrete variables, where min(i) is the minimum variable value of all
N possible paths starting from node i, and max(i) is the maximum variable value of all N


## Page 10

Mathematics 2022, 10, 925
10 of 22
possible paths starting from node i. It should be emphasized that the discretization will not
be needed if Zij(T) is null.
The average value of the
solutions containing a
given path in the first T
generations (+)
The path distance(−)
 The path pheromone value
in the near-optimal
pheromone matrix
The dispersion degree of
path distance(−)
The main influence factors
H2
H0
The adjustment variables
The pheromone
importance
factorα(−)
The heuristic
function degree
factorβ(−)
The control
variables
The extreme value influence of
path distance(+)
H3
H4

Figure 3. The results of the hypothesis test.
(b)
Incorporating the identiﬁcation rules and predicting the near-optimal path in different
scenarios.
After the variables’ discretization, there would be 12 scenarios that are composed
of different dij and Zij(T), as shown in Table 2. It is assumed that the effect of one main
variable will not completely offset the effect of another main variable, and the identiﬁcation
results are denoted by three grade variables, which are high, middle, and low value. When
dij belongs to a high level and Zij(T) belongs to a low level, the ﬁnal judgment result is a
low level because both main variables predict that the pheromone value of the path (i, j)
in the near-optimal pheromone matrix will be a low level. In the same way, when dij and
Zij(T) are both at the middle level, the path (i, j) pheromone value in the near-optimal
pheromone matrix is predicted to be at the middle level. When dij is a low level and Zij(T)
is a high level, the value of the path pheromone in the near-optimal pheromone matrix is
predicted to be a high level. When Zij(T) is null, H2 will be invalid and the pheromone
value of the path (i, j) in the near-optimal pheromone matrix is only judged according to dij
based on H0.
Table 2. The results of identiﬁcation rules in different scenarios.
Zij(T) = High
Zij(T) = Medium
Zij(T) = Low
Zij(T) = NAN
dij = high
medium
low
low
low
dij = medium
high
medium
low
medium
dij = low
high
high
low
high
Notes: dij is the path distance from city i to city j. Zij(T) refers to the average value of solution containing the
path (i, j) in the ﬁrst T generations.


## Page 11

Mathematics 2022, 10, 925
11 of 22
(c)
Updating the pheromone matrix.
The high, low, and medium values of the qualitative identiﬁcation results of the path
pheromone respectively represent the increased, decreased, or unchanged evolutionary
trend that the pheromone value of the path (i, j), namely, τij(T), would show during the
evolution of the pheromone matrix, and it is assumed that the change value of each path
pheromone Q1 is ﬁxed. According to Table 2, the qualitative pheromone matrix updating
formula is obtained, as shown in Formula (9), where τ′
ij is the prediction value of the path
pheromone of (i, j).
τ′
ij
=



τij + Q1, i f the pheromone of path(i, j)inthenear −optimalpheromonematrixishigh, ∀i, j ∈V
τij, i f the pheromone of path(i, j)inthenear −optimalpheromonematrixismedium, ∀i, j ∈V
τij −Q1, i f the pheromone of path(i, j)inthenear −optimalpheromonematrixislow, ∀i, j ∈V
(9)
(d)
The test of the qualitative identiﬁcation rules.
In order to preliminarily verify the validity and applicability of the near-optimal path
qualitative identiﬁcation rules, 24 test data sets were used, and the experimental results
were compared with the traditional ACO algorithm. First of all, in order to reasonably
distinguish the different path performance from the pheromone value level, Q1 was selected
as three values which are 0.1, 0.5, and 1 by observing the path pheromone value before
updating. These three values could cover the change range of path pheromone and good
simulation results would be relatively obtained through such parameter setting. Then,
when the traditional ACO algorithm ran to the 20th generation, the pheromone matrix
was updated with Formula (8). After updating, the ACO algorithm continued to run for
one generation to output the optimized results. The average optimization result Y′. of the
24 data sets after the pheromone updating was compared with the average optimization
result Y of the traditional ACO algorithm on the same data sets at the 20th generation so
as to evaluate the effectiveness of the near-optimal path qualitative identiﬁcation rules.
Meanwhile, the optimization rate, that is, the proportion of the data sets with reduced
running time after the application of the prediction rules in all experimental data sets, is
used to evaluate the applicability of the near-optimal path qualitative identiﬁcation rules.
The experimental results are shown in Table 3. When Q1 is equal to 0.1, Y′ of 24 data sets
is better than Y, and the overall optimization rate reaches 41.67%. When Q1 is equal to 1,
although Y′ of 24 data sets is not better than Y, the overall optimization rate reaches 50%.
Table 3. The test results of qualitative prediction scheme.
Situation
Average Optimization
Result of 24 Data Sets
Optimization Rate
the traditional ACO at the
20th generation
1.015285551789795 × 105
-
Q1 = 0.5
1.104654039153430 × 105
0
Q1 = 0.1
1.014970895838640 × 105
0.4167
Q1 = 1
1.019495374707328 × 105
0.5
Notes: Q1 is the change value of each path pheromone.
The experiment preliminarily conﬁrms that the domain knowledge extracted in this
study can effectively predict the evolutionary trend of the pheromone matrix. However,
this experiment only used a qualitative method to make a rough discrete prediction of
the near-optimal path. However, when the value of Q1 is 0.1, the average optimization
results improved. While the optimization degree and optimization rate are not particularly
prominent, this study further constructs a model for predicting the near-optimal path from
a quantitative perspective to predict the near-optimal pheromone matrix continuously and
improve performance of the SEACO algorithm.
The model of near-optimal path prediction is as follows:


## Page 12

Mathematics 2022, 10, 925
12 of 22
(1)
Null variable treatment.
When the Zij(T) is null, Zij(T) will be equal to
max(Zij(T))+min(Zij(T))
2
, so it is transformed into a continuous variable.
(2)
Construct the model for predicting the near-optimal path. Based on the veriﬁed
Formula (9), the following model for predicting the near-optimal path is shown in
Formula (10).
τ′
ij = τij(T) + sin

π
2 ∗

Zij(T) −min
 Zij(T)

max
 Zij(T)
 −min
 Zij(T)
 −
dij −min(di)
max(di) −min(di)
!!
, ∀i, j ∈V
(10)
where τij(T) denotes the pheromone value of the path (i, j) at the Tth generation. τ′
ij refers to
pheromone prediction value of the path (i, j) in the near-optimal pheromone matrix. Zij(T)
describes the average value of the solutions containing paths (i, j) before T generations.
Zij(T) is a vector representing average values of the solutions, and each solution contains
one path starting from i. dij is deﬁned as the distance of path (i, j) and di symbolizes a
vector which contains all the paths distance starting from i.
5.2. Steps of the SEACO Algorithm
As shown in Figure 1, the detailed steps of SEACO algorithm are as follows:
(1)
Initialize the algorithm.
Let the number of ants be m, pheromone importance factor be α, heuristic function
important factor be β, pheromone volatilization factor be ρ, constant coefﬁcient be Q,
heuristic function be η, the maximum number of iterations be Tmax in the ACO algorithm
and set the starting generation for operating the saltatory evolution.
(2)
Iterate for T times.
At the beginning of each iteration, m ants are randomly placed on the initial position.
and the selection probability of each path is calculated by Formula (2). Then according
to the roulette method, the path selection is completed one by one, and the values of m
solutions are obtained and the solution with shortest distance is selected as the output
of this iteration. Finally, the pheromone value of each path will be updated according to
Formulas (4) and (5), and each row of the pheromone matrix is normalized. After updating
the pheromone matrix, step 2 is repeated until the number of iterations T is equal to Tmax,
or T reaches the starting generation of the saltatory evolution.
(3)
Identify the near-optimal path and update the pheromone matrix.
When the number of iterations T reaches the starting generation of saltatory evolution,
Zij(T), the average value of the solutions containing path (i, j), will be calculated according
to Formula (5). Then Zij(T) and the path distance dij will be input into the near-optimal
path prediction model as shown in Formula (10) to update the pheromone matrix.
(4)
Conduct the saltatory evolution.
With other variables unchanged, run the traditional ACO algorithm using the updated
pheromone matrix according to step 2. If the number of iterations T reaches Tmax, the near-
optimal solution of the last iteration will be output. Otherwise, judge whether T reaches
the starting generation of saltatory evolution. If yes, repeat step 3. If not, go to step 2.
6. Experimental Results and Model Comparison
6.1. The Saving Generations of SEACO Algorithm Compared with Traditional ACO Algorithm
In order to verify the effectiveness of the SEACO algorithm in improving the opti-
mization speed, the SEACO algorithm was compared with the traditional ACO algorithm
in terms of the time complexity ﬁrstly. The asymptotic time complexity of the algorithm
T[n] is calculated by O( f (n)) [24], where n denotes the input amount, f (n) indicates the
sum of the number of running each line of code, and O refers to the positive proportional
relationship. Accordingly, the time complexity of the traditional ACO algorithm is O(n2).


## Page 13

Mathematics 2022, 10, 925
13 of 22
While the running time of the SEACO algorithm is 2n2 + n, which is also O(n2) after ig-
noring the coefﬁcients and low-power terms. Therefore, the SEACO algorithm does not
increase the running time complexity of the traditional ACO algorithm, which means the
time complexity of the two algorithms increases at the same rate with the increase of the
input amount n.
Next, the experiment was run on 24 test data sets, which were randomly selected from
the TSPLIB database, and these data sets were broadly representative because their city
numbers ranged from 100 to 1379. The running time was compared when the SEACO
algorithm and the traditional ACO algorithm got the same result. For example, if the near-
optimal solution of the SEACO algorithm at the Tth generation is smaller than or equal to
the near-optimal solution of the traditional ACO algorithm at the (T + t)th generation, it
means that the SEACO algorithm saves t generations of running time than the traditional
ACO algorithm. The experiment was applied on Matlab R2017b software with i7 Intel
processor and 32GB internal storage. Based on the parameters of traditional ACO and other
improved ACO algorithm [21–23], the following parameters of the SEACO algorithm were
set. The number of ants m was 200; the pheromone importance factor α was 1; the heuristic
function important factor β was 5; the pheromone volatilization factor ρ was 0.1, and the
constant variable Q was 1. The SEACO algorithm was conducted with pheromone matrix
updated at the 10th, 20th, 30th, 40th, 50th, 60th, 70th, 80th, 90th, and 100th generation of the
traditional ACO algorithm, and continue running 3 generations after each update to ﬁnd
the best solution. The consumed generations for achieving the same solution are compared
between the SEACO algorithm and the traditional ACO. The complete comparison results
are shown in Table 4, and Figure 4 displays the data sets with the largest improvement in
different injected generations.
Table 4. The saving generations of SEACO algorithm than ACO algorithm on the test data sets.
Data Sets
10th
20th
30th
40th
50th
60th
70th
80th
90th
100th
att532
12
41
31
21
11
4
0
0
0
0
d1291
12
29
19
9
0
1
6
0
0
0
d1655
22
32
22
12
10
0
3
3
7
0
d493
10
28
18
9
0
0
5
0
0
0
d657
30
20
10
0
10
0
2
1
0
0
ﬂ1577
5
19
3
0
3
0
0
0
5
0
gil262
6
4
0
0
0
15
5
9
0
0
kroB200
0
27
15
7
0
2
12
2
7
0
kroC100
0
22
12
3
6
0
0
7
0
0
kroE100
13
3
1
10
0
0
3
1
7
0
nrw1379
20
34
27
15
7
1
0
0
1
0
p654
40
30
20
10
0
9
0
0
7
0
pa561
21
16
14
6
0
0
0
1
0
0
pcb1173
29
37
27
17
7
0
0
0
0
0
rat575
0
13
5
0
3
0
6
11
1
0
rat783
5
18
8
0
0
0
0
0
2
0
rd100
13
3
16
7
0
0
1
17
7
0
u1432
42
43
39
23
13
9
0
0
0
0
u1817
12
34
27
23
3
0
0
0
1
0
u574
21
28
25
23
5
0
2
3
2
0
u724
9
28
20
10
6
0
4
4
0
0
rl1304
49
39
29
30
20
14
0
3
0
0
rl1323
45
52
48
32
22
12
2
0
0
0
u1060
6
48
48
40
28
12
4
0
0
0
Mean
17.6
27
20.2
12.8
6.4
3.3
2.3
2.6
2
0
Max
49
52
48
40
28
15
12
17
7
0
Optimization
rate
0.88
1
0.96
0.80
0.63
0.42
0.54
0.50
0.46
0
Notes: 10th means the SEACO algorithm conducts the saltatory evolution at the 10th generation and so on.


## Page 14

Mathematics 2022, 10, 925
14 of 22

0
10
20
30
40
50
60
10
20
30
40
50
60
70
80
90
100
The average saving generations  than the traditional
ACO algorithm
The generation when the saltatory evolution  is applied
'gil262'
'kroB200'
'rd100'
rl1304'
'rl1323'
'u1060'
Figure 4. The saving generations of SEACO algorithm on test data sets.
As shown in Table 4, the optimization rate of the SEACO algorithm on the test data sets
is over 46% before 90th generation, and over 80% before 40th generation. This indicates that
the SEACO algorithm has wide applicability and effectiveness on approximating TSPs with
limited time window. Moreover, it can be seen from Figure 4 that the earlier the SEACO
algorithm is conducted, the faster the optimization speed is improved. Speciﬁcally, the
SEACO algorithm performs best at the 20th generation with 100% optimization rate, and
52 generations can be saved at most, and 27 generations can be saved on average. However,
the performance of the SEACO algorithm has not been improved at the 100th generation,
which indicates that the SEACO algorithm is more suitable to be injected into the ACO
algorithm in the early stage, and the quantitative analysis model for identifying the near-
optimal path needs to be reconstructed so as to continue accelerating the traditional ACO
algorithm after the 100th generation.
In order to further verify the wide applicability of the SEACO algorithm, the experi-
ment was also run on all 79 TSP data sets, and the average saving generations of the SEACO
algorithm are shown in Table 5. These data sets were divided into ﬁve groups according to
their city scales, where the number of cities n lies in (0, 100], (100, 200], (200, 400), [400, 800],
and (800, 2000], respectively. Then, the optimized performance of the SEACO algorithm on
different data sets with different city scales are compared, and the data sets with the largest
improvement in different injected generations are shown in Figures 5–9.


## Page 15

Mathematics 2022, 10, 925
15 of 22
Table 5. The average saving generations of SEACO algorithm than ACO algorithm on all data sets.
Data Sets
10th
20th
30th
40th
50th
60th
70th
80th
90th
100th
(0, 100]
13.2
20
17.7
21
18.9
18.8
14
14.4
7
0
(100, 200]
11.2
15.5
12.5
13.3
9.7
5.6
7
6.9
4.8
0
(200, 400)
16.7
18.1
12.3
10.5
5.9
8.2
5.8
9.7
5.4
0
[400, 800]
19.2
23.7
15.8
10.9
4.7
2.4
1.9
3.5
2.6
0
(800, 2000]
31.6
39.3
33.2
25
15.5
6.3
2
0.3
1.3
0
all data sets
18.38
23.32
18.3
16.14
10.94
8.26
6.14
6.96
4.22
0
optimization rate of
all data sets
0.80
0.85
0.90
0.80
0.70
0.53
0.53
0.60
0.68
0
Notes: (0, 100] represents data sets where n is in (0, 100] and so on.

0
10
20
30
40
50
60
70
80
90
100
10
20
30
40
50
60
70
80
90
100
The average saving generations  than the traditional
ACO algorithm
The generation when the saltatory evolution  is applied
 burma14
 ulysses16
 ulysses22
 bayg29
 dantzig42
 eil51
Figure 5. The optimization results of SEACO algorithm for data sets where n is in (0, 100].
The results shown in Table 5 present the optimization rate of the SEACO algorithm
before 90th generation is over 68% on all 79 TSP data sets and over 80% before 40th
generation. This means that the SEACO algorithm can be widely applied on different TSP.
It can be seen from Table 5 that the SEACO algorithm performs best in the ﬁrst group
of city data sets where n is in (100, 200]. Speciﬁcally, it can be seen from Figure 5 that
the SEACO algorithm achieves the best performance on the data sets named dantzig42
at the 10th generation, whose optimization result is equivalent to the traditional ACO
algorithm at the 100th generation, and 87 generations of running time are saved. In
addition, the SEACO algorithm on the data sets of ulysses16, burma14, ulysses22, and eil51
also respectively shows the best performance when the SEACO injected at the 30th, 40th,
and 50th generations, and saved 67, 57, 47, and 37 generations of running time separately.
As shown in Figures 5–9, the optimization ability of the SEACO algorithm presents a
decreased trend with the delay of injection time on all city-scale data sets, which means it
can slightly improve the optimization speed when injected in the earlier running stage. As
shown in Figure 10, the SEACO algorithm reﬂects better performance on the larger scale
data sets than the smaller one in general. Speciﬁcally, the SEACO algorithm performs best
in the data sets where the city number is within (800, 2000], and nearly 40 generations on


## Page 16

Mathematics 2022, 10, 925
16 of 22
average can be saved when injected at the 20th generation. This means that the SEACO
algorithm can signiﬁcantly improve the optimization speed of the large-scale TSP.

0
10
20
30
40
50
60
70
10
20
30
40
50
60
70
80
90
100
The average saving generations  than the traditional
ACO algorithm
The generation when the saltatory evolution  is applied
 pr107
 pr136
 gr137
 pr152
Figure 6. The optimization results of SEACO algorithm for data sets where n is in (100, 200].

0
5
10
15
20
25
30
35
40
45
10
20
30
40
50
60
70
80
90
100
The average saving generations  than the traditional
ACO algorithm
The generation when the saltatory evolution  is applied
 ts225
 pr226
 a280
 linhp318
Figure 7. The optimization results of SEACO algorithm for data sets where n is in (200, 400).


## Page 17

Mathematics 2022, 10, 925
17 of 22

0
10
20
30
40
50
60
70
10
20
30
40
50
60
70
80
90
100
The average saving  generations  than the traditional
ACO algorithm
The generation when the saltatory evolution  is applied
 fl417
 u1432
 pr439
 gr666
Figure 8. The optimization results of SEACO algorithm for data sets where n is in [400, 800].

0
10
20
30
40
50
60
10
20
30
40
50
60
70
80
90
100
The average saving  generations  than the traditional
ACO algorithm
The generation when the saltatory evolution  is applied
 u1060
 rl1304
 rl1323
 vm1748
Figure 9. The optimization results of SEACO algorithm for data sets where n is in (800, 2000].


## Page 18

Mathematics 2022, 10, 925
18 of 22

0
5
10
15
20
25
30
35
40
45
10
20
30
40
50
60
70
80
90
100
The average saving  generations  than the traditional
ACO algorithm
The generation when the saltatory evolution  is applied
Mean(0,100]
Mean(100,200]
Mean(200,400)
Mean[400,800]
Mean(800,2000]
Figure 10. The average optimization results of SEACO algorithm on different data groups.
Finally, in order to investigate the performance of the SEACO algorithm under different
conditions of the control variables, the average optimization results are compared in
different situation. Firstly, the data sets are divided into ﬁve groups by mapping the
path distance variances S2 into (0, 1000), (1000, 100,000), (100,000, 1,000,000), (1,000,000,
100,000,000), or (100,000,000, 200,000,000) interval, and the average optimization results on
these groups are shown in Figure 11. It can be seen that there is no signiﬁcant difference on
optimization results among these groups with different path distance variances. Next, the
data sets are divided into four groups by mapping ∆E into (0.001, 0.01), (0.01, 0.1), (0.1, 1),
or (1, 21) interval, and the results are shown in Figure 12. It can be found that the SEACO
algorithm performs more prominently in the data sets with smaller ∆E than the data set
with larger ∆E. This implies that the SEACO algorithm is more suitable for the TSP whose
extreme value of the path distance has a small inﬂuence on the average value of the path
distance.
6.2. The Comparison with Other Improved Algorithms
On the one hand, this study compares SEACO and other improved ACO algorithms
such as the parallel-ranking ant colony optimization (PRACO) [3] and ACO for enhancing
the negative feedback mechanism (ACON) [17] algorithm to further prove the effectiveness
of the SEACO algorithm. First, the time complexity of PRACO and ACON is the same as
SEACO. Then, the solution qualities of three algorithms are compared under the same time
window (running 23 generations), as shown in Table 6. The parameters are the same as the
above experiments in Section 6.1, the PRACO algorithm includes three ant subgroups, and
the total number of ants is 200.


## Page 19

Mathematics 2022, 10, 925
19 of 22

0
5
10
15
20
25
30
10
20
30
40
50
60
70
80
90
100
The average saving generations than the traditional
ACO algorithm
The generation when the saltatory evolution  is applied
Mean(0,1000)
Mean(1000，10000)
Mean(10000,100000)
Mean(1000000,10000
0000)
Mean(100000000,200
000000)
Figure 11. The classiﬁed statistics of path distance dispersion.

0
5
10
15
20
25
30
35
40
10
20
30
40
50
60
70
80
90
100
The average saved generations than the traditional
ACO algorithm
The generation when the saltatory evolution  is applied
Mean(0.001,0.01)
Mean(0.01,0.1)
Mean(0.1,1)
Mean(1,21)
Figure 12. The classiﬁed statistics of the extreme inﬂuence of path distance.


## Page 20

Mathematics 2022, 10, 925
20 of 22
Table 6. The target value of SEACO algorithm compared with other improved algorithms.
Value Excess
Data Sets
Best Target Value
Average Target Value
Worst Target Value
SEACO-PRACO
(0, 100]
−810.99
−130.93
3.85
(100, 200]
−4666.54
−687.10
2397.09
(200, 400)
−8854.31
−1675.57
40.09
[400, 800]
−2414.67
−308.71
0.00
(800, 2000]
−34,799.82
−13,577.59
−2362.92
all data sets average
−10,309.27
−3275.98
15.62
SEACO-ACON
(0, 100]
−4921.54
−300.96
704.05
(100, 200]
−5639.19
−573.60
973.32
(200, 400)
−7829.89
−1633.28
16.33
[400, 800]
−11,239.99
−2767.47
175.87
(800, 2000]
−27,514.66
−12,354.15
−1519.72
all data sets average
−11,429.05
−3525.89
69.97
(RNN-SEACO)-RNN
(0, 100]
−22,771.54
−2699.50
−24.68
(100, 200]
−14,072.58
−2058.86
0.00
(200, 400)
−3326.52
−458.44
0.00
[400, 800]
−12,997.75
−2666.25
599.16
(800, 2000]
0.00
0.00
0.00
all data sets average
−10,633.678
−1576.61
114.896
Notes: (0, 100] represents data sets where n is in (0, 100] and so on.
As shown in Table 6, the solution quality of SEACO is the best when running the same
generations. Among all the TSP data sets, the SEACO algorithm shows a better solution
quality than the PRACO algorithm on 87.34% of TSP data sets, with an average reduction
of 3275.98. Meanwhile, the SEACO algorithm has a better solution quality than the ACON
algorithm on 79.75% of TSP data sets, with an average reduction of 3525.89.
On the other hand, in order to further verify the effectiveness of the improvement
measures of the SEACO algorithm, the RNN-SEACO algorithm is designed based on RNN,
as RNN is an algorithm with high solution quality at present [25]. The main idea of the
RNN-SEACO algorithm is that in the ﬁrst generation of the SEACO algorithm, one solution
is generated by the RNN algorithm, and the other solutions are randomly generated by
the pheromone matrix. At the same time, the optimal solution generated up to the current
generation is retained in each generation. The idea of RNN is to start with a tour of k
nodes, where k is the number of vertices that make up the partial tours, and then perform a
Nearest-Neighbor search from there on. After doing this for all permutations of k nodes,
the result gets selected as the shortest tour found [26].
The comparison of target values between RNN-SEACO and RNN algorithms when
running 23 generations is shown Table 6. The k of RNN is 2, and other parameters and TSP
data sets are the same as above. It can be seen from Table 6 that the RNN-SEACO algorithm
is able to reduce the target value of 22,771.54 at most and can reduce the target value of
1576.61 on average. This shows that the mechanism of saltatory evolution proposed by this
study can get a satisfactory solution on the basis of RNN.
In summary, the effectiveness and wide applicability of the SEACO algorithm are
veriﬁed in various TSP data sets. At the same time, the SEACO algorithm can better
accelerate the optimization speed in the early stage of the traditional ACO algorithm and
is more applicable to approximate large-scale TSP with limited time window, which can
provide a promising direction to improve searching speed of the traditional ACO algorithm
on large-scale combination optimization. In addition, the comparison with other improved
ACO algorithms indicates that the solution quality of the SEACO algorithm is much better,
which also veriﬁes its effectiveness and applicability. In addition, adding the results of the
RNN algorithm to the initial solution of the SEACO algorithm can approach the global
optimal solution more efﬁciently.


## Page 21

Mathematics 2022, 10, 925
21 of 22
7. Conclusions
In order to overcome the shortcoming of long optimization time of the traditional ACO
algorithm, this study constructs a new type of fast-approximating ACO algorithm—the
SEACO algorithm, which is constructed in three stages, namely, the path performance
evaluation stage, the near-optimal path identiﬁcation rules generation stage, and the near-
optimal path identiﬁcation stage from the perspective of near-optimal path identiﬁcation.
Then the SEACO algorithm is compared with the traditional ACO algorithm and other
improved ACO algorithms on the TSPLIB, respectively. On the test data sets, the optimiza-
tion rate of SEACO algorithm is above 46% before the 90th generation, and it achieves
100% optimization rate when injected at the 20th generation with 52 generations saved at
most and 27 generations saved on average. On all 79 data sets, the optimization rate of
the SEACO algorithm is over 68% before the 90th generation, and it reaches 90% when
SEACO is injected at the 30th generation, and on average 17 generations and maximum
77 generations time are saved. This fully veriﬁes that the SEACO algorithm proposed in
this study can effectively improve the approximating speed and can be widely applied to
various TSPs with a limited time window. What is more, an excellent performance can
be obtained when the SEACO algorithm is injected into the traditional ACO algorithm in
earlier stage. In terms of the solution quality, the SEACO algorithm shows a better solution
quality than the PRACO algorithm on 87.34% TSP data sets, with an average reduction
of 3275.98, and it has a better solution quality than the ACON algorithm on 79.75% TSP
data sets, with an average reduction of 3525.89. The comparison from different city scales
of the data sets reveals that the SEACO algorithm can save more running time on the
larger scale TSP data sets. This means it can provide a promising direction to deal with the
problem of slow optimization speed of the traditional ACO algorithm and better improve
the solution quality than other improved ACO algorithms. In addition, after using the RNN
algorithm to update the initial solution, the global optimal solution can be approached
more effectively.
This study also has the following limitations. Firstly, the SEACO algorithm is injected
only once to accelerate the optimization speed. The optimization efﬁciency of multiple
injections of the SEACO algorithm will be investigated in the future. In addition, the
performance of multiple injections is expected to achieve continuous acceleration and
effectively avoid the ACO algorithm from falling into local optimal solutions. Secondly,
this study mainly focuses on obtaining a good solution in a short time, neglecting to
search the global optimal solution. How to approximate TSP quickly as well as effectively
with the SEACO algorithm will be studied in the future. Finally, the SEACO algorithm
can be applied to some other practical optimization problems so as to further verify its
effectiveness and wide applicability.
Author Contributions: Conceptualization, S.L.; methodology, S.L., X.L. and H.Z.; software, X.L. and
Z.Y.; writing—original draft preparation, X.L. and Y.W.; writing—review and editing, X.L., Y.W. and
H.Z; supervision, S.L. and Z.Y.; funding acquisition, S.L. All authors have read and agreed to the
published version of the manuscript.
Funding: This research was supported by the Chinese National Natural Science Foundation
(No. 71871135).
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1.
Dorigo, M.; Maniezzo, V.; Colorni, A. Positive Feedback as a Search Strategy. June 1991. Available online: http://citeseerx.ist.psu.
edu/viewdoc/summary?doi=10.1.1.52.6342 (accessed on 14 January 2022).
2.
Dorigo, M.; Birattari, M.; Stutzle, T. Ant colony optimization. IEEE Comput. Intell. Mag. 2006, 1, 28–39. [CrossRef]


## Page 22

Mathematics 2022, 10, 925
22 of 22
3.
Yu, J.; Li, R.; Feng, Z.; Zhao, A.; Yu, Z.; Ye, Z.; Wang, J. A Novel Parallel Ant Colony Optimization Algorithm for Warehouse Path
Planning. J. Control Sci. Eng. 2020, 2020, 5287189. [CrossRef]
4.
Tomanova, P.; Holy, V. Ant Colony Optimization for Time-Dependent Travelling Salesman Problem. In Proceedings of the 4th
International Conference on Intelligent Systems, Metaheuristics and Swarm Intelligence (ISMSI)/India International Congress on
Computational Intelligence (IICCI), Thimphu, Bhutan, 18–19 April 2020; pp. 47–51.
5.
Lucky, L.; Girsang, A.S. Hybrid Nearest Neighbors Ant Colony Optimization for Clustering Social Media Comments. Informatica
2020, 44, 63–74. [CrossRef]
6.
Yin, C.; Li, T.; Qu, X.; Yuan, S. An Improved Ant Colony Optimization Job Scheduling Algorithm in Fog Computing. In
Proceedings of the International Symposium on Artiﬁcial Intelligence and Robotics, Kitakyushu, Japan, 8–10 August 2020;
Volume 11574, p. 115740G. [CrossRef]
7.
Zannou, A.; Boulaalam, A.; Nfaoui, E.H. Relevant node discovery and selection approach for the Internet of Things based on
neural networks and ant colony optimization. Pervasive Mob. Comput. 2021, 70, 101311. [CrossRef]
8.
Yu, J.; You, X.; Liu, S. Dynamic Density Clustering Ant Colony Algorithm With Filtering Recommendation Backtracking
Mechanism. IEEE Access 2020, 8, 154471–154484. [CrossRef]
9.
Dai, X.; Long, S.; Zhang, Z.; Gong, D. Mobile Robot Path Planning Based on Ant Colony Algorithm With A(*) Heuristic Method.
Front. Neurorobot. 2019, 13, 15. [CrossRef] [PubMed]
10.
Zheng, F.; Zecchin, A.C.; Newman, J.P.; Maier, H.R.; Dandy, G.C. An Adaptive Convergence-Trajectory Controlled Ant Colony
Optimization Algorithm With Application to Water Distribution System Design Problems. IEEE Trans. Evol. Comput. 2017, 21,
773–791. [CrossRef]
11.
Chen, X.; Dai, Y. Research on an Improved Ant Colony Algorithm Fusion with Genetic Algorithm for Route Planning. In
Proceedings of the 4th IEEE Information Technology, Networking, Electronic and Automation Control Conference (ITNEC),
Electr Network, Chongqing, China, 12–14 June 2020; pp. 1273–1278.
12.
Gao, S.; Wu, J.; Ai, J. Multi-UAV reconnaissance task allocation for heterogeneous targets using grouping ant colony optimization
algorithm. Soft Comput. 2021, 25, 7155–7167. [CrossRef]
13.
Zhang, S.; Pu, J.; Si, Y. An Adaptive Improved Ant Colony System Based on Population Information Entropy for Path Planning of
Mobile Robot. IEEE Access 2021, 9, 24933–24945. [CrossRef]
14.
Deng, W.; Xu, J.; Song, Y.; Zhao, H. An effective improved co-evolution ant colony optimisation algorithm with multi-strategies
and its application. Int. J. Bio-Inspired Comput. 2020, 16, 158–170. [CrossRef]
15.
Pan, H.; You, X.; Liu, S.; Zhang, D. Pearson correlation coefﬁcient-based pheromone refactoring mechanism for multi-colony ant
colony optimization. Appl. Intell. 2021, 51, 752–774. [CrossRef]
16.
Wei, X. Task scheduling optimization strategy using improved ant colony optimization algorithm in cloud computing. J. Ambient
Intell. Humaniz. Comput. 2020, 1–12. [CrossRef]
17.
Li, J.; Xia, Y.; Li, B.; Zeng, Z. A pseudo-dynamic search ant colony optimization algorithm with improved negative feedback
mechanism. Cogn. Syst. Res. 2020, 62, 1–9. [CrossRef]
18.
Gao, W. New ant colony optimization algorithm for the traveling salesman problem. Int. J. Comput. Intell. Syst. 2020, 13, 44–55.
[CrossRef]
19.
Lipowski, A.; Lipowska, D. Roulette-wheel selection via stochastic acceptance. Phys. A Stat. Mech. Appl. 2012, 391, 2193–2196.
[CrossRef]
20.
Reinelt, G. TSPLIB—A Traveling Salesman Problem Library. ORSA J. Comput. 1991, 3, 376–384. [CrossRef]
21.
Duan, H.B.; Ma, G.J.; Liu, S.Q. Experimental study of the adjustable parameters in basic ant colony optimization algorithm. In
Proceedings of the 2007 IEEE Congress on Evolutionary Computation, Singapore, 25–28 September 2007; pp. 149–156. [CrossRef]
22.
Li, Z.; Chen, X.; Wang, H. Modiﬁed ACO for General Continuous Function Optimization. In Proceedings of the 2012 Second
International Conference on Intelligent System Design and Engineering Application, Sanya, China, 6–7 January 2012; pp. 348–354.
23.
Hong, W.-C.; Dong, Y.; Zheng, F.; Lai, C.-Y. Forecasting urban trafﬁc ﬂow by SVR with continuous ACO. Appl. Math. Model. 2011,
35, 1282–1291. [CrossRef]
24.
Jasser, M.B.; Sarmini, M.; Yaseen, R. Ant Colony Optimization (ACO) and a Variation of Bee Colony Optimization (BCO) in
Solving TSP Problem: A Comparative Study. Int. J. Comput. Appl. 2014, 96, 1–8.
25.
Chauhan, A.; Verma, M. 5/4 approximation for Symmetric TSP. arXiv 2019, arXiv:1905.05291.
26.
Klug, N.; Chauhan, A.; Ragala, R. k-RNN: Extending NN-heuristics for the TSP. Mob. Netw. Appl. 2019, 24, 1210–1213. [CrossRef]

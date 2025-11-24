# 

**Source:** `Manuscript_for_IRIS.pdf`
---

## Page 1

24 November 2025
Alma Mater Studiorum Università di Bologna
Archivio istituzionale della ricerca
Bacciaglia A.,  Falcetelli F.,  Troiani E.,  Di Sante R.,  Liverani A.,  Ceruti A. (2022). Geometry
reconstruction for additive manufacturing: From G-CODE to 3D CAD model
[10.1016/j.matpr.2022.09.496].
Published Version:
Geometry reconstruction for additive manufacturing: From G-CODE to 3D CAD model
Published:
DOI: http://doi.org/10.1016/j.matpr.2022.09.496
Terms of use:
(Article begins on next page)
Some rights reserved. The terms and conditions for the reuse of this version of the manuscript are
specified in the publishing policy. For all terms of use and more information see the publisher's website.
Availability:
This version is available at: https://hdl.handle.net/11585/896484 since: 2024-11-06
This is the final peer-reviewed author’s accepted manuscript (postprint) of the following publication:
This item was downloaded from IRIS Università di Bologna (https://cris.unibo.it/).
When citing, please refer to the published version.


## Page 2

iM3F 2022_Bacciaglia 
[Materials today: Proceedings] 
Geometry Reconstruction for Additive Manufacturing: 
from G-CODE to 3D CAD Model 
 
Antonio Bacciagliaa, Francesco Falcetellia, Enrico Troiania, Raffaella Di Santea, Alfredo 
Liverania, Alessandro Cerutia 
aDepartment of Industrial Engineering, University of Bologna, 47121, Forlì, Italy  
Abstract 
In the last decades, the flourishing of Additive Manufacturing (AM) promoted innovative design solutions in many different sectors. 
Despite the numerous advantages of AM technology, there are still open challenges in the field. In Fused Deposition Modelling 
(FDM) structures the layer-by-layer manufacturing process induces anisotropy in the material properties of the structures. The 
correct characterization of the mechanical properties is fundamental in the design and development stages but at the same time 
difficult to achieve. The experimental approach can be extremely long and expensive. An alternative is the use of an accurate 
numerical approach and performing a Finite Element Analysis (FEA) of the geometry which is effectively printed. However, to the 
best of the authors' knowledge, there is not a common and well-established procedure to reconstruct the real geometry which is 
generated after the slicing process. In this paper, starting from the information provided by the G-CODE, an easy-to-use, and 
reproducible methodology to reconstruct the printed geometry is presented. The performance of the innovative approach is 
evaluated via qualitative observations by referring to several case studies. The results are thoroughly analysed, and future trends 
and research needs are highlighted. 
 
Keywords: Additive Manufacturing; Fused Deposition Modelling; G-CODE; CAD; 
1. Introduction 
In the last decades, Additive Manufacturing (AM) employment skyrocketed not only in industrial engineering 
contexts such as automotive [1], aerospace [2] and biomedical [3] but also in more exotic fields such as jewellery, 
clothing [4], and even in the manufacturing of musical instruments [5]. AM is viewed as a viable alternative to 
traditional manufacturing methods such as chip removal, casting, milling, and lathing, which all require adherence to 
many design limitations [6]. This manufacturing technology is based on the addition of new raw materials layer by 
layer, and it is extremely convenient for all those applications characterized by small, customized production volumes 
and for rapid prototyping of down-scaled models, mock-ups and so on [7]. AM technology has various benefits, 
including a quick design-to-manufacturing cycle, design flexibility, the capacity to create complicated forms in one 
piece, limiting the waste of raw material and the ability to mimic low-weight bioinspired geometries. 
Nowadays the design tools available to engineers do not keep up with the constant innovations of AM technologies 
[8] and the strong limits of Computer-aided design (CAD) software in the integration of design, technology, 
optimization, and smoothing processes highlighted in the literature [9]. In addition, the key drawbacks of AM 
technology to date are the material anisotropic qualities and the high surface roughness, especially valid for the Fused 
Deposition Modelling (FDM) technique [10] investigated in this research. Furthermore, AM is characterized by a 
restricted material portfolio; inspection and maintenance in complicated one-piece assemblies are problematic. High 
raw material and machine prices, and a delayed certification procedure affect AM products. This is owing to the 
substantial structural performance variability caused by differences in raw material qualities, changes (often minor) 
in machine settings or ambient factors, and the response of AM structures under fatigue loads. 
In the typical design workflow, especially for critical applications, after the 3D digital model is designed, engineers 
should investigate the mechanical behaviour of manufactured components through numerical or experimental 
approaches before the commercialization of the final product. On the one hand, in the scientific literature is plenty of 
 
 Corresponding author: Antonio Bacciaglia 
E-mail address: antonio.bacciaglia2@unibo.it 


## Page 3

contributions dealing with the description and discussion of experimental tests of AM specimens (FDM [11], 
Stereolithography [12] and Selective Laser Melting [13] and [14]) while few contributions employ Finite Element 
Analysis (FEA) to estimate the mechanical performances even if it is well known that FEA has an extremely lower 
economic impact on a typical design workflow. Indeed, several material configurations and manufacturing settings 
can be rapidly tested without wasting raw material and the operator’s working hours.  
However, the strong anisotropy, i.e. a significant change in mechanical characteristics in various directions, of AM 
products [15] limits the diffusion of numerical approaches in the literature. Thus, due to the inherent anisotropy, 
complex components, and unpredictable quality of 3D-printed components, traditional methods of FEA may not be 
suitable. If on the one hand FEA well estimates the behaviour of components created by traditional techniques, on the 
other, it cannot reliably forecast the behaviour of 3D-printed parts. Moreover, the multitude of Additive Manufacturing 
processes and the relatively new technology still in a development phase, hence rather few strength data, add to the 
complexity. Researchers established many assumptions to simulate the mechanical characteristics of AM objects 
through simplified models.  
Though, the approximations are confined to certain load scenarios or AM processes. For example, [16] focuses just 
on tensile loads applied on FDM specimens and estimates their stiffness by applying the strength of materials 
principles. To evaluate the elastic properties of additive produced components under compressive stresses, [17] used 
the rule of mixture and property transformation equation and excellent agreement between analytical and experimental 
findings was discovered. Of particular interest are the study reported in [18], in which a layered sub-modelling 
technique and FEA were used to assess the mechanical properties of 3D-printed components and in [19] where a 
computational homogenization technique is used to get the mechanical behaviour of 3D printed composite laminates. 
This is the only contribution that seeks to explain mechanical behaviour by using the true geometry of additively 
created parts starting from tooling path information. The process for obtaining the rebuilt geometry, however, is not 
mentioned. Indeed, to get the 3D real geometry model for FEA purposes, reverse modelling techniques should be 
developed knowing the tooling path, i.e. extrusion head for FDM, contained in the G-CODE files. In this regard, [20] 
can be seen as a first step towards the mimic of the real geometry for optical fibers embedding [21] in AM products 
using a manual reconstruction coded in Python, taking inspiration from the resulting preview of G-CODEs in slicing 
software.  
Thus, to the best of the authors’ knowledge, there is a lack of contributions dealing with the reconstruction of the 
real geometry from the tooling path information with a clear and reproducible methodology. From the analysis of the 
state-of-the-art [22], it has been highlighted the need for ease and reproducible methodologies capable of 
reconstructing the real 3D geometry from the information collected in the G-CODEs file useful for FEA. Currently, 
to simulate the mechanical properties of 3Dprinted objects, simplified models are used. However, these approaches 
are not capable of modelling the anisotropic nature of AM parts. Thus, tools and solvers should be created to accurately 
estimate and characterise the mechanical characteristics to use FEA to approximate the behaviour of additively 
manufactured objects. 
To overcome this technological gap, this research aims to describe a never-explored reproducible methodology 
which aim is to extract and obtain the 3D real geometry model of AM products, suitable for FEAs. This is done starting 
from the reading of useful information contained in the G-CODE which is used to recreate the tool path of AM 
machines. A set of simple geometries with variable infill and printing settings is used to validate the approaches and 
to compare the performances of the programmed routines through qualitative analysis. 
2. Methodology 
The methodology developed in this research aims to generate a STEP file representing the real printed geometry 
as output given a certain G-CODE as input. The STEP format enables comprehensive product specifications to be 
exchanged between CAD and FEM environments. To reconstruct the true geometry coming from the FDM process, 
the authors propose to exploit the capabilities offered by the sweep command, available in every CAD package. 
Indeed, using the sweep command, a 2D object (profile) is swept along an open or closed route (spine) to generate a 
3D surface or solid. The sweep command specification is ideal for the suggested methodology's goal of reconstructing 
real-world produced geometry: with the extrusion section profile and the route of the extruder's tool, any form may be 
recreated.  
The final aim of the research is achieved through three main steps, represented by the three coloured blocks in Fig. 
1. In the following subsections, each block is explained in detail. 


## Page 4

 
Fig. 1. Main methodology flow chart. 
2.1 
Coordinates extraction from G-CODE 
The G-CODE file is generated using common slicing software. For the scope of this research, the open-source software 
Ultimaker Cura [23] has been employed. The initial objective is to extract the information about the toolpath 
coordinates included in the G-GODE, once it is accessible. Indeed, the scope is to track the lines where there is material 
extrusion and nozzle movement since there is no interest in tracking lines with feed rate or extrusion temperature 
changes. This task is achieved using the following steps: 
• read the G-CODE file as a series of strings of characters;  
• the lines of interest are identified by reading the keyword at the front of each stringer line. In particular, three 
keywords are of interest for the scope of the research, namely the G0 and G1 commands (extrusion head motion) 
and the LAYER command, meaning a change of the extruded layer; 
• depending on the command contained in each line, a flag is assigned: 
– flag=1 if the instruction contains an extrusion command (G1); 
– flag=2 if the instruction contains an extrusion head movement without extruded material (G0); 
– flag=3 if the instruction contains a layer change (LAYER); 
• for each of these lines, an array containing the spatial coordinates of the tooling path and the relative flag is saved; 
• the final mx4 matrix is saved as .mat file.  
The procedure can be visually summarized by looking at the flow chart in Fig. 2. 
 
 
Fig. 2. Flow chart of the G-CODE extraction algorithm 


## Page 5

2.2 
Definition of the extruded path as a sweep list 
Once the toolpath coordinates are available, a Python code has been developed to provide a list containing all the 
sweep paths (spines) to be generated. At this level, just the movements involving the material extrusion should be 
evaluated. It's vital to distinguish between situations when the nozzle is extruding material (flag=1) and situations 
where the nozzle is just moving to a different coordinate without printing (flag=2). This is done by exploiting the flag 
values available at two consecutive lines. Referring to Table 1, the flag couples in the “A” scenario correspond to the 
toolpath coordinates where extrusion is taking place, whereas if the flag couples lie in the “B” scenario, then the 
toolpath coordinates do not have to be considered for the sweep procedure. For example, if line i contains a LAYER 
command (flag=3), and line i+1 contains a G1 command (flag=1), the FDM machine is deposing material from the 
starting point contained in i to the point i+1 (first column in Table 1). On the other hand, if line i contains a G1 
command (flag=1) and i+1 contains a G0 instruction (flag=2), the tool is moving from point i to i+1 without extruding 
new material (fourth column of Table 1) and for this reason, this case should not be considered in the sweep path 
reconstruction. 
 
Table 1. Definition of two possible scenarios (A and B) based on flag values of two consecutive G-CODE lines. 
 
A 
B 
ith Line 
3 
1 
2 
1 
2 
2 
1 
3 
(i+1)th  Line 
1 
1 
1 
2 
2 
3 
3 
2 
 
Whenever Case A is encountered, the new point is added to the open list, while if Case B appears at some point, it 
means that the continuous extrusion of material is interrupted by an extrusion head movement. For this reason, the 
actual list containing the coordinates of a sweep spine should be closed and a new list can be created. A list containing 
all the spine paths, considered as lists, can be exported as a .csv file. The complete flowchart of this procedure is 
shown in Fig. 3. 
 
 
Fig. 3. Sweep list management through python code. 
2.3 
FreeCAD 3D model reconstruction 
The last step leverages the open-source software FreeCAD to make all the sweep commands by reading the .csv 
file produced in the previous step. To adapt the methodology to different case studies, the user can choose between 
three different sweep profiles. For simplification purposes, circular and rectangular profiles could be adopted, while 
the ‘slot’ one, somehow approximates the real nozzle profile (Fig. 4). For example, the rectangular profile could be 
used to obtain a final geometry with sharp corners where a structured mesh could be adopted in an FEA, whereas the 


## Page 6

slot profile could be used to better reproduce the final geometry and model the actual bonding between different layers. 
Once all the sweep operations are completed, the FreeCAD macro exports a STEP file containing the real printed 
geometry. Fig. 5 summarizes this methodology in a flowchart. 
 
 
Fig. 4. Implemented sweep profiles library: circular (left), rectangular (centre) and slot (right). 
 
 
Fig. 5. FreeCAD flowchart for real geometry reconstruction. 
3. Results 
3.1 
Computational time evaluation 
The performance of the code is assessed by measuring the computational time needed for different case studies to 
recreate the actual geometry. All the simulations are performed by running the programmed codes on a workstation 
with 128 GB RAM and an Intel i9-11900 @ 2.50GHz CPU. Two geometries are considered: a cube with dimensions 
of 10x10x10 mm and a 30x100 mm dog-bone specimen. The dog-bone model has been used to test the methodology 
in a real case scenario and to highlight the capability of the innovative approach to model even curved paths rather 
than straight ones. Then, for each shape, different infill percentages and profile topologies are tested to see how these 
parameters affect the approach's efficiency. The gyroid and pyramid infill types, in particular, have been used to see 
how the methodology behaves with a gradient in the infill pattern along the third direction. Finally, each of these cases 
is further divided into three additional subcases corresponding to the three different geometry profiles. This 
comprehensive collection of simulations allows the reader to see how the infill pattern and density, the exterior 
geometry, and the profile used, affect the methodology performance. 
The results are outlined in Table 2. The times' columns were coloured according to a conditional formatting rule: 
the more a certain time value is lower than the mean of the three profiles time values, being fixed the infill % and the 
digital model, the more its colour tends to be green. In the opposite case, the cell value tends toward the red colour. It 
is visible at a glance that the rectangular profile is the most efficient while, depending on the specific cases, the circular 
or the slot profiles require more time.  
Moreover, it is possible to infer that the computational time depends on the number of sweeps rather than on the 
G-CODE file dimension as one may expect. 


## Page 7

Table 2. The computational time for different case studies. 
 
Infill 
sweeps time [s] 
G-CODE 
Cases 
[%] type 
n° 
circular 
rectangular slot 
KB N° Lines 
Cube 10x10x10 
20 
lines 
443 
73.00 
68.80 
87.50 
64 
2430 
Cube 10x10x10 
50 
lines 
827 
376.40 
361.30 
379.50 
104 4014 
Cube 10x10x10 
100 lines 
1499 
1478.60 
1419.30 
1449.70 
122 4062 
Dog-bone specimen 10 
lines 
1069 
720.90 
693.00 
740.90 
192 6726 
Dog-bone specimen 20 
lines 
1621 
1742.90 
1666.80 
1682.00 
248 8804 
Dog-bone specimen 50 
lines 
3231 
7889.10 
7705.10 
7508.40 
401 14436 
Dog-bone specimen 100 lines 
5899 
62384.10 60815.30 
63944.40 487 15490 
Cube 10x10x10 
20 
gyroid 
375 
110.00 
78.60 
106.70 
220 7404 
Dog-bone specimen 20 
pyramid 1578 
1571.60 
1540.00 
1560.00 
231 8020 
 
The data contained in Table 2 are plotted and fitted using the MATLAB fitting toolbox, which highlighted that a 
power law exists between the number of sweeps and the numerical simulation time (Fig. 6). 
 
Fig. 6. Computational time versus the number of sweeps for different sweep profiles and 3D models. 
3.2 
Quality assessment of reconstructed geometry 
The quality of the reconstructed geometry was assessed with several qualitative observations of the tested case 
studies. For instance, Fig. 7 shows how the dog-bone specimen geometry (20% infill) was reconstructed. From a first 
evaluation, it is possible to say that all the main geometry features were correctly captured and reconstructed, such as 
the outer skin and the infill type. 


## Page 8

 
Fig. 7. Example of geometry reconstruction of a specimen with a 20% infill 
 
The three-section views shown in Fig. 8 prove that the proposed code was able to reconstruct the real printed cube 
geometry using the three different sweep profiles. 
 
 
Fig. 8. Profiles comparison: circular (up-left), rectangular (up-right), and slot (down-centre) with highlighted edges for a more comprehensive 
geometry visualization. 
The last qualitative observation has been made considering as a case study the cube with the gyroid infill type, 
because of its complex topology made of curved paths and not constant along with different layers. The cube was 


## Page 9

printed using an Artillery Sidewinder X1 FDM machine. The printing process was deliberately interrupted before 
completion to show the gyroid infill pattern (Fig. 9 left). This result is compared with the one obtained in the FreeCAD 
reconstruction process (Fig. 9 right). The results suggest that the methodology was reliable even in the case of a 
complex infill pattern. 
 
 
Fig. 9. Comparison of real geometry (left), and reconstructed geometry in FreeCAD (right). 
4. Discussion and conclusions 
This study investigates a new and reproducible methodology to reconstruct the geometry of additively 
manufactured components knowing the G-CODE information. The reconstructed shape is exported as a STEP file to 
make it compatible with the majority of CAD and FEM packages. The aim of the research is achieved in three main 
steps namely: toolpath coordinates extraction (MATLAB), filtering of Marlin instructions and creation of a list of 
extrusion paths to be reproduced (Python), and geometry reconstruction through sweeps (FreeCAD). Table 3 
summarizes the pros and cons of the proposed methodology. 
Table 3. Advantages and challenges of the methodology. 
Pros 
Cons 
Possibility to reconstruct different profile sections and 
infills 
Limited profile section portfolio 
External geometry does not affect the methodology 
 
Limited by computational requirements 
Ease and reproducible 
 
1st version includes three different software 
 
Different geometries, infill patterns and density and sweep profiles are qualitatively investigated to understand their 
effect on the methodology performance. The results proved to be promising in terms of reconstruction quality even in 
the most complex scenarios. At the same time, the computational time might be a limiting factor for the simulation of 
bigger components because it grows with a power law as a function of the number of sweeps to be generated. In this 
regard, assuming that the astonishing increase in computational power seen in the last decade will continue at the same 
rate, it is reasonable to assume that bigger and more complex geometry, which now are unfeasible to reconstruct, 
might be modelled with this approach in the near future. Then, this potentially opens the possibility of importing the 
STEP file into an FEA software for structural simulations without requiring expensive and time-consuming 
experimental campaigns. 
The technique will be evaluated on additional topologies with a larger range of infill patterns and density in future 
research. To evaluate the importing, management, and meshing of complex 3D models, the final geometry will be 
uploaded into FEA software. Thus, a numerical technique might be utilised to comprehend the component's 
mechanical behaviour and compare it to experimental data to determine the validity of the approach presented in this 


## Page 10

study. Furthermore, the proposed methodology paves the way for the development of models specifically addressing 
the intra and inter-layer bounding of the material, where the anisotropy can be modelled by adjusting the amount of 
overlapping region within adjacent layers. 
To conclude, this work aims to provide a practical guide to all the researchers involved in the modelling of AM 
components in a clear and reproducible manner. We hope that this paper could promote and foster in the scientific 
community the need of sharing a common methodology to model AM structures. 
References 
[1] 
S. Mantovani, S. Barbieri, M. Giacopini, A. Croce, A. Sola, and E. Bassoli, ‘Synergy between topology 
optimization and additive manufacturing in the automotive field’, Proceedings of the Institution of 
Mechanical Engineers, Part B: Journal of Engineering Manufacture, 2020, doi: 10.1177/0954405420949209. 
[2] 
L. Zhu, N. Li, and P. R. N. Childs, ‘Light-weighting in aerospace component and system design’, Propulsion 
and Power Research, vol. 7, no. 2, pp. 103–119, 2018, doi: 10.1016/j.jppr.2018.04.001. 
[3] 
H. S. Park, D. S. Nguyen, T. Le-Hong, and X. Van Tran, ‘Machine learning-based optimization of process 
parameters in selective laser melting for biomedical applications’, J Intell Manuf, Apr. 2021, doi: 
10.1007/s10845-021-01773-4. 
[4] 
T. D. Ngo, A. Kashani, G. Imbalzano, K. T. Q. Nguyen, and D. Hui, ‘Additive manufacturing (3D printing): 
A review of materials, methods, applications and challenges’, Composites Part B: Engineering, vol. 143, pp. 
172–196, 2018, doi: 10.1016/j.compositesb.2018.02.012. 
[5] 
A. Bacciaglia, A. Ceruti, and A. Liverani, ‘Evaluation of 3D printed mouthpieces for musical instruments’, 
RPJ, vol. 26, no. 3, pp. 577–584, 2019, doi: 10.1108/RPJ-07-2019-0187. 
[6] 
I. Campbell, D. Bourell, and I. Gibson, ‘Additive manufacturing: rapid prototyping comes of age’, Rapid 
Prototyping Journal, vol. 18, no. 4, pp. 255–258, 2012, doi: 10.1108/13552541211231563. 
[7] 
I. Gibson, D. W. Rosen, and B. Stucker, Additive manufacturing technologies: 3D printing, rapid prototyping, 
and direct digital manufacturing, 2. ed. New York, NY: Springer, 2015. 
[8] 
G. Vega, R. Paz, A. Gleadall, M. Monzón, and M. E. Alemán-Domínguez, ‘Comparison of CAD and Voxel-
Based Modelling Methodologies for the Mechanical Simulation of Extrusion-Based 3D Printed Scaffolds’, 
Materials, vol. 14, no. 19, p. 5670, 2021, doi: 10.3390/ma14195670. 
[9] 
A. Bacciaglia, A. Ceruti, and A. Liverani, ‘Surface smoothing for topological optimized 3D models’, Struct 
Multidisc Optim, 2021, doi: 10.1007/s00158-021-03027-6. 
[10] O. A. Mohamed, S. H. Masood, and J. L. Bhowmik, ‘Modeling, analysis, and optimization of dimensional 
accuracy of FDM-fabricated parts using definitive screening design and deep learning feedforward artificial 
neural network’, Adv. Manuf., vol. 9, no. 1, pp. 115–129, Mar. 2021, doi: 10.1007/s40436-020-00336-9. 
[11] B. Rankouhi, S. Javadpour, F. Delfanian, and T. Letcher, ‘Failure Analysis and Mechanical Characterization 
of 3D Printed ABS With Respect to Layer Thickness and Orientation’, J Fail. Anal. and Preven., vol. 16, no. 
3, pp. 467–481, Jun. 2016, doi: 10.1007/s11668-016-0113-2. 
[12] J. M. Dulieu-Barton and M. C. Fulton, ‘Mechanical Properties of a Typical Stereolithography Resin’, Strain, 
vol. 36, no. 2, pp. 81–87, May 2000, doi: 10.1111/j.1475-1305.2000.tb01177.x. 
[13] S. Romano, A. Brückner-Foit, A. Brandão, J. Gumpinger, T. Ghidini, and S. Beretta, ‘Fatigue properties of 
AlSi10Mg obtained by additive manufacturing: Defect-based modelling and prediction of fatigue strength’, 
Engineering Fracture Mechanics, vol. 187, pp. 165–189, Jan. 2018, doi: 10.1016/j.engfracmech.2017.11.002. 
[14] P. Mercelis and J. Kruth, ‘Residual stresses in selective laser sintering and selective laser melting’, Rapid 
Prototyping Journal, vol. 12, no. 5, pp. 254–265, Oct. 2006, doi: 10.1108/13552540610707013. 
[15] C. S. Lee, S. G. Kim, H. J. Kim, and S. H. Ahn, ‘Measurement of anisotropic compressive strength of rapid 
prototyping parts’, Journal of Materials Processing Technology, vol. 187–188, pp. 627–630, Jun. 2007, doi: 
10.1016/j.jmatprotec.2006.11.095. 
[16] J. F. Rodríguez, J. P. Thomas, and J. E. Renaud, ‘Mechanical behavior of acrylonitrile butadiene styrene fused 
deposition materials modeling’, Rapid Prototyping Journal, vol. 9, no. 4, pp. 219–230, Oct. 2003, doi: 
10.1108/13552540310489604. 
[17] M. Sugavaneswaran and G. Arumaikkannu, ‘Analytical and experimental investigation on elastic modulus of 
reinforced additive manufactured structure’, Materials & Design, vol. 66, pp. 29–36, 2015. 
[18] J. Zarbakhsh, A. Iravani, and Z. Amin-Akhlaghi, ‘Sub-modeling Finite Element Analysis of 3D printed 
structures’, in 2015 16th International Conference on Thermal, Mechanical and Multi-Physics Simulation and 
Experiments in Microelectronics and Microsystems, Budapest, Hungary, Apr. 2015, pp. 1–4. doi: 
10.1109/EuroSimE.2015.7103095. 


## Page 11

[19] M. Somireddy and A. Czekanski, ‘Computational modeling of constitutive behaviour of 3D printed composite 
structures’, Journal of Materials Research and Technology, vol. 11, pp. 1710–1718, Mar. 2021, doi: 
10.1016/j.jmrt.2021.02.030. 
[20] F. Falcetelli, R. Di Sante, and E. Troiani, ‘Strategies for Embedding Optical Fiber Sensors in Additive 
Manufacturing Structures’, in European Workshop on Structural Health Monitoring, vol. 128, P. Rizzo and A. 
Milazzo, Eds. Cham: Springer International Publishing, 2021, pp. 362–371. doi: 10.1007/978-3-030-64908-
1_34. 
[21] F. Falcetelli, L. Rossi, R. Di Sante, and G. Bolognini, ‘Strain Transfer in Surface-Bonded Optical Fiber 
Sensors’, Sensors, vol. 20, no. 11, p. 3100, May 2020, doi: 10.3390/s20113100. 
[22] J. R. C. Dizon, A. H. Espera, Q. Chen, and R. C. Advincula, ‘Mechanical characterization of 3D-printed 
polymers’, Additive Manufacturing, vol. 20, pp. 44–67, Mar. 2018, doi: 10.1016/j.addma.2017.12.002. 
[23] ‘Ultimaker Cura’. Accessed: May 30, 2022. [Online]. Available: https://ultimaker.com/it/software 
 



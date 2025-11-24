# Digital Twin of Fused Filament Fabrication Prints for Finite Element Analysis via G-Code Reverse Engineering
**Author:** Santiago Ochoa, Santiago Ferrándiz, Luis Garzón, and Christian Cobos
**Subject:** 3D Printing and Additive Manufacturing 0.0

**Source:** `ochoa-et-al-2024-digital-twin-of-fused-filament-fabrication-prints-for-finite-element-analysis-via-g-code-reverse.pdf`
---

## Page 1

ORIGINAL ARTICLE
Digital Twin of Fused Filament Fabrication Prints for Finite
Element Analysis via G-Code Reverse Engineering
Santiago Ochoa,1 Santiago Ferrándiz,2 Luis Garzón,1 and Christian Cobos1
Abstract
As additive manufacturing by fused ﬁlament fabrication has gained popularity, computational analysis has
become fundamental in predicting the mechanical behavior of 3D models. This paper proposes the development
of a method for the ﬁnite element (FE) simulation of 3D-printed parts, implementing model design reverse
engineering using G-code to obtain their digital twins (DTs). Samples were printed under the ASTM D638
standard with different nozzle diameters and layer heights, which allowed them to be mechanically characterized
by tensile tests. The tensile tests determined that the diameter of the nozzles used (between 0.2 mm and 1.0 mm)
inﬂuences the material’s tensile strength. The greater the diameter, the greater the stiffness, which translates into
a change in the Young’s modulus, as well as greater tensile strength and thus a reduction of the deformation, for
which a value of 2.66 6 0:6% was obtained, i.e., the ﬁlament diameter did not inﬂuence this aspect. After
carrying out the reverse engineering process of the samples to obtain DTs of the physical models, the printing
G-code was used with the help of a Python script for their conversion to trajectories. These trajectories were
introduced into Rhinoceros software with the Grasshopper add-on to obtain the reconstructed 3D models. The
deposited ﬁlament proﬁle used to reconstruct the DT was obtained by microscopy of the section of the physical
samples. The predominant proﬁle observed was that of a ﬂattened oval. FE simulation was then carried out,
obtaining a similarity of 90% between the simulated and mechanical tests, which validated the proposed method
of predicting mechanical stresses in printed 3D elements.
Keywords: 3D printing, FEA, digital twins, G-code, reverse engineering
Introduction
Fused ﬁlament fabrication (FFF) additive manufacturing
uses a ﬁlament made of thermoplastic material to create parts
layer by layer (Davoudinejad and Pérez).1,2 The FFF process
is relatively simple and affordable and is widely used for the
manufacture of prototypes and functional parts.3–5
However, the process also has certain micromechanical
limitations, such as the formation of holes between layers
and a nonhomogeneous distribution of the deposited ﬁlament
that results in weak interlayer bonding6–8 limitations that can
reduce the mechanical properties of 3D-printed parts.9–11
The 3D printing material used has a strong inﬂuence on
the mechanical properties of the printed parts.12 Polylactic
acid (PLA) is a biodegradable thermoplastic polymer
obtained from renewable resources and is commonly used in
3D printing.13 It also has good mechanical strength and
excellent corrosion resistance,14 although it is associated
with certain limitations, such as a low heat resistance and a
tendency to deform.15,16
Two main methods can be used to determine and charac-
terize the mechanical properties of 3D-printed parts17: the
ﬁrst is by destructive mechanical tests that consist of sub-
jecting the parts to loading tests to measure their strength,
stiffness, ductility, and other properties,15 besides their
mechanical properties by a more expensive method that
requires a longer time18; the second method is by numerical
simulations using mathematical models to predict the printed
parts’ mechanical behavior,18,19 which although less accurate
than mechanical tests, is faster and easier to perform.4,20,21
This present proposal can be used to obtain digital twins
(DTs) that adequately represent 3D-printed physical speci-
mens and will be useful for researchers in new materials,
avoiding the production of large numbers of specimens for
1New Materials and Transformation Processes Research Group GiMaT, Universidad Politécnica Salesiana, Cuenca, Ecuador.
2ITM, Plaça Ferrándiz i Carbonell, Universitat Politècnica de València, s/n, Alcoi, Spain.
1
3D PRINTING AND ADDITIVE MANUFACTURING
Volume 00, Number 00, 2024
ª Mary Ann Liebert, Inc.
DOI: 10.1089/3dp.2023.0325
Open camera or QR reader and
scan code to access this article
and other resources online.


## Page 2

mechanical characterization and avoiding the expense of
specialized machinery to produce the specimens.22–25
There are many studies in the literature on 3D-printed part
simulation using ﬁnite element analysis (FEA)2,6,26,27 in a
wide range of aspects, including stress and strain distribu-
tion, the formation of free spaces between the ﬁlaments, and
the inﬂuence of the process parameters.28–30 However, most
of these works performed part simulations that did not repre-
sent the objects’ real internal structure, considering them as
completely solid elements or as pseudo-solids reconstructed
by voxels, which cannot reﬂect the real situation.13,31,32
Our aim in the present study was to develop a method of
simulating 3D-printed parts by FEA, consisting of recon-
structing the trajectory of the material deposition from the
G-code, generating a DT that faithfully resembles the struc-
ture of the actual printed part to improve the simulation
accuracy, as this can capture the micromechanical process
details more accurately.
Materials and Methods
Materials
The specimen were printed from CoLiDo’s PLA natural
brown ﬁlament, with a diameter of 1.75 – 0.02 mm. For opti-
mal results, the manufacturer recommends nozzle tempera-
tures ranging from 190C to 210C and bed temperatures
between 60C and 70C.
Method
Specimen printing.
The specimen design was carried out
under ASTM D63833 standards for tensile testing with the
dimensions shown in Figure 1.
Printing was performed on a Prusa MK3S printer and
varying the printing nozzle diameter from 0.2 mm to 1 mm.
These variations were made to evaluate the effect of print
resolution on the specimens’ mechanical properties.
The designed specimens did not contain any width
reduction or restriction, due to previous tests and experi-
ments, when stretching specimens with width extractions
as in the Dogbone test specimen design, the external ﬁla-
ments start to separate independently before an adequate
characterization can be made.34
The specimen slicing process allowed the generation of
the G-code, which contains the instructions for the printer by
using the Open-source Ultimaker Cura software version
4.13.1.35
The general printing parameters are shown in Table 1.
According to Fernádez and Quajin,34,36 the most rigid and
strongest inﬁll patterns for 3D-printed parts are the “Honey-
comb” or “Cubic,” so we used the latter as the inﬁll pattern.
The layer thickness was parameter varied and was set at
60% of the installed nozzle diameter to ensure good layer
adhesion and surface quality, as shown in Table 2. This
value was set considering that a layer thickness greater than
80% can lead to excessive surface roughness in 3D prints
(Bintara).37
Tensile test.
The printed specimens were characterized
on a Shimadzu AGS-300kNX model AGS-300kNX38 uni-
versal testing machine by means of a tensile test.
FIG. 1.
Specimen dimensions.
Table 1. General 3D Printing Parameters
General 3D printing parameters
Walls [#]
3
Inﬁll [%]
50
Inﬁll Pattern
Cubic
Printing Temperature [C]
215
Build Plate Temperature [C]
60
Printing Speed [mm/s]
65
Table 2. Print Height vs Nozzle Diameter
Printing parameters by nozzle diameter
[ Nozzle [mm]
0.2
0.3
0.4
0.5 0.6
0.8
1.0
Layer height [mm] 0.12
0.18 0.24 0.3 0.36
0.48 0.6
FIG. 2.
Reverse engineering ﬂowchart.
2
OCHOA ET AL.


## Page 3

Eight specimens were tested for each nozzle diameter
installed, i.e., 56 specimens, which were subjected to a ten-
sile test with a jaw spacing of 74.3 mm and a speed of
3 mm/min, according to the ISO 527 tensile test standard.39,40
The displacement velocity was selected from previously
published studies.41 Tensile strength, Young’s modulus, and
elongation were also analyzed.
Microscopic section analysis.
To determine the recon-
struction proﬁle of the specimen used (see Section 3.2.4),
cross-sectional micrographs were taken of the specimens
already tested.
A Stemi 508 microscope equipped with a Zeiss Axiocam
208 camera42 was used in combination with the Zeiss Lab-
scope Android application.
Micrographs were taken at 8 · magniﬁcation, transmitted
illumination, and in the digital capture mode.
Specimen reverse engineering.
To obtain a similar DT
to the printed specimen, a reconstruction process was per-
formed of the G-code obtained by the slicer.
The ﬂow diagram shown in Figure 2 illustrates the process
followed to obtain the digital specimens.
Slicing was performed from the CAD ﬁle with the speci-
mens’ dimensions on Ultimaker Cura software to obtain the
G-code, after which Python script was used to generate a
DXF ﬁle with the trajectories and deposition curves of the
molten material.
The Python script used an algorithm to identify the
G-code deﬁning the printing coordinates and the resulting
DXF ﬁle contained a series of lines and curves represent-
ing the printing trajectories, as can be seen in Figure 3.
The script used to obtain the DXF ﬁle of the specimen
produced by a nozzle diameter of 0.8 mm can be found in
Supplementary Data S1.
The DT was generated from the DXF ﬁle by the pipe com-
mand in Rhinoceros and its Grasshopper plug-in.
FEA simulation.
The DT was subjected to an FEA on
Ansys software Version 2023 using the “Static Structural”
module to determine the Stress-Strain response.
The material was characterized considering the differen-
ces between working with injected parts and layer-by-layer
extrusion. The Young’s modulus therefore was not the same
as in the conventional literature, so considering the studies
by Torres43 and Alharbi44 as reference, the Young’s modulus
of the mechanical tests performed was obtained.
For the tensile test simulation, the specimen geometry was
trimmed to the test extension (distance between grips) of
74.3 mm and the X axis was considered to be symmetrical,
as can be seen in Figure 4, to reduce the computational cost
of the test.
We considered using a “Body Sizing” of 3 mm for the
meshing to obtain the optimum mesh quality. The mesh
quality metric was the “Aspect Ratio” with a nominal value
of 1.23, which indicates a mostly good distribution of the
mesh elements, with no elongated or ﬂattened elements that
could affect the results (Figure 5).
Figure 6 gives the conﬁguration to replicate the ISO
527 tensile test.
Results
Specimen printing
Printed ASTM D638-compliant specimens were obtained
by varying the nozzle diameter to control the specimens’
layer height.
Figure 7A shows the inﬁll in a printed specimen, whereas
Figure 7B shows the specimen used for mechanical tests.
Tensile test
The inﬂuence of ﬁlament diameter and layer thickness
was analyzed from the maximum stress, modulus of elas-
ticity, and elongation of the tensile specimens, as shown in
Figure 8.
The average values of the seven tests carried out with the
nozzle diameters analyzed can be seen in Table 3.
The comparison of the maximum stress average values
showed variations between the specimens produced by dif-
ferent nozzle diameters (minimum values of 73.12 MPa and
maximum values of 62.34 MPa for 0.2 and 1.0 mm nozzle
diameters, respectively), indicating the signiﬁcant inﬂuence
of nozzle diameter on strength.45 In Figure 8, it can also be
FIG. 3.
Curves and trajectories (DXF File).
FIG. 4.
Specimen geometry for simulation.
FIG. 5.
Specimen meshing.
FIG. 6.
Conﬁguration of test conditions: A) “Frictionless
support,” B) “Fixed support,” C) “Displacement (3 mm/min).”
FIG. 7.
Printed specimens.
3D PRINTING DIGITAL TWINS FEA SIMULATION
3


## Page 4

seen that as nozzle diameter increases the stiffness also
increases, together with a change in the Young’s modulus.
The maximum deformation of an average of 2.66 – 0:6%
showed that nozzle diameter did not signiﬁcantly affect
deformation. The elastic modulus contained values between
50.08 MPa and 61.79 MPa as minimum and maximum
respectively, as can be seen in Figure 8.
Figure 9 contains the stress—strain diagram of the ana-
lyzed specimens, also the deformation and stress on breakage.
It can be seen that the deformation in the plastic zone is
variable, reaching a higher deformation in specimens printed
at a 0.3 mm nozzle diameter. As this diameter increases (0.6;
0.8; 1.0 mm), maximum tensile strength also increases,
reducing the deformation. It can also be seen that the 0.2 and
0.4 mm nozzle specimens have a similar deformation behav-
ior to that of the 0.3 mm nozzles.
Microscopic section analysis
The side view of all the specimens show a constant
cross-section owing to the linear deposition path, as can be
seen in Figure 10A and D. The specimen also exhibits cir-
cular cross sections, as seen in Figure 10B and E. How-
ever, the predominant specimen proﬁle has a ﬂattened oval
shape (Fig. 10C and F).
Since the specimen’s reconstruction in reverse engineer-
ing needs a constant proﬁle, we considered the proﬁle pos-
sessed by the majority of the specimens. This provided the
reconstruction section shown in Figure 11A, in which “H” is
the layer height and “W” is the installed nozzle diameter.
The proﬁle can also be obtained by merging overlapping
circular sections, as shown in Figure 11B.
We found that as the ﬁlament diameter increased, the number
of spaces was reduced but that the dimensions also increased,
whereas the upper and lower layers almost completely fused the
ﬁlaments, leaving very small free spaces (Fig. 12).
Specimen reverse engineering
Specimens in the STL format produced in accordance with
ASTM D638 were obtained from a CAD modeling process in
Fusion 360 (Fig. 13A). Ultimaker Cura was then used to gen-
erate a G-code ﬁle containing the necessary commands to cre-
ate the specimens (Fig. 13B). A DXF ﬁle was obtained with a
Python script and the G-code (Fig. 13C) containing the trajec-
tories and curves that deﬁned the specimen. Finally, Rhinoc-
eros was used to reconstruct the CAD specimen from the
DXF ﬁle suitable for FE simulation (Fig. 13D).
The challenges involved in this process were as follows:
some trajectories did not contribute material when making
FIG. 8.
Stress [MPa] vs. strain [%] diagram nozzle comparison.
Table 3. Summary of Tensile Test Results
Nozzle diameter [mm]
Max. Stress [MPa]
Std [MPa]
Max. Strain [%]
Std [%]
Elastic modulus [MPa]
Std [MPa]
1.0
73.12
0.426
1.46
0.376
50.08
1.756
0.8
66.58
0.429
1.18
0.227
56.42
0.098
0.6
63.42
0.132
1.11
0.021
57.13
1.253
0.5
62.34
0.130
1.13
0.034
55.16
0.227
0.4
65.35
0.200
1.13
0.169
57.83
0.313
0.3
67.97
0.566
1.10
0.314
61.79
1.318
0.2
64.44
0.281
1.22
0.016
52.81
0
4
OCHOA ET AL.


## Page 5

the Python script for converting the G-code to DXF (dis-
placement movements) and affected the subsequent proc-
esses. The Python script thus had to go through several
iterations and corrections until a ﬁlter was obtained that only
considered the movements that contributed material.
In the DXF to STP conversion process, a solid is gener-
ated for each trajectory. As the specimen was made up of
considerable number of solids, to solve this problem and
unify the solids, we had to go through an additional Boolean
combination operation, which did not work optimally in all
cases.
The DT was ﬁnally obtained after overcoming all these
obstacles and an FEA was performed to compare the results
with those of the mechanical tests.
FIG. 9.
Stress [MPa] vs. strain [%] diagram nozzle comparison with deformation and break point.
FIG. 10.
Microscopic section analysis, all the images were obtained using 8 · magniﬁcation.
3D PRINTING DIGITAL TWINS FEA SIMULATION
5


## Page 6

FEA simulation
The simulation results showed that the highest stress con-
centration occurred in the internal part of the specimen (Fig.
14A), whereas its external part had better mechanical
strength (Fig. 14B).
The following results were obtained for the specimens
using the Ansys Workbench, with its Static Structural
component.
The responses were compared with the mechanical tests,
obtaining the results shown in the Figures 15–21.
It should be noted that the FE analysis carried out only
considered the elastic zone of the material, whereas in future
work we hope to use a polynomial model that can also ana-
lyze the plastic zone.
To perform the calculation that converts the result in N to
MPa, it is necessary to consider that the specimen has a non-
solid cross-sectional area, which can be approximated as fol-
lows (Figure 22).
Equation (1) represents the area of the specimen’s perime-
ter section, which can be calculated from the nozzle diameter
(a), the number of perimeters (b) and the height of the speci-
men (H):
A1 ¼ A2 ¼ a · b · H
(1)
Equation (2) represents the area of the specimen’s top
and bottom sections, which can be obtained from the width
(W), the parameters (a), and (b) as described above, the
number of top and bottom layers (c), and the layer height
(d):
A3 ¼ A4 ¼ W  2 · a · b
ð
Þ · c · d
(2)
Equation (3) represents the specimen’s inﬁll section area:
A5 ¼ W · H
ð
Þ  A1  A2  A3  A4
2
(3)
Equation (4) calculates the total area of the specimen:
AT ¼ A1 þ A2 þ A3 þ A4 þ A5
(4)
and ﬁnally Equation (5) is the area, considering 50% of
empty space due to the inﬁll percentage:
A ¼ AT
2
(5)
Where:
a = Nozzle diameter [mm]
b = Perimeters [#]
c = Top and Bottom Layers [#]
d = Layer height [mm]
H = Specimen height [mm]
W = Specimen width [mm]
Table 4 summarizes the area calculation for the specimens
tested.
Once the real resistant areas shown in Table 4 had been
determined, the computational results were obtained as
shown in Table 5, taking the maximum stress of the tests as
the reference.
The force results of both the mechanical and simulated
tests had an error of less than 4%.
Discussion
Some factors were generated during printing that modiﬁed
the specimen geometry, such as the Elephant’s Foot effect in
the ﬁrst layers deposited, which can be corrected during seg-
mentation by adding a shrinkage factor to the ﬁrst layers.
Due to the perpendicular edges of the specimens, the dep-
osition rate is complex to replicate computationally and can
FIG. 11.
Reconstruction proﬁle.
FIG. 12.
Fusion of perimeters on upper and lower layers.
FIG. 13.
Reverse engineering results.
FIG. 14.
Simulated specimen stress concentration.
6
OCHOA ET AL.


## Page 7

FIG. 15.
Stress vs. strain comparison (nozzle 1.0 mm).
FIG. 16.
Stress vs. strain comparison (nozzle 0.8 mm).
FIG. 17.
Stress vs. strain comparison (nozzle 0.6 mm).
FIG. 18.
Stress vs. strain comparison (nozzle 0.5 mm).
FIG. 19.
Stress vs. strain comparison (nozzle 0.4 mm).
FIG. 20.
Stress vs. strain comparison (nozzle 0.3 mm).
7


## Page 8

be seen as an accumulation of material on the edges of the
geometry.
The material shrinkage cannot be adequately replicated
due to cooling during printing, another factor that was not
considered when obtaining the DT.
Due to the combination of circular and oval proﬁles found
under the microscope, the macro-mechanical properties of
the different specimens corresponded signiﬁcantly with the
results obtained computationally, in which both reconstruc-
tion proﬁles were considered.
Even though it faithfully represents the printed specimens,
the computational cost of generating the process described in
the present paper is high as the current reconstruction method
generates a solid for each trajectory. In future work, we pro-
pose to obtain a single polyline instead of several trajectories
and generate a single solid, avoiding Boolean operations,
which can increase the complexity of the generated model.
Conclusions
In this study, we determined that increasing the ﬁlament
diameter also increases the mechanical tensile strength. This
could be due to the fact that the percentage of free spaces
between the ﬁlaments is reduced. These can function as
stress concentrations during the test and are a relevant factor
in increasing the strength.
The nozzle diameter has a signiﬁcant impact on the plastic
deformation behavior of 3D-printed parts. Specimens printed
with smaller diameter nozzles show higher plastic deformation,
whereas those printed with larger diameter nozzles show lower
deformation. This can be explained by the smaller diameter
nozzles extruding a smaller amount of material per unit time,
which leads to a denser and more compact part structure and
partially hinders plastic deformation.
The simulation values as the tensile tests obtained a simi-
larity of 97 – 2%, which could have been due to several
reasons difﬁcult to control during the computational recon-
struction of the specimen, as described below:
1. Expansion deformation in the ﬁrst layer (3D Print
Elephant’s Foot).
2. Flow velocity, a parameter that cannot be controlled dur-
ing the computational reconstruction of the specimen.
3. Material shrinkage.
4. Extrusion failures in the specimens due to assuming
constant material deposition during the reconstruction,
while this is not so in printed specimens, as we found
in the microscopy images.
5. The CAD-reconstructed specimen does not have seams
(union of the beginning of the ﬁlament with the end of
the perimeter).
6. Thermal variation of the joint during layer deposition,
depositing hot material on solidiﬁed layers.
All these factors could have been responsible for the var-
iations in the results between the mechanical testing and
computational simulation.
Taking the above factors into consideration, plus the level
of similarity achieved, reverse engineering and a computa-
tional testing method can be applied as a computational anal-
ysis method.
Reconstructing and testing DTs requires a large amount of
computational resources, in addition to the fact that the cur-
rent CAD software is not fully prepared to handle the
FIG. 21.
Stress vs. strain comparison (nozzle 0.2 mm).
FIG. 22.
Specimen cross-sectional area. A1 and A2 are
perimeter areas, A3 and A4 are top and bottom areas, and
A5 is the inﬁll area.
Table 4. Calculated Areas
a [mm]
b [#]
c [#]
D [mm]
A1 [mm2]
A2 [mm2]
A3 [mm2]
A4 [mm2]
A5 [mm2]
At [mm2]
1.0
3
2
0.6
18
18
16.8
16.8
25.2
94.8
0.8
3
2
0.48
14.4
14.4
14.59
14.59
31
88.99
0.6
3
3
0.36
10.8
10.8
17.71
17.71
31.48
88.51
0.5
3
3
0.3
9
9
15.3
15.3
35.7
84.3
0.4
3
3
0.24
7.2
7.2
12.67
12.67
40.12
79.87
0.3
3
3
0.18
5.4
5.4
9.82
9.82
44.77
75.22
0.2
3
3
0.12
3.6
3.6
6.76
6.76
49.63
70.36
8
OCHOA ET AL.


## Page 9

considerable number of trajectories and solids contained in
the specimen.
In the FE simulation, the numerous nodes and ﬁnite ele-
ments required very long simulation times.
Authors’ Contributions
S.O.: Review and Editing (equal); writing—original draft
(lead); Software (lead); Methodology (equal). S.F.: Software
(supporting); Methodology (supporting). L.G.: Writing—
Review & editing (supporting) Validation (equal). C.C.:
Conceptualization
(lead);
Methodology
(lead).
Writing—
Review & Editing (supporting); Validation (lead).
Author Disclosure Statement
No competing ﬁnancial interests exist.
Funding Information
No funding was received for this article.
Supplementary Material
Supplementary Data S1.
References
1. Davoudinejad A, Cai Y, Pedersen DB, et al. Fabrication of
micro-structured surfaces by additive manufacturing, with
simulation of dynamic contact angle. Materials Amp; Design
2019;176:107839; doi: 10.1016/j.matdes.2019.107839
2. Perez DB, Celik E, Karkkainen RL. Investigation of inter-
layer interface strength and print morphology effects in
fused deposition modeling 3D-printed PLA. 3D Print Addit
Manuf 2021;8(1):23–32; doi: 10.1089/3dp.2020.0109
3. Vanaei H, Shirinbayan M, Deligant M, et al. Inﬂuence of pro-
cess parameters on thermal and mechanical properties of pol-
ylactic acid fabricated by fused ﬁlament fabrication. Polym
Eng Sci 2020;60(8):1822–1831; doi: 10.1002/pen.25419
4. Yang J, Yue H, Mirihanage W, et al. Multi-stage thermal
modelling of extrusion-based polymer additive manufacturing.
Polym (Basel) 2023;15(4):838; doi: 10.3390/polym15040838
5. Singh P, M.Singari R, Mishra RS. A review of study on
modeling and simulation of Additive Manufacturing Proc-
esses. Mater Today: Proceedings 2022;56:3594–3603; doi:
10.1016/j.matpr.2021.12.057
6. Gupta C, Mb P, Shet NK, et al. Microstructure and mechan-
ical performance examination of 3D printed acrylonitrile
butadiene styrene thermoplastic parts. Polym Eng Sci 2020;
60(11):2770–2781; doi: 10.1002/pen.25507
7. Al Rashid A, Khan SA, G. Al-Ghamdi S, et al. Additive
Manufacturing of polymer nanocomposites: Needs and chal-
lenges in materials, processes, and applications. J Mater Res
Technol 2021;14:910–941; doi: 10.1016/j.jmrt.2021.07.016
8. Ramezani Dana H, Barbe F, Delbreilh L, et al. Polymer
additive manufacturing of ABS structure: Inﬂuence of print-
ing direction on mechanical properties. J Manuf Processes
2019;44:288–298; doi: 10.1016/j.jmapro.2019.06.015
9. Rogkas N, Vakouftsis C, Spitas V, et al. Design aspects of
additive manufacturing at Microscale: A Review. Microma-
chines (Basel) 2022;13(5):775; doi: 10.3390/mi13050775
10. Monfared V, Bakhsheshi-Rad HR, Ramakrishna S, et al.
A brief review on additive manufacturing of polymeric
composites and nanocomposites. Micromachines (Basel)
2021;12(6):704; doi: 10.3390/mi12060704
11. Garcia Collado A, Dorado Vicente R, Carazo Álvarez D, et al.
Evaluation of the mechanical properties and microstructure of
Aisi 316L alloy specimens printed by fused ﬁlament fabrica-
tion. DYNAII 2022;97(3):254–257; doi: 10.6036/10423
12. Yuan S, Li S, Zhu J, et al. Additive manufacturing of poly-
meric composites from material processing to structural
design. Compos Part B: Eng 2021;219:108903; doi: 10
.1016/j.compositesb.2021.108903
13. Postiglione G, Natale G, Grifﬁni G, et al. Conductive 3D
microstructures by direct 3D printing of polymer/carbon
nanotube nanocomposites via liquid deposition modeling.
Compos Part A: Applied Sci Manuf 2015;76:110–114; doi:
10.1016/j.compositesa.2015.05.014
14. Shabana N, Santosh RV, Sarojini J, et al. Evaluating the
mechanical properties of commonly used 3D printed ABS
and PLA polymers with multi layered polymers. Int J of
Eng Adv Technol 2019;8(6):2351–2356; doi: 10.35940/ijeat
.f8646.088619
15. Butt J, Bhaskar R. Investigating the effects of annealing on
the mechanical properties of FFF-printed thermoplastics.
JMMP 2020;4(2):38; doi: 10.3390/jmmp4020038
16. Zhou X, Deng J, Fang C, et al. Additive Manufacturing of
CNTS/PLA composites and the correlation between micro-
structure and functional properties. J Mater Sci Amp; Tech-
nol 2021;60:27–34; doi: 10.1016/j.jmst.2020.04.038
17. Kumar Srivastava A, Kumar N, Rai Dixit A. Friction stir
additive manufacturing—an innovative tool to enhance
mechanical and microstructural properties. Mater Sci Eng:
B 2021;263:114832; doi: 10.1016/j.mseb.2020.114832
18. Zhang Z, Wang Y, Ge P, et al. A review on modelling and
simulation of Laser Additive Manufacturing: Heat transfer,
microstructure evolutions and mechanical properties. Coat-
ings 2022;12(9):1277; doi: 10.3390/coatings12091277
19. Favaloro A, Brenken B, Barocio E, et al. Dassault Sys-
temes’ Science in the Age of Experience. In: Simulation of
polymeric composites additive manufacturing using abaqus.
Researchgate: Chicago; 2017.
20. El Moumen A, Tarfaoui M, Lafdi K. Additive Manufactur-
ing of polymer composites: Processing and modeling
approaches. Composites Part B: Engineering 2019;171:
166–182; doi: 10.1016/j.compositesb.2019.04.029
21. Tang R, Zhang C, Liu J. Concurrent topological structure and
cross-inﬁll angle optimization for material extrusion polymer
additive manufacturing with microstructure modeling. Micro-
machines (Basel) 2022;13(6):852; doi: 10.3390/mi13060852
22. Cobos CM, Garzón L, López J, et al. Study of thermal and
rheological properties of PLA loaded with carbon and
Table 5. Results Comparison
Nozzle diameter
[mm]
Real
[MPa]
Simulation
[MPa]
Error
[%]
1.0
73.12
70.71
3.30%
0.8
66.58
64.45
3.20%
0.6
63.42
61.20
3.50%
0.5
62.34
60.03
3.70%
0.4
65.35
62.93
3.70%
0.3
67.97
65.66
3.40%
0.2
64.44
62.44
3.10%
3D PRINTING DIGITAL TWINS FEA SIMULATION
9


## Page 10

Halloysite nanotubes for additive manufacturing. RPJ 2019;
25(4):738–743; doi: 10.1108/rpj-11-2018-0289
23. Cobos CM, Fenollar O, López J, et al. Effect of maleinized
linseed oil (MLO) on thermal and rheolological properties
of PLA/MWCNT and PLA/HNT nanocomposites for addi-
tive manufacturing. RPJ 2020;26(6):1027–1033; doi: 10
.1108/rpj-08-2019-0217
24. Mosquera A, Andrade P, Cobos C, et al. Redesign of a 3D
low cost ﬁlament printer, adapting it to a pellet extruder for
new material assays. Macromol Symposia 2022;404(1); doi:
10.1002/masy.202100323
25. Cobos C, Conejero A, Fenollar O, et al. Inﬂuence of the
addition of 0.5 and 1% in weight of multi-wall carbon nano-
tubes (mwcnts) in poly-lactic acid (PLA) for 3D printing.
Procedia Manufacturing 2019;41:875–881; doi: 10.1016/j
.promfg.2019.10.010
26. Harris M, Potgieter J, Archer R, et al. Effect of material and
process speciﬁc factors on the strength of printed parts in
fused ﬁlament fabrication: A review of recent developments.
Mater (Basel) 2019;12(10):1664; doi: 10.3390/ma12101664
27. Craton MT, Albrecht JD, Chahal P, et al. in situ nanocompo-
site fabrication for RF Electronics applications with Additive
Manufacturing. IEEE Trans Microwave Theory Techn 2020;
68(5):1646–1659; doi: 10.1109/tmtt.2020.2977030
28. Bamiduro O, Owolabi G, Haile MA, et al. The inﬂuence of
load direction, microstructure, raster orientation on the
quasi-static response of fused deposition modeling abs. RPJ
2018;25(3):462–472; doi: 10.1108/rpj-04-2018-0087
29. Mohebbi MS, Ploshikhin V. Implementation of nucleation in
cellular automaton simulation of microstructural evolution
during additive manufacturing of Al Alloys. Additive Manu-
facturing 2020;36:101726; doi: 10.1016/j.addma.2020.101726
30. Goh GD, Yap YL, Tan HK, et al. Process–structure–
properties in polymer additive manufacturing via material
extrusion: A Review. Critical Reviews in Solid State and
Materials
Sciences
2019;45(2):113–133;
doi:
10.1080/
10408436.2018.1549977
31. Roy M, Tran P, Dickens T, et al. Composite reinforcement
architectures: A review of ﬁeld-assisted additive manufac-
turing for polymers. J Compos Sci 2019;4(1):1; doi: 10
.3390/jcs4010001
32. Cohen A, Barath S. Integrating large-scale additive manu-
facturing and bioplastic compounds for architectural acous-
tic performance. Proceedings of the 28th Conference on
Computer Aided Architectural Design Research in Asia
(CAADRIA) [Volume 2]. 2023; doi:10.52842/conf.caadria
.2023.2.179
33. Standard test method for tensile properties of plastics [Inter-
net]. Available from: https://www.astm.org/d0638-14.html
[Last accessed: November 24, 2023].
34. Fernandez-Vicente M, Calle W, Ferrandiz S, et al. Effect of
inﬁll parameters on tensile mechanical behavior in desktop
3D printing. 3D Print Addit Manuf 2016;3(3):183–192; doi:
10.1089/3dp.2015.0036
35. Ultimaker C. Release Ultimaker Cura 4.13.1. Ultimaker/-
Cura [Internet]. 2022. Available from: https://github.com/
Ultimaker/Cura/releases/tag/4.13.1 [Last accessed: Novem-
ber 24, 2023].
36. Ma Q, Rejab M, Kumar AP, et al. Effect of inﬁll pattern,
density and material type of 3D printed cubic structure
under quasi-static loading. Proceedings of the Institution of
Mechanical Engineers, Part C: Journal of Mechanical Engi-
neering Science 2020;235(19):4254–4272; doi: 10.1177/
0954406220971667
37. Bintara RD, Lubis DZ, Aji Pradana YR. The effect of layer
height on the surface roughness in 3D printed polylactic acid
(PLA) using FDM 3D printing. IOP Conf Ser: Mater Sci Eng
2021;1034(1):012096; doi: 10.1088/1757-899x/1034/1/012096
38. Shimadzu. Autograph AGS-X series—specs [Internet].
Available from: https://www.shimadzu.com/an/products/
materials-testing/uni-ttm/autograph-ags-x-series/spec.html
[Last accessed: November 24, 2023].
39. Standardization IO for. Plastics—determination of tensile prop-
erties—part 1: General principles. ISO 527-1:2019(En) [Inter-
net]. 2022. Available from: https://www.iso.org/obp/ui/#iso:
std:iso:527:-1:ed-3:v1:en [Last accessed: November 24, 2023].
40. Rankouhi B, Javadpour S, Delfanian F, et al. Failure analysis
and mechanical characterization of 3D printed ABS with
respect to layer thickness and orientation. J Fail Anal and Pre-
ven 2016;16(3):467–481; doi: 10.1007/s11668-016-0113-2
41. Grijpma DW, Altpeter H, Bevis MJ, et al. Improvement of
the mechanical properties of poly(D, L-lactide) by orienta-
tion. Polym Int 2002;51(10):845–851; doi: 10.1002/pi.988
42. Zeiss Stemi 508 stereo microscope with 8:1 zoom. [Internet].
Available from: https://www.zeiss.com/microscopy/en/
products/light-microscopes/stereo-and-zoom-microscopes/
stemi-508.html [Last accessed: November 24, 2023].
43. Torres J, Cotelo J, Karl J, et al. Mechanical property optimi-
zation of FDM PLA in shear with multiple objectives. JOM
2015;67(5):1183–1193; doi: 10.1007/s11837-015-1367-y
44. Alharbi M, Kong I, Patel VI. Simulation of uniaxial stress–
strain response of 3D-printed polylactic acid by nonlinear
ﬁnite element analysis. Appl Adhes Sci 2020;8(1); doi: 10
.1186/s40563-020-00128-1
45. Czy_zewski P, Marciniak D, Nowinka B, et al. Inﬂuence of
extruder’s nozzle diameter on the improvement of func-
tional properties of 3D-printed PLA products. Polym
(Basel) 2022;14(2):356; doi: 10.3390/polym14020356
Address correspondence to:
Christian Cobos
New Materials and Transformation Processes Research
Group GiMaT
Universidad Politécnica Salesiana
Calle vieja y Elia Liut
Cuenca 010107
Ecuador
E-mail: ccobos@ups.edu.ec
10
OCHOA ET AL.



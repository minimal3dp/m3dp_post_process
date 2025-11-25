#
**Author:** Anthony Kibort

**Source:** `IMECE2024_143962_ENHANCINGTHESTRUCTURALPERFORMANCEOF3DPRINTEDOBJECTSTHROUGHGCODEOPTIMIZATIONVIAFEAINTHEFDMPROCESS (1).pdf`
---

## Page 1


1
© 2024 by ASME

Proceedings of the ASME 2024
International Mechanical Engineering Congress and Exposition
IMECE2024
November 17–21, 2024
Portland, OR, USA

IMECE2024-143962
ENHANCING THE STRUCTURAL PERFORMANCE OF 3D PRINTED OBJECTS THROUGH
G CODE OPTIMIZATION VIA FEA IN THE FDM PROCESS

Saquib Shahriar, Razaul Islam, Jaejong Park, PhD
Prairie View A&M University
Prairie View, TX


ABSTRACT
Additive manufacturing, an innovative process that
assembles materials layer by layer from 3D model data, is
recognized as a transformative technology across diverse
industries. Researchers have extensively investigated the impact
of various printing parameters of 3D printing machines, such as
printing speed, nozzle temperature, and infill, on the mechanical
properties of printed objects. Specifically, this study focuses on
applying Finite Element Analysis (FEA) in G code modification
in Fused Deposition Modeling (FDM) 3D Printing. FDM
involves extruding a thermoplastic filament in layers over a build
plate to create a three-dimensional object. In the realm of load-
bearing structures, the Finite Element Analysis (FEA) process is
initiated on the target object, employing the primary load to
identify areas with high-stress concentrations. Subsequently,
optimization techniques are used to strategically assign printing
parameter combinations to improve mechanical properties in
potentially vulnerable regions. The ultimate objective is to tailor
the G code, a set of instructions for the printer, to strengthen
particular areas and improve the printed object's overall
structural integrity. To evaluate the suggested methodology's
efficacy, the study conducts a comprehensive analysis of printed
objects, both with and without the optimized G code.
Simultaneously, mechanical testing, such as tensile testing,
demonstrates quantitative data on structural performance. This
comprehensive analysis aims to identify the impact of G code
alteration on the finished product. Preliminary experimental
results using simple tensile specimens indicate notable
improvements in structural performance. Importantly, these
improvements are achieved without any discernible mass
increase, optimizing material usage and reducing the cost of
additive manufacturing. The modified G code targets to
strengthen critical areas using updated printing parameters
without a net increase in the overall material consumption of the
object. This finding holds significant implications for industries
reliant on additive manufacturing for load-bearing components,
offering a promising avenue for improved efficiency and
durability. Integrating advanced techniques, such as G code
modification and finite element analysis (FEA), as the additive
manufacturing landscape evolves presents a pathway toward
optimizing mechanical properties. By contributing valuable
insights and laying the groundwork for further exploration and
refinement of these methodologies, this study paves the way for
enhanced structural performance in various additive
manufacturing applications. Ultimately, it
encourages
innovation and progress in the field, propelling the industry
toward new heights of efficiency and reliability.

Keywords: Finite Element Analysis, G-Code Optimization,
3D Printing, Additive Manufacturing

1.
INTRODUCTION

Additive manufacturing is a groundbreaking technology
used across many industries. It has been widely used in
manufacturing industries, biomedical applications, aerospace,
and buildings nowadays [1][2]. Because of the wide possibility
of applications, researchers have examined how different
printing factors, like temperature and speed, affect the strength
of printed items for better product quality. For instance,
researchers have [3] investigated the influence of temperature
and material variation on the mechanical properties of parts
fabricated with FDM additive manufacturing, revealing
temperature as a significant factor affecting tensile strength and
process optimization. Additionally, Tessa Jane Gordelier et al.
[4]
review
strategies for
optimizing FDM
additive
manufacturing for maximum tensile strength, identifying key
factors
influencing
mechanical
properties.
Moreover,
the thermal behavior of 3D printers has been investigated, which
provided insights into optimizing FDM processes for improved
printing quality and efficiency. Adjustments to FDM technique
process parameters have drawn significant attention from
researchers. For example, Murugan et al. [5] investigated how
different parameters influence 3D printed structures. Their
findings highlighted the notable impact of layer height on
ultimate tensile strength and printing duration, while extrusion


## Page 2


2
© 2024 by ASME
temperature significantly affects the elastic modulus. Notably,
nozzle temperature is crucial in determining the mechanical
properties and overall quality of FDM printed parts, especially
with PLA as the printing material. Many researchers have
observed that increasing nozzle temperatures enhances the
mechanical properties of PLA printed materials [6]. This finding
was verified by Alsoufi et al. [7], who found the highest tensile
strength when the nozzle temperature was raised from 180°C to
220°C for parts with 100% infill. Moreover, print speed along
the platform significantly influences the quality of 3D-printed
parts. Traditionally, the operating speeds of FDM 3D printers
used for PLA printing are low, usually less than 100 mm/s [8].
Researchers, such as Napolitano et al. [9], have even analyzed
PLA's mechanical properties at 110mm/s, revealing that higher
printing speeds lead to the highest tensile strength for PLA
materials. Therefore, exploring higher speeds is crucial for
understanding how PLA materials perform under conditions of
increased velocity, potentially resulting in enhanced material
properties, reduced printing times, and broader applications for
PLA materials in 3D printing. Also, the nozzle temperature has
an impact on mechanical characteristics. Elevating the nozzle
temperature to 230°C maximized the tensile properties of PLA
parts showed maximized tensile property at 230°C. Additionally,
research by Yang et al. [10] and Heidari-Rarani et al. [11]
emphasized the importance of optimizing printing speed for
FDM 3D printing to improve the mechanical characteristics of
PLA samples. They concluded that optimizing printing speed is
essential for achieving better mechanical properties in FDM-
printed PLA parts. However, conflicting findings exist, as noted
in some works [12] [13], where it has been suggested that the
mechanical properties [18] of PLA materials decrease with
increased printing speed.  An experimental work by Rezaeian
and colleagues [14] examined printing speeds at various rates
and the mechanical and fracture performance of FDM-ABS
parts. Their optimal results were obtained when printing at 70
mm/s, exhibiting the highest elongation and fracture resistance
compared to specimens at different nozzle speeds. Summarizing
these works proves that increasing the temperature and
decreasing printing speed can be important in increasing product
strength in 3D printing. Still, the unwanted fact is that increasing
the temperature results in higher power consumption. If we
decrease the speed of printing for large-scale operations, it will
increase the cycle time of production, which is also not
acceptable for large-scale applications. In solution to this issue,
this work describes some experiments to determine if it is
possible to increase the temperature to the specific regions where
the product faces maximum stress while bearing load and if it is
possible to decrease the speed in that region so that the power
consumption of the 3D printing machines can be controlled.
Also, the production time is not hampered. Here, for identifying
the high-stress regions, finite element analysis has been
performed to guide and optimize the G-Codes for those high-
stress layers that print in high temperatures in high-stress regions
and keep the printing process slower. The effect of increasing the
nozzle temperature and decreasing the printing speed has been
verified by tensile testing using the MTS Tensile testing
machine, and the peak load, peak stress, and modulus have been
compared with the specimen from the constant temperature and
speed settings to prove if it can be a solution to the existing issue.

2. MATERIALS AND METHODS

For this experimental investigation, a rectangular specimen
of 100 mm in height, 40 mm in width, and 3 mm in width with a
strategically positioned 10 mm radius aperture was chosen to
primarily evaluate the effects of changing the temperature and
speed of 3D Printing.



FIGURE 1: PROPOSED FEA-GUIDED G-CODE ADJUSTMENT
PROCESS

Finite element analysis (FEA) was executed to identify regions
susceptible to high stress. At first, the design was divided into
more minor, manageable elements through meshing. Cubic
elements of 2 mm have been used to discretize the geometry for
this analysis. PLA material has been selected to understand how
the material behaves under various load conditions, while one
side of the rectangular is kept fixed, and a force of 2000 N
has been applied to the other side of the shape as a boundary
condition. Once the mesh is generated, boundary conditions and
the material properties are assigned, FEA solves the system of
equations derived from the equilibrium of forces and
compatibility of displacements. After the solution is obtained,
von Mises stress is calculated for each element in the mesh.



FIGURE 2: STRESS CALCULATION VIA FINITE ELEMENT
ANALYSIS ON THE SPECIMEN

Ordinarily, the slicer defaults on the printing temperature for
Ultimaker S3 machines to 200 degrees Celsius. While printing
the geometry in a 3D printer, the resolution was kept to the Fine


## Page 3


3
© 2024 by ASME
(0.1 mm) setting, and line infill and shell thickness of 4 mm by
200 mm were used. The specimens were printed with the default
temperature setting and then tested with the MTS tensile testing
machine. After that, for the modified samples, temperature
modification in the high-stress region areas changed the G-code
so that the printer stopped and increased the temperature by 10
degrees as the previous research states increase of printing
temperature improves the product strength [7] [10]. Then, the
layers were printed with the modified settings. The rest of the
parameters were kept the same to analyze the effect of
temperature increases.


FIGURE 3: MODIFIACATION OF G-CODE FOR HIGH-
STRESS REGION LAYERS

A A similar procedure was employed for printing on the
Flashforge Adventure 4 Lite printer to modify the G-Code
specifically for layers experiencing higher stress levels. In line
with this approach, the printing speed was reduced within the
high-stress regions. Subsequently, specimens printed at default
speed settings were compared with those printed using modified
speed settings in a tensile testing scenario to discern any
discrepancies. This approach draws upon previous research
findings [12] [13], which have consistently highlighted the
efficacy of temperature increases and speed decreases in
enhancing the strength of 3D printed specimens. Leveraging
insights gleaned from prior analyses conducted by researchers,
the G-Code was adjusted accordingly to align with established
optimization strategies.



FIGURE 4: (a) PRINTING IN VERTICAL DIRECTION (b)
PRINTING IN HORIZONTAL DIRECTION

For both cases, the specimens were printed with vertical and
horizontal directions [16] with the machine default settings of
20% infills with a line infill pattern. As we wanted not to affect
the printing quality by the infills, we printed the specimen with
100% infill [15].


FIGURE 5: (a) ULTIMAKER S3 (b) FLASHFORGE
ADVENTURE 4 LITE



## Page 4


4
© 2024 by ASME
Ultimaker S3 and Flashforge Adventure 4 lite were used for this
experiment to determine if the two different 3D printers show
consistency.


FIGURE 4: DATA OBTAINED FROM THE TENSILE
TESTING MACHINE

For each sample, a comprehensive evaluation of mechanical
properties was conducted through meticulous tensile testing
utilizing an MTS tensile tester, a well-established and
standardized procedure recognized for its reliability in assessing
material behavior under tension [17]. The testing procedure was
performed with the careful mounting of the specimens onto grips
capable of accommodating a width of 3mm. Subsequently, a
precisely controlled tensile load is applied to the specimen with
strain rate of 1mm/min until fracture occurs, allowing for the
systematic observation and recording of critical data points
throughout the test duration. This includes the meticulous
documentation of load-displacement and stress-strain curves,
facilitating a detailed analysis of the material's response to
varying stress levels. From this extensive dataset, mechanical
properties are extracted and recorded for each specimen,
encompassing key parameters such as peak load, peak stress,
Young's modulus, and strain at the break point. These recorded
properties serve as invaluable indicators of the material's
inherent strength and stiffness characteristics, offering profound
insights into the efficacy of temperature and speed optimization
strategies employed in high-stress regions of specimens derived
from 3D printers. Through this rigorous testing regimen, the
experiment aims to validate and quantify the tangible
improvements realized through meticulous adjustments in
printing parameters, thereby enhancing the overall mechanical
integrity and performance of the printed specimens.



FIGURE 6: TENSILE TESTING UTILIZING THE MTS
TENSILE TESTING MACHINE

3. RESULTS AND DISCUSSION

3.1 Effect of Increasing Temperature

The experimental
findings indicate a
significant
enhancement in the mechanical properties of printed specimens
when the printing temperature is increased in high-stress regions
[19]. For example, when the temperature was increased with
100% infill in the high-stress region, several vital parameters
exhibited notable improvements. The average peak load
experienced an enhancement of 8.98%, demonstrating increased
load-bearing capacity under these conditions [19]. Similarly,
peak stress significantly increased by 8.89%, indicating better
resistance to deformation and failure. The modulus, a measure of
material stiffness, experienced a notable rise of 3.06%,
suggesting improved structural integrity and rigidity [19].
Additionally, the strain at the break increased by 8%, indicating
enhanced ductility and deformation capacity before failure [19].
These improvements were particularly pronounced when
printing in the vertical direction. These findings align closely
with previous research [7] [10], reinforcing the validity and
significance of the observed enhancements resulting from
temperature adjustments in high-stress regions.


## Page 5


5
© 2024 by ASME


FIGURE 7: PEAK LOAD COMPARISON:
DEFAULT VS.
MODIFIED TEMP (ULTIMAKER S3)



FIGURE 8: PEAK STRESS COMPARISON: DEFAULT VS.
MODIFIED TEMP (ULTIMAKER S3)


FIGURE 9:
MODULUS
COMPARISON:
DEFAULT VS.
MODIFIED TEMP (ULTIMAKER S3


FIGURE 10: AVERAGE MODULUS COMPARISON: DEFAULT
VS. MODIFIED TEMP (ULTIMAKER S3)

However, for the 20% infill, the mechanical properties of the
printed specimen from the 3D printers degraded the mechanical
properties, which is visualized in Figure 9, and the outcome
matches the findings from previous research [16] [19] [20].



FIGURE 9: PEAK LOAD COMPARISON WITH 20% INFILL
(ULTIMAKER S3)

3.1 Effect of Decreasing Speed

Decreasing the printing speed with 100% infill in the high-stress
region resulted in noticeable improvement across various
mechanical parameters. The average peak load, peak stress,
modulus, and strain at the break experienced significant
enhancements, showing increases of 21.28%, 33.17%, and
21.77%, respectively. These findings corroborate earlier research
studies [12] [13] [14], further validating the efficacy of this
approach in enhancing 3D printing mechanical performance.
However, it's worth noting that the experiment revealed a
degradation in the average strain at break, indicating the need for
further investigation and analysis in future studies. Additionally,
when applying a 20% infill, the reduction in printing speed led


## Page 6


6
© 2024 by ASME
to a degradation of mechanical properties similar to the effects
observed with increased temperature.



FIGURE 11: PEAK STRESS COMPARISON: DEFAULT VS.
MODIFIED SPEED (ADVENTURE 4 LITE)


FIGURE 12: COMPARING AVERAGE PEAK STRESS: DEFAULT
VS. MODIFIED PRINT SPEED (ADVENTURE 4 LITE)

Interestingly, even though both our selected geometry and
specimens from the Ultimaker S3 were produced using the same
Fused Deposition Modeling (FDM) technology and adhered to
identical printing settings, a visible discrepancy in mechanical
properties was observed. The observed discrepancy in
mechanical properties between our selected geometry and
Ultimaker S3 specimens, despite sharing the same Fused
Deposition Modeling (FDM) technology and printing settings,
underscores the complexity inherent in additive manufacturing
processes. This observation prompts a comprehensive
investigation into the underlying factors contributing to these
variations, beyond mere G-code alterations. It suggests the
presence of nuanced variables, such as material composition,
printer calibration, and environmental conditions, which may
exert significant influence on the final product's mechanical
performance [21] [22]. This necessitates further research and
comparative analysis to unravel the intricate interplay of these
multifaceted factors. By gaining deeper insights into these
underlying mechanisms, we can refine optimization strategies
aimed at enhancing the consistency and reliability of additive
manufacturing processes. Such findings hold significant
implications for advancing the understanding and practice of
additive manufacturing in various industries.



FIGURE 13: PEAK STRESS COMPARISON: DEFAULT VS.
MODIFIED PRINT SPEED (ADVENTURE 4 LITE)


FIGURE 14: COMPARING AVERAGE PEAK STRESS: DEFAULT
VS. MODIFIED PRINT SPEED (ADVENTURE 4 LITE)

4. CONCLUSION

In conclusion, our preliminary study underscores the
profound impact of optimizing 3D printing parameters based on
geometrical finite elements of PLA materials. We observed
significant improvements in mechanical properties, which have
been tested using MTS Tensile testing, validating the positive
effect of the alteration of the G-code. Moreover, keeping the
printing temperature lower helps reduce power consumption,


## Page 7


7
© 2024 by ASME
and also the decreased printing speed for only specific stress-
sensitive regions improves production cycle time. The idea
generated from this experimental study can be used for more
complex structures to prove its practicality for more efficient
energy usage and optimized printing experience.

ACKNOWLEDGEMENTS

The authors gratefully acknowledge the National Science
Foundation awards #2110760, #2107140, and the Department of
Energy award #DENA0003987 for supporting this research
work.

REFERENCES

[1] Jandyal, Anketa, Ikshita Chaturvedi, Ishika Wazir, Ankush
Raina, and Mir Irfan Ul Haq. "3D printing–A review of
processes, materials and applications in industry 4.0."
Sustainable Operations and Computers 3 (2022): 33-42.
[2] Jandyal, Anketa, Ikshita Chaturvedi, Ishika Wazir, Ankush
Raina, and Mir Irfan Ul Haq. "3D printing–A review of
processes, materials and applications in industry 4.0."
Sustainable Operations and Computers 3 (2022): 33-42.
[3] Sehhat, M. Hossein, Ali Mahdianikhotbesara, and Farzad
Yadegari. "Impact of temperature and material variation on
mechanical properties of parts fabricated with fused deposition
modeling (FDM) additive manufacturing." The International
Journal of Advanced Manufacturing Technology 120, no. 7
(2022): 4791-4801.
[4] Gordelier, Tessa Jane, Philipp Rudolf Thies, Louis Turner,
and Lars Johanning. "Optimising the FDM additive
manufacturing process to achieve maximum tensile strength: a
state-of-the-art review." Rapid Prototyping Journal 25, no. 6
(2019): 953-971.
[5] Murugan, Ramu, R. N. Mitilesh, and Sarat Singamneni,
"Influence of process parameters on the mechanical behavior and
processing time of 3D printing," Int. J. Mod. Manuf. Technol,
vol. 1, pp. 21-27, 2019.
[6] Elhattab, Karim, Sarit B. Bhaduri, and Prabaha Sikder,
"Influence of fused deposition modeling nozzle temperature on
the rheology and mechanical properties of 3d printed β-
tricalcium phosphate (TCP)/polylactic acid (PLA) composite,"
Polymers, vol. 14, no. 6, p. 1222, 2022.
[7] Alsoufi, Mohammad S., and Abdulrhman E. Elsayed,
"Surface roughness quality and dimensional accuracy—a
comprehensive analysis of 100% infill printed parts fabricated
by a personal/desktop cost-effective FDM 3D printer," Materials
Sciences and Applications, vol. 9, no. 01, p. 11, 2018.
[8] Ansari, Anis A., and M. Kamil, "Effect of print speed and
extrusion temperature on properties of 3D printed PLA using
fused deposition modeling process," Materials Today:
Proceedings, vol. 45, pp. 5462-5468, 2021.
[9] Napolitano, Francesco, Ersilia Cozzolino, Ilaria Papa,
Antonello Astarita, and Antonino Squillace, "Experimental
integrated approach for mechanical characteristic optimization
of FDM-printed PLA in an energy-saving perspective.," The
International Journal of Advanced Manufacturing Technology,
vol. 121, no. 5, pp. 3551-3565, 2022.
[10] Yang, Yuan, Xilin Dai, Bo Yang, Peng Zou, Feng Gao, Jihao
Duan, and Changxu Wang, "Optimization of polylactic acid 3D
printing parameters based on support vector regression and
cuckoo search," Polymer Engineering & Science, vol. 63, no. 10,
pp. 3243-3253, 2023.
[11] Heidari-Rarani, Mohammad, Niloofar Ezati, P. Sadeghi, and
M. R. Badrossamay, "Optimization of FDM process parameters
for tensile properties of polylactic acid specimens using Taguchi
design of experiment method," Journal of Thermoplastic
Composite Materials, vol. 35, no. 12, pp. 2435-2452, 2022.
[12] Ł. Miazio, "Impact of print speed on the strength of samples
printed in FDM technology.," Agricultural Engineering, vol. 23,
2019.
[13] Khosravani, Mohammad Reza, Filippo Berto, Majid R.
Ayatollahi, and Tamara Reinicke. , "Characterization of 3D-
printed PLA parts with different raster orientations and printing
speeds.," Scientific Reports, vol. 12, no. 1, p. 1016, 2022.
[14] Rezaeian, Parham, Majid R. Ayatollahi, A. Nabavi-Kivi,
and Nima Razavi, "Effect of printing speed on tensile and
fracture behavior of ABS specimens produced by fused
deposition modeling.," Engineering Fracture Mechanics, vol.
266, p. 108393, 2022
[15] Tanveer, Md Qamar, Gautam Mishra, Siddharth Mishra, and
Rohan Sharma. "Effect of infill pattern and infill density on
mechanical behaviour of FDM 3D printed Parts-a current
review." Materials today: proceedings 62 (2022): 100-108.
[16] Farashi, Sajjad, and Fariborz Vafaee. "Effect of printing
parameters on the tensile strength of FDM 3D samples: a meta-
analysis focusing on layer thickness and sample orientation."
Progress in Additive Manufacturing (2022): 1-18.
 [17] Torrado, Angel R., and David A. Roberson. "Failure
analysis and anisotropy evaluation of 3D-printed tensile test
specimens of
different geometries and print
raster
patterns." Journal of Failure Analysis and Prevention 16 (2016):
154-16


## Page 8


8
© 2024 by ASME
[18] Al Khawaja, Huda, Haleimah Alabdouli, Hend Alqaydi, Aya
Mansour, Waleed Ahmed, and Hamad Al Jassmi. "Investigating
the mechanical properties of 3D printed components." In 2020
Advances in Science and Engineering Technology International
Conferences (ASET), pp. 1-7. IEEE, 2020.
[19] Rismalia, Mia, S. C. Hidajat, I. G. R. Permana, B.
Hadisujoto, Muslimin Muslimin, and Farid Triawan. "Infill
pattern and density effects on the tensile properties of 3D printed
PLA material." In Journal of Physics: Conference Series, vol.
1402, no. 4, p. 044041. IOP Publishing, 2019.
[20] Rismalia, Mia, S. C. Hidajat, I. G. R. Permana, B.
Hadisujoto, Muslimin Muslimin, and Farid Triawan. "Infill
pattern and density effects on the tensile properties of 3D printed
PLA material." In Journal of Physics: Conference Series, vol.
1402, no. 4, p. 044041. IOP Publishing, 2019.
[21] Moetazedian, Amirpasha, Andrew Gleadall, Xiaoxiao Han,
and Vadim V. Silberschmidt. "Effect of environment on
mechanical properties of 3D printed polylactide for biomedical
applications." Journal of the mechanical behavior of biomedical
materials 102 (2020): 103510.
[22] Ma, Lei, Qing Zhang, Zijian Jia, Chao Liu, Zhicong Deng,
and Yamei Zhang. "Effect of drying environment on mechanical
properties, internal RH and pore structure of 3D printed
concrete." Construction and Building Materials 315 (2022):
125731.

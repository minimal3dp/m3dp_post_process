# Influence of printing time reduction on dimensional accuracy of final build FDM parts by modifying the G-code program
**Author:** Dharavathu Naresh
**Subject:** International Journal on Interactive Design and Manufacturing (IJIDeM), https://doi.org/10.1007/s12008-024-01965-1

**Source:** `InfluenceofprintingtimereductionondimensionalaccuracyoffinalbuildFDMpartsbymodifyingtheGcodeprogram.pdf`
---

## Page 1

International Journal on Interactive Design and Manufacturing (IJIDeM)
https://doi.org/10.1007/s12008-024-01965-1
ORIGINAL ARTICLE
Inﬂuence of printing time reduction on dimensional accuracy of ﬁnal
build FDM parts by modifying the G-code program
Dharavathu Naresh1 · Alluri Sujatha Priyadarshini2 · Ramesh Raju3 · Vinothkumar Sivalingam4,5 · V. Revathi6 ·
A. Somaiah7 · Ashish Kumar8
Received: 31 October 2023 / Accepted: 21 June 2024
© The Author(s), under exclusive licence to Springer-Verlag France SAS, part of Springer Nature 2024
Abstract
In the material extrusion process, dimensional accuracy and printing time depend on the printing process parameters. Due
to consistent layer height, traditional material extrusion takes a long time to print at low-thick layers. The current research
proposes a novel way to print low-layer thickness at crucial dimensions and alter the RepRap ﬂavor G code to print the rest with
a higher-layer thickness. The current research has decreased printing time by 22.5% over the conventional material extrusion
process. This work also presents a novel approach for Z-direction dimensional accuracy. The slicing software determines the
total number of printing layers based on the material extrusion thickness and the model’s total height. When the total number
of layers results in decimals, the decision to print a decimal layer depends on the percentage of the decimal value in the layer
thickness. This study found that if the percentage of the decimal value is equal to or more than half of the layer height, slicing
software will accommodate a layer; in this case, the ﬁnal height of the part will be oversized. If it is less than half of the layer
height, slicing software won’t accommodate the layer; in this case, the height of the part will be undersized. Adopting this
method improves dimensional accuracy in the Z direction by editing the code for decimal value, and optimizes material and
energy consumption for oversized components. Similarly, the component’s linear dimensions are determined by layer width
and extrusion percentage. If the extrusion percentage increases, the linear dimensions of the component will also increase.
This approach can be used on all geometrical shapes and materials to print critical dimensions with a lower layer thickness
and the rest with a higher layer thickness. The printing process parameters, type of material, and geometry complexity do not
affect the method’s efﬁciency.
Keywords G code · Material extrusion process · Material extrusion thickness · RepRap · Time reduction · Dimensional
accuracy
B Ashish Kumar
ashishrahul79@gmail.com
Dharavathu Naresh
nareshdharavathu07@gmail.com
Alluri Sujatha Priyadarshini
sujathapriyadarshini.a@gmail.com
1
International Advanced Research Centre for Powder
Metallurgy and New Materials (ARCI), Autonomous
Research and Development Centre of Department of Science
and Technology (DST), Balapur, Hyderabad, India
2
Pragathi Engineering College, Kakinada, India
3
Department of Mechanical Engineering, SRM Institute of
Science and Technology, Tiruchirappalli Campus,
Tiruchirappalli, Tamil Nadu 621105, India
4
Key Laboratory of High-Efﬁciency and Clean Mechanical
Manufacture, National Demonstration Center for
1 Introduction
3D printing is an emerging technology in advanced manufac-
turing. In any manufacturing process, time constraints play
Experimental Mechanical Engineering Education, School of
Mechanical Engineering, Shandong University, Jinan 250061,
Shandong, China
5
Department of Mechanical Engineering, Saveetha School of
Engineering, SIMATS, Tamil Nadu, Chennai 602105, India
6
Department of Applied Sciences, New Horizon College of
Engineering, Bangalore, India
7
Department of Mechanical Engineering, Institute of
Aeronautical Engineering, Hyderabad, Telangana, India
8
School of Mechanical Engineering, Lovely Professional
University, Phagwara, India
123


## Page 2

International Journal on Interactive Design and Manufacturing (IJIDeM)
a major role. 3D printing is a one-time, digitally controlled
building process that involves setting printing parameters like
layer height, inﬁll, wall count, adhesion type, and so on. In
addition to slicing software, the printer can control a few
parameters in the printer settings while printing the model.
Optimizing printing parameters can optimize the printing
time, but under time constraints, this optimization directly
impacts the surface quality, bond strength between lay-
ers, dimensional accuracy, and mechanical properties [1–3].
Even though the process is faster and easier when compared
to conventional manufacturing, it still takes more time for
each print. Robin Lofﬂer et al. [4] developed a new type
of extruder geometry to improve dimensional accuracy and
reduce printing time. They developed a slot-shaped printing
nozzle to achieve variable layer widths for accurate compo-
nent printing. They achieved the ﬁne details of the component
by rotating the nozzle with respect to the printing direction.
However, the challenge lies in the slot dimensions, which
measure 1.32 × 0.4 mm, making it extremely difﬁcult to con-
trol the ﬂowability of material. The printing nozzle’s larger
opening signiﬁcantly reduces the inﬁll time, but it becomes
more challenging to achieve the inﬁll volume when the inﬁll
is less than 100%. Generating tool paths is challenging, as it
is only possible for a circular open nozzle. In this scenario,
calculating material ﬂow and controlling the ﬂow rate present
signiﬁcant challenges.
Coupek et al. [5] conducted a study on support structures
and inﬁll density in order to decrease the overall construc-
tion time. They achieved this by integrating an FDM print
head into a 7-axis CNC machine and developing a univer-
sal approach to designing the print head’s trajectory. They
reduced the printing time by completely removing support
structures using multi-directional slicing and tilting the build
plate to avoid overhangs. They also proposed an approach to
reduce material and printing time by removing the inﬁll and
replacing it with pre-manufactured thermoplastic material.
The work area’s accessibility limitations and the presence of
overhanging structures restricted the printing process to only
the outer surface. This was achieved by building the inﬁll pat-
tern using multi-axis FDM. Here, developing the trajectory
path will be more difﬁcult. Moving the print head with the
build and holding the pre-manufactured inﬁll is a big chal-
lenge, and printing the outer surface will be more difﬁcult.
Jiang et al. [6] elucidated a novel support generation tech-
nique in their study, which aims to optimize production time
by considering both internal and external supports. In order
to enhance production efﬁciency, they have adjusted the noz-
zle route and orientation of the model on the bed. They built a
prototype with several orientations to investigate the printer’s
highest achievable angle of printing. However, they failed to
take into account the surface roughness or dimensional errors
[7], both of which have a direct impact on the mechanical
characteristics. Mueller et al. [8], in their study, proposed
wire printing instead of layer-wise solid printing. Using this
method, they were able to reduce the printing time by 10
times when compared to conventional layer-wise printing.
In this method, they used wire-printing software to gener-
ate the model and G-code. In the subsequent iteration, they
attempted to print the component’s wall. Here, only print-
ing time was concentrated. This printing method may result
in the loss of the component’s strength and surface quality.
Installing additional equipment on the print head is necessary
to print the outer layer in intricate areas. Le et al. [9] improved
the print conﬁguration to reduce the printing duration while
minimizing any negative impact on the mechanical proper-
ties. They discovered that the size of the nozzle, the amount of
inﬁll, and the thickness of the outer wall signiﬁcantly impact
the duration of the printing process in material extrusion.
However, their approach results in a decrease in mechanical
characteristics [9]. Perry et al. [10] suggested a redesigned
print head nozzle as a means to decrease the duration of the
printing process. The nozzle’s outlet attaches a copper strip
to raise the printing temperature, which in turn increases the
ﬂow rate. As a result of the higher ﬂow rate, printing time
decreased by 48% compared to the normal nozzle. An inher-
ent limitation of this technology is its inability to accurately
reproduce key dimensions as a result of material overﬂow.
The closed non-uniform rational B-spline (NURBS) route
planning method, which is described in references [11–14],
is an alternative method that might cut down on the time
needed for construction. This strategy relies on analytical
mathematical models.
Abas et al. [15] conducted parametric research and opti-
mization of process parameters to analyze dimensional
aberrations in the FDM printing process. They conducted
research to analyze the impact of process factors on dimen-
sional variations, including measurements such as length,
breadth, and height. They determined that the density of inﬁll
had the greatest impact on variations in length and breadth.
For height, extrusion thickness is the most inﬂuential param-
eter. They studied the component with a 55 × 10 × 10 mm
sample, and they cut it into 0.1, 0.2, and 0.3 mm. While slic-
ing the component with different extrusion thicknesses, they
did not consider the total number of layers, which results in
decimals. They failed to account for the decimal layer thick-
ness, which led to a height deviation. Based on their results, it
is clear that the height deviation due to layer height and print
orientation is very high when compared to other parameters
[15]. Burhan et al. [16] studied the dimensional accuracy of
the inner and outer corners of FDM-printed samples with dif-
ferent adhesion types, different angles, different lengths, and
differentmaterials.Theyconcludedthatadhesiontypesaffect
dimensional accuracy as sample length increases, but dimen-
sional deviations decrease comparatively. In their study, they
found that the brim adhesion type provides better dimen-
sional control than other adhesion types. However, they did
123


## Page 3

International Journal on Interactive Design and Manufacturing (IJIDeM)
not consider the layer height and its effect on the total height
of the sample, and they also failed to mention the exact rea-
sons for the deviation in height.
Kim et al. [17] conducted research on improving dimen-
sional stability in the FDM process, taking into account
different extrusion temperatures and inﬁll volume effects on
different materials. They concluded that length and width
linear dimensions need to be considered while improving
dimensional accuracy, and height deviations are steady in the
material extrusion process. Their experimental results clearly
demonstrate a steady deviation in the height direction, which
they attribute to decimal layer heights and other unconsid-
ered printing parameters. Mansaram et al. [18] investigated
the dimensional accuracy of ABS M30 material and came to
the conclusion that the rapid cooling of semi-molten ﬁlament
is what causes dimensional accuracy. They sliced the model
into 0.127, 0.178, and 0.254 mm, which may cause a deci-
mal value in calculating the total number of layers. Therefore,
0.127 may result in minimum volumetric deviations. While
preparing the experiments’ design, they did not consider the
model height. Zharylkassyn et al. [19] reviewed 31 articles
on process parameters that impact dimensional accuracy. Out
of 31 articles, 19 conclude that layer height is the most inﬂu-
ential parameter in improving dimensional accuracy in the Z
direction. None of the articles shed any light on the value of
the left-over decimal layer thickness.
Various sectors employ rapid prototyping, yet it often
takes days to print the model due to its lengthy process.
The aforementioned citations proposed various methods to
reduce the printing time, including process parameter mod-
iﬁcation [15–17, 19] and hybrid printing methods [5]. But
they did not consider the component’s complexity and crit-
ical dimensions, where dimensional accuracy plays a major
role. Functional prototypes demand dimensional accuracy
and better strength properties. Maintaining these properties
requires maintaining as low process parameters as possible,
which signiﬁcantly increases the printing time. The earlier
studies demonstrated that layer height, inﬁll density, and
print orientations all affect dimensional deviation in the Z
direction. But none of the authors discussed the calculation
of the total number of layers. They studied different layer
heights that affected the height dimensions but did not elab-
orately discuss formation layers. To reduce the printing time
for a complex model without affecting its complex features,
the present work proposes a method to reduce the printing
time without effecting the critical dimensions of the model.
The fusion of different layer heights in the RepRap ﬂavor G
code is necessary to balance the printing time and dimen-
sional accuracy, while also preserving dimensional stability.
Also, the slicing software’s overall height values increase or
decrease when the total height of the component is not in the
multiples of layer height. Here, a novel method is proposed
to correct this overall height by modifying G-codes directly
to improve the dimensions in the Z direction and optimize
material and energy consumption for oversized components.
By manually adjusting the value while printing, this article
investigated the material extrusion percentage effect on the
x and y linear dimensions.
2 Materials and methodology
2.1 Modelling and material selection
In the earlier citations, authors developed and proposed mul-
tiple methods to reduce the printing time [4–6, 8–10] and
improve the dimensional accuracy of the model [16, 18,
19]. The development of FDM slicing software is ongoing,
with updates aimed at simplifying the printing process and
enhancing control. Figure 1a shows a 3D solid model of col-
let, which has different features and complex geometry to
print. Figure 1b shows the collet’s dimensional details, with a
total height of 53.5mmandamaximumdiameter of 18.5mm.
The collet’s critical dimensions involve cutting portions of
three jaws, and with a gap of 1 mm between each jaw, captur-
ing the details becomes challenging when printing at a higher
layer height value. We printed the model with a ﬁne layer
height to capture the jaw geometry, a process that took 1 h
and 56 min to complete. The next iteration involved building
the model with a 0.2 mm layer height, resulting in a print-
ing time of 59 min. But when printing with a 0.2 mm layer
height, the jaw curve where the object surface is going to
contact is not captured perfectly. In order to capture the jaws
and reduce printing time, it is not necessary to print the collet
portionafterthejawswithaﬁnelayerheight(LH).Thisisdue
to the absence of forces acting on the collet, and since the end
of the collet serves to open the jaws for inserting the drill bit
or grinding wheel, precision and accuracy at this end are not
essential. The objective of reducing print time compromises
the dimensional accuracy of the part. Locally, PLA is the
most readily accessible material, exhibiting diverse qualities
and printing circumstances. We use the Ultimaker PLA ﬁla-
ment for printing the collete because its production at a lower
temperature leads to a reduction in energy consumption com-
pared to other materials. PLA provides superior control over
material extrusion while operating at higher printing speeds.
Since we implemented this procedure before the actual print-
ing process, we can use it on any kind of material.
2.2 Methodology
The printing process’s duration is primarily determined by
the layer height, layer breadth, printing speed, and compo-
nent inﬁll [4–6]. To decrease the printing time, it is necessary
to adjust either the layer height, printing speed, or inﬁll
percentage correspondingly [15–17, 19]. However, altering
123


## Page 4

International Journal on Interactive Design and Manufacturing (IJIDeM)
Fig. 1 a 3D CAD model b Dimensional details of the model
Fig. 2 Process ﬂow methodology
CAD Modeling
Design Evaluation
and stl file
conversion
Slicing
Generating gcode
for different layer
heights
Merging gcode for
final print
printing
Time reduction
calculation for each
print
these parameters has an impact on the physical charac-
teristics, precise measurements, and outside appearance of
the printed component. To enhance printing efﬁciency and
ensure precise dimensions, the conventional printing code is
adjusted, and a novel code is created by combining several
layer height codes. Figure 2 illustrates the process approach.
The Massachusetts Institute of Technology invented G-
codes in the 1960s, and under the name RS274D, they
developed a ﬁnal revision in 1980. All the FDM printers
use G-codes and M-codes to control the nozzle path move-
ment. G-codes in the FDM printing process come in various
ﬂavors, as illustrated in Table 1. From this, we can observe
that all the ﬂavors utilize either relative or absolute extrusion
modes to extrude the material through a nozzle. The G-code
ﬁle indicates the relative extrusion mode with M83, and the
absolute extrusion mode with M82. In the relative extrusion
mode, the last layer’s ending position serves as the reference
for printing a new layer, while in the absolute extrusion mode,
the origin serves as the reference, indicating the starting point
of the extrusion value for all layers. In relative extrusion, the
extrusion values for each layer are reset to zero, whereas in
Table 1 G-code ﬂavor and extrusion mode
G code ﬂavor
Extrusion mode
RepRap
Relative extrusion
Makerbot
Absolute extrusion
Bits from bytes
Absolute extrusion
Mach3
Absolute extrusion
Repetier
Absolute extrusion
absolute extrusion mode, the extrusion value increases con-
tinuously with respect to the origin point. The combination of
layer heights depends on the minimum and maximum layer
heights achieved by the nozzle. You must modify the layer
number while developing the G code to avoid print failure or
damage to both the print head and the component. Since we
introduced the method after the slicing process, the geome-
try’s complexity remains unaffected. To maintain the feature
on the model, print the intricate geometry at a lower thick-
ness. This methodology enables the maintenance of a lower
123


## Page 5

International Journal on Interactive Design and Manufacturing (IJIDeM)
layer thickness for intricate geometries and a higher layer
height for the rest of the model.
3 Experimental setup
In any 3D printing technology, the ﬁrst step is the CAD
modeling of an object. A collet was designed in the SOLID-
WORKS 2017 student version; the dimensions of the collet
are shown in Fig. 1b. After converting the CAD model into an
STL ﬁle, Ultimaker CURA 4.0.0 (RepRap ﬂavor) with rela-
tive extrusion mode was used for slicing. The slicing software
imports a.stl ﬁle to calibrate the number of layers and print-
ing time. After setting all the parameters, the slicing software
calibrates the printing time, weight of the component, total
number of layers, and required length of material in meters.
The model was sliced with different layer heights to study
the time required to build the component with the conven-
tional layer printing method. A Creality Ender 3D printer
was used to build the model, which has a build volume of
235 × 235 × 250 mm with a heated bed. Ender 3D supports
different G-code ﬂavors (Table 1). The model was printed
with a 0.4 mm nozzle using Ultimaker PLA material with
a printing temperature of 220 °C and a bed temperature of
65 °C as suggested by the Ultimaker.
Using Ultimaker CURA software, G codes for both 0.1
and 0.2 mm layer heights are generated. The standard 0.4 mm
nozzle can achieve maximum and minimum layer heights of
80% and 25%, respectively, compared to the nozzles sug-
gested by Ultimaker and Prusa. From the earlier citations,
printers give better results at 0.1 and 0.2 mm layer heights.
The CURA slicing software generates a readable G code ﬁle.
Table 1 lists the different types of G Code ﬂavors that CURA
can generate. To develop the alternate layer printing method,
manually modify the G code using Notepad software accord-
ing to the critical dimensions. Figure 1b illustrates that after
18.4 mm from the holder end, the collet’s diameter is con-
stant. The geometry is complex, and the required dimensions
are critical up to the height of 18.4 mm; the rest of the length
serves only as a guide for insertion, without any need for
part quality. Therefore, we used a layer height of 0.1 mm
for the initial 18.4 mm and then increased it to a 0.2 mm
layer height. We edited the G-code in the Notepad app on
the Windows 10 OS. Notepad opens both G-codes (0.1 and
0.2 mm); in the 0.1 mm layer height program, up to 18.4 mm,
it maintains the same G-codes and clears the remaining G-
codes until the ﬁnal layer. In the subsequent step, once the
total number of layers in Z 18.4 mm reaches 184, we will
increment Z to 0.2 mm in the next layer, resulting in Z 18.6,
where we replace the 0.1 mm layers with the 0.2 mm layer
height program. The same procedure can be applied to dif-
ferent heights in a single component, and the same method
can be applied to each layer, and every layer can be printed
with a different material extrusion thickness.
While editing the G code, do not change the initial lines
because it consists of machine preparation commands like
bed heating, extruder heating, and homing of all axes. The
build position should be the same for all layer height pro-
grams; otherwise, layers will be mismatched, causing print
failure, and the print head will move away from the printing
position. After merging the G-code of different layer heights,
we need to change the “layer count” number. The layer num-
bers should be sequential. If the layer numbers are not in
order, the extruder will abruptly travel downward and col-
lide with the object. Check the type of extrusion mode before
modifying the G-code, as you can only copy and paste the
G-codes directly in the relative extrusion mode. In absolute
extrusion mode, we need to calculate the extrusion value and
modify it accordingly for each layer. Do not disturb the end-
ing lines of G-code, as the end G-code remains the same for
all G-code ﬁles, and any change in the end G-code causes
damage to the build component.
Non-critical cross sections were printed at higher layer
heights comparatively and at the same speed as lower layer
height layers. The printing time variation in combined layer
height is primarily due to modiﬁed layers. As the modiﬁed
layer count is decreasing, the printing time is close to the
constant layer height print time. The dimensional accuracy
of the non-critical part is lower when compared to a smaller
layer height.
4 Results
Table 2 provides the printing time for various layer heights.
CURA software does not have the capability to estimate the
printing time for a modiﬁed G-code program. Hence, col-
let was printed for different layer heights, and G-code was
merged to calculate the reduction in printing time. As seen
in Fig. 3a, b, c, the production time for a 0.1 mm extrusion
thickness is 1 h, 44 min, 24 s (Fig. 3a, d), and for a 0.2 mm
extrusion thickness, 53 min, 30 s (Fig. 3b, e). The print time
for a merged G-code is 1 h, 21 min, and 21 s (Fig. 3c, f). When
compared to 0.1 mm layer height, merging G-code reduces
printing time by 22.11%. This percentage varies according
to the number of layers sharing the higher layer height value
and LH value of merging G-code (Fig. 4).
In this case, the bottom of the collet is almost solid where
ﬁne details are needed, so the extrusion thickness is kept at
0.1 mm. After that, the collet is hollow with a thickness of
1.25 mm, so the material thickness is kept at 0.2 mm. Critical
dimensions can vary depending on the component. When
critical dimensions were required, the G-code adjusted to a
smaller layer height to maintain precision and reduce printing
time without compromising the component’s dimensions.
123


## Page 6

International Journal on Interactive Design and Manufacturing (IJIDeM)
Table 2 Calibration of printing
time and no of layers for different
layer heights in Ultimkaer
CURA slicing software
Sample name
Layer height (LH)
Initial layer height (ILH)
No of layers
Printing time
Collet_1
0.1 mm
0.1 mm
535
104 min
Collet_2
0.2 mm
0.2 mm
268
53 min
Fig. 3 Printing time for a 0.1 mm layer height b 0.2 mm layer height c 0.1 and 0.2 mm layer height merged component d 0.1 mm layer height print
e 0.2 mm layer height print f 0.1- and 0.2-mm merge layer height print
Fig. 4 The relation between the different merged LH with constant
0.1 mm LH, printing time and time reduction percentage
4.1 Effect of different layer heights on final height
of printed component
The number of slicing layers depends on the layer height and
the initial layer height value in Ultimaker CURA. The total
height of the collet case is 53.5 mm (Fig. 1b). The collet was
sliced with LH = 0.1 mm and ILH = 0.1 mm. At this time,
the total number of printing layers is 535. After slicing the
collet with LH = 0.2 mm and ILH = 0.2 mm, we were able
to create 267 possible layers, with a collet height of 53.4 mm
and a 0.1 mm gap. At this time, CURA cannot adapt back to
0.1 mm LH to print the exact height. Therefore, CURA will
directly increment to 0.2 mm, resulting in a total height of
53.6 mm. The last G-code of the 0.2 mm layer height program
replaces the ﬁnal Z value of the collet in Fig. 5a, b with the
0.1 mm layer height program. In this scenario, we can achieve
the perfect height of the collet; if not, we will increment the
ﬁnal height of the collet by 0.1 mm. Slicing the model at a
height of 0.3 mm results in an achieved height of 53.4 mm,
a decrease of 0.1 mm from the required height of 53.5 mm.
The CURA slicing phenomenon is that it generates minimal
height errors. If any height remains after slicing equal parts,
and it is less than 50% of the layer height, it will not print the
123


## Page 7

International Journal on Interactive Design and Manufacturing (IJIDeM)
next layer. If the left height is half of the layer height or more
than half of the LH, it will print the next layer. The problem
can be solved by replacing or adding the G-code.
Figure 6a shows the ﬁnal build height versus layer height;
it is developed from the G-code program shown in Fig. 5,
which is directly affecting material consumption and energy
consumption. Figure 6b shows the relation between layer
height and material consumption. Figure 6 suggests that
variations in layer height also lead to variations in mate-
rial consumption. The consumption of material may increase
or decrease depending on the components ﬁnal height. The
component’s ﬁnal height is directly proportional to material
consumption, and vice versa. Similarly, energy consumption
also varies based on the difference between the actual height
and the ﬁnal build height.
A digital vernier caliper was used to measure the height
and critical dimensions of the collet. Table 3 shows the mea-
suredheightatdifferentpositions,anditisworthnoticingthat
samples 1 and 3 have the same Z value in the G code program.
However, slicing sample 2 in the Ultimaker CURA results in
an oversized ﬁnal build, surpassing the actual model’s height.
Table 3 reveals that the deviation between samples 1 and 3 is
very low, which means the merged model gives better results
at a lower printing time. Table 4 also displays the diameter
measurementofthemodiﬁedsection.Wemeasurethecollet’s
diameter at various locations to compare it with the constant
layer printing model. Sample 1 and sample 3 give closer
results when compared to sample 2. This is because when
printing with a 0.1 mm layer height, the extrusion value is
lower than when printing with a 0.2 mm layer height. During
the actual printing process, the material compresses between
the previous layer and nozzle, causing it to expand in the
width direction, ultimately enlarging the dimensions. When
printing with a smaller layer thickness, it is possible to cap-
ture the critical features of the model. It is sufﬁcient to hold
the grinding wheels in the collet’s nose section.
4.2 Effect of face width or layer width
on the dimensions
Face width, which is called layer width in the CURA slicer,
determines the layer width during printing. Layer width is
mainly determined by the gap between the nozzle and the
bed or previous layer, as well as the extrusion value and ﬂow
rate. During printing, the layer width will be increased due
to earlier factors. The extrusion value will vary depending on
LH and layer width. When the layer height shifts from 0.1
to 0.2 mm LH due to an increase in LH and extrusion value,
it causes an overﬂow of material and increases the overall
dimensions of the ﬁnal printed component shown in Fig. 7.
Figure 8 shows the relationship between the standard
CURA slicer value and the measured layer width value of
different prints with different layer widths. When compared
to the CURA value, the measured value is higher and steadily
increasing. Lowering the ﬂow rate to between 85 and 95%
will control this, reduce overﬂow, and improve print quality.
Printing time is also dependent on layer width. As the
layer width decreases, the number of beads in the horizon-
tal direction increases. If the layer width value decreases,
the printing quality will also decrease, but the dimensional
accuracy will improve. In order to assess the impact of layer
width on printing, it is necessary to print the outer shell and
compare the discrepancy between the program value and the
real value. Figure 8b illustrates the deviation between the
assigned layer width and the actual achieved value at 100%
ﬂow rate. At a 100% ﬂow rate, as the LH value increases,
the layer width value also increases. However, if the LH
value is lower than the LW value, there is a greater likeli-
hood of uneven surfaces, potentially leading to print failure.
Increasing the material ﬂow rate at a lower LH is necessary
to increase the LW value. Figure 9 shows that when the ﬂow
rate increased to 150%, the layer width value at lower LH
increased.
Layer width is directly proportional to the ﬂow rate. As the
ﬂow rate increases, the amount of material coming out of the
nozzle increases. Due to the constant gap between the nozzle
and previous layer, layer width expands more due to the over-
ﬂow of material, which directly affects the outer perimeter
thickness. In this case, with a 0.1 LH at a 100 percent ﬂow
rate, the layer width value is close to the assigned value in
slicing software and consumes less power and material when
compared to a 0.1 mm LH with a 150 percent ﬂow rate, which
implies the same for a 0.2 mm LH.
5 Discussions
The FDM printing process is a digitally controlled manufac-
turing process whose starting and ending depend on digital
values to control the ﬁnal output. Any manufacturing pro-
cess must maintain the dimensional accuracy of the ﬁnal
component. In the FDM printing process, the dimensional
accuracy of the ﬁnal component depends on various process
parameters, including layer height [15, 18, 19], inﬁll percent-
age [17], print speed, wall thickness [9], orientation, layer
width [9], and so forth. Zisopol [20] has studied the effect
of printing process parameters on a dog bone sample. They
investigated the effect of inﬁll percentage and layer thick-
ness on the component’s ﬁnal dimensions. Their main goal
is to ﬁnd the optimal process parameters to minimize the
error parentage by using the Taguchi method to optimize and
Minitab software to analyze the results. They concluded that
the overall dimensions of the printed part are signiﬁcantly
larger than those of the actual part. As the layer thickness
increases, it gives better dimensional accuracy. Adjusting the
layer thickness improves the dimension in the Y direction,
123


## Page 8

International Journal on Interactive Design and Manufacturing (IJIDeM)
Fig. 5 Final height of printing of a 0.1 mm layer height b 0.2 mm layer height c 0.3 mm layer height
Fig. 6 Shows a ﬁnal build height versus different layer heights b ﬁnal build height versus material consumption
Table 3 Height of the collet after
printing
Sample no.
Layer height (mm)
H1
H2
H3
H4
Avg. height ± SD
1
0.1
53.66
53.62
53.62
53.64
53 ± 0.63
2
0.2
53.79
53.79
53.74
53.78
53 ± 0.77
3
0.1 and 0.2 merge
53.56
53.67
53.59
53.62
53 ± 0.61
whereas modifying the inﬁll percentage can have a signiﬁ-
cant effect in the Z direction [20].
Abas et al. [15] did a study investigating the inﬂuence of
print parameters on the ﬁnal size. The factors examined were
layer height, wall count, ﬁlling volume, ﬁlling pattern angle,
nozzle movement speed, heat input of the material heater and
bed, and position of the model on the bed. They modiﬁed
settings using a speciﬁc screen layout called DSD (Deﬁnite
Scree Design). According to their study, they conclude that
the percentage of inﬁll has the most signiﬁcant effect on the
length and width, while the thickness of each layer has a sig-
niﬁcant inﬂuence on the inclination and variation in height.
The thickness of each layer signiﬁcantly affects the level of
unevennessonthesurface,wearresistance[21,22],andprint-
ing time [23]. Elkaseer [24] conducted a study to look at the
impact of ﬁve process parameters inﬁll%, extrusion thick-
ness, print head speed, extruder temperature, and surface
inclination angle on precision in dimensions. The author’s
assertion is that the precision of the printed item is mostly
determined by the thickness of each layer and the velocity
at which the printing process is executed. The length and
Table 4 Measured diameter at
critical section of the collet
Sample no.
Layer height (mm)
D1
D2
D3
D4
Avg. diameter ± SD
1
0.1
20.24
20.18
20.19
20.18
20 ± 0.19
2
0.2
20.26
20.2
20.28
20.19
20 ± 0.23
3
0.1 and 0.2 merge
20.14
20.16
20.21
20.17
20 ± 0.17
123


## Page 9

International Journal on Interactive Design and Manufacturing (IJIDeM)
Fig. 7 shows the printing of different layer height with different layer
widths a 0.1 mm LH with 0.1 LW b 0.1 mm LH with 0.2 LW c 0.1 mm
LH with 0.3 LW d 0.1 mm LH with 0.4 LW a 0.2 mm LH with 0.1 LW
b 0.2 mm LH with 0.2 LW c 0.2 mm LH with 0.3 LW d 0.2 mm LH
with 0.4 LW
Fig. 8 Shows the deviation of software assigned layer width and actual layer width of a 0.1 mm LH with different LW b 0.2 mm LH with different
LW at 100% ﬂow rate
power consumption of printing mostly depend on the mate-
rial extrusion height of each layer and the printing speed. The
extrusion thickness and the angle of inclination both affect
the surface roughness.
In the study of the inﬂuence of FDM process parame-
ters on the ﬁnal accuracy of the build component modelled
using feed-forward artiﬁcial neural networks [25] and hybrid
techniques using Mat Lab [26], it was found that layer height,
inﬁll density, and inclination angle play a major role in decid-
ing the ﬁnal accuracy of the printed component. The surface
roughness value increases as the inclination value decreases
[7]. The surface deviation is also dependent on the type of
material used for printing [27]. Different polymer materi-
als have different properties, which makes them suitable for
speciﬁc manufacturing parameters and speciﬁc applications
[28–35]. The design and modelling of alternate layer print-
ing have been discussed but have not explained the physical
characteristics of the ﬁnal printed part [36]. All the citations
mentioned above primarily rely on the extrusion thickness
to determine dimensionality, while orientation, inﬁll density,
and printing speed play a crucial role in reducing printing
time and energy consumption. However, the phenomenon of
the conversion between height and the number of printing
layers remains unaddressed. In this conversion, dividing the
total height by the component’s height yields decimals for
123


## Page 10

International Journal on Interactive Design and Manufacturing (IJIDeM)
Fig. 9 Shows the deviation of
software assigned layer width
and actual layer width of 0.1 mm
LH with different LW at 150%
ﬂow rate
the total number of layers, leading to either undersized or
oversized ﬁnal prints depending on the decimal value. This
research primarily addressed dimensional deviations and the
optimization of printing time after slicing and prior to the
actual printing process.
6 Conclusions
Building a component with a ﬁne layer thickness to main-
tain dimensional stability requires more time in the current
conventional layer-wise FDM process. Here, we propose
an adaptive layer thickness by editing and merging the G-
codes of different layer heights, which reduces the printing
time while maintaining dimensional accuracy. We designed
and printed this collet using PLA material for better control
over dimensions. Using this method resulted in a 22.11%
reduction in printing time for the collet, while maintaining a
dimensional tolerance comparable to that of a 0.1 mm layer
height. This method allows for printing a model with more
complex geometries without compromising the ﬁnal build’s
geometrical features. But while merging the G codes of dif-
ferent layer heights, pay attention to the height of the critical
section and replace that height G code with a lower layer
height. Also, the component’s position and orientation on
the bed should be the same for all layer heights. If the posi-
tion or orientation changes for different layer heights after
merging the code layers, mismatches result in the model’s
failure.
The dimensional accuracy of material-extruded parts
depends on a wide range of process parameters. In the mate-
rial extrusion process, there is a situation where dimensional
deviation is present in the process ﬁle before starting the
printing process in the Z direction. The proposed method
corrects dimensional deviations and prints a deviation-free
model. Slicing the model with different layer heights results
in a decimal value of the total number of layers. Based on the
percentage of decimal value in layer height, the printed part
is oversized or undersized. If the model is undersized, it is
necessary to accommodate the decimal left-over layer. If the
part is oversized, adjust the ﬁnal layer height to the actual
height to optimize material and energy consumption. The
model’s linear dimensions depend on the outer wall thick-
ness. The LW and ﬂow rate have an impact on the outer wall
thickness. For good print quality and strength, the LW value
has to be kept higher than the LH value, which aids in bet-
ter material ﬂow and bonding strength. Maintaining high LH
and low LW while printing material causes improper layer
bonding and porous surfaces. If the ﬂow rate value increases,
the layer width also increases, which affects length and width
dimensions. If the ﬂow rate increases due to the constant gap
between the nozzle and the previous layer, contact pressure
increases. For this reason, the outer wall width increases, and
the length and width of the model also increase.
Adaptive layer thickness may be used by any FDM printer,
independent of the intricacy of the geometry or the material
being used. The study concentrated on implementing adap-
tive layer thickness only in essential dimensions to examine
its inﬂuence on both printing duration and dimensional pre-
cision. Additional investigations into different layer heights
are necessary to examine the shift from crucial to non-critical
characteristics of the model. The impact of this transition
on the strength of the component has to be emphasized.
The adaptive layer thickness approach may be used for each
layer to create alternative thickness layers, hence enhancing
the mechanical characteristics. Adaptive layer thickness may
be implemented across all layers to modify the thickness of
every other layer, resulting in a substantial reduction in the
123


## Page 11

International Journal on Interactive Design and Manufacturing (IJIDeM)
gaps between the layers. However, this method takes a long
time to determine the precise number of layers that need
modiﬁcation, replace them with a new G code, and adjust all
layer count numbers accordingly. Adopting a direct software
program to modify the G code program will save a lot of time
in printing the component.
Data availability No Supplementary Files are intended to include
research data sets, research instruments, source texts or other materials.
Declarations
Conﬂict of interest No conﬂict of interest among all authors.
References
1. Raju, R., Manikandan, N., Palanisamy, D., Arulkirubakaran, D.,
Binoj, J.S., Thejasree, P., Ahilan, C.: A review of challenges and
opportunities in additive manufacturing. In: Palani, I.A., Sathiya,
P., Palanisamy, D. (eds.) Recent Advances in Materials and Mod-
ern Manufacturing Lecture Notes in Mechanical Engineering.
Springer, Singapore (2022)
2. Raju, R., Varma, M.M.M.K., Baghel, P.K.: Optimization of pro-
cess parameters for 3D printing process using Taguchi based grey
approach. Mater. Today Proc. 68, 1515–1520 (2022). https://doi.
org/10.1016/j.matpr.2022.07.163
3. Varma, M.M.M.K., Baghel, P.K., Raju, R.: Additive manufac-
turing of thermosetting resins in-situ carbon ﬁbers: a review. In:
Palani, I.A., Sathiya, P., Palanisamy, D. (eds.) Recent Advances in
Materials and Modern Manufacturing Lecture Notes in Mechanical
Engineering. Springer, Singapore (2022)
4. Löfﬂer, R., Koch, M..: Innovative extruder concept for fast and
efﬁcient additive manufacturing. IFAC-PapersOnLine. 52(10),
242–247 (2019)
5. Coupek, D., Friedrich, J., Battran, D., Riedel, O.: Reduction of
support structures and building time by optimized path planning
algorithms in multi-axis additive manufacturing. Proced. CIRP 67,
221–226 (2018). https://doi.org/10.1016/j.procir.2017.12.203
6. Jiang, J., Xun, Xu., Stringer, J.: Optimization of process planning
for reducing material waste in extrusion based additive manufactur-
ing. Robot Computer-Integr. Manuf. 59, 317–325 (2019). https://
doi.org/10.1016/j.rcim.2019.05.007
7. Enemuoh, E.U., Duginski, St., Feyen, C., Menta, V.G.: Effect of
processparametersonenergyconsumption,physical,andmechani-
cal properties of fused deposition modeling. Polymers 13(15), 2406
(2021)
8. Mueller, S., Im, S., Gurevich1, S., Teibrich1, A., Pﬁsterer, L.,
Guimbretière, F., Baudisch, P.: WirePrint: 3D printed previews for
fast prototyping. In: UIST 2014—Proceedings of the 27th Annual
ACM Symposium on User Interface Software and Technology,
pp. 273–280. (2014)
9. Le, L., Rabsatt, M.A., Eisazadeh, H., Torabizadeh, M.: Reducing
print time while minimizing loss in mechanical properties in con-
sumer FDM parts. Int. J. Lightweight Mater. Manuf. 5(2), 197–212
(2022). https://doi.org/10.1016/j.ijlmm.2022.01.003
10. Parry, G.R., Felton, H.J., Ballantyne, R., Su, S., Hicks, B.: Reduc-
ing prototype fabrication time through enhanced material extrusion
process capability. Proc. Des. Soc. 3, 3025–3034 (2023). https://
doi.org/10.1017/pds.2023.303
11. Thirugnanasambantham, K.G., Francis, A., Ramesh, R., Aravind,
M., Reddy, M.K.: Investigation of erosion mechanisms on IN-718
based turbine blades under water jet conditions. Int. J. Interact. Des.
Manuf. (2022). https://doi.org/10.1007/s12008-022-00910-4
12. Francis, A., Thirugnanasambantham, K.G., Ramesh, R., et al.:
High-temperature erosion and its mechanisms of IN-738 superal-
loy under hot air jet conditions. Int. J. Interact. Des. Manuf. (2022).
https://doi.org/10.1007/s12008-022-01013-w
13. Jin, G., Li, W., Tsai, C., Wang, L.: Adaptive tool-path generation
of rapid prototyping for complex product models. J. Manuf. Syst.
30, 154–164 (2011)
14. Jin, G., Li, W., Gao, L.: An adaptive process planning approach of
rapid prototyping and manufacturing. Robot. Comput. Manuf. 29,
23–38 (2013)
15. Abas, M., Habib, T., Noor, S., Salah, B., Zimon, D.: Parametric
investigation and optimization to study the effect of process param-
eters on the dimensional deviation of fused deposition modeling of
3D printed parts. Polymers 14(17), 3667 (2022). https://doi.org/10.
3390/polym14173667
16. Ekinci, B., Ehrmann, A.: Inﬂuence of printing parameters on the
dimensional accuracy of concave/convex objects in FDM print-
ing. Eng. Proc. 31, 40 (2022). https://doi.org/10.3390/ASEC2022-
13811
17. Kim, J., Ko, J.: A parameter study to improve dimensional accuracy
of FDM-type 3D printer based on various ﬁlaments. J. Adv. Mar.
Eng. Technol. 45(2), 60–69 (2021). https://doi.org/10.5916/jamet.
2021.45.2.60
18. Mansaram, M.V., Chatterjee, S., DinbandhuSahu, A.K., Abhishek,
K., Mahapatra, S.S.: Analysis of dimensional accuracy of ABS
M30 built parts using FDM process. In: Parwani, A.K., Ramkumar,
P., Abhishek, K., Yadav, S.K. (eds.) Recent Advances in Mechan-
ical Infrastructure Lecture Notes in Intelligent Transportation and
Infrastructure. Springer, Singapore (2021)
19. Zharylkassyn, B., Perveen, A., Talamona, D.: Effect of process
parameters and materials on the dimensional accuracy of FDM
parts. Mater. Today Proc. 44, 1307–1311 (2021). https://doi.org/
10.1016/j.matpr.2020.11.332
20. Zisopol, D.G., Portoaca, A.I., Tanase, M.: Dimensional Accuracy
of 3D Printed Dog-bone Tensile Samples: a case Study. Eng. Tech-
nol. Appl. Sci. Res. 13(4), 11400–11405 (2023)
21. Fernández, F.M., Sánchez, M.J.M.: Analysis of the effect of the sur-
face inclination angle on the roughness of polymeric parts obtained
with fused ﬁlament fabrication technology. Polymers 15(3), 585
(2023)
22. Portoac˘a, A.I., Ripeanu, R.G., Dinit,˘a, A., T˘anase, M.: Optimization
of 3D printing parameters for enhanced surface quality and wear
resistance. Polymers 15(16), 3419 (2023)
23. Yang, J., Liu, Y.: Energy, time and material consumption modelling
for fused deposition modelling process. Proced. CIRP. 90, 510–515
(2020)
24. Elkaseer, A., Schneider, S., Scholz, S.G.: Experiment-based pro-
cess modeling and optimization for high-quality and resource-
efﬁcient FFF 3D printing. Appl. Sci. 10(8), 2899 (2020)
25. Mohamed, O.A., Masood, S.H., Bhowmik, J.L.: Modeling, analy-
sis, and optimization of dimensional accuracy of FDM-fabricated
parts using deﬁnitive screening design and deep learning feedfor-
ward artiﬁcial neural network. Adv. Manuf. 9, 115–129 (2021)
26. Deswal, S., Narang, R., Chhabra, D.: Modeling and parametric
optimization of FDM 3D printing process using hybrid techniques
for enhancing dimensional preciseness. Int. J. Interact. Des. Manuf.
13, 1197–1214 (2019)
27. Bahnini, I., et al.: Accuracy investigation of fused deposition mod-
elling (FDM) processed ABS and ULTRAT parts. Int. J. Manuf.
Mater. Mech. Eng. 12(1), 1–19 (2022)
28. Gupta, T.K., Budarapu, P.R., Chappidi, S.R., SudhirSastry, Y.B.,
Paggi, M., Bordas, S.P.: Advances in carbon based nanomaterials
for bio-medical applications. Curr. Med. Chem. 26(38), 6851–6877
(2019). https://doi.org/10.2174/0929867326666181126113605
123


## Page 12

International Journal on Interactive Design and Manufacturing (IJIDeM)
29. Jayanthi, N., Babu, B.V., Rao, N.S.: Survey on clinical prediction
models for diabetes prediction. J Big Data 4, 26 (2017). https://doi.
org/10.1186/s40537-017-0082-7
30. Kalyani, G., Janakiramaiah, B., Karuna, A., et al.: Diabetic
retinopathy detection and classiﬁcation using capsule networks.
Complex Intell. Syst. 9, 2651–2664 (2023). https://doi.org/10.
1007/s40747-021-00318-9
31. Budarapu, P.R., Yb, S.S., Javvaji, B., et al.: Vibration analysis
of multi-walled carbon nanotubes embedded in elastic medium.
Front. Struct. Civ. Eng. 8, 151–159 (2014). https://doi.org/10.1007/
s11709-014-0247-9
32. Raji, A., Nesakumar, J.I.E.T., Mani, S., Perumal, S., Rajangam, V.,
Thirunavukkarasu, S., Lee, Y.R.: Biowaste-originated heteroatom-
doped porous carbonaceous material for electrochemical energy
storage application. J. Ind. Eng. Chem. 98, 308–317 (2021). https://
doi.org/10.1016/j.jiec.2021.03.037
33. SudhirSastry, Y.B., Budarapu, P.R., Madhavi, N., Krishna, Y.:
Buckling analysis of thin wall stiffened composite panels. Com-
put. Mater. Sci. 96, 459–471 (2015). https://doi.org/10.1016/j.
commatsci.2014.06.007
34. SudhirSastry, Y.B., Krishna, Y., Budarapu, P.R.: Parametric studies
on buckling of thin walled channel beams. Comput. Mater. Sci. 96,
416–424 (2015). https://doi.org/10.1016/j.commatsci.2014.07.058
35. Singh, B., Kumar, I., Saxena, K.K., Mohammed, K.A., Ijaz Khan,
M., Moussa, S.B., Abdullaev, S.S.: A future prospects and current
scenario of aluminium metal matrix composites characteristics.
Alex. Eng. J. 76, 1–17 (2023). https://doi.org/10.1016/j.aej.2023.
06.028
36. Naresh, D., Raju, R., Parveen, S.: Design and development of alter-
nate layer printing method to reduce the porosity in FDM printing
process. Int. J. Interact. Des. Manuf. (2023). https://doi.org/10.
1007/s12008-023-01624-x
Publisher’s Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional afﬁliations.
Springer Nature or its licensor (e.g. a society or other partner) holds
exclusive rights to this article under a publishing agreement with the
author(s) or other rightsholder(s); author self-archiving of the accepted
manuscript version of this article is solely governed by the terms of such
publishing agreement and applicable law.
123

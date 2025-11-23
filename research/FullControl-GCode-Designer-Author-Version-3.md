# Optimisation of the surface porosity of 3D printed tissue engineering scaffolds for cell viability and surgical suturing
**Author:** Andy Gleadall

**Source:** `FullControl-GCode-Designer-Author-Version-3.pdf`
---

## Page 1

 
 
 
 
1 
 
 
 
FullControl GCode Designer: open-source software for unconstrained design 
in additive manufacturing 
Andrew Gleadall 
 
Wolfson School of Mechanical and Manufacturing Engineering, Loughborough University, Loughborough, 
Leicestershire, LE11 3TU, UK 
E-mail: a.gleadall@lboro.ac.uk      Tel: +44 (0) 1509 227 578 
 
AUTHOR VERSION 
PUBLISHER VERSION AVAILABLE AT HTTPS://DOI.ORG/10.1016/J.ADDMA.2021.102109 
Graphical abstract 
 
Abstract 
A new concept is presented for the design of additive manufacturing procedures, which is implemented in 
open-source software called FullControl GCode Designer. In this new design approach, the user defines 
every segment of the print-path along with all printing parameters, which may be related to geometric and 
non-geometric factors, at all points along the print-path. Machine control code (GCode) is directly generated 
by the software, without the need for any programming skills and without using computer-aided design (CAD), 
STL-files or slicing software. Excel is used as the front end for the software, which is written in Visual Basic. 
Case studies are used to demonstrate the broad range of structures that can be designed using the software, 
Conformal lattice cells
Conformal 
lattice 
cells
Designed 
terminal 
lattice 
cells
Directly design GCode 
(machine code)
• No CAD
• No STL files
• No slicer software
Mathematically define print-paths
Systematically control all printing parameters
Produce previously inconceivable geometric structures
Achieve unparalleled printing quality with precise control of the process
Draw strings < 1/10th 
nozzle diameter
Vertically printed stent


## Page 2

 
 
 
 
2 
 
 
including: precisely controlled specimens for printer calibration, parametric specimens for hardware 
characterisation utilising hundreds of unique parameter combinations, novel mathematically defined lattice 
structures, and previously inconceivable 3D geometries that are impossible for traditional slicing software to 
achieve. The FullControl design approach enables unconstrained freedom to create nonplanar 3D print-paths 
and break free from traditional restrictions of layerwise print-path planning. It also allows nozzle movements 
to be carefully designed - both during extrusion and while travelling between disconnected extrusion volumes 
- to overcome inherent limitations of the printing process or to improve capabilities for challenging materials. 
An industrial case study shows how explicit print-path design improved printer reliability, production time, and 
print quality for a production run of over 1,000 parts. FullControl GCode Designer offers a general framework 
for unconstrained design and is not limited to a particular type of structure or hardware; transferability to 
lasers and other manufacturing processes is discussed. Parametric design files use a few bytes or kilobytes 
of data to describe all details that are sent to the printer, which greatly improves shareability by eliminating 
any risk of errors being introduced during STL file conversion or due to different users having inconsistent 
slicer settings. Adjustable parameters allow GCode for revised designs to be produced instantly, instead of 
the laborious traditional routine using multiple software packages and file conversions. The FullControl design 
concept offers new opportunities for creative and high-precision use of additive manufacturing systems. It 
facilitates design for additive manufacturing (DfAM) at the smallest possible scale based on the fundamental 
nature of the process (i.e. assembly of individual extrusions). The software and source code are provided as 
supplementary data and ongoing updates to improve functionality and the user interface will be available at 
www.fullcontrolgcode.com. 
Keywords 
DfAM; Calibration; Toolpath; Manufacturing plan; Slicer software. 
1. Introduction 
In the last twenty years, material extrusion additive manufacturing (MEAM) has grown from a prototyping 
technology to one that produces intricate structures such as tissue engineering scaffolds [1–3], electronic 
components [4–6] and spatially designed fibre-reinforced components [7,8]. MEAM also has the ability to use 
materials that are difficult to process with other manufacturing technologies such as cell-laden hydrogels 
[3,9,10] and ceramics [11–13]. These materials and applications are generally associated with a shift in the 
use of MEAM technology towards higher value applications, where fidelity and defects are critical, as opposed 
to prototyping. 
This shift is also evident from the development of new MEAM systems in recent years; for example, to allow 
continuous carbon fibre reinforcement (e.g. Markforged X7 and Anisoprint ProM IS 500) and metal printing 
(e.g. Desktop Metal Studio System; Markforged Metal X). For more intricate structures, more challenging 
materials and higher value applications, problems associated with the print-path, which is typically generated 
using 3D printing slicing software, are of more critical importance.  
A recent review paper highlighted that “suitable methodologies have yet to be established to fully enable and 
exploit the true potential of [functionally graded additive manufacturing]” and identified a need for new 
approaches for print-path generation [14]. The limitations of slicing programs, and constraints they put on the 
user, have led to custom print-path scripts being developed for several research studies [15–17]. The need 
for new design software has also been identified industrially, as demonstrated by the following extract from 
an article by Sarat Babu, founder of the additive manufacturing company Betatype:  


## Page 3

 
 
 
 
3 
 
 
“One of the big challenges [for additive manufacturing design] is that software really needs to be 
informed by the entire process from design to production. On the design side, we need tools that help 
us to explore the design space, unconstrained” [18]  
In contrast to design approaches that provide design freedom by excluding manufacturing considerations, 
this study presents a generic framework for users to explore the design space for structures that can only be 
achieved by coupling the designed geometry with the manufacturing procedure. This is important for parts in 
which geometric features are of a similar size to the process resolution or when the geometry is directly 
affected by process parameters.  
Some relevant software has been developed to allow precise control for specific fields and applications, 
including: layerwise scaffold design for bioprinters [19], printing in well plates for bioprinters [20], graded 
scaffolds [21], fibre placement for carbon fibre reinforced printers [22–24], continuous extrusion for ceramics 
[11], controlled discontinuous extrusion for ceramics [13] and integration of multiple processes [25]. 
Additionally, scripts to translate CAD sketches or vector graphics into print-paths have been developed [26,27] 
as well as scripts for post-processing GCode generated by slicers [28]. However, the approach presented 
here is the first generic framework (i.e. it is not limited to a particular type of print-path or print procedure) 
developed for the unconstrained design of print-paths and associated printing parameters. Importantly, it 
allows the design of non-geometric GCode, to control manufacturing aspects beyond the geometric print-
path. The software is described conceptually and practically in the next two sections. Case studies in Section 
4 demonstrate its unique capabilities to achieve parts that would be difficult or impossible to achieve using 
other methods. 
2. FullControl GCode Designer: concept description 
The typical approach to generate GCode is a multi-step process (Figure 1A) involving CAD, STL file 
conversion and slicing software, which slices the model into layers and identifies a print-path for each layer, 
resulting in GCode (an example line of GCode shown in Figure 1B). Each step involves limitations and 
introduces errors [29].  
In the FullControl design approach, a practical framework has been developed which allows the print-path to 
be explicitly defined (Figure 1A) along with all parameters for each individual segment of the print-path, 
including: 
• 
Direction 
• 
Print speed 
• 
Extrusion rate (controlling extrudate height/width) or set as a non-extruding ‘travel’ movement 
• 
Material choice (or print head/tool number) 
• 
Other relevant parameters (e.g. acceleration/jerk, nozzle temperature, bed temperature, fan speed) 
The user defines each step of the manufacturing plan in a sequential manner. This is similar to features being 
created and modified in a CAD feature tree. In contrast to CAD, the design information provided by the user 
fully defines the whole manufacturing procedure. The user designs a sequence of 3D lines, including all data 
in the bullet points above, with the potential to also include non-geometric GCode text strings at any point in 
the sequence. The practical implementation of this approach, described in Section 3, overcomes the 
complexity of defining potentially millions of X-Y-Z coordinates through functionality similar to linear and polar 
arrays in CAD packages or through mathematical definition (i.e. curve equations).  
 


## Page 4

 
 
 
 
4 
 
 
 
Figure 1 The FullControl design approach and example parts. A) Flow chart comparing the traditional approach using 
3D printing slicing software and the FullControl approach, in which the geometric print-path and all non-geometric 
printing instructions are explicitly designed. B) Example line of GCode for one print-path segment. C) Example 
adjustment to the print-path (moving the nozzle outside of the structure) [30]. D) Example print-path with multiple 
materials printed at different heights above the print platform in a designed non-sequential manner [3]. E) An identical 
print-path was used to print several different graded meshes, by designing a variable extrusion width [31]. F) A single-
filament-wide mesh wall printed by combining vertical extrusion (away from the print platform) with horizontal extrusion 
(parallel to the print platform). All parts of the figure, even when linked to publications, were created from original media. 
Scale bars = 5 mm unless otherwise indicated. 
A tissue engineering scaffold structure from recent research [30] is used as an example to introduce the 
FullControl approach and potential benefits (Figure 1C). The typical approach to manufacture lattice scaffolds 
is to create a cuboid CAD file and select slicing software parameters to achieve a porous grid print-path. A 
commonly seen flaw in such structures is that uncontrolled extrusion blocks pores at the edges (Figure 1C). 
This can be caused by multiple factors, including: (i) acceleration and deceleration at the boundary of the 
structure, which allows more time for extrusion, (ii) the printhead moving along the boundary and therefore 
‘double printing’ some segments of the grid, leading to wider or offset extrusion, and (iii) extruded material 
being dragged laterally by the nozzle after direction changes. When the toolpath was designed with the 
FullControl design approach, a minor adjustment overcame the issue of blocked pores by considering 
process limitations: the print-path was designed to deposit the undesired excess material away from critical 
CAD model
STL file
Model sliced
into layers
print-path 
(for each 
layer)
GCode
Manufacture
Design full 
print 
procedure
Part 
requirements 
and design
Traditional approach
Geometric errors 
introduced
Geometric errors 
introduced
Geometric and process 
errors introduced
Specific process limitations considered at microscale (e.g. print-path direction changes)
Errors designed out, compensated or minimised
Generic process 
limitations considered
Manufacturing 
errors
Manufacturing 
errors
Feedback directly implemented
with full control
Feedback indirectly implemented
through limited parameters
A
Blocked pores
Excess polymer outside 
scaffold instead of inside pores
Conventional print-path
print-path with 100 µm adjustment 
(extra step outside scaffold)
C
G1     X10 Y10 Z0.5      F1000    E0.5
TO THIS POSITION
MOVE
AT THIS SPEED ( MM . MIN-1 )
EXTRUDING THIS MUCH 
MATERIAL ( MM3 )
Example GCode command
-
G1 X10 Y10 Z0.5 F1000 E0.5
B
D
E
F
Hydrogel
Polymer
1 mm


## Page 5

 
 
 
 
5 
 
 
regions. A small extension of the printed line that directly crosses the structure was designed (Figure 1C), 
which meant excess deposition occurred on the external surface (non-critical geometry) rather than inside 
pores (critical geometry). This simple adjustment was not possible using conventional 3D printing software, 
and too cumbersome to implement in bioprinting software. It is important to optimise processes to minimise 
the source of errors; for example, by using ‘linear advance’ algorithms to achieve consistent extrusion at 
corners or instantaneously stop extrusion to prevent ‘double printing’. But in some cases, such optimisation 
may be challenging (e.g. specific firmware; Bowden printers; flexible materials). Therefore, process 
optimisation and process-informed design should be combined in a complementary manner. 
In addition to overcoming process limitations, explicit print-path design provides opportunities to break free 
from the traditional approach of printing layers sequentially, as shown in Figure 1D. Several layers of polymer 
were printed before printing hydrogel at a lower height within a recess, to (i) allow the less viscous hydrogel 
to be contained within the polycaprolactone scaffold, and (ii) to ensure the hydrogel did not flow onto the top 
surface of the polymer, which would have interfered with interlayer bonding. 
The FullControl design approach also enables freedom beyond geometric print-path design. Extrusion rate 
and speed were continuously varied in a recent study [31] to achieve five different graded lattice geometries 
for an identical print-path (Figure 1E). In the FullControl design approach, it is also possible to parametrically 
vary retraction, temperature, acceleration and any other parameter that can be controlled with GCode. The 
GCode is generated in the same format as that produced by slicers and it is possible including advanced 
firmware algorithms and associated settings for compatible printers (e.g. by inserting an “M900 K0.18” 
command to adjust ‘linear advance’ settings).  
2.1. Key advantages  
The distinguishing capability of FullControl GCode Designer, and its underlying design approach, is 
unconstrained freedom for users to design every aspect of the printing procedure. It empowers users to 
design structures in a completely new way and enables a wide range of technical additive manufacturing 
operations that are challenging or impossible for slicing software, as shown by case studies in Section 4. It 
allows intricate consideration of process limitations and for the control of auxiliary equipment. New software 
(described in Section 3) is required for the approach to be practically achievable: manual editing in a text-
based GCode editor would be too complicated and time consuming for all but the simplest of structures. One-
off GCode-generation scripts, CNC machining software, and software for converting CAD geometry into 
GCode are all focused on specific types of geometry or manufacturing procedures, and do not allow for 
generic design of wide-ranging additive manufacturing procedures.  
Many benefits of the FullControl design approach originate from it instilling a completely different way of 
thinking about design and from it changing the overall workflow for GCode creation: 
• 
A new way of thinking for design 
o X, Y and Z coordinates, as well as extrusion volume, speed and other settings are 
simultaneously considered for each segment of the print-path. This facilitates unconventional 
print-paths and print settings; for example, in nonplanar print-path design, extrusion rate can 
be designed to vary with layer height. 
o Non-extruding travel movement is fully designed. Therefore, associated defects can be 
eliminated or minimised, including the position of stringing, undesired deposition, nozzle 
collisions with lips at part edges, top-surface scoring from fast-travel nozzle movement, and 
shear deformation of structures as the nozzle moves away from them. 


## Page 6

 
 
 
 
6 
 
 
o Custom GCode strings are a natural part of the design process since they are defined at the 
same time as the print-path. Therefore, any aspect of the process that is controllable with 
GCode can be implemented in the design. For example, pauses can be designed to allow 
stabilisation and focus of a microscope tool. 
o Mathematical definition of print-paths is possible in combination with non-mathematical 
geometry, which allows complicated print-paths to be simply and parametrically defined.  
o Feature-based design of GCode means each print-path segment or GCode instruction can be 
modified after initial creation. This allows for intricate control of specific points in a 
manufacturing procedure and enables parametric calibration procedures to be designed.  
o Simplicity of the print-path is naturally encouraged to minimise design effort. Although this 
limits part-shape complexity (discussed in the next section), simple print-paths reduce the 
scope for unanticipated errors. Each unnecessary step in a printing procedure, such as 
retraction or fast travel movement, introduces additional risk of failure (e.g. material feed 
issues or part detachment from the print platform). Therefore, designing simple continuous 
print-paths with smooth nozzle movement and no retraction improves printing reliability. 
• 
Benefits of the new workflow and software 
o No programming skills are required to generate the GCode. 
o Parametric feature-based design means file-size efficiency is high and GCode can be 
parametrically adjusted without reproducing a CAD model, STL file and slicing procedure. 
o The full manufacturing plan is designed from start to finish, and it can be directly translated 
between printers without the risk of inconsistencies due to different users’ slicer setups. 
o No data transfer errors are introduced due to the elimination of conventional conversion 
processes from CAD to STL to sliced layers to print-paths. 
2.2. Key limitations 
One limitation is that a reasonably high level of process expertise is required to design a print-path and set 
all print parameters. The user must be aware of factors that are often set automatically in slicing software, 
such as cooling fan speed, priming the nozzle before printing, and understanding the challenges involved in 
stopping extrusion and travelling (without extrusion). However, with appropriate guidance from an expert, 
even novice users can achieve high-quality results quickly. For example, the mesh structure in Figure 1F was 
technically designed and manufactured by a project student (see Acknowledgements) within two weeks of 
first using a 3D printer. This sort of structure (a porous single-filament-wide wall) had never been produced 
before due to the lack of software accommodating the FullControl design approach, but may have broad 
potential applications, including filters, biomedical meshes, vascular models and fluid flow devices. It 
demonstrates that this limitation (i.e. the need for process expertise) can be negated if an expert guides the 
user to only vary parameters that are relevant to their application, for example by providing a pre-created 
design file. Ways to reduce requirements for process expertise are being investigated, including the creation 
of design templates and integration of the design approach into existing slicing software.  
A second limitation is that complicated non-systematic print-paths are technically challenging for human 
design. Many typical components would be difficult to design using the presented method due to discrete 
changes in geometry requiring different print-paths in different locations. The design effort may still be justified 
if print reliability or quality is critical. The risk of human error must also be considered when the designer is 
given more control. A key strength of slicing software is the ability to undertake millions of computations 
(identifying print-path coordinates) that would be unfeasible for a human. For typical components to be 
designed using the presented approach in an accessible manner, some of the automation aspects of slicing 


## Page 7

 
 
 
 
7 
 
 
software would need to be incorporated into the print-path design process. The distinction between well-
suited and poorly suited geometry is not obvious, but in general, the FullControl approach is most suited to 
structures where coordinates can be identified systematically or mathematically.  
A final consideration is that some hardware systems use a proprietary machine control code format, as 
opposed to a GCode text file, or use web-based software that cannot be loaded with custom-written GCode. 
These systems are currently unsuitable for FullControl GCode Designer without direct collaboration with the 
hardware developer. For systems that require an unusual format of GCode, a simple revision to the GCode 
formatting algorithm would be required.  
3. FullControl GCode Designer: practical implementation 
Akin to how CAD packages provide a framework for the generation of 3D models, FullControl GCode 
Designer provides a framework for the generation of print-paths. Additionally, whereas CAD offers the user 
the capability to assign details such as material or tolerance requirements to each part of the model, 
FullControl offers the user the capability to assign printing details such as print speed and print direction to 
each part of the printing procedure.  
The practical implementation presented here for the FullControl design approach allows the user to 
sequentially describe every segment of the print-path by defining ‘features’ in an Excel spreadsheet, line by 
line, including details about how the printer should operate as it traverses each individual segment. 
FullControl interprets the list of features in the sequence in which they were defined by the user, similar to a 
feature tree in CAD: the GCode described for the first feature is generated before the next feature is evaluated, 
which may generate new GCode, or adjust or replicate GCode that was generated by earlier features.  
As with CAD, the user defines ‘features’ using a range of feature-types, which are shown in Figure 2 and 
described in this section. The most fundamental feature-type is to define a ‘print-path segment’ (Section 3.1). 
A second fundamental feature-type is to define a ‘custom GCode string’ (Section 3.2). Additional feature-
types (Section 3.3) improve usability - for example, to allow print-path segments to be repeated in a linear or 
polar array. The actual software implementation of FullControl GCode Designer is described in Section 3.4, 
including an example design workflow. Availability of the software is described in Section 3.5.  
3.1. Fundamental feature-type 1: print-path segment 
For each print-path segment (i.e. G0 or G1 command in GCode), the user defines: 
• 
Coordinates of the start of the segment (mm) 
o X, Y, Z values - directly equivalent to the coordinate system used by the printer and GCode 
o Alternatively, polar coordinates may be used (automatically converted to Cartesian in GCode) 
• 
Coordinates of the end of the segment (mm) 
• 
Information about the amount of extrusion during the print-head movement for this segment 
o Option 1: define the nominal width and height of the filament (mm) 
o Option 2: explicitly define the magnitude of ‘E’ in the GCode - typically identifying the length of 
feedstock-filament to feed into the printer for this print-path segment (mm) 
o Option 3: select ‘travel’ motion, in which no extrusion occurs, and speed is typically fast 
• 
Speed of the print head whilst printing the segment (mm.min-1) 
• 
Print-head ID (for multi-material or multi-tool printers) 


## Page 8

 
 
 
 
8 
 
 
Additional parameters for specific systems could be incorporated in revised versions of FullControl (by 
modifying the open-source code), including pressure for pneumatic syringe systems, or equivalent aspects 
for other extrusion system designs and alternative manufacturing tools. 
3.2. Fundamental feature-type 2: custom GCode string 
As opposed to creating a line of GCode that instructs the printer to move the print head, the ‘custom GCode 
string’ feature-type allows the user to give non-geometric instructions to the printer by inserting a GCode 
string during the printing process. This is useful for aspects such as: 
• 
Retraction 
• 
Temperature (nozzle, print platform, chamber) 
• 
Acceleration and jerk 
• 
Fan speeds 
• 
Homing axes 
• 
Pausing the print for inspection or insertion of prefabricated components 
• 
Outputting information to the display screen 
• 
Adding comment lines to GCode to improve human legibility 
• 
Controlling auxiliary equipment such as cameras or ultraviolet curing lights 
To allow for parametric variation, the custom GCode string can be defined as a concatenation of multiple 
strings and numbers, as opposed to a single text string. This enables the numeric values to be adjusted each 
time the line of GCode is repeated - as recently used to incrementally increase acceleration in a single test 
print, allowing the identification of which acceleration values caused greatest fluctuations in extrusion due to 
resonant vibration (often called ‘ringing’) [31]. 
 
Figure 2 Map of the different feature-types that are provided in FullControl GCode Designer to design a print-path and/or 
associated non-geometric instructions. Examples indicate which parameters must be defined by the user for five feature-
types. Features are created sequentially and evaluated by the software in a similar manner to a CAD feature tree. 
Example
Example
Example
Example
Example
Print-path 
segment
Multiple print-
path segments
Custom 
GCode string
Replication
Parametric 
variation
Circle/arc
Polygon
Mathematical 
curve
Cartesian or 
polar repeat
Reflect
Reproduce 
and 
recalculate
Repeat rule
Postprocessing
Cartesian 
coordinates
Polar  
coordinates
Required parameters:
• Start position (X,Y,Z)
• End position (X,Y,Z)
• Nominal width of extrusion
• Nominal height of extrusion
• Print speed
• Other details depending on system
Required parameters:
• Arc centre (X,Y,Z)
• Start point (polar angle and radius)
• Arc angle
• Printing direction (clockwise/anti-CW)
• Number of segments to divide arc into
• Nominal width of extrusion
• Nominal height of extrusion
• Print speed
• Other details depending on system
Required parameters:
• ID numbers of features to reflect
• Reflection line start position (X,Y,Z)
• Reflection line end position (X,Y,Z)
Required parameters:
• ID numbers of features to modify
• Type of modification 
• (e.g. displacement field)
• Details about modification
• (e.g. X,Y,Z equations for 
displacement field)
Types of features
Required parameters:
• Text string
• E.g. “G4 P10000”
(Pause for 10 sec)


## Page 9

 
 
 
 
9 
 
 
3.3. Additional feature-types for practical design 
Additional feature-types allow the user to design complicated structures without needing to manually define 
the coordinates of every print-path segment, which would be unfeasible for structures with thousands of 
segments. Instead, the user describes the desired print-path in a manner that allows FullControl to identify 
the coordinates. It is important to state that FullControl does not make any decisions: all aspects are fully 
defined by the user and FullControl is simply undertaking the associated numerical calculations. Full details 
are given here for the circle/arc feature-type as an example (also discussed later in relation to Figure 3B), 
whilst other feature-types are briefly described (detailed information for all feature-types is included in the 
software). Three main categories of the additional feature-types (besides those in Sections 3.1 and 3.2) are: 
• 
Multi-segment geometry 
o Circle/arc - for an arc in an X-Y plane, the user describes the arc geometry and all necessary 
information for FullControl to automatically determine the individual print-path segments (as 
opposed to manually defining them), including: 
▪ 
X-Y-Z values of the arc-centre 
▪ 
Polar angle and radius of the start point 
▪ 
Arc angle (360° = circle) 
▪ 
Direction of printing (clockwise or anti-clockwise) 
▪ 
Number of segments (the arc is printed as a series of straight segments) 
▪ 
Information about extrusion amount, speed and print-head ID (as required for manual 
definition of a print-path segment in Section 3.1, unless inherited from overall settings)  
o Polygon – the user defines polygon size, shape, orientation and order/direction to print the 
sides. 
o Mathematical curve - user defines X/Y/Z or polar equations for nozzle movement, which allows 
printing of sinusoidal waves, spirals, or any other mathematical curve. Speed and extrusion 
rate may also be varied according to a mathematic equation. 
• 
Replication of existing features 
o Cartesian and polar repeats - the user identifies which previously defined features should be 
repeated and gives geometric details for the repetition. A critical distinction from CAD is that, 
in addition to replicating print-path segments, replication feature-types also replicate non-
geometric GCode (e.g. retraction). This is important because if a single layer is designed and 
then repeated multiple times using a cartesian array feature, it is essential that all GCode 
instructions are repeated, not just the segment coordinates. This highlights a key distinction 
between FullControl GCode Designer and scripts that translate CAD drawings to GCode. 
o Reflection - to create mirror images of previously defined features, for print-paths with 
reflective symmetry. 
o Reproduction and recalculation of mathematical equations - for equations that are functions 
of the current nozzle coordinates (e.g. its current position above the print bed), it is necessary 
to recalculate the associated print-path segments each time the equation feature is repeated. 
• 
Parametric variation rules 
o ‘Repeat rule’ - this rule allows aspects of the print-path or parameters to be varied in a 
systematic manner. For features that have been replicated multiple times (e.g. replicating an 
identical print-path for multiple layers), the user can describe how the print-path or parameters 
vary for a specific replicate-range or to incrementally vary with each repetition. As an example, 
a single-filament-thick micro-tensile-testing specimen was recently developed, in which dog-


## Page 10

 
 
 
 
10 
 
 
bone geometry was achieved by incrementally varying extrusion width for each printed layer 
(see discussion related to Figure 4A for more details).  
o ‘Postprocessing’ - this feature-type also allows user-selected previously defined features to 
be modified. It is similar to the ‘Repeat rule’ feature-type but can be applied to all features as 
opposed to only those that are created during a replication feature. In many cases, the same 
design can be described using either a ‘Repeat rule’ or a ‘Postprocessing’ feature, but the 
distinction may be advantageous for more complicated designs. 
The above feature-types are demonstrated in the next section and in case studies. 
3.4. Software overview and design workflow 
To embed the sequential nature of GCode into the design process, features are defined in the order in which 
they are ultimately written in the GCode file. Each new feature (and the necessary parameters for its definition) 
is entered by the user in a new line in the user interface in FullControl GCode Designer.  Microsoft Excel was 
chosen as the user interface due to its ability to facilitate parametric and mathematical definitions and its 
widespread availability and use. Since the FullControl design approach is based around explicit definition of 
numerical values, Excel is naturally well suited to it and enhances design capabilities in a way that typical 
user-input forms would constrain. The FullControl framework’s program code is written in Visual Basic 
(approximately 2,500 lines of code). Once the user has defined all the features in their design, the GCode is 
generated and can be previewed in the user’s preferred software (e.g. Repetier Host [32]).  
An auxetic lattice is used to exemplify several feature-types of FullControl and demonstrate the design 
workflow, which involves the following steps: 
1. Conceptually design the part geometry 
• 
Typically, hand-drawn sketches - see leftmost schematic in Figure 3A 
2. Design the overall print-path sequence 
• 
Typically, hand-drawn schematics on gridline paper - see central layer-by-layer schematics in 
Figure 3A 
3. Identify geometric information necessary to fully define the print-path 
• 
Typically, annotations on the print-path schematic, such as arc-centre coordinates in absolute 
or relative terms - see rightmost schematic in Figure 3A. Similar to how engineering drawings 
contain all necessary information to allow a part to be manufactured in a workshop, these 
annotated print-path schematics contain all necessary information to allow the part to be 
created in FullControl. For mathematical feature definitions, graphing calculators are useful to 
develop equations [33]. 
4. Design the print-path in FullControl - see Figure 3B, which is explained in the paragraph following 
these bullet points 
• 
Use coordinate data already identified in the schematics discussed above. There are infinite 
different ways to create an identical print-path, similar to how a sphere could be modelled in 
CAD using many different functions (e.g. filleting a cylinder or cube, or revolving a semicircle) 
5. Preview the print-path during the design process and before manufacture - see Figure 3C-H 
• 
The print-path preview supports iterative development of bullet points 1-4 
 


## Page 11

 
 
 
 
11 
 
 
 
Figure 3 Design workflow for the FullControl design approach. A) Hand-drawn schematics are useful to (1) conceptually 
design the structure, (2) design the print-path sequence to achieve the concept structure, and (3) identify the detailed 
geometric information necessary for technical design of the structure in the FullControl software. B) User interface 
screenshot of FullControl GCode Designer, showing seven features that describe the design in (A) and are evaluated 
sequentially to generate GCode. Parameters of the ‘Circle/arc’ feature are identified with labelled arrows for cross-
reference to Section 3.3. C-H) Previews of the GCode after sequential inclusion of each of the seven features in (B). 
The arrow-linked steps labelled 1 to 5 are listed and described in Section 3.4. Grid in (C-H) = 10 mm. 
The FullControl user interface with the completed design for the auxetic lattice example is shown in Figure 
3B (provided as the ‘Lattice’ example design in the software [34]). Print-path previews are shown after each 
feature was created (Figure 3C-H), to demonstrate the continuous and systematic nature of the design 
method. These previews also show how the features are aggregated and sequentially evaluated by the 
software. Features 1 and 2 in Figure 3B both generate new GCode for arcs. Features 3-6 are all evaluated 
to replicate the GCode commands of previous features with modified coordinates (Cartesian offset or 
reflection). Feature 7 is evaluated to modify the coordinates of the GCode generated in feature 6: to rotate 
Feature 1 only
Print an arc 
made of 16 segments
+ Feature 2
Print a second arc
+ Feature 3
Repeat features 1-2 
in Y direction
+ Feature 4
Mirror features 1-3 
in X direction
+ Feature 5
Repeat features 1-4 
in X direction
+ Features 6 and 7
Repeat features 1-5 in Z 
direction for 99 extra layers 
(feature 6) and rotate each 
layer 90 (feature 7)
A
B
C
H
D
E
F
G
X
Y
X-centre
Y-centre
Z-height
Radius
Polar angle at start
Arc angle
Print direction
Segments
Width
Height
Y-offset
Number of times to repeat
X-offset
Z-offset
X-centre
Y-centre
90 rotation
Printing direction
1. Conceptual design
2. Print-path sequence design
3. Detailed geometric design
4. Create design in FullControl
5. Preview print-path


## Page 12

 
 
 
 
12 
 
 
the position of print-path segments in each layer by 90° in the X-Y plane. The parameters for the first feature 
Figure 3B (a circle/arc feature) are identified with labelled arrows for cross-referencing to the description of 
the circle/arc feature-type in Section 3.3. Particularly relevant parameters for other features are also identified 
to support interpretation of the respective print-path preview images on 10-mm grids. The most complicated 
aspect of this design is the trigonometric calculation of arc centre points and rotation points for each layer - 
highlighting the importance of detailed schematics (rightmost image in Figure 3A). Other features were 
created with ease. The design was created to be entirely parametric (unit cell size, number of unit cells, arc 
curvature, number of layers, layer height and filament width). This simple design resulted in over 100,000 
lines of GCode, which took just 14 seconds to generate. When the design parameters are saved as a comma-
separated values (csv) file, they require 300 bytes, with lossless quality. This is in the region of four orders 
of magnitude smaller file size than an STL file, which would have geometric errors and not contain any 
information about print-path, direction, speed and similar aspects. These benefits of parametric design have 
led to dedicated software to define the 3D geometry of lattices, such as nTopology [35]. In addition to allowing 
designs with adjustable parameters, conditional statements can easily be incorporated in a design - for 
example, features may be activated for certain conditions, such as switching from three to four perimeters if 
a parameter for part size exceeds a threshold value. 
FullControl also incorporates some necessary functionality that is not associated with the design of the printed 
structure. In particular, the instructions at the start and end of the GCode file are specific to a given printer 
and ensure it begins printing correctly and finishes the printing process safely (e.g. disabling heaters). 
Therefore start-GCode and end-GCode instructions are incorporated into all generated GCode files. Before 
using FullControl for a new printer, the start-GCode and end-GCode must be identified from the user manual 
of the printer or by examination of existing GCode.  
Other functionality has been included in FullControl to improve the usability, such as saving/loading designs, 
disabling/enabling features, creating adjustable parameters, describing coordinates in absolute or relative 
manners (i.e. relative to the nozzle position at the end of the previous feature), and the addition of automatic 
travel movements if the user creates disconnected print-path segments (e.g. between the first and second 
printed waves in Figure 3F). However, it is recommended as good practice to explicitly define all print-path 
segments, including non-extruding travel segments. Additionally, there is a section in the software user 
interface where information about the overall printing process is entered, such as default printing speeds and 
temperatures. 
Video S1 (<2 min) in supporting data [34] highlights some of the structures enabled by FullControl and 
includes video clips of the 3D printing process. Video S2 (≈20 min) in supporting data [34] gives a detailed 
technical introduction to FullControl with live-recorded demonstrations of features being defined and GCode 
being generated. 
The software has evolved over several years, iteratively improving to allow increasingly complex structures, 
as shown in the case studies in Section 4. This has led to practical software, which has been extensively 
tested for over a thousand hours by more than twenty students and researchers and used for several 
thousand hours of printing on systems ranging from £200 to £200,000.  
3.5. Software availability and development 
FullControl GCode Designer is open source and permanently available in a research data repository [34]. It 
is being further developed, and updated versions of the software will be available from 
www.fullcontrolgcode.com. Specific developments or new functionality may be requested by contacting the 
author of this article.  


## Page 13

 
 
 
 
13 
 
 
4. Demonstrations and discussion 
This section demonstrates the FullControl design approach with a series of case studies. All manufactured 
parts were designed and manufactured using FullControl GCode Designer or developmental versions of it. 
CAD software was not used (not even to support the design phase, despite the author and other software 
users being regular CAD-users) since schematics are naturally more appropriate and useful for parametric 
definition of designs, as discussed in the previous section.  
Multiple printers were used (Ultimaker 2+, Raise3D Pro2, regenHU 3DDiscovery, German RepRap X400) 
but all structures are achievable with a wide range of materials using any MEAM system that reads GCode. 
It has been successfully used to print silicone, conductive inks and clay. The designs for case studies are 
included in the software [34] or described in associated journal papers.  
4.1. Process calibration, characterisation and hardware development 
It is common for GCode to be manually written for simple process calibrations - for example, to move the 
nozzle to set locations of the print platform to level it. FullControl allows the creation of such print-paths and 
much more complicated parametric calibration with little effort. FullControl GCode Designer has been used 
to calibrate or characterise: 
• 
Print platform height/level - by printing multiple concentric squares 
• 
Retraction settings - by printing a parametric array of discontinuous lines, with each non-extruding 
travel movement assigned a different amount of material retraction and retraction speed  
• 
Fibre orientation in short-fibre-reinforced polymer 
• 
Extrusion widths for different print settings 
• 
Quality of different overhang angles 
• 
Capabilities for entirely novel structures - as discussed later in relation to Figure 7 
• 
Position of auxiliary hardware - by printing lines at controlled positions on the print platform 
By allowing the design of non-geometric factors as well as the precise print-path, expansive parametric 
process characterisation procedures can be designed. A recent study characterised how the width of 
extruded filaments could be varied continuously along their length to achieve a new scale of design for MEAM 
(discussed later in relation to Figure 4D) [31]. That study investigated hundreds of different combinations of 
speed, acceleration, jerk, retraction, extrusion width, and other parameters. By enabling design geometric 
tolerances an order of magnitude smaller than the nozzle diameter,, a new micro-tensile-testing specimen 
was designed with extrusion-widths of filaments carefully controlled to achieve a dog-bone geometry (Figure 
4A) [36,37]. This demonstrates the potential to design at completely new scales if process limitations are 
considered. These tensile-testing specimens allowed higher throughput and more detailed characterisation 
of mechanical properties compared to sliced CAD models of ASTM specimens. The FullControl design for 
the specimens consisted of just seven features - it is provided as the ‘TensileTestingBox’ example design in 
the software [34]. FullControl readily allows direct comparison of different 3D printers because a single design 
can be used to generate identical print-paths and print parameters in multiple GCode formats. The micro-
tensile-testing specimens have achieved comparable results by at least ten users, on twenty different printers, 
from five different system manufacturers, by avoiding any potential introduction of errors due to inconsistent 
slicer settings or similar. 
Custom-developed hardware, such as printing on a mandrel or with a multi-process print head (e.g. utilising 
both material-extrusion and machining tools), is well-suited to the FullControl design approach due to the 
flexibility to design non-extruding tool movements and custom GCode strings.  


## Page 14

 
 
 
 
14 
 
 
 
Figure 4 Structures designed at the scale of individual filaments using FullControl GCode Designer. A) Micro-tensile-
testing specimen with individually designed filament-widths. B) Tissue engineering scaffolds with different spacing 
between extruded filaments [30]. C) A parametric lattice structure, where each individual extruded filament was explicitly 
designed for a relatively large part (8 cm wide). D) Mesh structures produced with an identical print-path but variable 
extrusion-width, achieved by sinusoidal variation of print speed and extrusion rate [31]. E) Nonplanar printing using a 
zigzag print-path with up-down nozzle movement in the Z direction, normal to the print platform, to improve mechanical 
performance [38]. F) Streamlined extruded-filaments with continuously varying extrusion width to fit the overall part 
geometry [31]. Videos S1 and S3 in supporting data [34] show the printing process for (E) and (D), respectively. A) 
Reproduced under the terms and conditions of the Creative Commons CC BY-NC-ND 4.0 License [39]. All other parts 
of the figure, even when linked to publications, were created from original media. Scale bars = 5 mm. 
4.2. Filament-scale design and novel print-paths 
For structures where the geometry of individual extruded filaments is critical, such as the micro-tensile-
tensing dog-bone specimens in the previous section), explicit design of the print-path and print settings and 
settings for individual filaments is a logical approach. This also applies for structures where the pores between 
individual filaments are critical (e.g. tissue engineering scaffolds in Figure 1C) or where individual extrusion 
Different structural 
gradings for identical 
print-path
Zigzag layer-interface for 
improved mechanical 
performance
Micro-tensile-testing   
dog-bone with geometric 
design/control of  20 µm 
(1/20th nozzle diameter) 
Precise control for consistent scaffold pore geometry
A
A
B
C
D
E
Conventional approach: 
geometric changes 
accommodated by varying 
number of filaments
CONVEX approach: 
geometric changes 
accommodated by streamlined 
filaments of variable width
F
Conventional 
slicing
CONVEX 
(streamlined slicing)
Pore defects
No defects


## Page 15

 
 
 
 
15 
 
 
of different material are assembled (e.g. printed electronics or scaffolds in Figure 1D). However, the lattice 
structure with six-filament-wide struts in Figure 4C demonstrates the benefits of the FullControl design 
approach for larger structures, to allow explicit definition of:  
i. 
the order in which struts were printed 
ii. 
the exact order and direction in which each filament was printed for each strut 
iii. 
the manner of travel between struts, which involved multi-step movements of the print head to ensure 
excess extrusion was deposited in the centre of struts rather than their external surface 
iv. 
parametric geometry, which allowed the print-path to be instantly regenerated for new parametric 
designs 
The microscale control enabled by the FullControl approach allows the geometry of individual filaments to be 
designed along their length, as opposed to considering filaments to have an unvarying geometry. This allows 
entirely new structures to be conceived, such as the graded mesh materials in Figure 4D; even though an 
identical print-path was used for all structures, geometric grading was achieved by sinusoidal variation of 
print speed and extrusion width [31]. This highlights how unconstrained design of the printing procedure 
enables new conceptual printing approaches. Although the geometry of individual filaments must be designed, 
adding a level of complexity, this can be a simple design process when using parametric or mathematic 
functions such as sinusoidal fluctuation. Mathematic design is discussed further in Section 4.3. The 
FullControl approach is appropriate for larger assemblies of extruded filaments, as demonstrated by it use to 
uninhibitedly investigate a new conceptual slicing strategy, ‘streamlined slicing’ [31], in which streamlines of 
the part geometry were used to define the print-path, and extrusion width was continuously varied based on 
the separation of these streamlines (Figure 4F). In this case, the ability to control acceleration independently 
for each print-path segment was important, highlighting the benefit of parametric design of both the print-path 
and print parameters.  
A key opportunity enabled by the FullControl design approach is the unconstrained ability to design print-
paths utilising all three dimensions, as opposed to the conventional approach of completing X-Y movements 
(print-platform plane) before moving by one layer-height in the Z direction (normal to the print platform). This 
allowed research into mechanical performance enhancement by using nonplanar interfaces between layers 
(Figure 4E): zigzag interfaces disrupted the fracture path and led to improved mechanical performance versus 
conventional planar layers [38]. The most important aspect to note here is not the improved performance, but 
rather that FullControl enabled investigations that were not possible with existing software. There is an infinite 
range of other structures and aspects that could be investigated. Controlled print-path design in the Z 
direction is further utilised in several examples in subsequent sections (discussions related to Figure 5D&E 
and Figure 7).  
4.3. Mathematical design 
When designing print-paths with FullControl GCode Designer, a useful approach is to define the paths with 
mathematical functions. Several examples of this are shown in Figure 5 and discussed here. The sinusoidal 
cylinders in Figure 5A were all produced with the same parametric design, with slightly adjusted parameters. 
In FullControl, the design consists of just one feature - a mathematically defined spiral curve with sinusoidal 
fluctuation of radius. The equations for X, Y and Z coordinates can be seen in the ‘SineTube’ example given 
in the software [34]. This simple design format allows the full detail of the design to be recorded with a few 
bytes of data, whilst allowing parametric generation of GCode with thousands or millions of print-path 
segments.  


## Page 16

 
 
 
 
16 
 
 
 
Figure 5 Mathematically defined structures produced using FullControl GCode Designer. A) Parametric spiral print-path 
with sinusoidal fluctuation, created with a single design feature in FullControl. B) Gyroid lattice structures. C) Lattice 
structure considered in Figure 3. D) Dodecagonal cylinder with sinusoidally varying layer height designed with just three 
features in FullControl. E) A concept shoe sole with conformal lattice geometry, nonplanar layers and specially designed 
terminal lattice cells - designed with just thirteen features in FullControl. F) Mathematically defined textures. Videos S1 
and S4 in supporting data [34] show the printing process for (C) and the manufactured part in (E), respectively. Scale 
bars = 5 mm. 
Mathematically defined lattices are also well-suited to FullControl because the curve equations for the print-
paths on each layer can be readily determined from theoretical mathematical descriptions of the lattices. The 
gyroid structures shown in Figure 5B required just 15 features in FullControl. This design allowed full 
parametric variation of unit cell sizes, the number of unit cells, and many other design or printing parameters. 
Over 500,000 lines of GCode were produced, depending on the structure size, and the computation time is 
less than two minutes (with scope for significant software-code optimisation for computation speed). In this 
ongoing research, the ability to control every print-path segment on every layer allowed investigative freedom 
and design optimisation for additive manufacturing that was not possible when using CAD and slicer software. 
The printed version of the structure in Figure 3 is shown in Figure 5C, which used trigonometric definitions 
for design parameters. Additionally, the potential to vary layer height according to a sinusoidal function is 
shown in Figure 5D for a dodecagonal cylinder, which had the same number of layers along the entire 
A
B
D
E
Nonplanar layers
Conformal lattice cells
Conformal 
lattice 
cells
Designed 
terminal 
lattice 
cells
C
F
Shape-fitted 
texture


## Page 17

 
 
 
 
17 
 
 
circumference; this allowed the nonplanar top-surface of the part to be printed in a single pass, eliminating 
stepping that traditionally occurs between printed layers. The design is included as the ‘NonplanarCylinder’ 
example in the software [34]. 
A mathematically defined concept shoe sole is shown in Figure 5E. The print-path for one layer was defined 
mathematically, including considerations to conform the lattice to the part geometry (top-down view in bottom-
left image). Conforming the lattice resulted in immense improvement in part quality compared to what would 
be achieved by filling an STL file (of the overall part geometry) with a regular lattice, which would have partial 
cells. Partial cells were also avoided by designing the terminal unit cells to have a different structure, enabling 
a neat external surface (bottom-right image in Figure 5E). This highlights a key capability of the FullControl 
framework to combine mathematical curve equations with non-mathematical features such as arcs or 
‘cartesian repeat’ features. By fully designing the print-path, it was possible to avoid non-extruding travel 
movements (a common cause of defects, especially for flexible polymers such as polyurethane used here). 
The ability to modify the print-path on different layers (using ‘repeat rule’ features) allowed non-vertical walls 
(skewed inwards) to be designed whilst maintaining a conformal lattice and avoiding any partial unit cells. 
The ability to design freely in all three dimensions allowed the straight side-sections to be printed with 
nonplanar layers to achieve varying part thickness whilst avoiding stepping artefacts associated with 
layerwise manufacturing of shallow gradients. Again, the design approach naturally allowed a conformal 
lattice for the nonplanar layer geometry (middle-bottom image in Figure 5E). Creating a CAD model of this 
part would be extremely inefficient and challenging, and would result in a poor product quality since errors 
would be introduced by the STL file conversion and by the generation of a print-path that would almost 
certainly include non-extruding travel movements. By comparison, a fully parametric design was created in 
FullControl (approximately 1 kilobyte of data versus an estimated 1 gigabyte for a non-parametric STL model) 
using just thirteen features: five mathematically defined lines, three features for repetition or reflection of 
those lines, and five features to define geometric skew and nonplanar modifications. These features resulted 
in 210,000 lines of GCode.  
As well as overall part geometry, mathematical definition of the print-path allows for the design of microscale 
features, as shown for textured parts in Figure 5F. A parametric design was created in which the print-path 
fluctuated sinusoidally to achieve a rippled texture. The magnitude and frequency of fluctuation is adjustable 
with user-defined parameters, along with other aspects of the design including overall size, shape, layer 
height and extrusion rate. To achieve the structure to the right in Figure 5F, parameters for layer height and 
extrusion rate were increased, as described in the design file, which is provided as supplementary information 
[34], including example parameter sets. The design is usable without any understanding of the mathematical 
print-path formulae, highlighting how expert knowledge can be integrated into a print-path design for team 
projects and collaboration. Since Excel is used as a front end for FullControl, it was possible to include usage 
instructions in the design file, along with parameter descriptions and a customised user interface with images 
of print-paths for example parameter sets.   
4.4. Industrial manufacturing 
In response to a short-term need for face visors, a suite of twenty 3D printers were used to manufacture over 
1,000 reusable visor-frames (Figure 6A). This case study has high industrial relevance due to the high 
production-volume, relatively large part dimensions, considerable time constraints, and specific customer 
requirements. The parts were sent for post-processing and assembly by Toyota Motor Manufacturing UK, 
who in turn liaised with healthcare end users. Some key constraints and considerations were: 
• 
Nylon material had to be used (to ensure reusability), which can be challenging to retract. 


## Page 18

 
 
 
 
18 
 
 
• 
Bowden-tube printers had to be used; these present an additional challenge for retraction due to the 
longer distance between the extruder and nozzle compared with direct-drive printers 
• 
Only minor revisions to the geometric design were permitted 
• 
Significant time constraints limited the potential for optimisation compared to typical research work 
• 
The printing procedure had to be resilient for reliable manufacturing on twenty printers, which often 
behaved considerably differently 
After manufacturing, the parts were post-processed to remove defects such as protrusions or strings, 
especially on the forehead band and in the visor slot. Post-processing was the bottleneck of the overall 
production process, so reducing post-processing time was a key aspect of optimisation. 
Despite several days of refinement by multiple experienced users with two different slicing software packages, 
the printing speed was limited by defects associated with the print-path and non-extruding travel movements 
of the nozzle between sections of the part (see string-defects in Figure 6C). By fully defining the print-path 
using FullControl, it was possible to minimise the number of non-extruding travel movements and ensure 
they occurred in non-critical areas. This is shown in Figure 6F, which compares previews of the slicer-
generated GCode that was originally being used to the final FullControl GCode. In particular, non-extruding 
travel movements were avoided for the forehead band (in contact with the user’s forehead) and the slot into 
which the visor sheet fitted. The successful reduction of stringing can be clearly seen in Figure 6C. Stringing 
was particularly prominent because the speed and extrusion width were set as high as they could be before 
introducing under-extrusion defects. Retraction capabilities were limited due to requirements for a high 
material flow rate, Bowden fed printers, and nylon material. For other situations, slicing software may be 
much more successful, but here, it was invaluable to be able to control the position of defects and undesired 
strings to be located in accessible areas (e.g. visor bolt holes which were rapidly post-processed with a hand 
drill). In addition, where possible, the print-path was designed to perform retraction and un-retraction 
operations in internal regions to minimise surface blemishes. 
Originally, a large proportion of post-processing effort went into ensuring that the forehead band was smooth. 
With FullControl, the band required no post-processing because it was printed with a single pass of the nozzle, 
extruding 250% of the nozzle diameter (aspect ratio of 5 for width:layer-height). This was found to achieve a 
solid structure with good mechanical integrity, as expected based on recent understanding that a wider aspect 
ratio for filament cross-sections improves mechanical performance [37] (discussed in Section 4.1). Due to 
improved mechanical integrity, it was possible to reduce weight by 20% whilst maintaining equivalent or 
improved performance. This highlights the potential to integrate expertise of process limitations into the 
design of the print-path (and relevant printing parameters) to improve performance. 
Printing speed was also improved by designing a smooth continuous print-path. No infill was used, and the 
part was printed using large sweeping arc motions. The smooth nature of the print-path improved aesthetic 
quality (eliminated defects/blemishes), and dramatically reduced the mechanical stresses put on the printers 
(when the nozzle quickly changes direction hundreds of times to complete infill of narrow regions).  
To allow multiple parts to be printed overnight without supervision, it was desirable to print a stack of visor 
bands in a single printing procedure (Figure 6A). Under-extrusion was deliberately employed to achieve 
discontinuous droplets of extruded material. This can be seen in Figure 6D, which shows three still images 
of the printing process at two-second intervals; the inset image to the right shows a zoomed-in view of a 
single under-extruded line made up of connected droplets. This type of discontinuous deposition provided 
sufficient support to achieve good quality for subsequent parts, whilst also allowing part-separation by hand.  
Towards the end of the printing process, the part geometry required material to be printed in between the 
front and rear walls of the visor slot (to connect these two regions). Printing perpendicularly across this slot 


## Page 19

 
 
 
 
19 
 
 
is the conventional approach to bridging it. However, this would have resulted in a staggered print-path and 
eliminated many of the benefits of the smooth sweeping print-path design described above. Therefore, a 
sinusoidally fluctuating arc was printed for one layer, to bridge the slot and act as support for slot-aligned 
print-paths in subsequent layers. This is shown in Figure 6E, where the left two images show the sinusoidal 
bridge during and after printing, and the right image shows it after two lines have been printed on top of it 
(aligned with the slot) on the subsequent layer. The mathematical definition of the sinusoidal bridging line 
made it far simpler to implement in FullControl than to define numerous perpendicular bridging lines, 
highlighting the practical potential to incorporate mathematical design (as discussed in Section 4.3) for 
mundane and functional purposes. 
The following benefits of parts produced using FullControl GCode Designer (instead of slicing software) are 
direct quotations from a senior manager at Toyota Motor Manufacturing UK (Daniel Nelson): 
1. “Increased product output from both printer speed increase and stacking on the print bed 
2. Reduced post-production time due the improved quality including surface finish 
3. Raw material reduction through weight optimisation 
4. Printer reliability improvement as the machines ran smoother” 
Overall, the production rate increased by 400% to 600% per printer, whilst also significantly reducing the 
time-demands on the printing technician, due to a combination of stacking, reduced weight, and increased 
printing speed. An improved product was achieved in terms of the business customer (Toyota - especially in 
terms of post-processing time) and the end user (in terms of comfort on the forehead). 
Although this section directly compares the FullControl approach to slicers, it should be considered as a 
demonstration of potential applicability of the new design approach rather than an evaluation of slicing 
software. The print-path preview in Figure 6F indicates a reasonably typical slicer print-path, but it could be 
improved using advanced capabilities of slicing software such as custom print settings in different regions of 
the model. Some aspects of the FullControl print preview appear leaner than the slicer version in the figure, 
but this mostly is due to the graphical representation: the extrusion width of the FullControl version was 250% 
of that for the slicer version, which is not apparent in the preview lines. Also, the attachment point for the 
elastic headband was oriented vertically instead of horizontally, so it was printed on every layer of the 
FullControl print-path, as opposed to only on some layers in the slicer version. Overall, the attachment-points 
were similar in size for both designs. This is a good example of the design process encouraging the simplest 
possible print-path. Rather than using support structures and conventional design rules such as 45° 
overhangs to achieve horizontal attachment points, the design requirements were met by a simple print-path 
design. An almost identical print-path was used on every layer, except some print-path segments in 
top/bottom regions were replaced with non-extruding travel movements to allow a gap between the visor 
frame and the attachment point, into which the elastic headband slotted. This allowed top and bottom layers 
to be identical, to facilitate neat vertical stacking of visors. 
The visor demonstrates the use of the presented design method beyond academic research, but it is a 
relatively simple geometry. Many 3D printed components, especially those manufactured by polymer printing 
systems with small nozzles and complicated print-paths, would be impractical for explicit print-path design. 
For the FullControl approach to be successful, it is important to consider the print-path early in the design 
process. The improvements to the printing procedure explained in this section would not have been possible 
if using scripts for GCode generation - too many different scripts would have been required (multiple print-
path concepts were tested). Repeatedly rewriting scripts for small changes to the printing procedure would 
have overly burdened progress and have been infeasible given the time constraints. The design was 


## Page 20

 
 
 
 
20 
 
 
described by 125 features in FullControl and took 4 minutes to generate 700,000 lines of GCode for a stack 
of eight visor-frames. It is provided as supplementary information [34]. 
For reasonable production runs (e.g. several hundred units), the effort/cost required for print-path design is 
justified by the benefits in terms of product quality, raw-material usage, printer maintenance, wastage for 
failed/rejected parts, production time and post-processing time. Print reliability is critically important for large 
structures, high-cost materials, materials with limited availability (e.g. autologous-cell-laden hydrogels), 
critical applications (e.g. medical implants), and many other fields. Therefore, improvements to print reliability 
may justify many weeks of effort to optimise the print-path design. 
 
Figure 6 Comparison between traditional slicer software and FullControl print -paths for a visor frame that was printed 
over 1,000 times. A) Stack of six visor frames printed together. B) Simplified top-view schematic of the print-path. C) 
Slicing software led to stringing and blemishes when printing at higher speeds. D) FullControl allowed precise design of 
under-extrusion between parts in a stacked print, resulting in connected droplets that sufficiently supported subsequent 
parts, whilst allowing separation by hand. E) A sine wave was printed to act as support when a gap needed to be bridged. 
F) Print-path previews for the original GCode produced by slicing software and the GCode produced by FullControl. By 
using the FullControl design approach, production rate increased by 400% to 600%, post-processing time was reduced, 
material usage was reduced, aesthetics was improved, comfort for the end-user was improved and printer reliability was 
improved. Video S5 in supporting data [34] shows the printing process for (E). Grid in (F) = 10 mm. Scale bars = 5 mm 
unless otherwise indicated. 
Traditional visor print-
path top-down view
FullControl visor print-path 
top-down view
Single-pass printed 
forehead band
Neat travel 
between 
sections
Printed line
Minimal fast-travel 
(not printed)
Smooth, continuous 
extrusion and nozzle 
movement
Traditional 
approach
Top-down-view 
schematic
A
B
F
50 mm
B
Designed 
under-extrusion 
between parts
Sine-wave 
bridge 
support
Two lines 
printed on 
sine-wave 
support
Point 2 in B
Point 1 in B
Point 2 in E
Point 1 in D
Slicer: unavoidable stringing 
at high speeds and 
wide extrusions
FullControl: continuous 
print-path design 
eliminated stringing
C
D
E
50 mm
Six-visor stack
2 secs
2 secs


## Page 21

 
 
 
 
21 
 
 
4.5. Novel structures 
By having full control over both the print-path (with full three-dimensional freedom) and all additional relevant 
factors (e.g. extrusion rate and speed), it is possible to achieve entirely new geometric structures. An 
interesting structure is the normally undesirable strings that result from quick movement of the nozzle 
between different parts of the printed object. By carefully controlling vertical movement (normal to the print 
platform) along with extrusion rate and speed, it was possible to achieve a designed pattern of strings, as 
shown in Figure 7A, in which the nozzle was quickly moved between opposing sides of a pre-printed frame. 
This structure was used to calibrate the printing procedure to be able to control repeatability and geometric 
properties of the drawn strings. With FullControl, the addition of one simple feature (‘Repeat rule’ in Section 
3.3) allowed each string to be printed with incrementally increasing speed, extrusion amount, vertical offset, 
and many other parameters. This allowed for rapid and informative characterisation of process capabilities 
for this previously unstudied structure. A variation of this calibration specimen was conversely used to 
optimise retraction settings to avoid strings when they were undesirable in other work. The design of a 
structure similar to that in Figure 7A is demonstrated in Video S2 in supporting data [34]. 
A more complicated implementation of strings, into a parametric hexagonal scaffold structure, is shown in 
Figure 7B. It was possible to achieve a precisely controlled structure with string diameters as low as 1/10th 
of the nozzle diameter, and repeatability such that 750 strings were all successfully printed in a single 
structure. These structures were designed with eight simply defined features in FullControl, and it took 1 
second to generate 4,000 lines of GCode. Due to the ability to quickly iterate the structural design and 
generate GCode, the process of design and manufacturing optimisation for this highly unusual structure was 
completed in three hours. A CAD file cannot be created for these structures that has any meaningful data to 
allow their production using slicing software: they are only possible through explicit design of the GCode.  
 
Figure 7 Novel structures produced with FullControl GCode Designer. A) Calibration specimen to optimise process 
parameters to manufacture repeatable drawn strings when the nozzle rapidly traverses from one side of a pre-printed 
frame to the other. B) Scaffolds manufactured by drawing strings across a hexagonal frame, with diameters as low as 
1/10th of the nozzle diameter. 750 strings were printed in a taller variant (inset) with 100% success rate and high fidelity. 
C and D) Polylactide stent structures printed upright (central axis normal to print bed) using designed combinations of 
vertical extrusion (nozzle moving directly away from the print platform) and lateral extrusions. When crimped after 
manufacture, the stent in (D) self-expanded at elevated temperature. Video S1 in supporting data [34] shows the printing 
process for (B) and (C), and Video S2 demonstrates the design of (A). Scale bars = 5 mm unless otherwise indicated. 
0.5 mm
A
C
B
D


## Page 22

 
 
 
 
22 
 
 
The ability to explicitly design speed, extrusion rate, and the 3D print-path are enabled the two demonstration 
stents in Figure 7C and D to be produced, which were printed vertically (central axis normal to the print 
platform). These structures were manufactured by using a combination of vertical extrusion of discrete pillars 
(moving the nozzle directly away from the print platform), followed by extrusion of bridging filaments between 
the pillars. This combination of extrusion-types was then repeated incrementally at increasing heights above 
the print platform to achieve several-centimetre-tall stents. These structures were only possible through 
careful parametric optimisation of the printing procedure, including the necessary design of multiple non-
extruding 3D print-path segments to move the nozzle between pillars without deflecting them (or 
compromising their quality in other ways). The ability to design custom GCode strings for controllable pauses 
ensured a good connection between struts was achieved. The stent in Figure 7D was naturally self-expanding: 
it was crimped to less than half its initial diameter before naturally expanding to the original diameter at 
elevated temperatures. These structures break free from typical perceived constraints of printing layer-by-
layer; slicing software is conceptually and practically incompatible with their design and manufacture. By 
designing printing procedures without constraints of typical software, entirely new applications for material 
extrusion additive manufacturing are possible. 
4.6. Alternative processes 
Whilst the described case studies considered the material extrusion additive manufacturing process, there 
are many other process technologies that use GCode with a similar or identical format, which could benefit 
from FullControl GCode Designer, with minor or no modifications. Minor edits to the open-source code would 
allow considerable different GCode languages. A particularly relevant use of FullControl, for which research 
is ongoing, is to design laser paths for processes including: 
• 
Laser cutting 
• 
Laser surface modification 
• 
Vat photopolymerisation 
• 
Selective laser sintering and melting (SLS and SLM)  
• 
Laser measurement devices 
Aside from lasers, there are many other potential uses of GCode for positional control in manufacturing and 
other fields, where the FullControl design approach may be of value, including: 
• 
Material jetting 
• 
Directed energy deposition 
• 
3D welding 
• 
Coordinate measurement machines (CMM) 
• 
Computer numerical control (CNC) machining 
• 
Motorised XY linear stages for any application 
The potential of FullControl to parametrically vary the tool path and other parameters, such as speed, opens 
up the potential for rigorous fundamental research and final-product manufacturing. 
 
 
 


## Page 23

 
 
 
 
23 
 
 
5. Concluding remarks 
Open-source software called FullControl GCode Designer was explained conceptually and in terms of its 
practical implementation. The typical workflow for directly designing GCode was described, and case studies 
highlighted the wide range of potential uses, from calibration prints for research studies to industrial 
collaboration for production runs >1,000. Advantages over existing additive manufacturing software were 
discussed. The direct design of GCode allowed structures that are inconceivable when using traditional 
software and offers greater potential for refinement of additive manufacturing procedures.  
The design approach represents an alternative way of thinking about additive manufacturing, in which the 
individual print-path segments are deliberately designed along with all printing parameters for each segment 
(e.g. speed, acceleration, extrusion rate, temperature) to allow absolute control over the manufacturing 
process.  
The generally accepted use of slicing software - and the lack of process-specific information incorporated in 
CAD files - has limited research progress by not allowing the fundamentals of the process (individual 
extrudates) to be effectively studied. This is evidenced by FullControl immediately enabling multiple recent 
publications (featured in case studies) that challenge the status quo. For parametrically defined geometries, 
it is achievable to define all details of the print-path. Typical 3D components, however, with non-systematic 
geometry, would be challenging to define the print-path for in many cases. The strength of slicing software is 
in its ability to handle any geometry and for rapid generation of acceptable, but not fully controllable, print-
paths. Custom-scripts for one-off structures also overcome limitations of slicing software, but they are 
naturally limited to a single application and require programming, unlike FullControl.  
The FullControl design approach offers the unconstrained ability to design print-paths and deliberately control 
any printing parameter for all sections of that print-path. Furthermore, it encourages innovation and creativity; 
particular opportunities are nonplanar printing, extrusion of material in nonconventional geometries, 
optimisation of print-paths for maximal quality/reliability, rigorous process characterisation, precise 
experimentation for computer model validation, and elimination of uncontrolled defects.  
The author is keen to collaboratively support improvement of the software to be more capable and more 
usable; by adding simulation capabilities or integration into slicing software, for example. 
Acknowledgments 
Thanks to all the people who have used FullControl GCode Designer for their research; in most case studies, 
the resulting journal paper is referenced, but additionally, thanks to Leung YinMing for specimens in Figure 
1F and Figure 7C/D, and John-Jo Pye for specimens in Figure 5B. Also, thanks to Vadim Silberschmidt for 
advice on this publication, and to Celal Soyarslan, Mary Lack, David Comberton and Simone Fontana, who 
were the motivation for parts in Fig. 4C, Fig. 5C, Fig. 5E and Fig. 5F, respectively. 
References 
[1] 
I. Zein, D.W. Hutmacher, K.C. Tan, S.H. Teoh, Fused deposition modeling of novel scaffold 
architectures for tissue engineering applications, Biomaterials. 23 (2002) 1169–1185. 
[2] 
T. Serra, J.A. Planell, M. Navarro, High-resolution PLA-based composite scaffolds via 3-D printing 
technology, Acta Biomater. 9 (2013) 5521–5530. 
[3] 
L. Ruiz-Cantu, A. Gleadall, C. Faris, J. Segal, K. Shakesheff, J. Yang, Multi-material 3D bioprinting of 
porous constructs for cartilage regeneration, Mater. Sci. Eng. C. 109 (2020) 110578. 


## Page 24

 
 
 
 
24 
 
 
[4] 
F. Daniel, J. Peyrefitte, A.D. Radadia, Towards a completely 3D printed hot wire anemometer, Sensors 
Actuators A Phys. 309 (2020) 111963. https://doi.org/https://doi.org/10.1016/j.sna.2020.111963. 
[5] 
J.O. Hardin, C.A. Grabowski, M. Lucas, M.F. Durstock, J.D. Berrigan, All-printed multilayer high 
voltage capacitors with integrated processing feedback, Addit. Manuf. 27 (2019) 327–333. 
https://doi.org/https://doi.org/10.1016/j.addma.2019.02.011. 
[6] 
S. Aslanzadeh, H. Saghlatoon, M.M. Honari, R. Mirzavand, C. Montemagno, P. Mousavi, Investigation 
on electrical and mechanical properties of 3D printed nylon 6 for RF/microwave electronics 
applications, 
Addit. 
Manuf. 
21 
(2018) 
69–75. 
https://doi.org/https://doi.org/10.1016/j.addma.2018.02.016. 
[7] 
A.N. Dickson, D.P. Dowling, Enhancing the bearing strength of woven carbon fibre thermoplastic 
composites 
through 
additive 
manufacturing, 
Compos. 
Struct. 
212 
(2019) 
381–388. 
https://doi.org/https://doi.org/10.1016/j.compstruct.2019.01.050. 
[8] 
H. Mei, Z. Ali, I. Ali, L. Cheng, Tailoring strength and modulus by 3D printing different continuous fibers 
and filled structures into composites, Adv. Compos. Hybrid Mater. 2 (2019) 312–319. 
[9] 
K.A. Deo, K.A. Singh, C.W. Peak, D.L. Alge, A.K. Gaharwar, Bioprinting 101: design, fabrication, and 
evaluation of cell-laden 3D bioprinted scaffolds, Tissue Eng. Part A. 26 (2020) 318–338. 
[10] 
S. Ji, E. Almeida, M. Guvendiren, 3D bioprinting of complex channels within cell-laden hydrogels, Acta 
Biomater. 95 (2019) 214–224. 
[11] 
J. Hergel, K. Hinz, S. Lefebvre, B. Thomaszewski, Extrusion-based ceramics printing with strictly-
continuous deposition, ACM Trans. Graph. 38 (2019) 1–11. 
[12] 
T. Yu, Z. Zhang, Q. Liu, R. Kuliiev, N. Orlovskaya, D. Wu, Extrusion-based additive manufacturing of 
yttria-partially-stabilized 
zirconia 
ceramics, 
Ceram. 
Int. 
46 
(2020) 
5020–5027. 
https://doi.org/https://doi.org/10.1016/j.ceramint.2019.10.245. 
[13] 
A. Ghazanfari, W. Li, M.-C. Leu, G. Hilmas, Novel Extrusion-Based Additive Manufacturing Process 
for Ceramic Parts, in: Solid Free. Fabr. 2016, 2016: pp. 1509–1529. 
[14] G.H. Loh, E. Pei, D. Harrison, M.D. Monzon, An overview of functionally graded additive manufacturing, 
Addit. Manuf. 23 (2018) 34–44. 
[15] 
J.W. Jung, J.-S. Lee, D.-W. Cho, Computer-aided multiple-head 3D printing system for printing of 
heterogeneous organ/tissue constructs, Sci. Rep. 6 (2016) 21685. 
[16] 
H.-W. Kang, S.J. Lee, I.K. Ko, C. Kengla, J.J. Yoo, A. Atala, A 3D bioprinting system to produce human-
scale tissue constructs with structural integrity, Nat. Biotechnol. 34 (2016) 312–319. 
[17] 
J.C.S. McCaw, E. Cuan-Urquizo, Curved-Layered Additive Manufacturing of non-planar, parametric 
lattice 
structures, 
Mater. 
Des. 
160 
(2018) 
949–963. 
https://doi.org/https://doi.org/10.1016/j.matdes.2018.10.024. 
[18] 
S. 
Babu, 
The 
future 
of 
additive 
manufacturing 
is 
all 
about 
design, 
Eng. 
(2017). 
https://www.theengineer.co.uk/the-future-of-additive-manufacturing-is-all-about-design/ 
(accessed 
July 17, 2020). 
[19] 
regenHU BioCAD, (2020). https://www.regenhu.com/3d-bioprinters/software. 
[20] 
B. Wong, G-Code Generator, (2020). https://github.com/brendanwong/g-code-generator. 
[21] 
E. Nyberg, A. O’Sullivan, W. Grayson, ScafSlicr: A MATLAB-based slicing algorithm to enable 3D-
printing of tissue engineering scaffolds with heterogeneous porous microarchitecture, PLoS One. 14 
(2019) e0225007. https://doi.org/10.1371/journal.pone.0225007. 
[22] 
Aura, (2020). https://anisoprint.com/product-aura. 
[23] 
Eiger, (2020). https://markforged.com/eiger/. 


## Page 25

 
 
 
 
25 
 
 
[24] 
Fibrify, (2020). https://www.9tlabs.com/product. 
[25] 
C. Bailey, E. Aguilera, D. Espalin, J. Motta, A. Fernandez, M.A. Perez, C. Dibiasio, D. Pryputniewicz, 
E. Macdonald, R.B. Wicker, Augmenting Computer-Aided Design Software With Multi-Functional 
Capabilities to Automate Multi-Process Additive Manufacturing, IEEE Access. 6 (2018) 1985–1994. 
https://doi.org/10.1109/ACCESS.2017.2781249. 
[26] S. Koda, H. Tanaka, Direct G-code manipulation for 3D material weaving, in: Nanosensors, Biosensors, 
Info-Tech Sensors 3D Syst. 2017, 2017. https://doi.org/10.1117/12.2261648. 
[27] 
G.C. Anzalone, B. Wijnen, J.M. Pearce, Multi-material additive and subtractive prosumer digital 
fabrication with a free and open-source convertible delta RepRap 3-D printer, Rapid Prototyp. J. 21 
(2015) 506–519. https://doi.org/10.1108/RPJ-09-2014-0113. 
[28] 
G. 
Hodgson, 
A. 
Anellucci, 
J. 
Moe, 
Slic3r 
Manual: 
Post-Processing 
Scripts, 
(2020). 
https://manual.slic3r.org/advanced/post-processing (accessed July 17, 2020). 
[29] 
S.A. Tronvoll, C.W. Elverum, T. Welo, Dimensional accuracy of threads manufactured by fused 
deposition modeling, Procedia Manuf. 26 (2018) 763–773. 
[30] 
D.O. Visscher, A. Gleadall, J.K. Buskermolen, F. Burla, J. Segal, G.H. Koenderink, M.N. Helder, P.P.M. 
van Zuijlen, Design and fabrication of a hybrid alginate hydrogel/poly (ε‐caprolactone) mold for 
auricular cartilage reconstruction, J. Biomed. Mater. Res. Part B Appl. Biomater. (2018). 
[31] 
A. Moetazedian, A.S. Budisuharto, V. V. Silberschmidt, A. Gleadall, CONVEX (CONtinuously Varied 
EXtrusion): a new scale of design for additive manufacturing, Addit. Manuf. 37 (2021) 101576. 
https://doi.org/10.1016/j.addma.2020.101576. 
[32] 
M. Littwin, R. Littwin, Repetier Host, (2020). https://www.repetier.com/download-software/. 
[33] 
Desmos graphing calculator, (2021). https://www.desmos.com/calculator. 
[34] 
A. Gleadall, Data for article: FullControl GCode Designer - open-source software for unconstrained 
design in additive manufacturing, (2021). https://doi.org/doi:10.17028/rd.lboro.12933320. 
[35] 
M. Shomper, Designing Lattice Structures for Biologically-Relevant Medical Implants, (2019). 
https://ntopology.com/blog/2019/07/25/designing-and-building-lattice-structures-for-biologically-
relevant-medical-implants/. 
[36] 
A. Moetazedian, A. Gleadall, X. Han, V.V. Silberschmidt, Effect of environment on mechanical 
properties of 3D printed polylactide for biomedical applications, J. Mech. Behav. Biomed. Mater. 102 
(2020). https://doi.org/https://doi.org/10.1016/j.jmbbm.2019.103510. 
[37] 
J. Allum, A. Moetazedian, A. Gleadall, V. V Silberschmidt, Interlayer bonding has bulk-material 
strength in extrusion additive manufacturing: new understanding of anisotropy, Addit. Manuf. (2020) 
101297. https://doi.org/10.1016/j.addma.2020.101297. 
[38] 
J. Allum, J. Kitzinger, L. Yimeng, V. V. Silberschmidt, A. Gleadall, ZigZagZ: improving mechanical 
performance in extrusion additive manufacturing by nonplanar toolpaths, Addit. Manuf. 38 (2021) 
101715. https://doi.org/10.1016/j.addma.2020.101715. 
[39] 
A. Gleadall, W. Poon, J. Allum, A. Ekinci, X. Han, V. V. Silberschmidt, Interfacial fracture of 3D-printed 
bioresorbable 
polymers, 
Procedia 
Struct. 
Integr. 
13 
(2018) 
625–630. 
https://doi.org/https://doi.org/10.1016/j.prostr.2018.12.103. 
 



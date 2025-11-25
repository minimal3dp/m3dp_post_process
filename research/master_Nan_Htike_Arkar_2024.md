# Title of thesis
**Author:** Nan Htike Arkar

**Source:** `master_Nan_Htike_Arkar_2024.pdf`
---

## Page 1







Master’s Programme in Mechanical Engineering

Non-planar Material Extrusion and
Continuous Fiber-Reinforced 3D Printing:
Algorithmic Modeling and G-code
Generation


Arkar Nan Htike
















Master’s thesis
2024



## Page 2







Copyright ©2024 Arkar Nan Htike








## Page 3






3

Author  Arkar Nan Htike
Title of thesis  Non-planar Material Extrusion and Continuous Fibre-Reinforced
3D Printing: Algorithmic Modeling and G-code Generation
Programme  Master’s Programme in Mechanical Engineering
Major Mechanical Engineering
Thesis supervisor  Prof. Jouni Partanen
Thesis advisor(s)  Tuomas Puttonen (DCs), Kumar Siddharth (MSc)
Collaborative partner  Aalto University Digital Design Laboratory (ADDLAB)
Date  31.10.2024
Number of pages  59
Language  English
Abstract
The thesis aimed to investigate the capabilities of non-planar 3D printing in
thermosplastic material extrusion printers and continuous fibre-reinforced
3D
printers.
Material extrusion can achieve many diverse benefits, thanks to the freedom
of geometry it brings. However, there are still significant challenges in
surface quality, freedom of movement and dimensional accuracy of the
manufactured parts. Therefore, from the point of view of the development of
the industry, it is important to investigate whether these challenges can be
solved by non-planar 3D printing.
This thesis aims to develop a comprehensive methodology for generating
custom G-code for non-planar toolpath movement in 3D printing, leveraging
tools such as Python, Rhino 3D, and Grasshopper. The first objective is to
successfully create G-code for a single non-planar layer of a 3D model,
followed by validating the process through the practical application of
extruding plastics to manufacture a shin guard as a case study. The second
phase explores extending this methodology to composite fiber printers,
enabling the application of non-planar techniques to advanced materials.
The research also outlines potential future directions, including non-planar
printing with carbon fiber and customizing 5-axis FFF printers. The
overarching goal is to provide a foundational manual for future work in non-
planar fused filament fabrication (FFF), advancing the understanding of its
scientific and industrial applications.
As a result of the thesis, promising results were obtained from the use non-
planar 3D printing and the benefits it could achieve. Despite the results, non-
planar 3D printing would still require further research. Further research and
development targets were presented to ABBLAB.
Keywords  Additive Manufacturing, Material Extrusion, Non-planar 3D printing.


## Page 4






4

Tekijä  Arkar Nan Htike
Työn nimi  Ei-tasomainen 3D-tulostus termoplastisen materiaalin ekstruusiolla
ja jatkuvalla kuituvahvisteisella 3D-tulostuksella: Algoritminen mallinnus ja G-
koodin luominen
Koulutusohjelma  Konetekniikan maisteriohjelma
Pääaine  Konetekniikka
Vastuuopettaja/valvoja  Prof. Jouni Partanen
Työn ohjaaja(t)  Dr Tuomas Puttonen, Kumar Siddharth, MSc
Yhteistyötaho  ADDLAB
Päivämäärä  31.10.2024  Sivumäärä  59
Kieli  Englanniksi
Tiivistelmä
Opinnäytetyön tavoitteena oli tutkia ei-tasomaisen 3D-tulostuksen ominaisuuksia
kestomuovien materiaalin pursotuksessaja jatkuvatoimisissa kuituvahvisteisissa
3D-tulostimissa.

Materiaalien pursotuksella, ja 3D-tulostuksella yleisesti voidaan saavuttaa monia
erilaisia etuja sen tuoman geometrian vapauden ansiosta. Valmistettujen osien
pinnan laadussa, lmekaanisissa ominaisuuksissa ja mittatarkkuudessa on kuitenkin
edelleen merkittäviä haasteita. Siksi alan kehityksen kannalta on tärkeää selvittää,
voidaanko nämä haasteet ratkaista ei-tasomaisella 3D-tulostuksella.

Tämän opinnäytetyön tavoitteena on kehittää kattava metodologia mukautetun G-
koodin generoimiseksi ei-tasomaiseen työstöradan liikkeeseen 3D-tulostuksessa,
hyödyntäen työkaluja, kuten Python, Rhino 3D ja Grasshopper. Ensimmäinen
tavoite on luoda onnistuneesti G-koodi yhdelle ei-tasomaiselle 3D-mallin
kerrokselle, mitä seuraa prosessin validointi soveltamalla materiaalin pursotusta
käytännön tapaustutkimuksena säärisuojan valmistamiseksi. Toisessa vaiheessa
tutkitaan tämän menetelmän laajentamista komposiittikuitutulostimiin, mikä
mahdollistaa
ei-tasomaisten
tekniikoiden
soveltamisen
kehittyneisiin
materiaaleihin.
Tutkimus
hahmottelee
myös
mahdollisia
tulevaisuuden
suuntaviivoja, mukaan lukien ei-tasotulostus hiilikuidulla ja 5-akselisten FFF-
tulostimien räätälöinti. Yleinen tavoite on tarjota perustavanlaatuinen käsikirja
tulevaa työtä varten ei-tasomaisessa sulatetun filamentin valmistuksessa (FFF),
mikä edistää sen tieteellisten ja teollisten sovellusten ymmärtämistä.

Opinnäytetyön tuloksena saatiin lupaavia tuloksia ei-tasomaisen 3D-tulostuksen
käytöstä ja sillä saavutettavista eduista. Tuloksista huolimatta ei-tasomainen 3D-
tulostus vaatisi vielä lisätutkimusta.


## Page 5

5

Table of contents
Preface and acknowledgements. ..................................................................... 7
Symbols and abbreviations ............................................................................. 8
Symbols ....................................................................................................... 8
Abbreviations .............................................................................................. 8
1
Introduction ............................................................................................ 9
1.1
Background ...................................................................................... 9
1.2
Aim of the thesis.............................................................................. 11
1.3
Research strategy and objectives .................................................... 11
2
Theory & Literature Review ................................................................... 13
2.1
Additive manufacturing .................................................................. 13
2.1.1 Additive manufacturing processes .............................................. 13
2.1.2
Material Extrusion ................................................................... 14
2.1.3
Benefits and limitations of additive manufacturing ............... 15
2.1.4
Additive manufacturing process chain ................................... 15
2.1.5
G-code ...................................................................................... 17
2.2
Non-planar additive manufacturing ...............................................18
2.2.1
The history of non-planar 3D printing .................................... 19
2.2.2
The benefits of non-planar 3D printing .................................. 21
2.2.3
Current research in non-planar FDM .................................... 22
2.2.4
Non-planar 3D printing applications ..................................... 24
2.2.5
The challenges of non-planar 3D printing for research ......... 25
2.2.6
Non-planar extrusion of fibre reinforced structures ............. 27
3
Materials & Methods ............................................................................. 29
3.1
Research objectives ........................................................................ 29
3.2
Build parameter considerations .................................................... 30
3.3
Hardware modifications for non-planar 3D printing .................... 31
3.3.1
Creality CR6-SE printer........................................................... 31
3.3.2
Ultimaker 2+ printer .............................................................. 32
3.3.3
Anisoprint Composer A4 ........................................................ 32
3.3.4
Nonplanar.xyz nozzle extender .............................................. 32
3.4
Strategies to generate non-planar layers ....................................... 33


## Page 6

6

3.4.1
3D modelling of test geometry ............................................... 33
3.4.2
Toolpath generation ............................................................... 34
3.4.3
Development of the continuous nonplanar toolpaths ........... 38
3.4.4
G-code generation ................................................................... 41
3.4.5
FDM printing parameters ...................................................... 45
4
Results & Discussions .............................................................................47
4.1
Nonplanar extrusion of the shin guard model .............................. 47
4.1.1 Extrusion with Slic3r software ................................................... 47
4.1.2
Extrusion with the Grasshopper script .................................. 49
4.2
Nonplanar extrusion of fibre reinforced structures ...................... 50
4.2.1
Anisotropy of composite prints .............................................. 50
4.2.2
Development of multi-axis printing systems .......................... 51
4.2.3
Fibre-matrix adhesion in curved extrusion paths .................. 51
5
Conclusion ............................................................................................. 53
References ..................................................................................................... 56







## Page 7

7

Preface and acknowledgements.
I want to thank Professor Jouni Partanen and my thesis advisor Dr Tuomas
Puttonen for the thesis introduction, good advice and guidance throughout
the thesis writing process. I also would like to extend my regards to the
laboratory manager at ADDLAB Roy Björkstrand, as well as Sunil Siddharth
Kumar for their assistance and mentoring.

Special thanks to my colleagues Wudith, Yuting and Shunyang for making
the office experience fun and motivating.

Otaniemi, Espoo, Finland
18 July 2024
Arkar Nan Htike





## Page 8

8

Symbols and abbreviations
Symbols

X,Y,Z
Axis coordinates
G, M
Tool functions
E
Extrusion rate
h
Layer height
L
Toolpath length
D
Filament diameter
w
Nozzle width

Abbreviations

ABS
Acrylonitrile butadiene styrene
AM
Additive manufacturing
CAD
Computer Aided Design
CCF
Continuous Carbon Fibre
CFRTPC
Continuous fibre-reinforced thermoplastic composites
CNC
Computer Numerical Control
DXF
Drawing Exchange Format
FDM/FFF Fused Deposition Modelling/Fused Filament Fabrication
GUI
Graphical User Interface
HDD
Hard Disk Drive
PA
Polyamide
PEEK
Polyether ether ketone
PETG
Polyethylene terephthalate glycol
PLA
Polylactic acid
STL
stereolithography



## Page 9

9

1 Introduction

1.1 Background

The manufacturing industry is evolving rapidly, driven by fierce competition
and the advent of Industry 4.0 technologies. Organizations are extensively
researching and adopting new cutting-edge methods such as robotics,
artificial intelligence, and advanced materials processing. Among these
innovations, additive manufacturing (AM) stands out for its ability to
produce complex objects with unprecedented design freedom (Clemon et al.,
2013) However, while AM offers significant benefits like reduced material
waste and the ability to create intricate geometries, its implementation
presents challenges such as consistency in part quality and limitations in
production speed (Tofail et al., 2018).

This thesis focuses on a specific area within AM: Fused Deposition Modeling
(FDM), commonly known as 3D printing. An emerging subset of FDM
technology, particularly known as non-planar 3D printing will be the focus of
this thesis. This method promises to overcome some limitations of traditional
layer-by-layer printing by allowing for more organic, curved surfaces and
potentially stronger parts. By investigating non-planar FDM, this research
aims to contribute to the ongoing evolution of manufacturing technologies,
addressing both the opportunities and challenges presented by this
innovative approach.


Figure 1. The Global Revenue for AM products and Services (Campbell et al., 2023)


## Page 10

10


The 2023 Wohlers Report on 3D printing and additive manufacturing states
that additive manufacturing has not remained only at the level of discussion,
but it has been increasing in revenue and market size every year since 2009
as seen in Figure 1 (Campbell et al., 2023). The additive manufacturing global
turnover of products and services has experienced significant growth in
recent years with the growth and the pace seems to be still accelerating.
Between 2009 and 2022, over the 13-year period, the combined global
revenue for additive manufacturing products and services grew more than 9
times with the total revenue reaching up to 18 billion U.S. dollars in 2022.

Despite the widespread adoption, traditional planar additive manufacturing
faces several fundamental limitations that affect part quality and
performance. The layer-by-layer deposition process creates inherent
anisotropic material properties, with parts showing significantly different
mechanical properties parallel and perpendicular to the build direction (X.
Zhang et al., 2023). This layering approach also results in the "stair-stepping
effect," compromising the surface quality especially on curved or inclined
surfaces (C. B. Carolo & Cooper O., 2022). Furthermore, planar printing
often requires extensive support structures for overhang structures, leading
to increased material waste and post-processing times (Armstrong et al.,
2022). In fiber-reinforced composites, the planar extrusion is restricted to
the fiber orientation in the XY plane, preventing optimal fiber placement for
load-bearing applications (Alberti et al., 2018).

Non-planar additive manufacturing offers potential solutions to these
challenges by adding additional unorthodox movements such as movements
in a non-planar direction which could lead to more complex geometries to be
manufactured more efficiently. Since non-planar AM already comes with cost
efficient and time cutting advantages, it would be beneficial process for all
the industry sectors that uses AM as a manufacturing method. However, its
widespread implementation still faces several technical hurdles. The
generation of collision-free  extrusion paths requires complex slicing
algorithms that must consider machine kinematics and tool geometry (T.
Zhang, 2023). Additionally, conventional 3D printers often lack the
necessary hardware capabilities for non-planar movements, and specialized
equipment such as robotic arms and nozzle extenders can be cost-
prohibitive. For fiber-reinforced printing, the complexity increases further as
the system must manage fiber placement along curved paths while
preventing fiber breakage or buckling.






## Page 11

11

1.2 Aim of the thesis

This thesis aims to investigate and advance the field of non-planar 3D
printing, with a particular focus on its application in reinforcement
structures, using a simple single-curved thickened surface as a test geometry.
The shape is similar to the protective shin guard plates used by soccer
players. The research strategy encompasses three primary objectives, each
building upon the last to create a comprehensive exploration of non-planar
fused filament fabrication (FFF) processes.

This thesis will also explore the current development of non-planar
movements in 3D printing, 5-axis FDM printing and the current limitations
and methods of improvement for continuous carbon fibre printers. The main
intention of this thesis is to meticulously conduct and document the research
work of non-planar 3D printing with thermoplastics and composites. This
thesis also aims to act as a solid foundation for the further research and
development in the field of non-planar extrusion and the potential
applications that could come with it.

The structure of the thesis is broken down into five sections and it consists of
an introduction, a literature review session, an experiment part, and a final
summary. Current research papers and industrial applications in non-planar
3D printing will be reviewed in the literature review section. This section will
also cover the theoretical part, in which the reader is given research-related
information on additive manufacturing, non-planar printing, the software,
and programming language used for the subject. The experimental section
introduces the research, experimental work, and the equipment. The actual
research work is started by mapping the current state of industrial research
and determining the development targets for the research work. When the
defined development targets are done, a concept of a 5-axis FDM composite
filament printer will be created. After this, the created non-planar printing
concept and its outputs are used in making two case studies, in each of which
the material is extruded non-planarly; demonstrating the advantages
brought by non-planar FDM compared to traditional cartesian extrusion.

1.3 Research strategy and objectives

The first objective is to develop a methodology for generating custom G-code
for non-planar toolpath movement in 3D printing. This will be achieved using
a combination of software tools including Python, Rhino 3D, Grasshopper,
and relevant plugins. The initial goal is to successfully generate G-code for a
single non-planar layer of the shin guard model.



## Page 12

12

Building on this foundation, the second objective is to demonstrate the
practical application of the generated non-planar toolpath by extruding
plastics to create a shin guard as a case study. This step will serve to validate
the G-code generation process and explore the real-world implications of
non-planar printing techniques.

The third objective extends the research to composite materials, aiming to
adapt the non-planar toolpath generation for use with composite fiber
printers. This expansion of scope allows for an exploration of how non-planar
printing techniques can be applied to more advanced materials and printing
systems.

While the core focus of this thesis is on these three objectives, the research
strategy also considers potential future directions. These include
demonstrating non-planar printing with carbon fiber, customizing plastic
and composite printers for 5-axis FFF printing, and designing custom print
heads and extruders for 5-axis FFF printing. These additional areas, while
beyond the immediate scope of this thesis, represent valuable avenues for
future research.

The overarching goal of this research is to create a comprehensive manual or
template that lays the groundwork for future non-planar FFF process work.
By exploring different materials and equipment within the context of non-
planar printing, this thesis aims to contribute to the broader understanding
of potential scientific and industrial applications of non-planar 3D printing
methods.


## Page 13

13

2 Theory & Literature Review

The purpose of the theory part of this thesis is to create an understanding of
the additive manufacturing process particularly the FDM method. In
addition to this, this theory section discusses the different materials and
extrusion methods as well as the main programming language G-code and
slicers used to achieve non-planar layering in 3D printing. The benefits and
current limitations in non-planar FDM printing are also explored.

In this chapter of the thesis, we also familiarize ourselves with the
prerequisites for non-planar 3D printing, the current and past research
projects, non-planar printing in fibre reinforced composite materials and the
challenges of implementing it in commercial additive manufacturing. The
goal is to explore the readiness of the technology in non-planar 3D printing
as well as to map the issues to be considered to create a successful non-planar
3D printing system for industrial applications. In addition, this thesis work
aims to support the development of an open-source general purpose slicer
that can also slice non-planar layers.

2.1 Additive manufacturing

Additive manufacturing, or more commonly 3D printing, is a manufacturing
method that fabricate parts by creating successive 2-dimensional cross-
sectional layers of the object to be manufactured. (Gao et al., 2015) Although
there are different variations of additive manufacturing, most commonly,
separate layers are made on top of each other and adhered together until the
desired piece is ready.

Before the two-dimensional layer-by-layer manufacturing, the process
begins with a three-dimensional virtual model. This is initially modelled
using 3D modelling software or scanned as a digital CAD (computer-aided
design) file, and then sliced into several layers by preparation software
depending on the manufacturing process.

2.1.1 Additive manufacturing processes

There are seven main processes in additive manufacturing according to the
ISO/ASTM
52900:2021
standard
(International
Organization
for
Standardization, 2021).
• Vat photopolymerization/ Stereolithography
• Powder bed fusion
• Material extrusion
• Material jetting


## Page 14

14

• Binder jetting
• Sheet lamination
• Directed energy deposition.

The seven additive manufacturing processes can be divided into several
subspecies. In this thesis, however, the focus is solely on Material Extrusion
method which is utilized in the 3D printers at ADDLAB.

2.1.2 Material Extrusion

Generally, 3D printers operating on the principle of extruding material are
the most common and most familiar to the public. In this method, a
thermoplastic or thermoforming material is heated to the melting point and
is pushed through a nozzle into a solid two-dimensional layer. After cooling,
the extruded layer adheres to the previous layer. This cycle is repeated until
the desired piece is ready.  This method is usually used for extruding plastics
under the name of Fused Deposition Modelling (FDM) or Fused Filament
Fabrication (FFF). Beyond polymer printing, this technology can be adapted
for metal and ceramic components through a hybrid process where metal or
ceramic particles suspended in a polymer matrix are printed and
subsequently sintered to remove the binding material. For composite and
concrete manufacturing, the process requires specialized equipment with
multiple extruders or co-extrusion capabilities to handle different materials
simultaneously. Only the plastics and composites extrusions will be relevant
for further discussion in this thesis.


Figure 2: FDM/FMM method illustration (W. Li & Leu, 2019)


## Page 15

15


Figure 2 illustrates a material extruding equipment operating with the Fused
Deposition Modelling (FDM) or the Fused Filament Fabrication (FFF)
building method. The material to be produced is typically in the form of a
coiled wire, which is fed using the toothed wheels of the heated extruder,
which melts the filament in extrusion before it solidifies into deposited layers
to form three dimensional products (W. Li & Leu, 2019).

2.1.3 Benefits and limitations of additive manufacturing

Additive manufacturing offers several benefits over traditional subtractive
manufacturing methods that remove materials such as machining. The
fundamentals and working principle of AM offer several advantages. (Zhai et
al., 2014)

• The fabricated materials have near-net-shape meaning the
component can be close in size and shape to the finished product.
• AM offer superior design and geometrical flexibility.
• Some AM methods also allows innovative multi-material fabrication
methods as seen in the Anisoprint filament printer described in this
paper.
• AM also reduces the need for tooling and fixturing compared to
traditional machining methods.
• It also offers shorter cycle time for both the design and manufacturing
processes.
• And most importantly, the efficiency in material, energy, and cost.

Although additive manufacturing brings new benefits and opportunities to
manufacture parts, however, it also has its own limitations. The fabricated
pieces with additive manufacturing are generally rougher in the surface
finish, when comparing to conventional manufacturing processes such as
machining. The surface quality also depends on the orientation of the piece,
the thickness of the extruded layers and the orientation of the material
deposition (Pérez et al., 2020). In fact, this is one of the issues this thesis is
tackling by using the non-planar FDM printing method.

2.1.4 Additive manufacturing process chain

Additive manufacturing technologies are rapidly evolving and being adopted
across various industrial sectors but to put the method in practice, different
kinds of design approaches are being used. Before the start of the
manufacturing process, the pieces to be manufactured are initially generated
as a 3D model using a Computer Aided Design (CAD) software such as


## Page 16

16

SolidWorks, Creo, Mastercam, Rhinoceros, etc. CAD could be used to create
designs of curves and figures in two-dimensional (2D) spaces; or curves,
surfaces, and solids in three-dimensional (3D) spaces (Schoonmaker, 2003).

One way to take advantage of the benefits of additive manufacturing is
through the topology optimization process. Topology optimization is a
computational method that optimizes the material distribution within a
given design space, aiming to meet a set of performance requirements and
constraints (Yang Li and Hsu, 2017). By iteratively analysing the structural
response using finite element analysis, the software determines the optimal
placement of material to achieve the desired mechanical properties, such as
maximum stiffness or minimum weight. Then, the resulting optimized
geometry is translated into a 3D model to be manufactured with additive
techniques.

Separately, the process of converting the 3D model into the layered
instructions required for 3D printing, known as slicing, is a critical step in
additive manufacturing. Computer software, commonly referred to as
"slicers," takes the 3D model and defines the individual 2D layers that will be
built up to create the final part. These slicers also generate advanced printing
parameters such as support structures, infill density, and adhesion settings.


Figure 3. User interface of UltiMaker Cura

Although there are different Slicing programmes according to the 3D printer
manufacturers and manufacturing methods, they all aim to achieve the same
thing, to generate 2-dimensional toolpaths for extruding the materials.
Slicers also provide you with the detailed simulation of the toolpath as well
as amount of material used, time needed for the print and the number of
layers. For the work in this thesis, UltiMaker’s Cura as seen in Figure 3, Open


## Page 17

17

source Slic3r and Anisoprint’s Aura are used as well as Grasshopper and
Rhinocerous 7 for generating custom slicing operations in non-planar
direction.

2.1.5 G-code

The movement of the print bed, the extrusion head as well as the different
settings of the nozzle temperature, cooling fans and the heated bed are
controlled and programmed automatically by a computer, most commonly
through slicers. The slicer converts the 2-dimensional toolpaths with the
detailed inputs on the printer settings into a programming language known
as G-code. G-code, also known as RS-274 stands for Geometry code since the
code essentially functions as a guide for the tools according to the geometry
of the workpieces (Evans et al., 1976).

G-code was initially developed for the intended use in subtractive
manufacturing processes with the introduction of CNC machines but
nowadays, it has also been utilized in additive fabrication using Fused
Filament Fabrication (FFF) processes. Table 1. represents the example G-
code functions. This G-code example is also created using Cura slicer settings
as shown in Figure 3. Simplified, G-code instructs the extruder where they
need to move in relation to a previously defined zero point. The speed of this
movement can also be specified in the G-code. Various G-code flavors differ
slightly from one 3D printer settings to another, but the coordinate-based
operating principle is fundamentally the same in all.

G-code
Functions
;FLAVOR:UltiG-code
;Generated with Cura_SteamEngine
5.2.2
G-code written after the semi-
colon are just comments with no
actual function.
M190 S60
M109 S230
Set the bed temperature to 60°C.
Set the extruder to 230°C.
M82
G92 E0
Set extruder to absolute mode.
Set position without extruding.
G1
F1200
X53.511
Y52.675
E0.0658
Set linear movement.
Set federate to 1200mm/min.
Move 53.511mm on the X axis
52.675mm on the Y axis and
extrude 0.0658mm of material
Table 1. Example G-code of a 3D structure sliced by Cura.





## Page 18

18

2.2 Non-planar additive manufacturing

As mentioned earlier, out of the seven main additive manufacturing
processes, the current focus on implementation of non-planar AM with
plastics is mostly with the material extrusion method. Theoretically,
robocasting also known as Direct Ink Writing can be applied non-planarly,
but the method is limited to a subset of ceramic materials and often focuses
on planar extrusion and small-scale applications (Chauvette et al., 2023). A
subbranch of Directed Energy Deposition called Robotic Wire Arc Additive
Manufacturing (WAAM) have been used more recently to make non-planar
layers for metal pieces (Bhatt et al., 2022). Hence, non-planar techniques
would also be very useful for DED applications with metal additive
manufacturing in addition to plastic material extrusion. However, due to the
time and resources, only Fused Filament Fabrication/ Fused Deposition
Modelling (FFF/FDM) using 3D printers will the focus for this thesis topic.


Figure 4. Illustrations of the 2.5D and non-planar FDM processes(Guidetti et al., 2023)

Merriam-Webster Dictionary defines non-planar as not lying or being able to
be confined within a single plane. Non-planar additive manufacturing means
the material being fabricated is not confined with the Z-axis in contrast to the
traditional fabrication processes. The current material extrusion in 3D
printing is often referred to as 2.5D printing since it is confined to the XY
plane and the incremental extrusion in the Z-axis in the form of sliced 2D


## Page 19

19

layers as seen in Figure 4a. This leads to the print designs always needing a
closed contour and flat layers as well as the flat top and bottom surfaces. In
contrast, non-planar extrusion offers freedom in the Z-axis so that the printer
nozzles do not need to wait for the incrementally sliced layers to deposit the
material, allowing free movement in the Z-direction with little constraints as
seen in Figure 4b.

By utilizing 5-axis printers for non-planar material deposition, FDM printing
can strategically align the nozzle's path with stress flow, thereby improving
the mechanical performance of the printed component (Guidetti et al., 2023).
For non-planar AM in material extrusion, different plastic materials such as
ABS, PA nylon, PEEK, PETG and PLA are already being used in research
projects and independent studies. Composite Filament Fabrication (CFF) is
another subset of material extrusion using composite materials which are
usually produced by mixing the plastic and fiber filaments in a specialized
composite printer such as the Anisoprint Composer A4.

2.2.1 The history of non-planar 3D printing

In contrast to the traditional 3D printer where the orientation of the nozzle
is fixed and only planar motion is applied, systems using multi-axis motion
have caught a lot of attention in recent years. Although the multi-axes milling
has been around for decades in manufacturing, only the XYZ positioning
space is utilized for all current methods of deposition-based 3D printing
(Keating & Oxman, 2013). The setup orientation of a model has significant
influence on the accessibility of its working surfaces (i.e., layers in 3D
printing), which has been proved by the prior research in 5-axis machining
as demonstrated in Figure 5.


Figure 5. Example of a 5-axis CNC machine (Okuma GENOS M560V-5AX) and the five
different axes the piece can be machined in (Song & Ma, 2019)



## Page 20

20

Research in the topic of non-planar 3D printing had been conducted as early
as in 2002 in the form of multi-axis Numeral Control (NC) Machining. The
development of collision-free toolpaths for multi-axis 3D printing directly
tackles a persistent accessibility issue in Computer Numerical Control (CNC)
machining, a challenge that has been the focus of research for more than 20
years. Radzevich & Goodman presented in 2002, a method to compute an
optimal workpiece orientation based on the geometry of the part surface to
be machined, of the machining surface of the tool, and of the degrees of
freedom available on the multi-axis NC machine (Radzevich & Goodman,
2002). Research work as such laid the foundation for the modern-day
programmes for non-planar layer slicing and since then CNC machining
centres have developed from traditional 3-axes system to 4-,5-,6- and 7- axes
machining centres with independent axes.

Non-planar 3D printing grew out of experiments conducted in 2018 by Ahlers
et al. from the University of Hamburg in Germany. The research works paved
way to the slicer programme that is capable of calculating non-planar
toolpath layers for FDM. Firstly, the slicing algorithm automatically
identifies the parts of the object that would benefit from nonplanar slicing.
Then, surfaces are grouped and filtered to prevent collisions of the printhead
with the previously printed structures. The algorithm is also integrated into
the popular slicing programme for normal prints using planar layers, the
Slic3r GUI, providing a 3D-preview of the standard planar and the novel
nonplanar toolpaths as seen in Figure 6 (Ahlers et al., 2019).


Figure 6. Slicer GUI developed by Ahlers et al.



## Page 21

21


2.2.2 The benefits of non-planar 3D printing

The main benefit of non-planar 3D printing is the ability to produce objects
with superior surface quality. Current FDM methods operate solely in X and
Y axes with the platform holding the part moves vertically in Z axis only in
between each layer. In FDM printing, the resulting parts demonstrate an
important property in mechanical anisotropy; meaning they are strong along
the filament's axial direction but significantly weaker perpendicular to these
axes (Ahn et al., 2002). The main advantage of non-planar printing lies in the
reinforcement of fabricated layers in directions not limited to the cartesian
coordinates.


Figure 7. Conventional (left) and non-planar (right) prints of the same design

Visually, non-planar 3D printing fabricates objects with smoother finishes
and fewer visible layer lines which is greatly beneficial for prints with curves,
complex geometries, and organic shapes. With the nonplanar layers, the
extrude material precisely follows the actual surface contour of an object
instead of slicing it into planar layers (Ahlers et al., 2019). With non-planar
3D printing, almost perfect surfaces can be achieved, particularly for smooth
curvatures within a range of tolerated angles which the extruder can access
without obstruction.  Figure 7 presents the comparison between the planar
prints and non-planar prints fabricated from the same printer with the same
material and mostly the same settings.

Non-planar 3D printing also cut print times and waste materials by reducing
the need for support structures necessary in traditional prints for


## Page 22

22

overhanging features. Since the extruder can be modified to travel in Z-axis
to a certain degree by the means of a nozzle extender or a robotic arm, it can
offer more flexibility in reorientating the nozzle in a perpendicular direction
towards the deposition surface layers constantly (X. Li et al., 2024).

2.2.3 Current research in non-planar FDM

Traditional optimization methods for 3D printing such as topology
optimization typically do not consider how the mechanical behaviour
introduced to the printed part by the layer-based AM fabrication process
resulting in pieces with significant difference in mechanical properties
between different directions of the printed parts. This property also known
as anisotropy is being researched and conducted with a method called Stress
Line Additive Manufacturing (SLAM), in which filament is deposited along
paths that follow the strongest stress lines in the part. This method combines
design and optimization to create stronger parts, especially for planar
designs (Tam & Mueller, 2017).


Figure 8. Laser-mounted robot arm scanning a non-planar surface as described in Pan, 2014

Montanuniversität Leoben in Austria did one of the earlier research projects
in the possibility of multi-axis additive manufacturing and non-planar 3D
printing. The research describes a new way of achieving non-planar 3D


## Page 23

23

printing with an industrial robot. A non-planar printing method is presented
in the research using a laser distance sensor mounted on a robot to scan an
arbitrary surface as seen in Figure 8. Levenberg-Marquardt method is then
applied to find a least-mean-square approximation and to reconstruct the
non-planar surface in real-time following the motion of the robot carrying a
3D printer head. A practicable approach consisting of surface scanning and
printing is successfully applied on a real robot during the thesis project (Pan,
2014).

Most recently, Rudd et al. presented in their conference paper for ASME, the
different ways of creating non-planar 3D printing toolpaths. Non-planar
toolpaths for infill within a print were created using an algorithm called the
Differential Line Growth algorithm in which the planar layer is generated by
transforming it into a single continuous toolpath using polygons which are
series of line-segments that connect points in space. This algorithm is
achieved by the researchers with a pseudocode using a combination of
MATLAB and C#. However, this model does not address how the next layers
should be changed to best bond to the current one. (Rudd et al., 2023)

An alternative method of creating non-planar 3D printing toolpaths
developed by Gleadall et al. in Loughborough University introduces an open-
source software that develops G-codes manually. The algorithm developed
called FullControl GCode introduced a unique method of developing non-
planar toolpaths without the need for slicing the 3D models. FullControl
GCode bypasses the traditional steps such as CAD models, STL files and
slicers by let the user design full print procedures manually with
mathematical functions. However, this method requires a higher level of
process expertise to ensure a successful design as most of the toolpaths are
designed manually (Gleadall, 2021).

Since the emergence of the research work in the topic of non-planar 3D
printing is quite recent, there has only been very few attempts in
commercializing the potential advantages and unique properties of non-
planar 3D printing. One such case is from the Canadian manufacturing
company nonplanar.xyz that produces the elongated nozzles as seen in
Figure 9. The use of extended nozzles enables non-planar printing for regular
3D printers as well as collaborating with several programmers and designers
in selling custom G-codes for hobbyists and researchers.




## Page 24

24


Figure 9. Printer nozzles produced by nonplanar.xyz for non-planar 3D printing


2.2.4 Non-planar 3D printing applications

Being able to print with a higher degree of freedom than 2.5 axes has been a
goal of a number of startups in the 3D printing industry. Non-planar additive
manufacturing allows to manufacture curved parts with a smoother surface
and better mechanical properties than the traditional cartesian additive
manufacturing (Pierre et al., 2024). Many of the robotic manufacturers such
as Kuka, BLOOM Robotics, Yaskawa, etc. have developed their own versions
of extruding robot platforms that allow 5- or 6-axis fabrication processes, but
the slicing of 3D models and G-code generation still present as major pain
points in the industry  (Fortunato et al., 2023).

Although, non-planar FDM has been used in the industry with robotic arms
as seen in Figure 10, a regular printer that is capable of printing in non-planar
is yet to be developed. There are available hardware configurations for the
current FDM printers to be modified into non-planar printers but to achieve
5-axis or even 4-axis without the use of a robotic arm still present as a
challenging task (Hong et al., 2023).



## Page 25

25


Figure 10: Non-planar 3D printing using Yaskawa Motoman GP12 robotic arm

Since non-planar AM already comes with cost efficient and time cutting
advantages, it would be beneficial process for all the industry sectors that
uses AM as a manufacturing method. In aerospace and automotive sectors in
particular, non-planar AM can potentially help produce intricate parts with
improved
strength-to-weight
ratio
including
optimized
structural
components, customized interior features, and aerodynamic exterior fairings
such as aircraft fuselages, aerofoil models for wings and load bearing
mechanical brackets. For example, one research in aerospace application
described the manufacturing of a multi-functional non-planar sandwich
panel for aircraft casing by utilising a 6-degree of freedom (6-DOF) robotic
platform in a custom heating enclosure, using 30 wt% carbon-reinforced
polyetheretherketone (PEEK) (Pierre et al., 2024a). Other applicable sectors
may include healthcare, construction, electronics, and energy industries.

2.2.5 The challenges of non-planar 3D printing for research

For the implementation of the research work, a mapping of the challenges of
non-planar additive manufacturing must be carried out. The mapping of the
challenges was carried out based on the theory part of the thesis and the
capability of hardware available at ADDLAB in Aalto University as well as the
experience and skills of the author. As non-planar 3D printing is a relatively
recent branch of additive manufacturing, it presents the challenges present
in traditional 3D printing as well as many obstacles that come with
developing custom G-codes for non-planar extrusion. The goal for the
mapping of the challenges was to outline the most significant challenges and
development targets.



## Page 26

26

Development of slicing programme: Slicing layers from the files with
the stereolithography format (.stl) is a necessary and crucial part before the
start of the non-planar 3D printing process. Although most 3D printers
provide slicers for slicing planar 2D layers, there is still a lack of reliable slicer
that slices non-planar layers. Challenges in slicing occur mostly in the surface
quality of the prints. In particular, the “staircase effect” is described as a step-
like pattern visible on the surface of a 3D-printed object caused by the
layering process used in FDM printing, where the edges of each layer can be
slightly visible on the object's surface (Fortunato et al., 2023). Therefore, it
is important to carefully simulate the toolpaths from the slicers before
printing.

Positioning of prints: The position of the part to be printed play a vital
role in non-planar 3D printing. Inconsistencies in print coordinates related
to the print bed could lead to failure in printing and at worst damage to the
print head and the printer. The support and the non-planar layer print need
to be positioned in the exact spot and the coordinates in the G-codes need to
be as accurately possible to reflect that. One solution for this challenge is by
making a custom print bed for the non-planar layer to be printed as
demonstrated by the Ambrosio team during the Product Development
Program 2024 Gala at Aalto Design Factory. As seen in Figure 11. Precise
positioning of non-planar prints being achieved with a custom print bedFigure 11, an
actual physical alignment feature using the precise machined piece of
aluminium adhered to the print bed is used to achieve accurate positioning
of the non-planar prints. The use of zero-point clamping systems, machine
vision and artificial intelligence algorithms could also be developed to solve
this challenge.

Toolpaths for extrusion: Toolpath generation is a time-consuming
process since the G-codes for toolpaths need to be carefully reviewed and
simulated. A mistake or inconsistency in the G-code can lead to prints failing
and result in serious damage to the printers. Important factors in generating
extrusion toolpaths with full collision avoidance include the algorithmic
modelling of G-codes, the orientation of the printed parts, the extruder
geometry as well as the hardware limitations if there are any robotic arms or
extended nozzles involved (Kipping et al., 2024).



## Page 27

27


Figure 11. Precise positioning of non-planar prints being achieved with a custom print bed

Since non-planar 3D printing is still quite a new topic, many of the potential
problems haven’t even been mapped yet. Slicing in 3-dimensions require
complex algorithms and 3D printing knowhow to safely execute non-planar
prints. The multiple variables of the non-planar 3D printing process form the
need for predicting the variables that occur during the fabrication process.

2.2.6 Non-planar extrusion of fibre reinforced structures

One important part of this thesis is the investigation for the practicality of
extruding non-planar structures with continuous carbon fibre using a
composite 3D printer. Although plenty of research work have been conducted
in continuous fibre composites, the subject of non-planar fabrication of
sandwiched composite structures is relatively new and sparse due to the
necessary equipment and higher complexity compared to the traditional
thermoplastic extrusions. The biggest advantage of continuous fibre
composites over traditional thermoplastics resins such as ABS, PLA, etc. is
their outstanding mechanical properties. Continuous fiber-reinforced
composites achieve the best combination of strength and stiffness by
combining the high-performance properties of carbon fibers with the
versatility of polymer resins, outperforming other reinforcement methods
(Matsuzaki et al., 2016).

For continuous fibre 3D printing in a composite printer, at least two different
materials are extruded together, one material acts as a matrix to maintain the


## Page 28

28

structure and the other to provide reinforcement. Usually, a thermoplastic
filament acts as a matrix while carbon fibres or glass fibres are used as
reinforcement. Composite sandwich panels fabricated using material
extrusion have been used for light aircrafts due to their incredible strength to
weight ratio. Pierre et al., (2024) demonstrated the capabilities of 30 wt%
carbon-reinforced polyetheretherketone (PEEK) as a multi-functional non-
planar sandwich panel for aircraft using a 6-degree of freedom robotic
platform. Three-point bending tests revealed that non-planar deposition, by
improving layer alignment throughout the specimen, increased effective
stiffness by 28% compared to conventional planar printing methods (Pierre
et al., 2024b).

In contrast to the thermoplastics extrusion where the printers can be
customized for non-planar printing, in fabrication of fibre reinforced
structures customizing the printer such as adding nozzle extenders and
removing hanging structures can be difficult due to the dual nozzle nature of
the printer and the increased intricacies in extruding as well as the more
expensive printer and maintenance cost of the composite printers compared
to the thermoplastic printers. Thus, robot arms are more commonly used in
non-planar extrusion of fibre reinforced structures. One current ongoing
project is from the printer manufacturer Anisoprint itself utilizing a Kuka
industrial robot arm to achieve 6-axis non-planar printing of reinforced
carbon fibre as seen in Figure 12.

Figure 12. Non-planar printing of reinforced carbon fibre with PROM PT Anisoprint 6-axis
robotic arm



## Page 29

29

3 Materials & Methods

This chapter outlines the experiments and methodology used in this thesis.
This article aims to validate and depict the feasibility of non-planar additive
manufacturing with the use of 3D printers by modelling and simulating the
non-planar toolpaths. A mixed-approach method was used to address the
objective of this thesis, which includes both simulative and practical
methods. A case study in the form of a football shin guard or knee guard was
conducted to aid the process of problem identification, and data
visualization. And the detailed process of model simulation and physical
extrusion is explained and presented.

This thesis will explore a use case for non-planar 3D printing with PLA and
PA filaments as well as a use case for non-planar extrusion of fiber reinforced
structures with Continuous Carbon Fiber (CCF) filaments reinforced with
PETG. The cases will be compared with the similarities and differences of the
properties being discussed.

3.1 Research objectives

The main goal of the research experiments is to create a G-code in a
continuous
toolpath
demonstrating
non-planar
3D
printing
for
reinforcement with a case study in a football shin guard. The focus here is in
non-planar 3D printing as well as non-planar slicing and toolpath generation
using the software Python, Rhino 3D, Grasshopper, and its plugins. The aim
of the thesis is to create a manual/template and lay basic groundwork for
future non-planar fused filament fabrication process work exploring
different materials and equipment. This thesis also aims to explore on the
realisation of potential scientific and industrial applications of the non-
planar 3D printing method.

The first objective of the thesis is to generate a custom G-code for the non-
planar toolpath movement in 3D printing using the modelling software
Rhino and Grasshopper. For this objective, the goal is to generate the G-code
of the nonplanar toolpath for a singular layer of the shin guard. The second
objective is to demonstrate the non-planar toolpath movement by extruding
plastics in the form of a football shin guard. The third objective is to generate
G-code for the same non-planar toolpath for the composite fibre printer.
Additional objectives such as demonstrating non-planar printing with
carbon fibre by modifying the composite printer, customizing the plastic and
composite printers for 5-axis FDM printing as well as designing and
producing custom print heads and extruders for 5-axis FDM printing could
be achievable milestones for the future thesis topics.


## Page 30

30

3.2 Build parameter considerations

For the non-planar extrusion, the Z-axis movement of the printer was
considered for the extruder movements along the non-planar toolpaths.
Creality CR6 for example has a fixed hot bed with an extruder moving up and
down and Z-direction while the Ultimaker 2+ move the hot bed along the Z-
axis with the extruder only moving across the XY-plane. This difference in
movement behaviour however didn’t have significant effects as hypothesized
over the non-planar printing of the football shin guards.

In addition, a clearance angle needed to be calculated, and the 3D printer
extruders were modified accordingly to eliminate the clashing of the extruded
prints with the nozzle parts. As seen in Figure 13, the clearance angle for an
Ultimaker 2+ printer would be either (a) an 8◦ angle and a 50 mm maximum
height taking the whole printhead into account or (b) a 45◦ angle and 7.5 mm
maximum height. This information is necessary to ensure accidental clashes
with the prints and the extruder don’t occur.


Figure 13. The angles and height clearances of the extruder of Ultimaker 2+ printer

The entire nozzle cage for the Creality CR6-SE printer also needed removed
to ensure the clearance of the extruder to the print. As seen in Figure 14, the
cooling fan, the nozzle cage and the heating block was removed and tucked
away to accommodate the minimum clearance height and angle for the
extruder. In addition, the nozzle extender from nonplanar.xyz as mentioned
earlier was purchased to be connected to the Creality printer.

A non-planar layer is extruded on top of a base support structure printed
planarly. A big consideration in this thesis is the relative position between
the base support structure and the non-planar layer on top since any
misalignment in the coordinates between the two structures could make the
printer nozzle crash into the support structure causing it to move in resulting
in print failure.


## Page 31

31


Figure 14. The extruder of CR6 (left) and with nozzle cage removed (right)

3.3 Hardware modifications for non-planar 3D printing

The hardware required for this thesis is provided by ADDLAB. Aalto
University Digital Design Laboratory (ADDLAB) is a research organization
initiated by the Aalto University's School of Engineering combined with
School of Arts, Design and Architecture. The printers for plastic extrusion,
composite extrusion as well as a working station to operate design and
programming software were all sponsored by ADDLAB and Aalto University
Department of Mechanical Engineering.


Figure 15. 3D printers used in this thesis (Left to right: Ultimaker 2+, Creality CR6-SE,
Anisoprint Composer A4)

3.3.1 Creality CR6-SE printer

Creality CR6-SE seen in Figure 15 (middle) is a 3D printer used for the plastic
extrusion part of the experiments with the PLA filament. It is a lightweight,
cheap and easily customizable printer that is ideal for the modifications
required for non-planar 3D printing. The Creality printer also has modular
extrusion head which means the cooling fan, heat sink, Teflon cube and heat


## Page 32

32

block can easily be removed or tucked away to avoid clashing with the printed
material in the non-planar printing applications. The Creality printer is also
the only printer that can be outfitted with the nozzle extender since they have
compatible nozzle diameters.

3.3.2 Ultimaker 2+ printer

The Ultimaker 2+ printer was used to get consistent results due to the stutter
movements in Creality printer because of the potential data processing issue
with the SD card. The material for Ultimaker 2+ is also PLA but the extruder
and nozzle were not customized or fitted with an extender due to a more
complicated extruder mechanism. In addition, compatible filament diameter
for Ultimaker 2+ is 2.85mm but the nozzle extenders only allow filaments up
to 1.75mm which left installing an extender on the Ultimaker machines
impossible.

3.3.3 Anisoprint Composer A4

The Anisoprint Composer A4 3D printer is used as a reference for the
simulation of nonplanar toolpaths for composite materials printing.
Anisoprint offers the Composite Fiber Coextrusion technology with its dual
nozzle system, each one assigned for plastics and carbon fibre. The dual
nozzle system, the rarity of spare parts at the time of research and it being
the only composite printer in the lab also being used for other research
projects mean Anisoprint Composer could not be modified for the nonplanar
printing purposes for this thesis. However, a toolpath for it is simulated in
Grasshopper and described in the later parts of this paper.

3.3.4 Nonplanar.xyz nozzle extender

A singular steel nozzle extender of 0.4mm diameter was purchased from
nonplanar.xyz for 30$ for the nonplanar printing tests and installed in
Creality printer as seen in Figure 16. However, the nozzle extender ended up
not being used for this thesis due to the delays in shipping and the problems
encountered when removing the original nozzle from the Creality printer. In
addition, it turned out not to be compatible with any of the other printers
from ADDLAB due to the different filament diameter tolerances leaving it out
of the picture for this thesis.



## Page 33

33


Figure 16. Nozzle extender and insulation sleeve installed on the Creality CR6-SEprinter

3.4 Strategies to generate non-planar layers

The strategies to generate non-player layers were achieved mainly with the
simulation software Grasshopper, modelling tool Rhinoceros and
SolidWorks. The bulk of the experimental work was on the software side by
using slicer programmes such as Cura and Aura to simulate nonplanar
tootpaths Several plugins from Grasshopper were also used including
Axolotl, Chimpanzee, Droid, Helix, Intralattice, Parakeet, Pufferfish,
Silkworm and Wombat. NCnetic is also used as a plugin with Notepad++ to
view G-code toolpath simulations. In addition, an Ubuntu Linux sever was
used to access the nonplanar slicer developed by Ahlers. NanoG-code addon
from nanoCAD software was also used to simulate nonplanar printing
toolpaths for Anisoprint G-codes. All the software mentioned will be stated
in detail in the following sections.

3.4.1 3D modelling of test geometry

Football shin guard is chosen as a use case model for nonplanar printing in
this thesis due to its shape parabolic shape with shallow depth, ideal for low
threshold nonplanar printing experiments. In addition, a solid base shape
was also modelled for supporting the overhang structures. The shape was
modelled firstly in SolidWorks in the .stl (stereolithography) format. This
format tessellates the shape into a set of triangles and simplifies the part
geometry by reducing it to its most basic components.  The advantage of the


## Page 34

34

STL format is that most CAD systems support it including the programmes
used in 3D printing such as the Cura slicer and Rhino. However, the
disadvantage is that the part loses some resolution, because only triangles,
and not true arcs, splines, etc., now represent the geometry (Wright, 2001).


Figure 17. CAD drawing of the shin guard (left) and base structure (right)

As seen in Figure 17 the dimensions of the shin guard are 120mm by 120mm
with a depth of 15mm at the maximus. These dimensions are decided based
on the size of the printer hotbed and to optimize the printing process by using
as little material as possible. A similar shin guard surface was also generated
in Rhino using Grasshopper in order to have everything in the same system.
Three points are defined in Grasshopper with coordinates ensuring it
maintains 120mm length and 15mm peak. The points are connected by the
Arc component and the arc is extruded for 120 mm along the Y-axis, using
the Extr component. The resulting surface and the script used to generate
the shape can be observed in the Figure 18 below.


Figure 18. Shin guard surface generated in Rhino and the related Grasshopper script

3.4.2 Toolpath generation

Rhinoceros, a CAD software, is utilized in visualizing nonplanar toolpaths
created by using its visual scripting add-on, Grasshopper. This software is
based on the NURBS (Non-Uniform Rational B-Splines) mathematical
model, which enables precise representations of curves and freeform
surfaces in computer graphics. Unlike the polygon mesh-based applications


## Page 35

35

such as SolidWorks, Blender, and Autodesk, NURBS allows for accurate
descriptions of a wide range of geometries, from simple 2D shapes to
intricate 3D organic forms. Due to their precision and flexibility, NURBS
models are suitable for various applications, including illustration,
animation, and manufacturing.

Rhinoceros version 7 is used in this thesis since it is easily accessible through
Aalto University virtual computer classrooms and its compatibility with the
Grasshopper add-on version 1.0.0007 and most of its plugins. Grasshopper
is a visual scripting tool that can write generative algorithms for parametric
modelling.  In this thesis, Grasshopper is the programme mainly responsible
for generating the nonplanar toolpaths. Grasshopper comes with some build
in plugins and some independent ones. Grasshopper plugins are files in .gha
(Grasshopper Assembly) format that are created by the user community and
3rd party developers intended to expand the functionalities and features of
Grasshopper. The plugins used for this thesis are listed below along with their
features.

Silkworm2.gha: Silkworm is a plugin that translates Grasshopper and
Rhino geometry into G-code for 3D printing. Silkworm allows for intuitive
and complete G-code manipulation, enabling users to create unique material
properties through non-solid geometry and digital crafting techniques. For
this thesis, Silkworm plugin is the main tool that allows compile outputs from
other plugins and outputs the toolpath in the G-code form. As seen in Figure
19 for example, the Silkworm component blocks take the nonplanar
toolpath lines generated using the Pufferfish plugin to generate the G-code
movements as well as the display interface to view the simulation.


Figure 19. Screenshot of part of the Grasshopper script where Silkworm plugin is used



## Page 36

36

Pufferfish3-0.gha: Pufferfish is a Grasshopper plugin that focuses on
Tweens, Blends, Morphs, Averages, Transformations, & Interpolations.
Pufferfish mainly uses parameters and factors as inputs for more custom
control over operations like tweens and grids as opposed to Grasshopper’s
usual division count inputs. For this thesis, Pufferfish component
ParamSrfIso (Parameter Surface Isocurve) is used to generate a basic
isocurve on the shin guard surface generated by Grasshopper. The curve is
then exploded into smaller segments and points on the curve to create
toolpath lines for Silkworm as seen in Figure 20 below.


Figure 20. Surface curve segments generated by Pufferfish to create nonplanar toolpaths

Droid_1.gha: Droid is another Grasshopper plugin library add-on,
specifically made for 3D printing with control over model Slicing, Custom
paths and G-code generation. For this thesis, Droid is used as a slicer for
converting 3D models into toolpaths and generating G-codes since it can do
conventional slicing features such as infill, shell thickness and caps, entirely
within the Rhino and Grasshopper environment making it easier to slice 3D
models without launching additional programs. The Cartesian G-code
Generator from Droid was used in the earlier part of the experimental
process to navigate the slicing behaviours and nonplanar toolpath
compatibilities of different 3D structures. As seen in Figure 21, the Droid G-
code generator take .stl files as input and generate .gcode files as output
while offering standard 3D printer slicer settings such as Infill percent, nozzle
width, etc.



## Page 37

37


Figure 21. Droid´s Cartesian G-code Generator interface in Grasshopper

Wombat131.gha: Wombat is a plugin that offers components generally
aimed to improve and streamline the Grasshopper modelling processes
particularly in data lists, files, folders as well as the surface and mesh
geometries. The component block Cull Ends for example is used in the
script to remove and trim the branches from the continuous toolpaths.

Intralattice.gha: Intralattice is a plug-in that can generate solid lattice
structures. This plugin was also used earlier in the experimental process of
this thesis for generating infill patters of the solid support structures.
Intralattice offers 10 different infill patterns that can manipulate the extruder
movement of the 3D printer. One of the honeycomb patterns for example can
be seen below in Figure 22.


Figure 22. Bottom and front view of the infill pattern generated with Intralattice plugin



## Page 38

38

Pancake.gha: Pancake is a plugin used to auto save the Grasshopper script
in case of unexpected programme failures. One of the Pancake components
TrueButton is also utilized to easily export the G-code file to local computer
and cloud.

3.4.3 Development of the continuous nonplanar toolpaths

For seamless extrusion of materials from the 3D printer, the nonplanar shin
guard surface is broken down into points on the surface and a continuous
path is created through the points. As mentioned in section 4.4.1, a shin
guard surface shape was created in Grasshopper using the Arc and Extr
component blocks.

Generation of nonplanar segments with connected ends: The shin
guard surface is broken down into individual paths with the help of
ParamSrfIso component from Pufferfish. The number of paths in this case
is limited to under 100 to reduce the data points and the use of unnecessary
computing power. As seen in Figure 23, the Toggle component controls the
direction of the paths and is set to False, meaning the direction of the paths
is along the curve and not across the curve.


Figure 23. Grasshopper script for generating nonplanar curve sections with connected ends

The resulting output from ParamSrfIso component is 41 arc-like curves
along the tangent. The individual curves are then exploded into smaller
segments and vertices using the Explode component resulting in 41 curve
segments as well as 2 points on each end of the segments adding to 82
vertices. The vertices matrix is flipped using Flip component to align the
points across the curve. The points are then shifted by 1 place in the matrix
using the Shift component so that they can be connected with a line using the
Ln block. Finally, the exploded nonplanar segments along the curve and the
planar line through the vertices across the curve is unionized with a Join
component. as seen in Figure 24, this process created bridges through
vertices between the isolated individual nonplanar segments making the
toolpath continuous without the need to stop between individual segments.



## Page 39

39


Figure 24. Resulting visual of the Grasshopper script from fig.22

Breaking down nonplanar curves into data points: The strategy to
generate continuous paths is by connecting the points along the curve
segments generated in the previous section. The 41 arc-like curves from
ParamSrfIso block are broken down into individual points on the
segments using the Divide component as seen in Figure 25. The number of
points on each arc is limited to 50 which is a good amount to have enough
data points for extrusion and not too many data points so that the
programme takes a longer time to process the data. The resulting output is a
data list of 2091 points covering the whole surface of the shin guard structure
with 51 points on each of the 41 arcs.


Figure 25. Grasshopper script for breaking down the curve segments (left) and the
resulting data points (right)

Connecting the data points into a continuous path: The field of points
is connected into a continuous path with the Grasshopper script shown in
Figure 26. An infill pattern of curvy lines looping along the arcs was selected
due to its simplicity to get the points connected. In contrast, infill patterns of
grid, gyroid or honeycomb would require more Grasshopper component
blocks to construct the pattern. In addition, the support provided by the infill
pattern is not necessary in this case since the goal is to print only one layer to
demonstrate the nonplanar movements.



## Page 40

40


Figure 26. Grasshopper script in creating a continuous looping path

For the continuous toolpath, the data points from individual arc segments
needed to be bridged alternatively going back and forth. The 2091 points are
grouped backed into their own arc segments with the TStat component
resulting back in 41 arcs. The 41 arcs are then broken down into two groups
with the Dispatch block. The two groups are sorted alternatively so that no
two neighbouring arcs are in the same branch.

The Branch components retrieve the data points from the corresponding
arcs meaning BranchA has all the even number arcs with their points and
BranchB with the odds. The list order of BranchB is reversed with the Rev
block and Merge component is used to combine the reverse list with the data
from BranchA. This results in a collection of data points on even numbered
arcs with regular direction neighbouring with odd numbered arcs in the
reverse direction. A similar procedure of shifting the list and connecting the
points is performed using the Shift and Ln components resulting in a single
continuous toolpath.

The Cull i component is used to get rid of the unnecessary line connecting
the very first and last points across the surface as seen in Figure 27. In this
case, the numbering system in Grasshopper starts from 0 instead of 1
resulting in 41 arcs even when it was inputted 40 as seen in the previous
section. This numbering issue and the trimming of the unnecessary index is
automated using the equation:

𝑅= {(𝑥+ 1) ∗(𝑦+ 1)} −1

Eq. (1)

where R is the resulting index number
            X is the number of arc segments, and
            Y is the number of points on each segment


## Page 41

41



Figure 27. Rhino visualization of the continuous path in bird eye views (left) and isometric
views (right) with the culled index (top) and final toolpath (bottom)

Filleting the continuous toolpath: The resulting continuous toolpath is
filleted into round edges to smoothen the extrusion process as seen in Figure
28. The vertices of the toolpath visualized above were separated using the
Cull Ends component from Wombat and connected with the PLine block
to construct a polyline. The line is then smoothened by the Fillet
component with the maximum fillet radius of 12 units and projected back
into the 3D space with the Project component.


Figure 28. Grasshopper script for filleting the toolpath corners (left) and the final resulting
toolpath

3.4.4 G-code generation

The required G-code for the simulated toolpath to use with the Creality
printer was mainly generated from the Grasshopper plugin Silkworm
components. On the other hand, the G-code to use with Anisoprint for
composite printing was specifically generated by the nanoCAD plugin
NanoG-code.


## Page 42

42


G-code Generation with Silkworm: The Grasshopper plugin Silkworm
allows the transformation the generated nonplanar toolpath into G-code that
defines the tool movements and extrusions in the 3D printer. The Silkworm
component Extrusion can translate the toolpaths into the extruder
movements. However, in contrast to the plugin description, Silkworm
compiler doesn’t automatically calculate accurate extrusion rate units (E
values) that determines how much material is to be extruded from the nozzle
at each coordinate.

As mentioned in the earlier section, G-code commands for additive
manufacturing usually consist of three components. The G, M or F
commands to control the tool behaviours, the X, Y, and Z commands for tool
movements and the E commands for extrusion. The compiler Silkworm
component outputs accurate tool control and movement units but the E
values generated are list of identical numbers. This error in extrusion rate
leads to the materials not extruding properly or not extruding at all when the
inputted G-code is processed through the 3D printer.

The Extrusion units are thus manually calculated using the equation:

                                             𝐸=
[ℎ2𝜋+4ℎ(𝑤−ℎ)]𝐿𝑀
𝐷2𝜋

             Eq. (2)

where E is the extrusion rate
            h is the layer height
            M is the flow multiplier
            L is the length of the toolpath
            w is the nozzle width, and
            D is the filament diameter. (Kim et al., 2022)

The length of the toolpath (L) is obtained from Grasshopper using the Len
component. The parameters used for extrusion will be discussed in detail in
the following section 3.4.5. The resulting extrusion rate (E) units need to be
added iteratively for the proper material extrusion from the printer nozzle.
The numbers are added, and the outcome of each addition is iteratively added
back to the E value again using the Ma mass addition component. This results
in 2090 iterative values of the extrusion rate for the filament to be deposited
at each of the 2090 different coordinates.



## Page 43

43


Figure 29. Grasshopper script for generating G-code with the panel displaying the G-code

Since the Silkworm plugin only compile the G-code script for movement, the
calculated E values needed to be combined with the G-code script from
Silkworm for the correct G-code that allows material extrusion. The wrong E
values from the Silkworm G-code are diverged into a different set of arrays
with Split block and the wrong E values are removed using the Item
component.

On the other hand, two additional extrusion rates with values of 0 are created
and added to the first 2 lines of the G-code using the Ins (Insert Items)
component. These first 2 lines are to accommodate the commands for setting
the position G92 E0 and setting the feed rate G1 F3000. All the characters
of the G-code are then combined with the Concat (Concatenate) component
and pasted into a panel as seen above in Figure 29, which automatically saves
the script to OneDrive in the .G-code format.

G-code Generation with NanoG-code: The nanoCAD plugin NanoG-
code has the feature to translate the 2D mapping points created from
Grasshopper into a 3D printable toolpath for the dual nozzle Anisoprint
composite printer. The main file format of nanCAD is .dwg format for
engineering drawings but .dxf format is used in this thesis since it allows easy
exchange between 2D and 3D formats. In contrast to Rhinoceros, nanoCAD
is specialized in 2D modelling and drawing and it adjusts the corner
compensation necessary for the correct toolpath in the material extrusion of
the carbon fibre.

The fibres being extruded have a turning radius at the corners due to the
tension of the continuous fibers themselves. Thus, the Continuous fibre-
reinforced thermoplastic composites (CFRTPC) cannot pass a smaller turn
than the radius, otherwise, the brittle continuous fibres will break. Even if
the fibre breakage does not occur at the corners, the actual printed track will
leave a void area error from the design track as seen in Figure 30 (Wang et
al., 2022). The NanoGCode plugin autocorrect this inaccuracy in toolpaths
misalignment without the need to actively account for the extrusion toolpath
at the corners.


## Page 44

44

Figure 30. Zoomed in picture of printed CFRTPC material showing the difference between
the actual tracks (yellow) and the theoretical tracks (white) with different corner angles

This .dxf file is generated in Grasshopper with the script seen in Figure 31
obtained from a Grasshopper forum post. Custom scripts in the C# language
were written for the components Bake and Export used to convert the 3D
toolpaths into the 2D DXF format. Since the experiments for this thesis only
use one layer for nonplanar printing, the toolpath can also be directly saved
to .dxf without defining additional layers.


Figure 31. Grasshopper script of the DXF generator

The generated .dxf file is opened in nanoCAD and transformed into G-code
for Anisoprint using the NanoGCode plugin. The generated G-code is
visualized with the Notepad++ plugin NCnetic as seen in Figure 32.



## Page 45

45


Figure 32. Interface of nanoCAD showing 2D toolpaths (top) and G-code visualized with
Notepad++ (bottom)

3.4.5 FDM printing parameters

The same printing parameters are used for the two printers for the
consistency of the results in the experiments. The print beds are set to 60°C
and the extruder temperature is set to 230°C. Typical 3D printing parameters
such as the infill percentage and pattern are not relevant for these
experiments since the layer is only one level. The print speed is set to 50% of
the feed rate from the Creality interface to observe the nonplanar printing
and to prevent any unnecessary damages to the printer nozzle. However, the


## Page 46

46

two printers used in the experiments have slightly different properties most
notably in the diameter of the filament used.

The diameter of the PLA filament used in Creality (D) is 1.75 mm and it is
used to calculate the area of the extruder inlet. The nozzle diameter (w) is
used to calculate the area of the extruder outlet and for Creality CR6-SE, it is
0.4 mm. A default layer height (h) value of 0.2 mm is used since the
experiments in this thesis are only for a singular layer. The values for layer
height and nozzle diameter are directly proportional to E values, Thus, more
layers and wider nozzles means more materials is extruded at each
coordinate leading to a decrease the printing length. Furthermore, a value of
1 is used for flow modifier in this Grasshopper script. A larger flow modifier
(M) allows the extruded filament material to withstand higher pressure
leading to stronger adhesiveness between the layers. (Koch et al., 2017)



## Page 47

47

4 Results & Discussions

This chapter outlines the outcomes of the experiments with further
discussions regarding the objectives of the study and the potential future
research work that could be done. Recommendations based on the
theoretical findings and the experimental observations are highlighted for
the significance of future research of the nonplanar FDM projects.

4.1 Nonplanar extrusion of the shin guard model

4.1.1 Extrusion with Slic3r software

The first few experiments of nonplanar extrusion were conducted with the
opensource Slic3r extension developed by Ahlers, et. al from the University
of Hamburg. This software can only be run on Linux and only allows the
deposition of a few nonplanar layers on top of the regular layers-by-layers
extrusion. This slicer is optimal for simple geometric structures such as the
shin guard in this case. The advantage is this slicer allows the extrusion of
planar infill material with the top nonplanar layers, eliminating the need to
develop a different solid model for the infill. As seen in Figure 33, the shin
guard structure is sliced appropriately with the planar layers acting as infill
supporting the non-planar layers on top of the structure.


Figure 33. Slic3r interface of the shin guard structure

On the other hand, slic3r face difficulties in slicing nonplanar layers with
complex geometries such as the case when the top layers are separate. As an
example, the Octopus 3D model is a complex 3D model with a unique


## Page 48

48

topographic geometry. As shown in Figure 34 only the head of the Octopus
would be possible for nonplanar printing since the tentacles are so low in the
relative vertical position compared to the maximum vertical height  of the
head.


Figure 34: Slic3r interface showing the height difference between the head and the
tentacles of the Octopus model

In addition, the prints from Slic3r extruded by the Creality printer result in
rough surface textures due to the stutter movements from the extruder.
When traveling in nonplanar movements, the extruder would abruptly stop
and start, leading to delays in movements and material deposition. Although
it is unclear where exactly this behavior comes from, one strong speculation
is that the processing rate of the removable disk (SD card) is not fast enough
to process a large data number of coordinate points at relatively high speeds.
Since non-planar movements require a lot of interpolated points with small
step sizes, the stuttering occurs more frequently compared to planar
extrusions. However, this does not really affect the printer during the
standard movements performing planar extrusions and could also be
hypothesized to be an issue with the slicer or the G-code. For future research
work, one way to bypass this issue could be by using a system like OctoPrint
which allows user to schedule prints and remotely control the printer using
their web interface. OctoPrint can relay G-code from a removable disk such
as a HDD or SSD and send it to the printer line by line, this means choosing
"upload locally" instead of saving G-code to the printer's SD card. (Ankerhold
& Tjepkema, 2024)



## Page 49

49

4.1.2 Extrusion with the Grasshopper script

The first few G-code scripts generated from Grasshopper did not extrude
material due to the error in E values. The finalized G-codes worked perfectly
as expected in the experiments. This method is ideal for the use case since it
allows complete freedom in modelling a single layer of nonplanar toolpath
for the shin guard structure. Grasshopper also allows the complete
customization for slicing using different plugins. However, there are also a
few disadvantages.


Figure 35: Print failure due to difference in relative positioning

Since the Grasshopper script only generate the G-code for extruding a single
nonplanar layer, a base for the print to take place needs to be printed. Most
often, the problems occur form the relative positioning between the base
structures and the extruded nonplanar layer. For example, the coordinates of
the base structure need to be within a certain tolerance relative to the
coordinates of the nonplanar toolpath. In addition, the base infill needs to be
firmly adhered to the build plate using tapes, glues or the adhesive spray to
prevent the base for moving away from the targeted coordinates. This
difference in relative position or the movement of the base could lead to print
failures resulting in mismatched toolpaths as seen in Figure 35.



## Page 50

50


Figure 36: Print failure in Ultimakers 2+ due to the clash of extruder to the base surface

Due to it being incompatible with the nozzle extender, the prints from
Ultimaker 2+ would often result in failure due to the printer clash with the
print and accidentally moving it from the original print location. As seen in
Figure 36, the printer nozzle is in the line of the print toolpath leading to the
movement of the print from original position and resulting in print failure.

4.2 Nonplanar extrusion of fibre reinforced structures

Nonplanar tests for fibre reinforced structures were not conducted in this
thesis due to the lack of time and easily accessible equipment. However, the
generated toolpath and the G-code generation methods would be solid
foundations that would encourage further development. Potential research
topics could include the anisotropy of nonplanar composite prints, the
development of multi-axis printing systems for complex nonplanar
geometries, or the investigation of fiber-matrix adhesion in curved extrusion
paths.

4.2.1 Anisotropy of composite prints

The nonplanar toolpaths can be modified to print in different directions to
test the anisotropic properties of the composite prints. Tailoring the fibre
orientation can also be used to investigate the optimal load paths in complex
geometries. In relation to the shin guard example, the tangential direction of


## Page 51

51

the toolpath would have a nonplanar effect as opposed to the lateral direction
as seen in Fig. 35. This difference in anisotropy could be demonstrated using
tensile tests, electrical conductivity tests, hardness tests or just by observing
the surface smoothness.


Figure 37: Shin guard toolpaths in lateral directions (left) and tangential directions (right)

4.2.2 Development of multi-axis printing systems

The development of multi-axis printing systems for complex nonplanar
geometries could be done either through designing of a custom print heads
or customization of an existing printer for nonplanar printing. Key challenges
would include precise motion control, path planning algorithms that account
for collision avoidance and optimal fibre orientation, and the development of
end effectors capable of extruding fibre-reinforced materials along curved
trajectories. Successful implementation of multi-axis printing systems could
revolutionize the production of complex composite structures, enabling the
creation of parts with improved strength-to-weight ratios, reduced material
waste, and enhanced functional properties. In addition, there is also a need
for the development of specialized slicing algorithms for nonplanar fibre
reinforced printing.

4.2.3 Fibre-matrix adhesion in curved extrusion paths

Investigation of fibre-matrix adhesion in curved extrusion paths could be
done by analysing the effect of different radii of curvature on interfacial shear
strength, examining how fibre pre-tension and extrusion pressures influence
adhesion in curved paths, and studying the formation of voids or defects at
the interface due to non-linear deposition. As fibres are deposited along
curved trajectories, they may experience varying degrees of tension,
compression, and shear forces, potentially impacting the fibre-matrix
interface. This research could be based on the understanding how the
curvature of the extrusion path affects the bonding between the reinforcing
fibres and the polymer matrix. Advanced characterization techniques such as
micro-CT scanning, nanoindentation, and in-situ mechanical testing may
also be employed to assess the quality of fibre-matrix bonding.
Understanding these phenomena is crucial for optimizing the mechanical


## Page 52

52

properties and long-term performance of nonplanar fibre-reinforced
structures.




## Page 53

53

5 Conclusion

This chapter summarized how the objective of the study has been achieved,
and how the study questions are answered. The study’s significance,
limitations and possible research in the future are presented.

This thesis has explored the practical applications of nonplanar 3D printing
in non-commercial environments. While the literature review demonstrated
extensive use of this technology in research and hobbyist contexts, its
adoption for mass production in industrial settings faces several challenges.
The primary obstacle is the absence of reliable, user-friendly slicer software
tailored for nonplanar printing, which impedes the technology's integration
into existing manufacturing processes. Additionally, the increased risk of
print failures and potential damage to equipment presents significant
hurdles for large-scale implementation. Furthermore, the availability of well-
established alternative manufacturing methods, such as multi-axis CNC
machining and conventional additive manufacturing techniques, currently
fulfils similar production needs effectively. These factors collectively
contribute to the slow commercialization of nonplanar 3D printing in
industrial applications, despite its promising potential in specialized
contexts.’

On the other hand, the potential applications using nonplanar 3D printing
could offer the industries an edge on their production and prototyping
departments. Nonplanar 3D printing, despite its current limitations in mass
production, holds significant promise for various industrial applications. In
the aerospace sector, this technology could revolutionize the production of
complex curved components for aircraft and spacecraft, potentially reducing
weight and improving aerodynamics. The automotive industry could benefit
from lightweight, structurally optimized parts that enhance vehicle
performance and fuel efficiency. In healthcare, nonplanar printing could
enable the creation of custom prosthetics and implants with improved
biomechanical properties, leading to better patient outcomes. The tooling
industry could leverage this technology to produce injection moulds with
conformal cooling channels, optimizing the manufacturing process for
plastic parts. Additionally, industries such as consumer products, sports
equipment, and architecture could exploit nonplanar printing to create
ergonomic designs, performance-optimized gear, and unique architectural
elements, respectively. As the technology matures and overcomes current
obstacles, its potential to unlock the design innovations and manufacturing
methods across the diverse sectors become increasingly apparent.

The advantages of non-planar 3D printing come with the complexity in the
sophisticated slicing algorithms and computational demands. The most


## Page 54

54

relevant challenge holding back against non-planar FDM methods currently
is the absence of a reliable slicing programme that is supported by the 3D
printing industry and the research community. The slicers described above
in the theory and review parts are still somewhat incomplete since they were
mostly developed by thesis students (in the case of Ahlers et al.), researchers
(in the case of Rudd et al.) and the 3D printing communities on GitHub,
YouTube, and Reddit. Apart from a few pioneering startups, the industry
hasn’t caught up or invested heavily on the research and development of non-
planar 3D printing and its potential applications.


Figure 38. Non-planar material deposition pattern according to Autodesk Patent

One of the biggest challenges for the commercialization of non-planar 3D
printing is due to the legality surrounding the topic. American software
company Autodesk has an active patent on the topic as early as 2015. Patent
US10005126B2 describes a similar method in which Autodesk developed an
algorithm for extrusion toolpath to achieve smoother surface as seen in Figure
38. The algorithm slices the object in a combination of mostly 2D planar layer
slicing and non-planar slicing for a few top layers describing a slicer closely
resembling to the one Ahlers et al., developed in 2019. (Sherwood Page, 2015)

Most of the 3D printer intended for domestic use are easily customizable for
non-planar 3D printing. Users only need to take necessary measures to
remove unnecessary hardware in the way of the nozzle clearance angle.


## Page 55

55

However, non-planar 3D printing for industrial use with mass production
still requires incredible demands. Non-planar 3D printing for industrial use
with multi-axis CNC machines or robot arms require meticulous planning
and careful slicing of the parts to be fabricated. This circles back to the
current issue of the lack of a commercial software for a reliable non-planar
slicing algorithm.

In conclusion, this thesis has thoroughly explored the landscape of nonplanar
3D printing, focusing on its practical applications in non-commercial settings
while also examining its potential for industrial adoption. The research has
revealed a dichotomy between the technology's current limitations and its
promising future. While nonplanar 3D printing faces significant challenges
in mass production environments, including software limitations, reliability
concerns, and competition from established manufacturing methods, its
potential to revolutionize various industries is undeniable. From aerospace
and automotive to healthcare and consumer products, the unique capabilities
of nonplanar printing offer opportunities for innovation in design, efficiency,
and functionality. As the technology continues to evolve, addressing current
obstacles will be crucial for its widespread adoption. This study serves as a
foundation for future research, highlighting the need for improved slicer
software, enhanced reliability, and further exploration of industry-specific
applications. Ultimately, the future of nonplanar 3D printing lies in striking
a balance between overcoming its current limitations and leveraging its
unique advantages to create value across diverse sectors of industry and
research.


## Page 56

56

References
Ahlers, D., Wasserfall, F., Hendrich, N., & Zhang, J. (2019). 3D Printing of
Nonplanar Layers for Smooth Surface Generation. [Masterthesis] Universität
Hamburg, https://doi.org/http://dx.doi.org/10.13140/RG.2.2.34888.26881
Ahn, S., Montero, M., Odell, D., Roundy, S., & Wright, P. K. (2002). Anisotropic
material properties of fused deposition modeling ABS. Rapid Prototyping
Journal, 8(4), 248–257. https://doi.org/10.1108/13552540210441166
Alberti, M. G., Enfedaque, A., & Gálvez, J. C. (2018). A review on the assessment
and prediction of the orientation and distribution of fibres for concrete.
Composites Part B: Engineering, 151, 274–290.
https://doi.org/https://doi.org/10.1016/j.compositesb.2018.05.040
Ankerhold, E., & Tjepkema, J. (2024, May). Non-Planar Post Processor: A Python
tool to post process 3D-printer G-Code for FDM printing on non-planar
surfaces. https://github.com/eliasankerhold/non-planar-post-processor
Armstrong, M., Mehrabi, H., & Naveed, N. (2022). An overview of modern metal
additive manufacturing technology. Journal of Manufacturing Processes, 84,
1001–1029. https://doi.org/https://doi.org/10.1016/j.jmapro.2022.10.060
Bhatt, P., Kulkarni, A., Kanyuck, A., Malhan, R., Santos, L., Thakar, S., Bruck, H.,
& Gupta, S. (2022). Automated process planning for conformal wire arc
additive manufacturing. The International Journal of Advanced
Manufacturing Technology, 119, 1–26. https://doi.org/10.1007/s00170-021-
08391-7
C. B. Carolo, L., & Cooper O., R. E. (2022). A review on the influence of process
variables on the surface roughness of Ti-6Al-4V by electron beam powder bed
fusion. Additive Manufacturing, 59, 103103.
https://doi.org/https://doi.org/10.1016/j.addma.2022.103103
Campbell, I., Diegel, O., Huff, R., Kowen, J., & Wohlers, T. (2023). Wohlers Report
2023. 3D Printing and Additive Manufacturing State of the Industry.
Chauvette, J., Hia, I. L., Pierre, J., Chenier, G., Farahani, R. D., Piccirelli, N., &
Therriault, D. (2023). Non‐Planar Multiprocess Additive Manufacturing of
Multifunctional Composites. Advanced Materials Technologies, 8(17).
https://doi.org/10.1002/admt.202300399
Clemon, L., Sudradjat, A., Jaquez, M., Krishna, A., Rammah, M., & Dornfeld, D.
(2013). PRECISION AND ENERGY USAGE FOR ADDITIVE
MANUFACTURING. In ASME International Mechanical Engineering
Congress and Exposition (Vol. 56185, p. V02AT02A015). American Society of
Mechanical Engineers.
Evans, J., O’neill, J., Little, J. , Clark, G. , Albus, J. , Barbera, A. , Smith, B. , Fife,
D. , Fong, E. , Gilsinn, D. , Holberton, F. , Lucas, B. , Lyon, G. and Marron, B.
(1977), Standards for computer aided manufacturing:, , National Institute of


## Page 57

57

Standards and Technology, Gaithersburg, MD, [online],
https://doi.org/10.6028/NBS.IR.76-1183 (Accessed November 16, 2024)
Fortunato, G. M., Nicoletta, M., Batoni, E., Vozzi, G., & De Maria, C. (2023). A fully
automatic non-planar slicing algorithm for the additive manufacturing of
complex geometries. Additive Manufacturing, 69, 103541.
https://doi.org/https://doi.org/10.1016/j.addma.2023.103541
Gao, W., Zhang, Y., Ramanujan, D., Ramani, K., Chen, Y., Williams, C. B., Wang,
C. C. L., Shin, Y. C., Zhang, S., & Zavattieri, P. D. (2015). The status,
challenges, and future of additive manufacturing in engineering. Computer-
Aided Design, 69, 65–89.
https://doi.org/https://doi.org/10.1016/j.cad.2015.04.001
Gleadall, A. (2021). FullControl GCode Designer: Open-source software for
unconstrained design in additive manufacturing. Additive Manufacturing,
46, 102109. https://doi.org/10.1016/j.addma.2021.102109
Guidetti, X., Balta, E. C., Nagel, Y., Yin, H., Rupenyan, A., & Lygeros, J. (2023).
Stress flow guided non-planar print trajectory optimization for additive
manufacturing of anisotropic polymers. Additive Manufacturing, 72, 103628.
https://doi.org/10.1016/J.ADDMA.2023.103628
Hong, F., Lampret, B., Myant, C., Hodges, S., & Boyle, D. (2023). 5-axis multi-
material 3D printing of curved electrical traces. Additive Manufacturing, 70,
103546. https://doi.org/10.1016/j.addma.2023.103546
International Organization for Standardization. (2021). SFS-EN ISO/ASTM
52900:2021:en Additive manufacturing. General principles. Fundamentals
and vocabulary (ISO/ASTM 52900:2021) (2nd ed.). Finnish Standards
Association SFS.
Keating, S., & Oxman, N. (2013). Compound fabrication: A multi-functional
robotic platform for digital design and fabrication. Robotics and Computer-
Integrated Manufacturing, 29(6), 439–448.
https://doi.org/https://doi.org/10.1016/j.rcim.2013.05.001
Kim, S., Andreu, A., Kim, I., Kim, J.-H., Lee, J., & Yoon, Y.-J. (2022). Continuously
varied infill pattern (ConVIP): improvement of mechanical properties and
printing speed of fused filament fabrication (FFF) 3D printing. Journal of
Materials Research and Technology, 18, 1055–1069.
https://doi.org/https://doi.org/10.1016/j.jmrt.2022.02.133
Kipping, J., Nettig, D., & Schüppstuhl, T. (2024). Looping: Load-oriented
optimized paths in non-planar geometry. Additive Manufacturing, 94,
104426. https://doi.org/https://doi.org/10.1016/j.addma.2024.104426
Koch, C., Van Hulle, L., & Rudolph, N. (2017). Investigation of mechanical
anisotropy of the fused filament fabrication process via customized tool path
generation. Additive Manufacturing, 16, 138–145.
https://doi.org/https://doi.org/10.1016/j.addma.2017.06.003


## Page 58

58

Li, W., & Leu, M. (2019). Material Extrusion Based Ceramic Additive
Manufacturing. Additive Manufacturing Processes. 97-111.
https://doi.org/10.31399/asm.hb.v24.a0006562
Li, X., Liu, W., Hu, Z., He, C., Ding, J., Chen, W., Wang, S., & Dong, W. (2024).
Supportless 3D-printing of non-planar thin-walled structures with the multi-
axis screw-extrusion additive manufacturing system. Materials & Design,
240, 112860. https://doi.org/10.1016/j.matdes.2024.112860
Matsuzaki, R., Ueda, M., Namiki, M., Jeong, T. K., Asahara, H., Horiguchi, K.,
Nakamura, T., Todoroki, A., & Hirano, Y. (2016). Three-dimensional printing
of continuous-fiber composites by in-nozzle impregnation. Scientific
reports, 6, Article 23058. https://doi.org/10.1038/srep23058
Pan, L. (2014). Surface scanning and path planning for non-planar 3D printing
[Diploma Thesis]. Montanuniversität Leoben.
Pérez, M., Carou, D., Rubio, E. M., & Teti, R. (2020). Current advances in additive
manufacturing. Procedia CIRP, 88, 439–444.
https://doi.org/https://doi.org/10.1016/j.procir.2020.05.076
Pierre, J., Verville, M., Chenier, G., Farahani, R. D., Piccirelli, N., Lévesque, M., &
Therriault, D. (2024a). Non-planar material-extrusion additive
manufacturing of multifunctional sandwich structures using carbon-
reinforced polyetheretherketone (PEEK). Additive Manufacturing, 84,
104124. https://doi.org/https://doi.org/10.1016/j.addma.2024.104124
Pierre, J., Verville, M., Chenier, G., Farahani, R. D., Piccirelli, N., Lévesque, M., &
Therriault, D. (2024b). Non-planar material-extrusion additive
manufacturing of multifunctional sandwich structures using carbon-
reinforced polyetheretherketone (PEEK). Additive Manufacturing, 84,
104124. https://doi.org/10.1016/j.addma.2024.104124
Radzevich, S. P., & Goodman, E. D. (2002). Computation of Optimal Workpiece
Orientation for Multi-axis NC Machining of Sculptured Part Surfaces. Journal
of Mechanical Design, 124(2), 201–212. https://doi.org/10.1115/1.1468634
Rudd, L., Faghihrasoul, Z., & Campbell, M. I. (2023, August 20). Methods for
Creating Additive Printing Paths on Nonplanar Surfaces. Volume 3B: 49th
Design Automation Conference (DAC). https://doi.org/10.1115/DETC2023-
110757
Schoonmaker, S. (2003). The CAD guidebook : a basic manual for understanding
and improving computer-aided design. Marcel Dekker.
Sherwood Page, J. (2015). Systems and methods for improved 3D printing (Patent
US10005126B2). USPTO.
Tam, K.-M. M., & Mueller, C. T. (2017). Additive Manufacturing Along Principal
Stress Lines. 3D Printing and Additive Manufacturing, 4(2), 63–81.
https://doi.org/10.1089/3dp.2017.0001


## Page 59

59

Tofail, S. A. M., Koumoulos, E. P., Bandyopadhyay, A., Bose, S., O’Donoghue, L., &
Charitidis, C. (2018). Additive manufacturing: scientific and technological
challenges, market uptake and opportunities. Materials Today, 21(1), 22–37.
https://doi.org/https://doi.org/10.1016/j.mattod.2017.07.001
Wang, Y., Liu, J., Yu, Y., Zhang, Q., Li, H., & Shi, G. (2022). Research on the
Simulation Model of Continuous Fiber-Reinforced Composites Printing
Track. Polymers, 14(13). https://doi.org/10.3390/polym14132730
Yang Li and Hsu, K. and B. B. and G. D. and M. F. and M. M. and W. S. (2017).
Additive Manufacturing Process Chain. In Additive Manufacturing of Metals:
The Technology, Materials, Design and Production (pp. 33–43). Springer
International Publishing. https://doi.org/10.1007/978-3-319-55128-9_2
Zhai, Y., Lados, D. A., & LaGoy, J. L. (2014). Additive Manufacturing: Making
Imagination the Major Limitation. JOM, 66(5), 808–816.
https://doi.org/10.1007/s11837-014-0886-2
Zhang, T. (2023). Geometric Computing Based Enabler for Multi-axis Additive
Manufacturing.
Zhang, X., Liang, Y., Yi, F., Liu, H., Zhou, Q., Yan, Z., & Lin, J. (2023). Anisotropy
in microstructure and mechanical properties of additively manufactured Ni-
based GH4099 alloy. Journal of Materials Research and Technology, 26,
6552–6564. https://doi.org/https://doi.org/10.1016/j.jmrt.2023.09.038

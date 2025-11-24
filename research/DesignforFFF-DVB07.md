# 

**Source:** `DesignforFFF-DVB07.pdf`
---

## Page 1

See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/282133348
Design for Fused Filament Fabrication Additive Manufacturing
Conference Paper · August 2015
DOI: 10.1115/DETC2015-46355
CITATIONS
32
READS
5,788
3 authors:
John Steuben
United States Naval Research Laboratory
94 PUBLICATIONS   904 CITATIONS   
SEE PROFILE
Douglas Lee Van Bossuyt
Naval Postgraduate School
135 PUBLICATIONS   936 CITATIONS   
SEE PROFILE
Cameron J. Turner
Clemson University
118 PUBLICATIONS   588 CITATIONS   
SEE PROFILE
All content following this page was uploaded by Douglas Lee Van Bossuyt on 24 September 2015.
The user has requested enhancement of the downloaded file.


## Page 2

Proceedings of the ASME 2015 International Design Engineering Technical Conferences &
Computers and Information in Engineering Conference
IDETC/CIE 2015
August 2-5, 2015, Boston, USA
DETC2015-46355
DESIGN FOR FUSED FILAMENT FABRICATION ADDITIVE MANUFACTURING
John Steuben
Post Doctoral Research Associate
Department of Mechanical Engineering
Colorado School of Mines
Golden, CO 80401, USA
Email: jsteuben@mines.edu
Douglas L. Van Bossuyt∗
Assistant Professor
Department of Mechanical Engineering
Colorado School of Mines
Golden, CO 80401, USA
Email: dvanboss@mines.edu
Cameron Turner
Assistant Professor
Department of Mechanical Engineering
Colorado School of Mines
Golden, CO 804010, USA
Email: cturner@mines.edu
ABSTRACT
In this paper, we explore the topic of Fused Filament Fab-
rication (FFF) 3D-printing. This is a low-cost additive manu-
facturing technology which is typically embodied in consumer-
grade desktop 3D printers capable of producing useful parts,
structures, and mechanical assemblies.
The primary goal of
our investigation is to produce an understanding of this process
which can be employed to produce high-quality, functional en-
gineered parts and prototypes. By developing this understand-
ing, we create a resource which may be turned to by both re-
searchers in the ﬁeld of manufacturing science, and industrial
professionals who are either considering the use of FFF-enabled
technologies such as 3D printing, or those who have already en-
tered production and are optimizing their fabrication process. In
order to paint a cohesive picture for these readers, we examine
several topic areas. We begin with an overview of the FFF pro-
cess, its key hardware and software components, and the inter-
relationships between these components and the designer. With
this basis, we then proceed to outline a set of design principles
which facilitate the production of high quality printed parts, and
discuss the selection of appropriate materials. Following natu-
rally from this, we turn to the question of feedstock materials for
FFF, and give advice for their selection and use. We then turn
to the subject of the as-printed properties of FFF parts and the
strong non-isotropic response that they exhibit. We discuss the
∗Address all correspondence to this author. Equally-shared corresponding
authorship with Cameron Turner.
root causes of this behavior and means by which its deleterious
effects may be mitigated. We conclude by discussing a mixed
numerical/ experimental technique which we believe will enable
the accurate characterization of FFF parts and structures, and
greatly enhance the utility of this additive manufacturing tech-
nology. By formalizing and discussing these topics, we hope to
motivate and enable the serious use of low-cost FFF 3D printing
for both research and industrial applications.
1
INTRODUCTION
Fused Filament Fabrication (FFF), also referred to as Fused
Deposition Modeling (FDM)1, is an increasingly commonplace
additive manufacturing technology [1]. In this paper we study
the subject of design for manufacturing using the FFF process.
We focus on the most common embodiment of this technology:
low-cost consumer-grade desktop “3D-printers,” such as that il-
lustrated in Figure 1. Multiple systems for this market have been
developed [2-4].
The primary intent of this study is to develop a guide for
the use of FFF for the production of engineered components in
ﬁelds such as prototype, customized, or high-mix-low-volume
manufacturing. This guide is largely geared to the needs of man-
ufacturing science researchers and industrial engineers who are
considering or have already adopted the use of FFF technology.
We also explore the FFF process in detail, and develop an under-
1“Fused Deposition Modeling” and “FD” ©Stratsys Inc.
1
Copyright © 2015 by ASME


## Page 3

FIGURE 1.
A typical desktop 3D printer which employs FFF.
standing of this technology which will enable the manufacture of
high-quality components with minimum cost and waste. To do
so, we examine several facets of fused ﬁlament fabrication.
1.1
Organization
We begin, in Section 2, by describing the FFF process as
hardware and software components. The relationships between
these components (and the design engineer) are shown, and the
critical parameters associated with these connections are out-
lined. To illustrate the importance of these parameters, and show
how they may be tuned, we proceed in Section 3 to lay out a set
of design principles which enable efﬁcient and productive FFF
manufacturing. Important considerations for maximizing part
quality and minimizing print time, cost, scrap rate, and wasted
material are given. This discussion also includes recommenda-
tions for improving the geometric accuracy of the parts produced.
In Section 4, we supplement the guidelines of Section 3 with a
discussion of the feedstock materials available for FFF, and the
best practices for selecting and printing with these materials. A
summary of useful data for the selection of feedstock materials
for an intended application is given. Section 5 expands upon the
material properties theme, by considering the sources and im-
plications of complex non-isotropic behaviors in FFF-produced
components. We explore the sources of this anisotropy, and pro-
vide design and production advice for mitigating its deleterious
effects. Finally, a discussion of the difﬁculties associated with
simulating the response of FFF-produced structures is presented
in Section 6. We further propose a mixed experimental/numeric
scheme for characterizing the “as-printed” properties of these
materials. By exploring these topics we produce a guide to the
process of low-cost 3D printing which is of interest to both re-
searchers and practicing engineers who are either exploring the
ﬁeld of additive manufacturing with this process, or those who
are already practiced in the art and wish to improve their own
processes. As recent studies have shown that this technology
is economically viable for distributed manufacturing [5, 6], we
believe that this guide will enable a broad spectrum of future re-
search.
1.2
Speciﬁc Contributions
In this paper, we gather observations and data which may
already be familiar to those practiced in FFF. However, much of
this important information has gone unreported, is reported in
scattered sources, or is only discussed informally. Compounding
this, much of the available scientiﬁc literature focuses on other
additive manufacturing processes such as selective laser sintering
[7] or powder and binder systems [8]. We wish to unify the avail-
able body of knowledge into a document which is useful both to
new practitioners in the ﬁeld of additive manufactures, and those
who are already well-versed in the ﬁeld.
Beside the collection of practices and data that are useful to
the manufacturing science researcher or production engineer, in
this paper we contribute to the fundamental understanding of the
FFF process in several aspects. In particular: 1) We formalize
a great deal of knowledge from the hobbyist and professional
communities, which has been validated in our laboratory.
2)
We identify key parameters of the FFF process, and tie them to
good design practice. 3) We present the best practices which we
have found for 3D printing with the most common FFF feed-
stock materials, as well as post-processing operations such as
vapor smoothing which may be utilized to improve output qual-
ity. 4) We combine existing research on the anisotropy of FFF-
produced components, with research into an additional source of
anisotropy, in order to identify the origin of delamination and
fracture failures in these components. This work is validated by
numerical and physical experimentation. 5) We identify short-
comings in both design practices and computational tools for ad-
dressing the complex anisotropic response behavior, and outline
what we believe to be a promising path to rectify this deﬁciency
through future research. Through these collective discussions,
we paint a clear picture of the current best practices for low-cost
FFF-based 3D printing, and enable the use of this technology
with minimal difﬁculty by a wide range of researchers and in-
dustrial professionals.
2
The FFF Process
Before we discuss the topic of design methodology for FFF,
we must ﬁrst review the nature of the process, and identify the
critical parameters which control it. Mechanically speaking, the
FFF process is straightforward as illustrated in Figure 2.
A
2
Copyright © 2015 by ASME


## Page 4

three-axis motion system moves an extruder in x-y-z coordinates,
while extruding a certain amount of material, according to a pre-
speciﬁed motion plan or “toolpath.” The extruder accepts poly-
mer feedstock in the form of a ﬁlament, typically one to three
millimeters in diameter and drawn from a spool. A drive gear en-
gages the ﬁlament, and forces it through a thermistor-regulated
heating block and nozzle. This produces a strand of molten plas-
tic which is deposited and subsequently cools in order to form
the FFF part. This deposition is produced in layers, built one
atop the next. The relative distance between the extruder nozzle
and build plate is adjusted in a ﬁxed increment between layers.
For each layer, both outer perimeter loops and a rasterized inﬁll
are extruded. The layers forming the top or the bottom of the
part, adjacent to this inﬁll region are typically solid. The inﬁll is
typically a sparse pattern in the areas of layers which correspond
to the interior of the part. The FFF process is discussed in greater
detail in [1]. Further review of common 3D printers employing
the FFF process is given in [2-4].
FIGURE 2.
Illustration of the basic hardware setup for FFF 3D print-
ing.
2.1
FFF Software Toolchain
Generally, the mechanical aspects of FFF are handled au-
tomatically by the printer hardware and ﬁrmware. It is there-
fore the generation a suitable toolpath which allows the pro-
duction of parts in an efﬁcient and timely manner. The soft-
ware toolchain which is used to produce these toolpaths is di-
agrammed in Figure 3. The primary stages are (a) the generation
of a 3D model from parametric engineering geometry such as
a computer-aided drawing and/or imported 3D scan geometry,
(b) converting the 3D model to a tetrahedral mesh ﬁle, almost
universally implemented in stereolithograpy (STL) format, (c)
splitting the tetrahedral mesh into layers and producing the tool-
path using a program known as a “slicer,” and (d) using a piece of
machine-control software to forward the toolpath to the printer it-
self, which then produces the part. This process is largely analo-
gous to that used for industrial computer numeric control (CNC)
machinery. The process of slicing, which is particularly com-
plex, is covered in depth in [9-14]. Figure 4 demonstrates the
full sequence of steps on a sample component.
FIGURE 3.
The FFF process, broken down into stages. Typically
each stage takes the form of a separate software tool.
The process of Figure 3 includes several connections which
indicate points at which iterative adjustment of the design may
occur. These are not comprehensive, but indicate what we ﬁnd
3
Copyright © 2015 by ASME


## Page 5

FIGURE 4.
The stages of toolpath generation, from top to bottom:
3D part geometry, tetrahedral mesh, close view of toolpath produced by
slicer, and ﬁnished product. Note that the part is rotated 90°.
to be the primary areas where designs must be adjusted to pro-
duce good results. Typically, the tetrahedral model will contain a
very large number of facets, and it is difﬁcult to manually check
for the presence of errors. The better approach is to proceed to
the slicing step, and observe if issues arise in the toolpath gen-
eration. The STL ﬁle input into the slicer must be a manifold
“watertight” shell, and free of degenerate faces. Some Computer
Aided Design (CAD) packages produce STL ﬁles containing de-
generate facets or other errors. In this case, a software utility
must be used to repair the STL ﬁle, such as those described in
[15,16]. Additionally, the slicer may reveal issues which require
correction by the designer. These issues may include thin fea-
tures which the slicer may “miss” or cases where support ma-
terial is difﬁcult or impossible to remove. Information on pre-
venting or rectifying these issues is discussed in Section 3. Other
issues may be observed after the printing process is completed,
and may require either redesign of the part to facilitate FFF, or
a complete problem reformulation in order to achieve acceptable
3D printed parts. Methods for reformulating and designing parts
for 3D printing are provided in Section 3.
2.2
Important FFF Parameters
The steps which follow the generation of the 3D model in
Figure 3 rely on a number of important parameters. These are
outlined and broken down by component in Table 1, below. The
items listed are not comprehensive, and may vary based on the
particular hardware and software used, but cover what we have
found to be the most important and often-adjusted parameters.
The typical values listed are based on our experiences with low-
cost 3D printing systems, and the more common feedstock ma-
terials. Other fabrication systems and materials may require sig-
niﬁcant deviation from the ranges given.
This section has shown that FFF is a complex multi-stage
process, which is governed by a large number of parameters.
The correct selection values for these parameters is crucial to
the production of high-quality low-cost parts. In the next section
we explore design principles for FFF, which may be used both
to generate FFF-ready components, and to more precisely select
values for these parameters.
3
Design for FFF (DF4)
One of the great strengths of FFF and other 3D printing
technologies is that they do not impose extensive design-for-
manufacturing requirements, and enable the manufacture of parts
which are difﬁcult, expensive, or impossible to produce by con-
ventional means. Examples of such parts are given in [17-20].
However, there are several design practices which may be ob-
served in order to produce parts using FFF in a time and cost-
effective fashion, especially for applications such as low-volume
manufacturing. In the following section, we outline several of
these practices which we have found to be most helpful, and
which give insight into the tuning of the parameters listed in the
prior section.
3.1
Part Orientation & Geometry
The layered nature of FFF, along with the physics of molten
plastic extrusion place several limitations on the geometry which
may be 3D printed. Chief amongst these are:
• The part must feature a planar surface which will be adhered
to the build plate during printing. This planar surface must
be of sufﬁcient size (typically greater than 1cm2) in order
to remain adhered to the build plate for the duration of the
printing process. If this is not possible the part should be
printed atop a “raft” structure of sufﬁcient area.
• The part should not exhibit geometric overhangs greater than
a critical angle α, typically 45-60°from vertical. Such over-
hanging geometry necessitates the use of support material,
as discussed in the next section.
• The part should be designed to carry major mechanical loads
in the plane parallel to the build plate. Large out-of-plane
4
Copyright © 2015 by ASME


## Page 6

TABLE 1.
Important parameters in the FFF process.
Parameter
Description
Typical Value
Tetrahedralization
Max. Linear Deviation
Maximum distance between tetrahedral surface and original model.
0.03-0.1 mm
Max. Angular Deviation
Maximum angle between normal vectors of adjacent facets.
5-30°
Slicing
Layer Thickness
Thickness of each layer of the FFF part.
0.05-0.3mm
Extrusion Width
Width of the plastic extrusion from the nozzle. Different widths may be speciﬁed
for inﬁll and perimeters.
0.1-0.4mm
Inﬁll Density
Relative density from 0 (totally hollow object) to 1 (totally solid object).
0-1
Inﬁll Orientation
Orientation of the inﬁll pattern relative to the x-axis of the 3D printer.
0-90°
Inﬁll Pattern
Pattern by which inﬁll is produced. Rectilinear and hexagonal grids are most com-
mon.
–
Perimeter Loop Number
The number of perimeter loops produced (see Figure 3).
1-4
Perimeter Loop Ordering
Binary decision to print perimeters from innermost to outermost, or vise-versa.
–
Support Density
The relative density of the support material (again from 0/none to 1/solid).
0-0.3
Support Orientation
Orientation of the support material relative to the x-axis of the 3D printer
0-90°
Support Pattern
Pattern by which inﬁll is produced. Rectilinear grids are most common.
–
Printing
Movement Velocity
Rate at which to move the extruder head during plastic deposition. Separate rates
may be speciﬁed for different extrusion types.
25-100 mm/s
Extruder Temperature
Temperature of the extrusion process
190-250 °C
Build Plate Temperature
Temperature of the build surface
0-140 °C
Cooling Power
Power applied to the cooling fans in order to solidify the extrusion.
0-100 %
loads promote delamination failures between the build lay-
ers due to the anisotropic material response characteristics,
which are discussed in Section 5.
• The use of an “inverted frustum” design concept, as shown
in Figure 5, can be used to accommodate these limitations.
Effectively, the part should be located entirely within an in-
verted frustum of angle α, with a sufﬁcient area on the bot-
tom face to prevent part detachment from the build surface.
The topic of part orientation is covered in detail by [21-24],
with extensive analyses. Even if the part is built within a frustum
as described, there may still be local areas which require support
material (e.g. some portions of the bracket in Figure 5). The next
section covers the topic of generating support material.
3.2
Support Material
Unlike other processes such as selective sintering, FFF 3D
printing requires the use of support material in order to produce
overhanging structures such as the example shown in Figure 6.
FFF printers which feature dual-extrusion heads may use one
extruder to print the part and the other, loaded with a dissolv-
able material, to print the support structure. Materials such as
polyvinyl alcohol (PVA) or high-impact polystyrene (HIPS) are
frequently used in this capacity, as they are soluble in water or
dipentene, respectively. More conventional printers with only
one extruder are limited to producing “curtains” of support ma-
terial which must be mechanically removed after the print. As
a result, printing with a second support material tends to pro-
duce better accuracy and surface ﬁnish. However, in both cases
5
Copyright © 2015 by ASME


## Page 7

FIGURE 5.
The inverted frustum design concept (with α = 45°) ap-
plied correctly on a wheel hub (top) and incorrectly on a bracket (bot-
tom).
it is desirable to minimize the use of supports, as it represents
additional material cost, post-processing cost, and machine time,
which are not realized in the ﬁnal product.
Examining Figure 6, it is clear that no reorientation of the
(circularly symmetric) part will allow printing with less support
material. This indicates that the part should either be printed in
the shown orientation, or a redesign for FFF should take place. In
this instance, if the studs were printed separately and press-ﬁt in
a secondary operation the part could be printed without support
in the orientation shown in Figure 5. Given normal settings for
support density and printer speed, this would result in a 37%
savings in material consumption and a 39% decrease in print time
based upon test prints of these conﬁgurations. These ﬁgures are
computed by comparing the time estimates reported by a slicing
program applied to both conﬁgurations using identical settings.
This indicates that if parts cannot be printed without excessive
support material, they should be split, printed in several parts,
and assembled afterward.
Even more problematic are situations where overhanging ar-
eas which require support feature protruding bosses, as shown in
Figure 7. This creates a situation where, for several layers, the
boss will be printed atop the support material with no connection
to the main part body. This causes very poor positional accuracy
of the boss feature relative to the main part body, and a poor part
ﬁnish on the bottom part of the boss. In cases where reorienting
or splitting the part is impossible, the designer should model a
support column and disable the automatic generation of support
in the slicer. This is demonstrated in the bottom portion of Figure
FIGURE 6.
Example of areas requiring support material. A cross sec-
tion of the wheel hub from Figure 5, with the addition of protruding
studs, is shown.
7.
FIGURE 7.
Overhanging features requiring support. It is advisable
to provide a solid support column to accurately locate the overhanging
boss.
A ﬁnal difﬁculty concerning support material involves the
concavity of regions where support is generated. If the support
is not printed from soluble material it must be mechanically re-
moved. Producing an acceptable surface ﬁnish usually requires
ﬁnishing with a ﬁle or other abrasive. If the support material had
been generated beneath a small concave area this process may be
difﬁcult or impossible. Additionally, if support material is placed
on top of a portion of the printed part, it will be more difﬁcult to
remove. These conditions are outlined in Figure 8.
In summary, the best design practices regarding support ma-
terial are:
• Always consider reorienting or splitting the part in order to
reduce or eliminate the usage of support material.
6
Copyright © 2015 by ASME


## Page 8

FIGURE 8.
Areas where support material may be particularly difﬁcult
to remove from a revolved part.
• Include pillar supports in order to accurately locate over-
hanging boss features.
• Avoid the generation of support material in areas where it
will be difﬁcult to remove (e.g. small concave regions).
• Support material should be generated at an angle orthogonal
to the long axis of the region which it supports
• The support lattice should be spaced by approximately 1
2 the
size of the smallest supported feature, or 3mm, whichever is
smaller.
3.3
Inﬁll
In order to minimize the use of material FFF, parts are usu-
ally built from a solid outer perimeter shell, but feature a sparse
interior inﬁll pattern on the interior. The perimeter and inﬁll are
generated automatically by the slicer program. Several of the pa-
rameters given in Table 1 can be adjusted to produce satisfactory
parts. As a rule, both the mechanical strength and production
cost will increase proportionally to the inﬁll density. We recom-
mend an inﬁll density of 0.1-0.125 for purely cosmetic parts, and
0.125-0.2 for light-duty parts (dust guards, cable guides, etc).
For more heavily-stressed components such as mechanical link-
ages or gears, a higher density in the range of 0.25-0.5 is rec-
ommended. For components such as wrenches or long levers, a
density of 1.0 (completely solid) has produced acceptable results.
The inﬁll is commonly constructed in either rectilinear or
hexagonal patterns, as shown in Figure 9.
Generally we prefer the use of rectilinear inﬁll for two rea-
sons. First, a rectilinear inﬁll is simpler to compute, results in a
smaller toolpath ﬁle, and requires slightly less printing time. For
the comparison shown in Figure 9 the linear inﬁll is 3% faster to
FIGURE 9.
Hexagonal (top) compared to rectilinear (bottom) inﬁll.
Note both the outer perimeters and the perimeters around the interior
holes.
print, as computed by slicing the same part twice, varying only
the pattern, and comparing estimated print times. Second, a rec-
tilinear inﬁll allows the relative orientation of the inﬁll strands
to be adjusted along with the mechanical properties of the part.
The orthogonal conﬁguration shown in Figure 9 is not manda-
tory. Alternate conﬁgurations enable the adjustment of mechan-
ical properties so as to reduce anisotropic material behaviors, as
discussed in Section 5.
3.4
Surface Finish
Achieving a ﬁne surface ﬁnish is highly desirable for most
3D printing processes, but achieving a consistently good surface
ﬁnish using FFF is difﬁcult. There are a multitude of factors
which contribute to this difﬁculty, such as the layered nature
of the part, the inherent unpredictability of the molten or semi-
molten plastic ﬂow, and drooping or sagging in overhanging re-
gions. In this section we focus on design measures which can
be used to improve surface ﬁnish. In Section 4 we discuss the
material-speciﬁc thermal management issues which can further
improve surface ﬁnish.
One of the key determinants of surface ﬁnish is layer thick-
ness, as illustrated in Figure 10. Given the idealized geome-
try shown in the top portion of Figure 10, it is clear that d1 =
sin(α′),d2 = t
2, and thus the surface deviation (d) is approx-
imated by d = d1 + d2 = ( t
2)(1 + sin(α′)) . This relationship
illustrates that both the layer thickness (t) and the slope of the
local geometry (α′) affect the surface ﬁnish on the “sides” of the
model. The lower portion of the ﬁgure illustrates the ﬁnish on
the “top” surface of the part, and shows that the extrusion width
does not play a major role and that the top surface deviation (d′)
is approximately given by d′ = t
2.
The strong dependence on layer thickness is clear, and by
reducing this dimension to 0.1 mm or less a very ﬁne surface
7
Copyright © 2015 by ASME


## Page 9

FIGURE 10.
Illustration of surface deviation in an idealized FFF
model.
ﬁnish can be obtained. Unfortunately, print time increases in a
fashion inversely proportional to layer thickness. For all practical
purposes this is an exact correspondence, e.g. printing at double
the layer thickness will halve print time. Typically the lower limit
of layer thickness is dictated by the mechanical accuracy of the
3D printers motion system, and the upper bound is equal to the
extruder nozzle diameter.
The idealized model shown in Figure 10 does not illustrate
several of the other factors associated with poor surface ﬁnish.
The use of support material, for instance, will reduce the sur-
face ﬁnish quality of the areas to which the support material is
attached. Another common problem is “droop” where the outer
perimeters of a layer are not supported properly by the layer(s)
below and are drawn downwards by gravity before the molten
extrusion can sufﬁciently solidify. Many of these effects can be
mitigated, however, by the correct selection of properties for the
perimeter loops which are given in Table 1. A few helpful obser-
vations include:
• Printing the perimeters from “outside” to “inside” produces
better dimensional accuracy, but reversing the ordering pro-
duces better surface ﬁnish on overhanging surfaces.
• Usually 2-3 perimeters are sufﬁcient to produce good di-
mensional accuracy and surface ﬁnish. For parts with ex-
cessively steep overhangs (or conversely, very gently slop-
ing non-overhanging regions), more perimeters may be re-
quired.
• The outermost perimeter should be printed at a slower speed,
roughly 50-75% the speed of other perimeters.
• Prior research has also shown that surface ﬁnish may be im-
proved by optimizing the vertices of the STL ﬁle which is
input to the slicer [25]. Further details concerning the gen-
eration of the STL ﬁle are given in the next section.
3.5
Generating the STL File
The conversion of a parametric solid model to a tetrahedral
mesh is the ﬁnal step of the design process for FFF, and should
be approached with care. The mesh must consist of one or more
manifold surfaces with no gaps or holes. Non-manifold meshes
typically cause errors and nonsensical toolpath generation during
slicing. Most CAD packages support the direct export of man-
ifold mesh ﬁles. A stereolithography STL ﬁle is almost always
used, although research in other additive manufacturing ﬁelds
has shown that specialized ﬁle formats may have some bene-
ﬁt [26]. Typically two tolerance parameters can be adjusted to
deﬁne the ﬁdelity of the mesh: maximum distance and angular
deviation. If these tolerances are too large, the mesh will not ade-
quately represent the underlying model; if the tolerances are too
small, the mesh will be excessively large and require extensive
time and computer resources to slice. The settings most com-
monly used in our work are:
• Fine models: Max Deviation = 0.025 mm, Max Angle = 5°
• Coarse models: Max Deviation = 0.1 mm, Max Angle = 20°
• Very ﬁne models: the maximum deviation should be equal to
the smallest feature which the FFF hardware can reproduce
(determined experimentally). The maximum angle tolerance
should be greater than 1°.
Regardless of the settings used, the output of the STL mesh
should not exceed a few hundred megabytes in size (unless it cor-
responds to a very large model). Typically gigabyte sized STL
ﬁles contain details that are far ﬁner than the printing hardware
can reproduce. These very ﬁne features will increase the time re-
quired for slicing, and may cause surface ﬁnish problems during
printing. An example of coarse, ﬁne, and very ﬁne meshes can
be seen in Figure 11.
FIGURE 11.
Coarse (left), ﬁne (center), and very ﬁne (right) meshes
of a mounting bracket.
A ﬁnal issue regarding meshing is that many CAD systems
produce poor quality STL output ﬁles that may contain very high
aspect-ratio facets, or other degenerate features. The use of re-
meshing software such as [15] to produce high-quality meshes is
encouraged. Some extremely high-aspect ratio triangles can be
seen in the ﬁne and very ﬁne portions of Figure 11.
The procedures and practices outlined in this section can be
used to design parts which can be efﬁciently produced using FFF.
8
Copyright © 2015 by ASME


## Page 10

This discussion has primarily involved the geometry, surface ﬁn-
ish, and representation of the part. Details and advice for the
actual fabrication of such parts, particularly with respect to ma-
terial selection and treatment, are given in the next section.
4
Material Selection
In the prior sections, we have discussed the topic of design-
ing a part for efﬁcient FFF production. Once this process has
been completed, we must turn our attention to the actual produc-
tion of such a design. The question of selecting an appropriate
FFF feedstock material remains, as do subsequent questions re-
garding the best practices for low-cost 3D printing with these
materials. In this section, we explore the properties of some of
the most common feedstocks and offer both general and speciﬁc
advice for their employment in inexpensive 3D printers. This
discussion also includes further discussion of tuning the process
parameters given in Table 1. The bulk properties of feedstock
materials are a good place to begin this study. While the FFF
process, particularly the bonding of layers, produces parts with
ultimately different properties, the bulk properties can be useful
for the selection of materials based on application or intended
usage. In Table 2, we give aggregate data on the properties of
four common materials used for FFF.
Of these materials, we have observed ABS and PLA to be
the most common FFF feedstocks for low-cost desktop 3D print-
ing applications, by a large margin. PLA is easier to print and
produces a good surface ﬁnish, but ABS typically produces more
durable parts. There are also a number of newer nylon polymers
that have been developed for FFF, which have not yet been rig-
orously characterized. We discuss practices for successful print-
ing for the materials in Table 2. There are also several general
practices which apply to all of these materials which should be
observed.
4.1
General Material Considerations
Among the materials frequently used in FFF, there are sev-
eral common practices which should be observed. The proper-
ties (from Table 2) of any feedstock material vary considerably
based on variations such as: manufacturer, trade name, or the
presence of additives or colorants. It is therefore necessary to
characterize the properties, especially the extrusion temperature,
when using new materials. It is generally desirable to print at
the highest temperature possible in order to improve bonding be-
tween layers. Printing a series of test specimens, starting at the
minimum temperature from Table 2 and increasing the extruder
temperature until the surface ﬁnish or mechanical accuracy of
the specimen degrades, is the easiest way to dial in this param-
eter. Usually raw polymers, free of dyes or stabilizers, exhibits
the best mechanical strength. Most of the feedstock polymers are
also hygroscopic, and must be stored in a sealed container with
TABLE 2.
Important parameters in the FFF process.
Property
Min.
Max.
Avg.
Units
ABS Acrylonitrile Butadine Styrene [27]
Elastic Modulus
1.00
2.65
2.09
GPa
Tensile Yield Strength
13.0
65.0
41.5
MPa
Tensile Ultimate Strength
23.0
49.0
38.0
MPa
Extrusion Temperature
215
274
229
°C
Max. Service Temperature
60
100
85.2
°C
PLA Polylactide / Polylactic Acid [28]
Elastic Modulus
0.23
13.8
3.63
GPa
Tensile Yield Strength
16.0
103.0 44.7
MPa
Tensile Ultimate Strength
16.0
114
49.3
MPa
Extrusion Temperature
171
220
201
°C
Max. Service Temperature
60
130
77.5
°C
PET Polyethylene Terephthalate [29]
Elastic Modulus
1.83
5.20
3.45
GPa
Tensile Yield Strength
47.0
90.0
62.4
MPa
Tensile Ultimate Strength
22.0
155.0 72.8
MPa
Extrusion Temperature
120
295
252
°C
Max. Service Temperature
100
225
153
°C
Polycarbonate [30]
Elastic Modulus
1.79
3.24
2.38
GPa
Tensile Yield Strength
58.6
70.0
63.7
MPa
Tensile Ultimate Strength
60.0
74.0
67.9
MPa
Extrusion Temperature
250
343
300
°C
Max. Service Temperature
115
135
124
°C
9
Copyright © 2015 by ASME


## Page 11

desiccant. Failure to do so results in steam formation in the ex-
truder’s hot zone, which causes radical degradation of the surface
ﬁnish of the printed part.
It is of paramount importance to ensure that the build plate
is parallel to the plane deﬁned by the x and y-axes of the 3D
printer. While some variation, on the order of 1
2 the layer thick-
ness, is tolerable, variation in the “bed leveling” reduces the geo-
metric accuracy of parts produced and also dramatically reduces
the adhesion of the ﬁrst layer to the print bed. This leads to a
high scrap rate if the printer is not routinely calibrated. While a
feeler gauge can be used to level the bed, this process is itera-
tive and time-consuming. We recommend the fabrication (using
FFF) of a clamp or bracket which allows the attachment of a dial
gage to the extruder body, such as the one shown in Figure 12.
The gauge can then be installed, the bed leveled, and removed in
much less time than leveling using feeler gages. Once the bed
has been accurately leveled in this fashion, the slicer can be in-
structed to print the ﬁrst layer at 1
2 to 3
4 the speciﬁed thickness,
producing a thinner, wider extrusion which adheres more tightly
to the build surface.
FIGURE 12.
Illustration of the use of a dial gauge for bed leveling.
4.2
Printing with PLA
PLA is the easiest material to print using conventional FFF
3D printers, and exhibits good mechanical properties. It is com-
paratively rigid and tends to exhibit fracture and delamination
failures long before yielding can occur.
PLA can be printed
without the use of a heated printbed. Materials such as acrylic
polymer or borosilicate glass are commonly used to construct
the printbed. Adhesion to the printbed can be improved, which
is especially helpful for large prints or those with limited con-
tact areas, by using a heated printbed at 70C. PLA prints can be
smoothed to erase layering artifacts by exposure to several sol-
vents; the most commonly used are methyl ethyl ketone (MEK),
ethyl acetate, and tetrahydrofuran (THF). Vapor smoothing can
be employed by suspending the part on a scaffold within a con-
tainer partially ﬁlled with solvent which is gently heated to pro-
duce vapor. An example of vapor smoothing is shown in Figure
13. Mechanical smoothing, using a brush to physically work sol-
vent against a part, is also feasible. In both cases, care should
be taken due to the ﬂammable and/or toxic nature of the solvents
used.
FIGURE 13.
Bevel gears manufactured from PLA using FFF in the
“as printed” state (at left), and after a 10-second exposure to ethyl ac-
etate vapor at 115 °C (right).
4.3
Printing with ABS
ABS is somewhat more difﬁcult to use for FFF as it typi-
cally exhibits a larger contraction upon cooling. This produces
forces that tend to pull the edges of the part up from the build
plate, which causes the entire part to detach before printing is
ﬁnished. The use of a heated printbed is mandatory. A printbed
temperature of 100-140 °C greatly improves adhesion. There are
several surface treatments which can be applied to the printbed
to further improve adhesion. The application of polyimide tape
can greatly improve adhesion, but adds expense to the printing
process as it requires frequent replacement. The application of a
slurry of ABS (usually produced from printing scraps) dissolved
in acetone which is allowed to evaporate produces an extremely
strong bond to the printbed. A ratio of around 20:1 of acetone
to ABS by weight is typical. High fractions of ABS produce
an excessively strong bond which renders printed parts difﬁcult
to remove from the build plate. A 5:1 mixture of water to water-
10
Copyright © 2015 by ASME


## Page 12

based wood glue produces a reliable surface bond which we have
found to be a good compromise between adhesion and easy part
removal.
The volumetric contraction of ABS as it cools also makes it
difﬁcult to print large parts without a loss of geometric accuracy,
or the formation of fractures in some cases. The use of a heated
enclosure maintaining an air temperature of 70-100 °C greatly
reduces this effect. ABS can be smoothed in the same manner as
described for PLA, but an acetone solvent is most effective.
4.4
Printing with PET
PET is a lightweight material with excellent mechanical
properties which can be used to manufacture high-durability me-
chanical parts using FFF. It is also produced in optically trans-
parent grades which are useful for producing parts compatible
with non-destructive testing regimes (e.g.
food-safe compo-
nents). Higher extrusion temperatures are favorable for promot-
ing transparency; lower temperatures produce an opaque ﬁnish.
PET is generally easier to print than ABS and does not require a
heated bed. Sufﬁcient adhesion can be achieved by applying blue
“painters tape” to the build plate. PET can also be smoothed us-
ing MEK or ethyl acetate. Care must be taken due to the toxic
and/or ﬂammable properties of these solvents.
4.5
Printing with Polycarbonate
Like PET, polycarbonate can be used to print high-durability
parts. Anecdotal evidence [31] indicates that it has successfully
been used to print high-speed rotating components for indus-
trial machinery. The downside of this material is that it requires
higher extrusion temperatures than many commodity 3D print-
ers are capable of producing. Printbed adhesion is most easily
achieved by using a polyimide tape coating. As with PET, higher
temperatures promote transparency in the printed part, and in the
case of polycarbonate higher temperatures are required to pre-
vent the formation of residual stresses. We have not conducted
experiments regarding the smoothing of polycarbonate parts, but
in theory any applicable solvent such as dichloromethane may
be used. Generally, the solvents appropriate for use in smooth-
ing polycarbonate are toxic, and care must be taken in their use.
The discussion in this section is limited to the bulk properties of
common FFF feedstock materials, and outlines their proper use
along with advice for their employment in 3D printing. In the
next section we concern ourselves with the “as printed” proper-
ties of structures produced from these feedstocks, and the com-
plex responses that they exhibit.
5
Anisotropy in FFF Structures
In many applications, objects produced using FFF need only
be the correct shape, and no speciﬁc mechanical properties are
required. Architectural models [32], simple toys, and artistic
sculptures [33] are examples of this sort of application; inex-
pensive desktop 3D printers have been used with great success
in these ﬁelds.
In these cases, the design and printing prac-
tices outlined in the previous sections can be used without mod-
iﬁcation.
However, there is a strong desire in both hobbyist
and professional communities to produce serviceable mechan-
ical and structural parts using FFF on inexpensive commodity
hardware. These applications require printed parts which exhibit
sufﬁcient strength, stiffness, wear resistance, or other properties.
It is therefore important to be able to estimate the mechanical
properties of a FFF-produced part before it is printed in order to
augment and inform the design process outlined previously. Fail-
ure to estimate mechanical properties accurately reduces the de-
sign process to a trial-and-error exercise which results in wasted
production time and material. Unfortunately, the complex geom-
etry and anisotropic constitutive response of FFF-produced parts
complicates this process greatly.
5.1
Sources of Anisotropic Behavior
The anisotropic behavior of FFF-produced parts has previ-
ously been observed and remarked upon [34-36]. This anisotropy
results from:
1. The pattern and orientation of the sparse inﬁll used [35].
2. The temperature-dependant nature of the bonding between
successively extruded polymer ﬁlaments.
Anisotropy due to the sparse inﬁll is caused by the inability
of the internal air voids which are formed to support mechanical
loads. Consider the case of rectilinear inﬁll as shown in Figure
9: each layer is printed with strands oriented in the same direc-
tion, and successive layers create the crosshatched pattern seen.
This implies that any given layer is relatively stiff along the di-
rection of the extruded strands, and relatively compliant in the
orthogonal direction. Stacking these layers results in orthotropic
behavior such as that typically seen in polymer-matrix compos-
ites [37].
The second source of anisotropy has been explored to a
lesser extent. Generally, the bonding of molten polymers is con-
trolled by a diffusion process [38, 39] which is dependent on the
temperature and contact pressure in the bonding zone, as well
as the time allowed for diffusion to occur. Given that bonding
in the FFF process occurs at ambient pressure, it appears that
printing speed is the primary factor in developing bond strength.
However, temperature difference also plays a major role [40]. If
the extruder is laying down molten polymer against freshly de-
posited substrate which is still near the extrusion temperature, the
local temperature will be high, thus promoting strong bonding.
However if the extruder is depositing plastic against a substrate
which has been allowed to cool, such as when beginning a new
layer of a large part, the bonding temperature will be compara-
tively low and result the resulting bonds will be far weaker.
11
Copyright © 2015 by ASME


## Page 13

The weak bonding between layers produced by thermal ef-
fects is compounded by the orthotropic material properties pro-
duced by the inﬁll.
The alternating stiffness and compliance
along a given axis in each layer produce stress concentrations be-
tween the layers. We conducted a simple numerical and physical
experimental pair to demonstrate this phenomenon. An ANSYS
ﬁnite-element model was used to model an orthotropic material
specimen of double-notch geometry with properties correspond-
ing to raw ABS polymer. A torsion load was applied in order to
produce the theorized stress concentration. The physical spec-
imen, when similar loads were applied, exhibited a delamina-
tion/fracture failure originating in the same location, and follow-
ing the same path, as predicted in the numeric model. These
results are shown in Figure 14. The geometry of the simulated
model differs from that of the physical specimen as the mechan-
ically gripped areas were presumed to be completely rigid, and
not simulated.
FIGURE 14.
FFF test specimen under simulated loading in AN-
SYS ﬁnite-element analysis (top left), with magniﬁed portion showing
inter-lamina stress concentrations (top right). A physical test specimen
which has failed due to these delamination forces (bottom center) is also
shown, with edges and fractures digitally highlighted for clarity.
This theoretical understanding is born out both in the
demonstration of Figure 14, and by observations during produc-
tion. Extrusions within one print layer bond at a relatively high
temperature especially due to the rasterized deposition which is
typically employed. The temperature is much lower for bonds
between layers, accounting for the poor strength of parts in this
direction.
5.2
Mitigating Anisotropic Effects
Given the sources of anisotropy outlined in the previous sec-
tion, it appears that there are only a few steps that can be taken
to improve the mechanical properties of FFF parts in order to
enable the manufacture of robust components. These include:
1. printing as slowly as is economical.
2. Extruding the highest temperature possible without degrad-
ing surface ﬁnish and geometric accuracy.
3. Designing parts to carry axial loads in the plane parallel to
the build surface.
4. Designing parts such that moment loads do not induce ex-
cessive inter-ply forces.
Of these recommendations, the fourth is most problematic.
Due to the high geometric complexity of typical FFF compo-
nents, computer simulation to determine interplay forces is infea-
sible for all but the simplest test cases. The application of tradi-
tional design methods for orthotropic polymer composites is not
appropriate either, as composites are almost never used to con-
struct large solid objects. Additionally, a typical FFF part may
consist of thousands of lamina rendering many of the computa-
tional techniques for composite design infeasible as well. This
indicates that there is a strong need to develop better design tools
for the analysis of FFF parts and structures.
6
Future Work and the Path Ahead
The discussion of anisotropy in Section 5 makes it clear that
there is a strong need for both better constitutive models of FFF-
produced material behaviors, and simulation methods which can
be used to predict the performance properties of components
manufactured from these materials. The development of these
methods will enable the extension of the practices given in Sec-
tions 3 and 4. We speculate that a mixed numerical-experimental
approach to this problem is appropriate. Given the loose sim-
ilarity between FFF materials and polymer composites, it may
be advantageous to utilize recently developed multiaxial robotic
testing techniques [41, 42] as part of this effort. The de-facto
choice of ﬁnite-element analysis for exploiting these constitutive
models should also be carefully considered. In our opinion, a
discrete element method [43] or hybrid ﬁnite/discrete element
method [44] formulation may be more appropriate. These meth-
ods offer superior performance in the analysis of discontinuous
failure modes (i.e. cracking and delamination) which we have
observed to be the dominant modes of failure in FFF compo-
nents.
There is a great deal of ongoing research into specialized
feedstock materials for FFF, such as electrically conductive, ther-
12
Copyright © 2015 by ASME


## Page 14

mochromic, or ﬁlled/ﬁber-reinforced ﬁlaments. These new prod-
ucts are largely uncharacterized, and require additional study.
The development of design guidelines to allow efﬁcient man-
ufacturing using these materials is also necessary. The use of
electrically conductive materials may offer an interesting oppor-
tunity; if electrical properties are proportional to bond strength,
as we might reasonably expect in a diffusion-driven process, then
electrical conductance may serve as a useful diagnostic or non-
destructive testing technique.
7
Conclusions
This work is an attempt to collect and formalize a great deal
of well-known but largely uncommunicated knowledge regard-
ing FFF. In the preceding sections we have provided a broad out-
line of the FFF process, and enumerated the parameters which
govern this process. This led to a presentation of practices which
enable efﬁcient and economical production using FFF using low-
cost, commonly available 3D printing hardware. These design
practices led to a discussion of bulk material properties, and the
discussion of how these feedstock materials should be selected
and printed. Moving on from bulk properties, we proceeded to
the subject of anisotropy, and the role that it plays in FFF tech-
nology. The sources of anisotropy were examined, and a nu-
meric/physical experiment illustrated their effect. This examina-
tion of anisotropy also illuminates some of the shortcomings of
current design methods and tools in a clear light, and we gave our
opinions on the best path towards addressing these deﬁciencies.
By researching and discussing these topics, we present a re-
source which is of beneﬁt to researchers in the ﬁeld of manufac-
turing science, and industrial professionals who are either con-
sidering the use of FFF-enabled technologies such as 3D print-
ing, or those who have already entered production and are op-
timizing their fabrication process. In so doing, we hope to mo-
tivate and enable increased effective use of FFF 3D printing for
both research and industrial applications. It is clear that this is not
a ﬁnished effort, and that there is a great deal of future research
which is required to fully realize the potential of FFF manufac-
turing.
ACKNOWLEDGMENT
The authors would like to acknowledge the advice and sup-
port of those involved with the Engineering Design Program and
Design Innovation and Computational Engineering Laboratory at
the Colorado School of Mines in completing this paper. A mod-
iﬁed Percent Contribution Indicated (PCI) approach has been
used to assign equal contributions to Dr. Cameron J. Turner and
Dr. Douglas L. Van Bossuyt as corresponding authors as de-
scribed within [45].
References
1. C. Chua, K. Leong, and C. Lim, 2010, Rapid Prototyping:
Principles and Applications, World Scientiﬁc Press.
2. M. Frauenfelder, 2012, Make: Ulitmate Guide to 3D Print-
ing, O’Reiley Media.
3. A. France, 2013, Make: 3D Printing: The Essential Guide
to 3D Printers, Maker Media Inc.
4. M. Frauenfelder, 2013, Make: Ultimate Guide to 3D Print-
ing 2014, Maker Media Inc.
5. B. Wittbrodt, A. Glover, J. Laureto, G. Anzalone, D.
Oppliger, J. Irwin, and J. Pearce, 2013, “Life-cycle eco-
nomic analysis of distributed manufacturing with open-
source 3-D printers,” Mechatronics, 23(6):713-726.
6. J. Pearce, 2012, “Building Research Equipment with Free,
Open-Source Hardware,” Science, 337(6100):1303-1304.
7. M. Agarwala, D. Bourell, J. Beaman, H. Marcus, and J. Bar-
low, 1995, “Direct selective laser sintering of metals,” Rapid
Prototyping Journal, 1(1):26-36.
8. E. Sachs, M. Cima, P. Wiliams, D. Brancazio, and J. Cornie,
1992, “Three Dimensional Printing: Rapid Tooling and Pro-
totypes Directly from a CAD Model,” Journal of Manufac-
turing Science and Engineering, 114(4):481-488.
9. A. Dolenc and I. Makela, 1994, “Slicing procedures for lay-
ered manufacturing techniques,” Computer-Aided Design,
26(2):119-126.
10. R. Crawford, 1993, “Computer aspects of solid freeform
fabrication: geometry, process control, and design,” Pro-
ceedings of the 1993 Solid Freeform Fabrication Sympo-
sium, p. 102-111.
11. P. Kulkarni and D. Dutta, 1996, “An accurate slicing proce-
dure for layered manufacturing,” Computer-Aided Design,
28(9):683-697.
12. P. Pandey, N. Reddy and S. Dhande, 2003, “Real time adap-
tive slicing for fused deposition modeling,” International
Journal of Machine Tools and Manufacture, 43(1):61-71.
13. S. Singamneni, A. Roychoudhury, O. Diegel and B. Huang,
2012, “Modeling and evaluation of curved layer fused
deposition,” Journal of Materials Processing Technology,
212(1):27-35.
14. B. Huang and S. Singamneni, 2014, “Adaptive slicing and
speed- and time-dependent consolidation mechanisms in
fused deposition modeling,” Journal of Engineering Man-
ufacture, doi:10.1177/0954405413497474.
15. P. Cignoni, M. Callieri, M. Corsini, M. Dellepiane, F.
Ganovelli, and G. Ranzuglia, 2008, “MeshLab: an Open-
Source Mesh Processing Tool,” Proceedings of Eurograph-
ics 2008 Italian Chapter Conference, p. 129-136.
16. B. Evans, 2012, Practical 3D Printers, Ch. 4, Apress Pub-
lishing.
17. C. Richter and H. Lipson, 2011, “Untethered Hovering Flap-
ping Flight of a 3D-Printed Mechanical Insect,” Artiﬁcial
Life, 17(2):73-86.
13
Copyright © 2015 by ASME


## Page 15

18. H. Lipson, F. Moon, J. Hai, and C. Paventi, 2004, “3-D Print-
ing the History of Mechanisms,” Journal of Mechanical De-
sign, 127(5):1029-1033.
19. U. Klammert, U. Gbureck, E. Vorndran, J. Rodiger, P.
Meyer-Marcotty, and A. Kubler, 2010, “3D powder printed
calcium phosphate implants for reconstruction of cranial
and maxillofacial defects,” Journal of Cranio-Maxillofacial
Surgery, 38(8):565-570.
20. L. Shor, M. Gandhi, X. Wen, W. Sun and S. Geri,
2008,
“Solid
Freeform
Fabrication
of
Polycapro-
lactone?Hydroxyapatite
Tissue
Scaffolds,”
Journal
of
Manufacturing
Science
and
Engineering”,
130(2)
doi:10.1115/1.2898411.
21. P. Alexander, S. Allen, and D. Dutta, 1998, “Part orienta-
tion and build cost determination in layered manufacturing,”
Computer Aided Design, 30(5):343-356.
22. K. Thrimurthulu, P. Pandey and N. Reddy, 2004, “Optimum
part deposition orientation in fused deposition modeling,”
International Journal of Machine Tools and Manufacture,
44:585-594.
23. P. Pandey, N. Reddy, and S.G. Dhande, 2007, “Part depo-
sition orientation studies in layered manufacturing,” Journal
of Materials Processing Technology, 185:125-131.
24. H. Byun and K. Lee, 2006, “Determination of the op-
timal build direction for different rapid prototyping pro-
cesses using multi-criterion decision making,” Robotics and
Computer-Integrated Manufacturing, 22:69-80.
25. G. Navangul, R. Paul, and S. Anand, 2013, “Error mini-
mization in layered manufacturing parts by stereolithogra-
phy ﬁle modiﬁcation using a vertex translation algorithm,”
Journal of Manufacturing Science and Engineering, 135(3)
doi:0.1115/1.4024035.
26. V. Kumar and D. Dutta, 1997, “An assessment of data for-
mats for layered manufacturing,” Advances in Engineering
Software, 28(3):151-164.
27. Material
Data
Sheet:
“Overview
of
materials
for
Acrylonitrile
Butadiene
Styrene
(ABS),
Extruded,”
http://www.matweb.com, Accessed April 7, 2014.
28. Material Data Sheet: “Overview of materials for Polylac-
tic Acid (PLA) Biopolymer,” http://www.matweb.com, Ac-
cessed April 8, 2014.
29. Material Data Sheet:
“Overview of materials for Poly-
carbonate, Extruded,” http://www.matweb.com, Accessed
April 7, 2014.
30. Material
Data
Sheet:
“Overview
of
materials
for
Polyethylene
Terephthalate
(PET),
Unreinforced,”
http://www.matweb.com, Accessed April 9, 2014.
31. K.
Moswen,
“FDM
Polycarbonate,”
http://www.stratasys.com/resources/case-
studies/commercial-products/fdm-polycarbonate, Accessed
April 2, 2014.
32. M. Stokes, 2013, 3D Printing for Architects with MakerBot,
Packt Publishing Ltd.
33. S. Hoskins and S. Hoskins, 2014, 3D Printing for Artists,
Designers and Makers: Technology Crossing Art and Indus-
try, Bloomsbury Academic Press.
34. A. Bellini and S. Guceri, 2003, “Mechanical characteriza-
tion of parts fabricated using fused deposition modeling,”
Rapid Prototyping Journal, 9(4):252-264.
35. S. Ahn, M. Montero, D. Odell, S. Roundy, and P. Wright,
2002, “Anisotropic material properties of fused deposition
modeling ABS,” Rapid Prototyping Journal, 8(4):248-257.
36. D. Hutmacher, T. Schantz, I. Zein, K. Ng, S. Teoh, and K.
Tan, 2001, “Mechanical properties and cell cultural response
of polycaprolactone scaffolds designed and fabricated via
fused deposition modeling,” Journal of Biomedical Materi-
als Research, 55(2):203-216.
37. J. Berthelot, 1999, Composite Materials: Mechanical Be-
havior and Structural Analysis, Springer.
38. K. Jud, H. Kausch and J. Williams, 1981, “Fracture mechan-
ics studies of crack healing and welding of polymers,” Jour-
nal of Materials Science, 16:204-210.
39. D. Kline and R. Wool, 2004, “Polymer welding relations in-
vestigated by a lap shear joint method,” Polymer Engineer-
ing and Science, 28(1):52-57.
40. X. Zhu, G. Liu, Y. Guo, and Y. Tian, 2007, “Study of PMMA
thermal bonding,” Microsystems Technology, 13:403-407.
41. J. Michopoulos, J. Hermanson, A. Iliopoulos, S. Lambrakos,
and T. Furukawa, 2011, “Data-Driven Design Optimization
for Composite Material Characterization,” Journal of Com-
puting and Information Science in Engineering, 11(2):1-10.
42. J. Steuben, J. Michopoulos, A. Iliopoulos, and C. Turner,
2013, “Inverse Characterization of Composite Materials Us-
ing Surrogate Models,” Proceedings of the 2013 ASME
IDETC/CIE Conferences.
43. J. Williams, G. Hocking, and G. Mustoe, 1985, “The theo-
retical basis of the discrete element method,” Proceedings of
the 1985 international conference on numerical methods in
engineering.
44. A. Munjiza and D. Owen, 1995, “A combined ﬁnite-discrete
element method in transient dynamics of fracturing solids,”
Engineering Computations, 12(2):145-174.
45. T. Tscharntke, M. Hochberg, T. Rand, V. Resh, and J.
Krauss, 2007, “Author Sequence and Credit for Contribu-
tions in Multiauthored Publications,” PLoS Biol, 5(1):e18.
14
Copyright © 2015 by ASME
View publication stats



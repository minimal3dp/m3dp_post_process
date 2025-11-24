# 

**Source:** `Using artificial.pdf`
---

## Page 1

461
INTRODUCTION
3D printing technology – particularly meth­
ods such as fused filament fabrication (FFF) and 
fused deposition modeling (FDM) – has become 
increasingly popular in both industrial and home 
applications. A crucial element of the 3D print­
ing process is the preparation of input files for the 
printer – so-called g-code files – which contain all 
the information necessary for the correct execu­
tion of the print. These files control and command 
the movements of the actuators responsible for 
nozzle positioning over the build area in the XYZ 
axes, the speed of the extruder mechanism, noz­
zle and bed temperatures, as well as many other 
critical printing parameters.
Traditional methods of generating g-code, im­
plemented in so-called slicers, rely on determinis­
tic algorithms that do not always lead to optimal 
results in terms of print quality [1, 2], build time, 
or material consumption [3, 4]. An interesting 
study is presented in [1], where the dimensional 
accuracy of a test part – compliant with the ISO 
16792:2021-04 standard – was evaluated. The 
Using artificial intelligence to optimize g-code files for fused 
filament fabrication/fused deposition modeling technology
Zbigniew Andrzej Pilch1* , Maciej Gibas1
1	 Faculty of Electrical Engineering, Cracow University of Technology, ul. Warszawska 24, Kraków, Poland
* Corresponding author’s e-mail: zbigniew.pilch@pk.edu.pl
ABSTRACT
3D printing technology – particularly thermoplastic-based methods such as fused filament fabrication (FFF) and 
fused deposition modeling (FDM) – has gained popularity in both industrial and home settings. A key element 
of the 3D-printing process is the preparation of the printer’s batch files – so-called g-code files – which contain 
all the information needed for correct execution of the print. Traditional methods of generating g-code rely on 
deterministic algorithms that do not always yield optimal results in terms of print quality (dimensional accuracy 
of the geometry), build time, material consumption, and functional parameters such as the mechanical strength of 
the printed part. In recent years, interest has grown in using artificial intelligence (AI) to optimize these processes. 
AI algorithms, including machine learning and deep learning, have the potential to analyse and optimize g-code 
in ways that surpass traditional approaches, offering higher print quality, greater energy efficiency, and shorter 
production times. This work explores the modification of print parameters recorded in g-code files through the 
use of AI, demonstrating that the modified files produce prints with improved mechanical strength. A large lan­
guage model (ChatGPT-4o) was used to selectively modify nozzle temperature parameters in g-code files, based 
on prompt engineering and filament datasheets. Tensile samples made from Easy PLA and Easy PET-G filaments 
were printed and tested in three-point bending, in accordance with ISO 14125. The samples were divided into 
three groups: unmodified (reference), modified every 2 layers, and modified every 3 layers. The results showed an 
increase in the average breaking force for PLA samples by 2.7% and 3.0%, and for PET-G samples by 4.3% and 
9.9%, respectively. Comparative analysis of the g-code files confirmed that the AI introduced cyclic temperature 
changes (increase in M104 commands from 3 to 30), improving interlayer adhesion. The flexural strength im­
provements were consistent with these modifications. In conclusion, AI-driven g-code optimization offers a simple 
and effective way to improve the mechanical properties of printed objects without altering geometry or increasing 
material usage. This approach holds great potential for advancing additive manufacturing processes, particularly 
in the context of Industry 4.0.
Keywords: additive manufacturing ; FFF/FDM technology, AI, optymize g-code.
Received: 2025.06.06
Accepted: 2025.08.10
Published: 2025.09.01
Advances in Science and Technology Research Journal, 2025, 19(10), 461–474
https://doi.org/10.12913/22998624/208233
ISSN 2299-8624, License CC-BY 4.0
Advances in Science and Technology 
Research Journal


## Page 2

462
Advances in Science and Technology Research Journal 2025, 19(10), 461–474
dimensional fidelity of prints created using FDM, 
SLA, and SLS methods was compared against 
the original CAD model. In [2], the influence of 
printing speed on the surface quality of printed 
components was investigated. Other studies focus 
on the mechanical properties of prints depending 
on infill pattern [5], material type [6], nozzle di­
ameter [5], or the temperature distribution within 
the printing zone [7].
In recent years, interest in the application of 
artificial intelligence (AI) to optimize these pro­
cesses has grown significantly. AI algorithms, in­
cluding machine learning and deep learning, have 
the potential to analyze and optimize g-code files 
in ways that surpass traditional approaches, offer­
ing improved print quality, enhanced energy effi­
ciency, and reduced production time [8], [9], [10].
3D printing technology
The origins of 3D printing technology date 
back to the 1980s, when Charles Hull began work 
on this manufacturing method for the purpose of 
rapid prototyping [11]. A key milestone in the de­
velopment of 3D printing was the creation of the 
STL file format (STereoLithography or Standard 
Tessellation Language) in 1983, which enabled 
communication between the 3D printer and the 
digital model. The first 3D printer was developed 
by Charles Hull and 3D Systems, and was named 
the Stereolithography Apparatus (SLA). The first 
commercial solution, called SLA 250, was intro­
duced in 1988 [11].
In 1990, the FDM technique was developed 
by Scott Crump, and the first patent application 
for 3D printing technology was filed in 1993. In 
recent years, 3D printing technology has expe­
rienced rapid growth, with numerous compa­
nies entering the market to develop increasingly 
advanced, reliable, and functional devices, as 
well as materials used in the printing process. 
Additive manufacturing technologies currently 
developed and implemented can be divided into 
three main groups:
	•
Printing with thermoplastic filaments, shaped 
into strands of a specified diameter, which are 
fed into a print head that melts and deposits 
the material layer by layer. This group in­
cludes FFF/FDM methods.
	•
Printing with photosensitive resins, which 
are locally cured by a light source. The light 
source may be a laser beam (SLA), a projector 
lamp (DLP), or an LED array (LED method).
	•
Printing with powdered materials, including 
CJP (gypsum), SLS (plastics), and SLM (met­
al powders).
All 3D printing methods require proper prepa­
ration of digital models. The complete cycle from 
idea to finished 3D-printed object is illustrated 
in Figure 1. In the classical approach, a virtual 
model is obtained either through CAD software 
modeling or by using one of the methods applied 
in reverse engineering (such as 3D scanning, pho­
togrammetry, coordinate measuring machines, 
etc.). Once the model is created, it is exported to 
a standard STL file, which is then processed in a 
slicer. The end result is a generated g-code file 
(for FFF/FDM technology), which is interpreted 
by the printer’s processor to execute movements 
along the respective axes.
The diversity of 3D printing methods has 
made this technology – originally classified as a 
rapid prototyping method – widely applicable not 
only in engineering but also in scientific research, 
art, and education. Examples of engineering ap­
plications include the fabrication of complex ge­
ometric shapes for planar and spatial electronics 
solutions [12], or the printing of blades for small 
wind turbines [13]. An example of such additive 
technology applications in other fields is bioprint­
ing in medicine [14]. Ferro et al. [15] are work­
ing on new structures made using SLM (selective 
laser melting) technology for anti-icing solutions 
Figure 1. Flow chart of the process of making a real model using FFF/FDM additive technology - classical 
procedure


## Page 3

463
Advances in Science and Technology Research Journal 2025, 19(10) 461–474
in aluminum. It is worth noting the emergence 
of studies on 4D printing [16], which involves 
materials that respond to external stimuli. Junk 
and colleagues have explored the possibility of 
printing grippers for specialized applications, in 
which the gripper closes as a result of tempera­
ture increase. Another branch of additive method 
development is the introduction of new types of 
materials. For instance, Kotorčević et al. [17] ex­
amined the use of PLA filament doped with cop­
per for water filtration systems. Kujawa et al. [18] 
investigated the improvement of tribological and 
strength properties of PLA material doped with 
MoC2. They demonstrated an improvement in 
the quality of printed objects and an improvement 
in their resistance to external loads. Zubrzycki 
et al. [19] investigated the influence of printing 
parameters (layer height, temperature and print­
ing speed) on the mechanical strength of samples 
made of ABS, PLA and PET-G materials.
To summarize, in every described case and 
development direction of additive manufacturing 
methods, users aim for the final printed part to 
be as accurate as possible compared to the CAD 
model - ensuring dimensional fidelity [1], mini­
mizing print time, and maximizing the mechanical 
properties of the printed part, as achievable with 
the input material. These criteria often conflict 
with each other. For example, increasing the print 
speed (to reduce print time) increases vibrations 
in the printer, which can degrade print quality [2]. 
Meeting all of these criteria simultaneously 
is challenging, but continuous improvements are 
being explored. One such effort is the study by 
Liu et al. [20], in which the traveling salesman 
optimization method was used to reduce idle noz­
zle movements (i.e., non-extruding travel), there­
by minimizing stringing effects that negatively 
affect print quality. On the other hand, Jadayel 
and Khameneifar [21] focused on improving print 
quality by modifying the STL file based on scans 
of a test print, without altering the g-code itself.
Artifical intelligence
Modern technological advancement is in­
creasingly focused on implementing the principles 
of Industry 4.0. One of the most transformative 
tools in this context is artificial intelligence (AI), 
which is revolutionizing industrial processes [22]. 
AI offers a wide range of capabilities depending 
on how the neural network is designed by the pro­
grammer. It can, for example, predict undesirable 
events through real-time data monitoring using 
purpose-specific sensors. This can involve statisti­
cal analysis or image detection and interpretation.
Beyond monitoring and diagnostics, AI sys­
tems are capable of autonomous decision-making 
and initiating appropriate procedures in response 
to various situations. The most commonly used 
methods for such purposes include linear regres­
sion and decision trees. This reduces the level of 
human intervention in industrial processes, shift­
ing the human role from primary operator to over­
seer, thereby minimizing human error. However, 
such applications require specialized knowledge 
in AI programming – typically using Python and 
libraries such as Keras, PyTorch, or TensorFlow.
Thanks to the development of large language 
models (LLMs) like ChatGPT, Gemini, or Copi­
lot, even users with limited programming experi­
ence can now create specialized tools. This is done 
through the crafting of well-designed “prompts” 
– commands or instructions that guide the AI to 
carry out specific tasks. AI has also found its way 
into 3D printing, especially in areas related to ma­
chine learning for process diagnostics and moni­
toring. With properly trained algorithms, a 3D 
printer can autonomously detect issues such as:
	•
print detachment from the bed,
	•
stringing defects,
	•
inadequate nozzle temperature leading to in­
consistent filament flow,
	•
clogged nozzles resulting in filament feed 
failure,
	•
filament depletion.
These issues can be detected using image 
analysis, which requires the integration of a 
camera with the printer to enable real-time im­
age processing. Some companies have already 
implemented such solutions. For instance, Bam­
bulab offers high-end printers that operate auton­
omously without requiring user intervention in 
the control system. In contrast, printers like the 
Ender 3 V3 Plus by Creality provide similar print 
speeds and quality, but integrating AI into these 
machines requires purchasing a compatible cam­
era and having basic technical skills.
Creating an AI-based print monitoring and 
diagnostic system is possible for nearly any 
3D printer equipped with a network interface. 
A Raspberry Pi microcontroller can be used 
to host a VPN server and process image data, 
though success may be limited by factors such 
as network latency, interruptions, or whether the 


## Page 4

464
Advances in Science and Technology Research Journal 2025, 19(10), 461–474
microcontroller’s processor can handle AI algo­
rithms, real-time image processing, and remote 
server operation simultaneously.
AI in 3D printing can be applied as early as 
the prototyping stage. Since the actual printing 
process is the final step in additive manufactur­
ing, generative modeling offers an opportunity to 
design parts with optimized geometries that are 
difficult to achieve using traditional modeling 
methods – while still meeting mechanical strength 
requirements. This can reduce material use with­
out compromising performance. In such cases, 
the user first creates a base shape, after which AI 
performs the optimization process.
This article also explores repeating the AI-as­
sisted optimization at the next stage: converting 
the STL file to g-code. Since g-code is a sequence 
of machine instructions and functions as a pro­
gramming language, it can be analyzed and modi­
fied like any other code – even by large language 
models like successive versions of ChatGPT. 
This practice is becoming increasingly common 
among both beginner and advanced developers.
This trend raises concerns about the potential 
impact on the job market, particularly for program­
mers who may be partially replaced by AI. The 
phenomenon – known as “prompt engineering” – 
is rapidly gaining traction and reshaping various 
long-standing professions. One could argue we 
are witnessing yet another industrial revolution.
Nvidia CEO Jensen Huang has even stated 
publicly that English is becoming one of the new 
programming languages – alongside Python, C, 
C#, C++, Java, and others [23]. While this was un­
thinkable until recently, the translation of human 
thought into code capable of generating or modi­
fying professional-grade software is now increas­
ingly achievable with each advancement in LLMs.
Advanced engineering software like MAT­
LAB already supports custom script execution 
for analysis, simulation, and control across many 
technical fields. Large language models such as 
ChatGPT now have the capability to generate 
such scripts. Moreover, even if it’s not yet possi­
ble to directly create a Simulink file (block-based 
graphical programming), AI can generate MAT­
LAB scripts that, when run, build the desired 
block sequence programmatically.
MATERIALS AND METHODS
Among the many filaments available on the 
market, two widely used and readily accessible 
types were selected: Easy PLA [24] and Easy PET-
G [25], both manufactured by Fiberlogy. For each 
of these filaments, the manufacturer provides es­
sential printing parameters (such as temperature 
and mechanical), which are summarized in Table 1.
Slicing computer program
The samples for comparative testing were 
modeled in the Autodesk Fusion 360 environment. 
The resulting STL models were then sliced using 
Cura – a popular, free, and open-source software 
widely used by additive manufacturing enthusi­
asts. Cura enables the generation of g-code files 
for printers operating with FFF/FDM technology.
Cura offers more than 400 customizable set­
tings, allowing for precise control over various 
aspects of the 3D model before printing. These in­
clude parameters such as layer height, infill, sup­
ports, wall thickness, cooling settings, and many 
others. The software integrates seamlessly with 
numerous popular CAD programs (e.g., Solid­
Works, Autodesk Inventor), facilitating a smooth 
transition from design to print. Importantly, Cura 
is compatible with a wide range of file formats, 
including STL, OBJ, X3D, 3MF, BMP, GIF, JPG, 
and PNG. Another key advantage is its ability to 
import material profiles from leading filament 
manufacturers, streamlining the process of setting 
optimal print parameters.
Table 1. Printing and technical basic parameters of the tested filaments – data provided by the filament manufacturer. 
[24, 25]
Material
Nozzle temp. °C
Bed temp. °C
Airflow %
Print aver. mm/s
Easy PLA
200–230
50–70
75–100
<100
Easy PET-G
220–250
90
0–25
<100
Material
Density g/cm3
Flexural modulus
MPa
Flexural strength MPa
Tensile modulus MPa
Easy PLA
1.24
3800
81
3500
Easy PET-G
1.27
2000
70
2800


## Page 5

465
Advances in Science and Technology Research Journal 2025, 19(10) 461–474
POINT BENDING STATION
The configuration of the measurement setup for 
testing the samples is shown in Figure 2. The com­
ponents are labelled with the following numbers:
1.	NEMA 57BYGH76 280 4a 4.25g stepper mo­
tor with a 4.25:1 gear ratio,
2.	DM860H stepper motor driver,
3.	Raspberry Pi 4,
4.	HDMI LCD display,
5.	Mechanism for converting rotary motion to 
linear motion using a TR8 trapezoidal threaded 
screw,
6.	Manson NTP-5531 laboratory power supply,
7.	Computer for data acquisition,
8.	Arduino Uno R3,
9.	SparkFun load cell amplifier,
10.	Test sample compliant with ISO 14125,
11.	NA27 strain gauge load cells.
To enable measurements on the constructed 
test stand, it is necessary to determine the quan­
tities that allow for identifying the displacement 
of the element applying pressure to the samples. 
The analysis began by calculating the relationship 
between the number of motor steps, the gear ratio, 
and the lead screw pitch. The number of steps per 
rotation was calculated using Equation 1:
	
𝑁𝑁𝑠𝑠=
360°
𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎=
360°
1.8° = 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠/𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟 	 (1)
where:	angstep = 1.80° – step angle of the NEMA 
57BYGH76 stepper motor.
The displacement of the carriage ∆x per one 
step of the stepper motor is calculated using 
Equation 2:
	
∆𝑥𝑥=
𝑃𝑃
𝑁𝑁𝑠𝑠 × 𝑖𝑖 𝑥𝑥𝑖𝑛𝑛	
(2)
where:	P = 8 mm – lead of the TR8 trapezoidal 
screw, i = 4.25 – gear ratio.
After substituting the values, we obtain the 
displacement △x = 0.0094 mm. The step constant 
was set in the motor driver to △t = 0.005 s, which 
means the motor performs 200 steps per second 
(1 full rotation), resulting in the screw moving 
200 · △x = 200·0.0094 = 1.88 mm/s. A key com­
ponent enabling the determination of the fracture 
forces of the samples is the strain gauge beams 
used in the test stand. The basic parameters of the 
strain gauge beams are presented in Table 2.
In the case of the considered tests, the load­
ing of the beams and the force measurement are 
performed in only one direction (Figure 3a). 
Hysteresis error becomes significant in measure­
ments where the deformation of the beams and 
the readings would be carried out bidirectionally 
(Figure 3b).
The repeatability coefficient was verified by 
repeatedly performing measurements involving 
Figure 2. Station for testing the strength of printed samples


## Page 6

466
Advances in Science and Technology Research Journal 2025, 19(10), 461–474
an increase in the applied force followed by its 
return to a value close to 0 N. This approach al­
lows for demonstrating the accuracy with which 
the force increases as a function of the sample’s 
displacement. The results of the recorded meas­
urements for both increasing and decreasing 
force values are presented in Figure 4. The area 
corresponding to force increase, marked with a 
frame, represents the sample fracture experiment 
(Figure 3).
Subsequently, the Type A uncertainty was 
determined (this type of uncertainty is calculat­
ed based on measurements).To determine it, the 
arithmetic mean of the performed measurements 
must be calculated according to the following 
formula:
	𝑥𝑁𝑠𝑖
𝑥𝑥̅ =
1
𝑛𝑛∑
𝑥𝑥𝑖𝑖
𝑛𝑛
𝑖𝑖=1
 𝑠	
(3)
where:	n = 4 – number of trials, xᵢ – value of the 
measurement in the i-th trial.
Based on the arithmetic mean (Eq. (3)), the 
standard deviation is calculated as follows [26]:
	𝑥𝑛𝑛𝑥𝑖𝑖
𝑠𝑠= √
1
𝑛𝑛(𝑛𝑛−1) ∑
(𝑥𝑥𝑖𝑖−𝑥𝑥̅)2
𝑛𝑛
𝑖𝑖=1
 𝑢𝐴𝑠	
(4)
Finally, the Type A uncertainty (standard un­
certainty of the mean) is calculated using Equa­
tion 5:
	𝑠𝑛𝑛𝑛𝑛
𝑢𝑢𝐴𝐴=
𝑠𝑠
√𝑛𝑛 	
(5)
The result of this experiment in the form of 
a measurement table (shown for example for the 
Table 2. Basic parameters of the NA27 strain gauge beams, with dimensions 80 × 13× 13 mm, used in the 
measurement system
Measure range N
non-linearity %F.S.
Hysteresis %F.S.
Repeatability %F.S.
100
0.03
0.03
0.03
Figure 3. Loading variants of the measurement beams: (a) unidirectional loading variant, (b) bidirectional 
loading variant
Figure 4. Results of the four performed loading tests of the strain gauge beams


## Page 7

467
Advances in Science and Technology Research Journal 2025, 19(10) 461–474
first 5 measurements out of 68 recorded for each 
trial) is presented in Table 3.
Based on the 4 conducted trials, in which 68 
measurements were recorded for each trial within 
the force increase range up to a maximum of 112 
N (see Figure 4), the Type A measurement uncer­
tainty and its mean value were estimated. The re­
sults are presented in Figure 5.
Samples for testing
For the testing of reference samples (un­
modified by the AI algorithm) and modified 
samples, test stands for three-point bending 
tests were used in accordance with ISO 14125.
According to this standard, the samples should 
have dimensions of L = 80 mm, b = 10 mm, and 
h = 4 mm. The standard also allows for samples 
with other dimensions. The shape of the sample 
used for testing is shown in Figure 6.
Basic gcode modified with AI
The proposed modified procedure involves 
the use of artificial intelligence algorithms to op­
timize the G-code in order to achieve a noticeable 
improvement in a selected parameter of the 3D 
printing process. This may include, for example, 
an enhancement of the mechanical strength of 
the print or an improvement in the printing pro­
cess itself (e.g., shortening the print time without 
compromising quality). Figure 1 presents a sche­
matic of the traditional model preparation work­
flow for a 3D printer. 
The proposed workflow incorporating AI-
based G-code modification is shown in Figure 
7. Creation of a specialized thread in the large 
language model Chat GPT-4o (Omni), primar­
ily intended for advanced operations that are not 
so much creative as technical and engineering-
oriented [27]. 
Table 3. Results of the first 5 measurements in each of the 4 trials, along with the arithmetic mean, standard 
deviation, and Type A uncertainty
Probe
x
s
uA
Measurements
1
2
3
4
1
5.7
6.7
7.4
7.5
6.83
0.42
0.21
2
6.1
6.9
7.4
7.9
7.0
0.33
0.17
3
7.3
7.7
7.8
8.4
7.8
0.23
0.11
4
8.6
9.0
8.9
9.6
9.03
0.21
0.10
5
9.0
9.8
9.9
10.0
9.68
0.23
0.11
Figure 5. The value of the Type A measurement uncertainty and its mean. The mean uncertainty within this 
range of force variation is 0.29 N


## Page 8

468
Advances in Science and Technology Research Journal 2025, 19(10), 461–474
The content of the prepared prompt is pre­
sented below.
Creation of a specialized thread in the large 
language model Chat GPT-4o (Omni), primar­
ily for advanced tasks that are more technical and 
engineering-focused rather than creative [27]. The 
content of the prepared prompt is presented be­
low: “Hello, please assume the role of a 3D print­
ing specialist. You specialize in modifying exist­
ing G-code programs. This thread of conversation 
concerns the modification of existing G-code. I am 
focused on increasing the strength of the prints. I 
cannot afford to increase the number of walls or 
the infill density or change the infill pattern. I am 
attaching the datasheet of my 3D printer and the 
datasheet of the filament I plan to use. Please op­
timize the G-code by modifying the speeds and 
temperatures used. Apply changes to every second 
or third layer in terms of speed and temperature to 
achieve the best possible strength results. I will be 
asking you to modify the G-code file that I will pro­
vide. Please refer only to scientifically proven op­
timization assumptions and information obtained 
through the analysis of the attached datasheets”.
1.	Polite greeting – interestingly, it has been ob­
served that when users of AI language models 
politely address the model as a conversation 
partner, better results are often achieved. Al­
though this is somewhat concerning, it is un­
derstandable given the immersive nature of the 
interaction.
2.	Specialization enforcement – at this point, the 
scope of the thread is deliberately limited to a 
non-creative context. By instructing the model 
to act as a specialist in the relevant discipline, 
the user ensures a higher likelihood of receiving 
accurate and technically grounded responses. 
The GPT-4o model was chosen for this scenario 
as it is particularly suited for technical tasks.
3.	Task specification – this is the most crucial part 
of the prompt. The language model is given a 
specific task along with a clear role definition. 
Without such a directive, the model is more 
prone to error due to a lack of context and role 
awareness.
4.	References and input constraints – another 
critical instruction. The language model may 
have been trained on data concerning typical 
3D printing materials such as PLA, PETG, or 
ABS. However, each filament may have dif­
ferent optimal parameters depending on the 
manufacturer, properties, or even color. By re­
quiring the model to refer to actual datasheets, 
the user ensures that the algorithm bases its 
modifications on verified data related to both 
the filament and the printer – two key compo­
nents of the FFF/FDM process.
5.	Task refinement – this functions as a reiteration 
of the task but with more detail. It specifies the 
exact type of modifications the user expects. 
Repeating the task (even multiple times) is im­
portant in prompt engineering, as it improves 
the model’s “understanding” of the desired 
output. Just like neural networks are trained 
through layers and input weighting, repeated 
instruction functions as additional learning 
Figure 6. Shape of the sample used in the measurements
Figure 7. Process diagram for manufacturing a physical model using additive FFF/FDM technology – procedure 
including G-code modification by an AI algorithm


## Page 9

469
Advances in Science and Technology Research Journal 2025, 19(10) 461–474
reinforcement for the thread.
6.	Reiteration of constraints – as mentioned, this 
serves as another safeguard layer. It ensures the 
creative module is suppressed. While creativity 
is beneficial in marketing content, in this tech­
nical context it poses a risk of generating mis­
leading or even hazardous instructions for the 
printer. Referring only to scientific, validated 
modifications serves as a solid protection mech­
anism in the training of the model’s behavior.
In the described case (Figure 8), traditional 
programming languages such as Python are not 
used. Instead, a linguistic model is applied by 
accurately and consciously formulating specific 
commands using natural human language—
moreover, in almost any language. This is par­
ticularly significant as it eliminates limitations 
caused by language barriers, creating new oppor­
tunities for programming artificial intelligence 
for a much broader audience, not necessarily 
English-speaking.
RESULTS
The results of the conducted measurement 
experiments are presented in the following sub­
sections in the form of graphs showing the in­
crease in force from the moment the test stand is 
activated until the maximum force is reached at 
the point of breakage (sample deformation). The 
experiments were carried out using samples with 
dimensions of 100 × 7.5 × 7.5 mm, which are ap­
proved for testing according to the ISO 14125 
standard. A greater sample height of 7.5 mm was 
selected (the standard height is 4 mm) to allow for 
more print layers, and thus more opportunities to 
change the printing parameters. For this chosen 
sample shape, three types of specimens were pro­
duced: original ones (without any modification 
of the g-code generated in the CURA software), 
specimens modified every 2 layers, and speci­
mens modified every 3 layers. The tests were con­
ducted on samples made of Easy PLA [24] and 
Easy PET-G [25] from Fiberlogy. These variants 
are referred to in the further sections as follows:
	•
NMP – samples without g-code modification,
	•
PM2L – samples with g-code modified every 
2 layers,
	•
PM3L – samples with g-code modified every 
3 layers.
Results for samples with a dimension of 100 × 
7.5 × 7.5 mm – Easy PLA material
For these sample dimensions, measurements 
were carried out on 10 specimens for each var­
iant. Figure 9 presents the results obtained for 
samples printed using unmodified g-codes gen­
erated by slicers (NMP), samples modified every 
2 layers (PM2L), and samples modified every 3 
layers (PM3L). The values ​for each of the tests 
are illustrated in Figure 9 and the maximum val­
ues ​of the breaking force are summarized in Table 
4. The cases NMP, PM2L and PM3L presented 
in the figure represent the time histories of the 
increase in force measured on the tensometric 
beams (the places where the samples were sup­
ported – see Figure 2). For each of the cases, 10 
tests were performed and summarized in the fig­
ure. The maximum values ​corresponding to the 
moment of sample fracture are summarized in 
Figure 8. Diagram of the AI prompt formulation process


## Page 10

470
Advances in Science and Technology Research Journal 2025, 19(10), 461–474
Table 4 and then the average value was calculated 
from the 10 maximum values ​(Favg in Table 4).
The increase in the breaking force of the Easy 
PLA samples based on AI-modified g-code files 
(PM2L) compared to the baseline samples (NMP) 
is just under 2.7%. The percentage difference in 
breaking force for samples modified every 3 lay­
ers (PM3L) relative to the NMP samples is just 
under 3.0%. The time histories of the force in­
crease shown in Figure 9 demonstrate the speci­
ficity of the PLA material. It consists in the fact 
that the samples transfer the load exerted in their 
central part to the supports until the limit value of 
the force is reached and then the samples break, 
which is manifested in the histories by a sudden 
drop in the force to 0.
Results for samples with a dimension of 100 × 
7.5 × 7.5 mm – Easy PET-G material
For these sample dimensions, measurements 
were conducted on 10 specimens for each variant. 
Figure 10 presents the results obtained for sam­
ples printed using unmodified g-codes (gener­
ated by slicers – NMP), samples modified every 
2 layers (PM2L), and samples modified every 3 
layers (PM3L). All samples were made from Easy 
PET-G using filament from a single spool. The 
values for each of the tests are illustrated in Fig­
ure 10 and the maximum values of the breaking 
force are summarized in Table 5. For each of the 
cases, 10 tests were performed and summarized in 
the figure. The maximum values ​corresponding to 
the moment of sample fracture are summarized in 
Table 5 and then the average value was calculated 
from the 10 maximum values ​(Favg in Table 5).
The increase in the breaking force of the Easy 
PET-G samples based on AI-modified g-code files 
(PM2L) compared to the baseline samples (NMP) 
is just under 4.3%. The percentage difference in 
breaking force for samples modified every 3 lay­
ers (PM3L) relative to the NMP samples exceeds 
9.9%. The time courses of force increase shown in 
Figure 10 show the specificity of the PET-G mate­
rial. It consists in the fact that the samples transfer 
the load exerted in their central part to the sup­
ports until the limit value of the force is reached 
and then the samples undergo plastic deformation 
– which is visible in the part of the course after the 
maximum value. The force does not decrease to 0 
Figure 9. Measurement results obtained for the baseline samples (NMP) and the samples modified every 2 
layers (PM2L) and every 3 layers (PM3L) using Easy PLA material
Table 4. Maximum values for the measurements conducted on the baseline samples (NMP) and the samples 
modified every 2 layers (PM2L) and every 3 layers (PM3L) made from Easy PLA material
Pr.
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
Favg N
NMP
187.3
185.0
184.8
186.4
184.1
187.0
186.3
191.2
188.6
196.9
187.76
PM2L
196.8
195.0
199.4
187.4
187.4
189.1
194.7
191.0
193.6
193.3
192.76
PM3L
197.3
193.5
192.8
196.2
194.4
164.7
202.7
195.2
197.9
198.7
193.34


## Page 11

471
Advances in Science and Technology Research Journal 2025, 19(10) 461–474
Figure 10. Measurement results obtained for the baseline samples (NMP) and the samples modified every 
2 layers (PM2L) and every 3 layers (PM3L) made from Easy PET-G material
Table 5. Maximum values for the measurements conducted on the baseline samples (NMP) and the samples 
modified every 2 layers (PM2L) and every 3 layers (PM3L) made from Easy PET-G material
Pr.
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
Favg N
NMP
146.1
139.6
145.3
139.5
144.3
139.7
140.8
140.2
135.9
143.8
141.52
PM2L
140.4
152.7
145.9
154.2
147.6
148.6
154.5
136.5
151.7
142.6
147.57
PM3L
155.9
153.0
157.6
153.8
158.6
157.3
153.5
157.8
155.8
152.2
155.55
Table 6. Values of key parameters extracted from the g-code files CE3_1.gcode, CE3_2.gcode, and CE3_3.gcode
Parameter/commands
CE3_1.GCODE
(CURA – ORIGINAL)
CE3_2.GCODE
CHATGPT-4
CE3_3.GCODE
CHATGPT-4O
Total lines
4058
4112
4112
G1 – controlled linear movement with optional extrusion
1697
1697
1724
G0 – fast linear movement without material extrusion
2120
2120
2120
G92 – setting current position as reference point
4
4
4
G28 – automatic positioning to zero position
1
1
1
M104 – number of commands setting the hotend 
temperature (without waiting)
3
30
30
M109 – number of commands setting the hotend 
temperature (with waiting)
1
1
1
M106 – enable cooling fan
4
4
4
M107 – disable cooling fan
2
2
2
M140 – setting bed temperature without waiting
3
3
3
M190 – setting bed temperature with waiting until 
reached
1
1
1
Comments
212
212
212
Z movements
36
36
36
X movements
3801
3801
3801
Y movements
3801
3801
3801
E movements – extruder position
1689
1689
1689
F (feedrate) – movement speed
2472
2472
2499
Layer changes layer change comments
27
27
27


## Page 12

472
Advances in Science and Technology Research Journal 2025, 19(10), 461–474
Figure 11. Temperature values extracted from the g-code files CE3_1.gcode, CE3_2.gcode, and CE3_3.gcode
(the moment of sample fracture) as in the case of 
samples made of PLA material. PET-G samples 
start to deform but do not break brittle.
G-CODE files for 100 × 7.5 × 7.5 samples 
(PM2L) – Easy PLA material, before and after 
modification
Printing parameters (nozzle temperature) 
were compared – Table 6 and Figure 11. Table 6 
lists the key commands saved in the g-code file, 
respectively: CE3_1.gcode – file generated by the 
CURA slicer, CE3_2.gcode – file generated by the 
CURA slicer and modified by ChatGPT-4 in June 
2024, and the CE3_3.gcode file – file generated 
by the CURA slicer and modified by ChatGPT-4o 
after a year in May 2025. As shown in previous 
chapters, g-code modifications due to tempera­
ture changes during printing have a measurable 
effect on the strength of samples tested using the 
three-point bending method. Figure 11 shows the 
temperature changes specified in the g-code files 
CE3_1.gcode, CE3_2.gcode, and CE3_3.gcode.
CONCLUSIONS
The conducted research demonstrated that the 
application of artificial intelligence algorithms 
to optimize g-code files used in fused filament 
fabrication (FFF/FDM) 3D printing technology 
yields measurable benefits in terms of improved 
mechanical performance of printed objects. 
Modifying g-code files using the ChatGPT-4o 
language model led to a 2.7% increase in average 
breaking force for Easy PLA samples when tem­
perature was modified every 2 layers, and a 3.0% 
increase when modified every 3 layers. Even more 
significant improvements were recorded for Easy 
PET-G, with a 4.3% increase in average breaking 
force for modifications every 2 layers and a 9.9% 
increase for every 3 layers.
These results indicate a material-dependent 
response to AI-based optimization: Easy PET-G 
exhibited nearly 3 times greater strength gain in 
the PM3L variant than Easy PLA, likely due to 
its wider optimal processing temperature range 
(220–250 °C vs. 200–230 °C) and higher thermal 
responsiveness. The proposed method, relying on 
large language models for g-code modification, is 
both technically accessible and effective, requir­
ing only a properly formulated prompt and knowl­
edge of the printer and filament specifications.
Comparative analysis of the g-code files re­
vealed that the AI-generated modifications in­
creased the number of M104 commands (hotend 
temperature setting) from 3 in the baseline file to 
30, introducing cyclic thermal adjustments that 
likely improved interlayer bonding. Additionally, 
the number of G1 commands increased slightly 
(from 1697 to 1724), indicating minor adjust­
ments to the extrusion path, and F values (fee­
drate commands) were modified (from 2472 to 
2499 entries), suggesting targeted optimization of 
movement speeds.


## Page 13

473
Advances in Science and Technology Research Journal 2025, 19(10) 461–474
This research confirms that AI-assisted g-code 
editing can lead to quantifiable improvements in 
3D printed part strength without altering geome­
try, increasing material use, or requiring hardware 
modifications. The method shows promise for 
broader application, particularly within Industry 
4.0 paradigms, where automated process optimi­
zation is highly valued.
REFERENCES
1.	 Jałowiec, M., Walcher, E.-M., Bodur, O., Poszvek, 
G., Klein, M., Bayrakçıl, M.D. Advanced quality as­
surance of additive manufacturing through comput­
ed tomog-raphy. In: Durakbasa, N.M., Gençyılmaz, 
M.G. (eds.) Industrial Engineering in the Industry 
4.0 Era, Springer, Cham 2024; 179–199.
2.	 Pilch, Z., Domin, J., Szłapa, A. The impact of vibra­
tion of the 3d printer table on the quality of print. 
In: WZEE’2015, 2015; 147–152.
3.	 Vaezi, M., Seitz, H., Yang, S. A review on 3d mi­
cro-additive manufacturing technologies. Interna­
tional Journal of Advanced Manufacturing Technol­
ogy 2013; 67(5–8), 1721–1754.
4.	 Pandey, P.M., Reddy, N.V., Dhande, S.G. Real time 
adaptive slicing for fused deposition modelling. In­
ternational Journal of Machine Tools and Manufac­
ture 2003; 43(1), 61–71.
5.	 Sala, R., Regondi, S., Pugliese, R. Design data and finite 
element analysis of 3d printed poly-caprolactone-based 
lattice scaffolds: Influence of type of unit cell, porosity, 
and nozzle diameter on the mechanical behavior. Eng 
2022; 3(1): 9–23. https://doi.org/10.3390/eng3010002
6.	 Özen, A., Auhl, D., Völlmecke, C., Kiendl, J., Aba­
li, B.E. Optimization of manufacturing parameters 
and tensile specimen geometry for fused deposition 
modeling (fdm) 3d-printed petg. Materials 2021; 
14(10). https://doi.org/10. 3390/ma14102556
7.	 Tichý, T., Šefl, O., Veselý, P., Dušek, K., Bušek, 
D. Mathematical modelling of temperature dis­
tribution in selected parts of fff printer during 3d 
printing process. Polymers 2021; 13(23). https://doi.
org/10.3390/polym13234213
8.	 Cacace, J., Finzi, A., V., L. A grasping simulator 
for informed grasp planning based on visual data. 
In: Proceedings of the IEEE/RSJ International Con­
ference on Intelligent Robots and Systems (IROS), 
2016; 1177–1183.
9.	 Wang, J., Zheng, P., Xu, X. An artificial intelli­
gence-based process planning framework for smart 
manufacturing. Journal of Manufacturing Systems 
2020; 54, 328– 340.
10.	Mueller, T., Koch, R. Ai-based optimization for additive 
manufacturing. Proce-dia CIRP  2020; 88, 279–284.
11.	Bellini, A., Güçeri, S.: Mechanical characterization 
of parts fabricated using fused deposition modeling. 
Rapid Prototyping Journal 2003; 9(4), 252–264. 
https://doi.org/10.1108/13552540310489631
12.	Macdonald, E., Salas, R., et al. 3d printing for 
the rapid prototyping of structural electronics. 
IEEE Access (2014) https://doi.org/10.1109/AC­
CESS.2014.2311810. Received February 14, 2014, 
accepted March 1, 2014, date of publication March 
13, 2014, date of current version April 7, 2014
13.	Poole, S., Phillips, R. Rapid prototyping of small 
wind turbine blades using additive manufactur­
ing. In: 2015 Pattern Recognition Association of 
South Africa and Robotics and Mechatronics In­
ternational Conference (PRASA-RobMech), Port 
Elizabeth, South Africa, 2015; 189–194. https://doi.
org/10.1109/RoboMech. 2015.7359521
14.	Tack, P., Victor, J., et al. 3d-printing techniques in 
a medical setting: a system-atic literature review. 
BioMedical Engineering OnLine 2016. https://doi.
org/10. 1186/s12938âĂŚ016âĂŚ0236âĂŚ4
15.	Ferro, C.G., Varetti, S., Maggiore, P.: Experimental 
evaluation of mechanical compression properties of 
aluminum alloy lattice trusses for anti-ice system 
applications. Machines 2024; 12(6). https://doi.
org/10.3390/machines12060404
16.	Junk, S., Einloth, H., Velten, D. 4d printing: A me­
thodical approach to product development using 
smart materials. Machines 2023; 11(11). https://
doi.org/10. 3390/machines11111035
17.	Kotorčević, N., Milenković, S., Živić, F., Jordović, 
B., Adamović, D., Todorović, P., Grujović, N.: Ma­
terial extrusion 3d printing of micro-porous cop­
per-based structure for water filters. Machines 2024; 
12(7). https://doi.org/10.3390/ machines12070470
18.	Kujawa, M., Głowacka, J., Pawlak, W., Sztorch, B., 
Pakuła, D., Frydrych, M., Sokolska, J., Przekop, R.E. 
Molybdenum disulphide modified polylactide for 
3D Printed (FDM/FFF) filaments. Polymers 2023, 
15, 2236. https://doi.org/10.3390/polym15102236
19.	Zubrzycki, J., Quirino, E., Staniszewski, M., 
Marchewka, T. Influence of 3D printing parameters 
by FDM method on the mechanical properties of 
manufactured parts. Advances in Science and Tech­
nology Research Journal, 2022; 16(6), 356–366. 
https://doi.org/10.12913/22998624/154024
20.	Liu, H., Liu, R., Liu, Z., Xu, S. Minimizing the 
number of transitions of 3d printing nozzles using 
a traveling-salesman-problem optimization model. 
Inter-national Journal of Precision Engineering and 
Manufacturing 2021; 22(6), 1617–1637. https://doi.
org/10.1007/s12541-021-00512-2
21.	Jadayel, M., Khameneifar, F. Improving geometric 
accuracy of 3d printed parts using 3d metrology 
feedback and mesh morphing. Journal of Manufac­
turing and Materials Processing 2020; 4(4). https://


## Page 14

474
Advances in Science and Technology Research Journal 2025, 19(10), 461–474
doi.org/10.3390/jmmp4040112
22.	Bonada, F., Echeverria, L., Domingo, X., Anzaldi, 
G. Ai for improving the overall equipment efficiency 
in manufacturing industry. In: Martínez, L.R., Rios, 
R.A.O., Prieto, M.D. (Eds.) New Trends in the Use of 
Artificial Intelligence for the Industry 4.0. IntechOpen, 
Rijeka (2020). Chap. 5. https://doi.org/10.5772/ 
intechopen.89967
23.	Nvidia: Children Will No Longer Need To Learn To 
Code. https://www.educationnext.in/posts/children-
will-no-longer-need-to-learn-to-code-nvidia-ceo-
jensen-huang. Dostęp: 13 października 2024, 2024.
24.	Fiberlogy: Easy PLA filament. https://fiberlogy.
com/pl/filamenty/filament-easy-pla/. Dostęp: 19 
lipca 2024, 2024.
25.	Fiberlogy: Easy PET-G filament. https://fiberlo­
gy.com/pl/filamenty/easy-pet-g/. Dostęp: 19 lipca 
2024, 2024.
26.	Ratcliffe, C., Ratcliffe, B.: Type A and Type B Ele­
mental Uncertainties, Springer, Cham 2015; 9–18. 
https://doi.org/10.1007/978-3-319-12063-8_2 . 
https: //doi.org/10.1007/978-3-319-12063-8_2
27.	Aljanabi, M., Yaseen, M.G., Ali, A.H., Mohammed, 
M.A. Prompt engineering: Guiding the way to effec­
tive large language models. Iraqi Journal for Com­
puter Science and Mathematics 2023.



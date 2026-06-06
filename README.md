PRINTED CIRCUIT BOARD DEFECT DETECTION BASED ON IMAGE PROCESSING

Printed circuit boards (PCBs) are an almost universal component of every electronic
device. With the fast advancement of integrated circuits and semiconductor technologies, 
the size of a PCB may be reduced to very small dimensions. As a result, high-precision and
quick detection of defects in PCBs is required. We reviewed various defect detection methods 
in PCBs by analyzing more than 100 related articles from 1990 to 2025. The methodology of how
to prepare this overview of the PCB defect detection methods is firstly introduced. Secondly,
manual defect detection methods are reviewed briefly. Then, traditional image processing-based, 
machine learning-based and deep learning-based defect detection methods are discussed in detail.
Their algorithms, procedures, performances, advantages and limitations are explained and compared. 
The additional reviews of this paper are believed to provide more insightful viewpoints,
which would help researchers understand current research trends and perform future work related to defect detection.


The printed circuit board (PCB) is one of the most vital units in the electronic industry. 
It plays a key role in electronic devices, mechanically holding up and electrically connecting 
various electronic parts together. PCBs are used in almost every kind of electronic equipment,
from electronic watches, smart phones to computers, communication electronic devices and military
weapon systems, as long as integrated circuits and other electronic components are present.
Benefitting from the development of integrated circuit and semiconductor technology, 
the size of electronic device components has shrunk down to a tiny scale.
PCBs supporting these components are becoming increasingly complicated, diminutive and delicate.
Thus, they must be manufactured at a high quality to meet customer demands. During the Fourth Industrial 
Revolution (Industry 4.0), PCB manufacturing is facing new challenges and opportunities. The core premise of 
Industry 4.0 is automated industrial processing with high quality, precision and reliability. Therefore, the
producing process of tiny complex PCB boards is required to be more stable and reliable with higher speed, 
meaning that PCB development must be expeditious. Thus, defect detection in PCBs is crucial. Currently, 
achieving real-time, high-precision defect inspection and quality control in PCBs to improve yield and
profit is vital for manufacturers.

 SOFTWARE REQUIREMENTS
Software requirements deal with defining software resource requirements and prerequisites that need to be installed on a 
computer to provide optimal functioning of an application. These requirements or prerequisites are generally
not included in the software installation package and need to be installed separately before the software is installed.
Platform – In computing, a platform describes some sort of framework, either in hardware or software, which allows 
software to run. Typical platforms include a computer’s architecture, operating system, or programming languages and 
their runtime libraries.
Operating system is one of the first requirements mentioned when defining system requirements (software). Software may 
not be compatible with different versions of the same line of operating systems, although some measure of backward 
compatibility is often maintained. For example, most software designed for Microsoft Windows XP does not run on 
Microsoft Windows 98, although the converse is not always true. Similarly, software designed using newer features
of Linux Kernel v2.6 generally does not run or compile properly (or at all) on Linux distributions using Kernel v2.2 or v2.4.
APIs and drivers – Software making extensive use of special hardware devices, like high-end display adapters, needs 
special API or newer device drivers. A good example is DirectX, which is a collection of APIs for handling tasks related
to multimedia, especially game programming, on Microsoft platforms.
Web browser – Most web applications and software depending heavily on Internet technologies make use of the default
browser installed on the system. Microsoft Internet Explorer is a frequent choice of software running on Microsoft
Windows, which makes use of ActiveX controls, despite their vulnerabilities.
1) Software: Anaconda
2) Primary Language: Python
3) Frontend Framework: Flask
4) Back-end Framework: Jupyter Notebook
5) Database: Sqlite3
6) Front-End Technologies: HTML, CSS, JavaScript and Bootstrap4

HARDWARE REQUIREMENTS
The most common set of requirements defined by any operating system or software application is the physical computer resources, also known as hardware, A hardware requirements list is often accompanied by a hardware compatibility list (HCL), especially in case of operating systems. An HCL lists tested, compatible, and sometimes incompatible hardware devices for a particular operating system or application. The following sub-sections discuss the various aspects of hardware requirements.
Architecture – All computer operating systems are designed for a particular computer architecture. Most software applications are limited to particular operating systems running on particular architectures. Although architecture-independent operating systems and applications exist, most need to be recompiled to run on a new architecture. See also a list of common operating systems and their supporting architectures.
Processing power – The power of the central processing unit (CPU) is a fundamental system requirement for any software. Most software running on x86 architecture defines processing power as the model and the clock speed of the CPU. Many other features of a CPU that influence its speed and power, like bus speed, cache, and MIPS are often ignored. This definition of power is often erroneous, as AMD Athlon and Intel Pentium CPUs at similar clock speed often have different throughput speeds. Intel Pentium CPUs have enjoyed a considerable degree of popularity, and are often mentioned in this category.
Memory – All software, when run, resides in the random-access memory (RAM) of a computer. Memory requirements are defined after considering demands of the application, operating system, supporting software and files, and other running processes. Optimal performance of other unrelated software running on a multi-tasking computer system is also considered when defining this requirement.
Secondary storage – Hard-disk requirements vary, depending on the size of software installation, temporary files created and maintained while installing or running the software, and possible use of swap space (if RAM is insufficient).
Display adapter – Software requiring a better than average computer graphics display, like graphics editors and high-end games, often define high-end display adapters in the system requirements.
Peripherals – Some software applications need to make extensive and/or special use of some peripherals, demanding the higher performance or functionality of such peripherals. Such peripherals include CD-ROM drives, keyboards, pointing devices, network devices, etc.
1)Operating System: Windows Only
2)Processor: i5 and above
3)Ram: 8gb and above 
4)Hard Disk: 25 GB in local drive





providing a comprehensive overview of various defect detection methods in PCBs, including traditional image processing-based, machine learning-based, and deep learning-based methods.
We compare and analyze the algorithms, procedures, performances, advantages, and limitations of these methods, which can help researchers choose the most suitable method for their specific application.
We also discuss the future directions and challenges in PCB defect detection, which can guide researchers to develop more advanced and efficient methods.
Especially, i  focused on the inference time and speed simultaneously of each PCB defect detection method instead of detection precision simply, as in real PCB related industries, detection speed is a significant factor that must be considered for application and deployment

FUNCTIONAL REQUIREMENTS
1. Data Collection
2. Image processing
3. Data augmentation
4. Training model
5. Final outcome
  

4.4 NON FUNCTIONAL REQUIREMENTS
NON-FUNCTIONAL REQUIREMENT (NFR) specifies the quality attribute of a software system. They judge the software system based on Responsiveness, Usability, Security, Portability and other non-functional standards that are critical to the success of the software system. Example of nonfunctional requirement, “how fast does the website load?” Failing to meet non-functional requirements can result in systems that fail to satisfy user needs. Non- functional Requirements allow you to impose constraints or restrictions on the design of the system across the various agile backlogs. For example, the site should load in 3 seconds when the number of simultaneous users is > 10000. Description of non-functional requirements is just as critical as a functional requirement.
Usability requirement
Serviceability requirement
Manageability requirement
Recoverability requirement
Security requirement
Data Integrity requirement
Capacity requirement
Availability requirement
Scalability requirement
Interoperability requirement
Reliability requirement
Maintainability requirement
Regulatory requirement
Environmental requirement




IMPLEMENTATION
MODULES:
Data exploration: using this module we will load data into system	
Image processing: Using the module we will process transforming an image into a digital form and performing certain operations to get some useful information from it.
Data augmentation: using this module used to address both the requirements, the diversity of the training data, and the amount of data
Model generation: Building the model in colab -	FasterRCNN -	ResNet FPN -	ResNet FPN V2 -	RetinaNet -	ResNet FPN -	ResNet FPN V2 -	SSD -	SSD lite -	YoloV3 - tiny -	Yolo V5s -	Yolo V5.
User signup & login: Using this module will get registration and login
User input: Using this module will give input for prediction
Prediction: final predicted displayed

Dataset Used : 

Using different techniques for analysis the datasets for detecting with different detection models, yolov3-tiny got 0.99
However, we can further enhance the performance by exploring other techniques such as Yolov5, from which Yolo v5x6, got 0.999% mAP
With the above, we can build the front end using the flask framework for user testing with authentication.
Algorithms:
FasterRCNN - Faster R-CNN is an object detection model that improves on Fast R-CNN by utilising a region proposal network (RPN) with the CNN model. The RPN shares full-image convolutional features with the detection network, enabling nearly cost-free region proposals.
ResNet FPN - Typically people use FPNs for segmentation/detection tasks (dense pixel-wise predictions), with skip connection between different levels^1 of the network, while ResNet is used for classification/regression tasks
RetinaNet - RetinaNet is one of the best one-stage object detection models that has proven to work well with dense and small-scale objects. For this reason, it has become a popular object detection model to be used with aerial and satellite imagery.
SSD -	SSD uses a matching phase while training, to match the appropriate anchor box with the bounding boxes of each ground truth object within an image. Essentially, the anchor box with the highest degree of overlap with an object is responsible for predicting that object's class and its location.
SSD lite -A key important difference of SSDlite compared to SSD is that the backbone of the first has only a fraction of the weights of the latter. This is why in SSDlite, the Data Augmentation focuses more on making the model robust to objects of variable sizes than trying to avoid overfitting.
YoloV3 - tiny -	YOLO v3 Tiny is a real-time object detection model implemented with Keras* from this repository and converted to TensorFlow* framework.
Yolo V5 - YOLOv5 uses a Convolutional Neural Network (CNN) backbone to form image features. These features are combined in the model neck and sent to the head. The model head then interprets the combined features to predict the class of an image.





SOFTWARE ENVIRONMENT
YOLO:
YOLO is an algorithm that uses neural networks to provide real-time object detection. This algorithm is popular because of its speed and accuracy. It has been used in various applications to detect traffic signals, people, parking meters, and animals.
This article introduces readers to the YOLO algorithm for object detection and explains how it works. It also highlights some of its real-life applications.
Introduction to object detection
Object detection is a phenomenon in computer vision that involves the detection of various objects in digital images or videos. Some of the objects detected include people, cars, chairs, stones, buildings, and animals.
This phenomenon seeks to answer two basic questions:
What is the object? This question seeks to identify the object in a specific image.
Where is it? This question seeks to establish the exact location of the object within the image.
Object detection consists of various approaches such as fast R-CNN, Retina-Net, and Single-Shot MultiBox Detector (SSD). Although these approaches have solved the challenges of data limitation and modeling in object detection, they are not able to detect objects in a single algorithm run. YOLO algorithm has gained popularity because of its superior performance over the aforementioned object detection techniques.
What is YOLO?
YOLO is an abbreviation for the term ‘You Only Look Once’. This is an algorithm that detects and recognizes various objects in a picture (in real-time). Object detection in YOLO is done as a regression problem and provides the class probabilities of the detected images.
The YOLO algorithm employs convolutional neural networks (CNN) to detect objects in real-time. As the name suggests, the algorithm requires only a single forward propagation through a neural network to detect objects.
This means that prediction in the entire image is done in a single algorithm run. The CNN is used to predict various class probabilities and bounding boxes simultaneously.
The YOLO algorithm consists of various variants. Some of the common ones include tiny YOLO and YOLOv3.
Why the YOLO algorithm is important
YOLO algorithm is important because of the following reasons:
Speed: This algorithm improves the speed of detection because it can predict objects in real-time.
High accuracy: YOLO is a predictive technique that provides accurate results with minimal background errors.
Learning capabilities: The algorithm has excellent learning capabilities that enable it to learn the representations of objects and apply them in object detection.
How the YOLO algorithm works
YOLO algorithm works using the following three techniques:
Residual blocks
Bounding box regression
Intersection Over Union (IOU)
Residual blocks
First, the image is divided into various grids. Each grid has a dimension of S x S. The following image shows how an input image is divided into grids.

Image Source
In the image above, there are many grid cells of equal dimension. Every grid cell will detect objects that appear within them. For example, if an object center appears within a certain grid cell, then this cell will be responsible for detecting it.
Bounding box regression
A bounding box is an outline that highlights an object in an image.
Every bounding box in the image consists of the following attributes:
Width (bw)
Height (bh)
Class (for example, person, car, traffic light, etc.)- This is represented by the letter c.
Bounding box center (bx,by)
The following image shows an example of a bounding box. The bounding box has been represented by a yellow outline.

Image Source
YOLO uses a single bounding box regression to predict the height, width, center, and class of objects. In the image above, represents the probability of an object appearing in the bounding box.
Intersection over union (IOU)
Intersection over union (IOU) is a phenomenon in object detection that describes how boxes overlap. YOLO uses IOU to provide an output box that surrounds the objects perfectly.
Each grid cell is responsible for predicting the bounding boxes and their confidence scores. The IOU is equal to 1 if the predicted bounding box is the same as the real box. This mechanism eliminates bounding boxes that are not equal to the real box.
Applications of YOLO
YOLO algorithm can be applied in the following fields:
Autonomous driving: YOLO algorithm can be used in autonomous cars to detect objects around cars such as vehicles, people, and parking signals. Object detection in autonomous cars is done to avoid collision since no human driver is controlling the car.
Wildlife: This algorithm is used to detect various types of animals in forests. This type of detection is used by wildlife rangers and journalists to identify animals in videos (both recorded and real-time) and images. Some of the animals that can be detected include giraffes, elephants, and bears.
Security: YOLO can also be used in security systems to enforce security in an area. Let’s assume that people have been restricted from passing through a certain area for security reasons. If someone passes through the restricted area, the YOLO algorithm will detect him/her, which will require the security personnel to take further action.

 


Structural Testing:
It is not possible to effectively test software without running it. Structural testing, also known as white-box testing, is required to detect and fix bugs and errors emerging during the pre-production stage of the software development process. At this stage, unit testing based on the software structure is performed using regression testing. In most cases, it is an automated process working within the test automation framework to speed up the development process at this stage. Developers and QA engineers have full access to the software’s structure and data flows (data flows testing), so they could track any changes (mutation testing) in the system’s behavior by comparing the tests’ outcomes with the results of previous iterations (control flow testing).

Behavioral Testing:
The final stage of testing focuses on the software’s reactions to various activities rather than on the mechanisms behind these reactions. In other words, behavioral testing, also known as black-box testing, presupposes running numerous tests, mostly manual, to see the product from the user’s point of view. QA engineers usually have some specific information about a business or other purposes of the software (‘the black box’) to run usability tests, for example, and react to bugs as regular users of the product will do. Behavioral testing also may include automation (regression tests) to eliminate human error if repetitive activities are required. For example, you may need to fill 100 registration forms on the website to see how the product copes with such an activity, so the automation of this test is preferable.

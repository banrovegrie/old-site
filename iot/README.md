# Fog Computing in Transportation

## Introduction

Due to the huge surge in population and urbanisation, the use of transportation has seen a voluminous rise and as a result, large number of problems intertwined with it have also surfaced. One of such major problems is **accidents** - many of which occur due to drivers' errors.

The absence of proper counter measures against accidents result in huge loses of life and economy. However, with the advent of Internet of Things and through it the evolution of **Intelligent Transport Systems**, we now have a way to tackle this problem.

The paper [1], on which this report is based, aims at attempting to solve this problem by **monitoring the driver's behaviour and immediate surroundings influencing it**.

### A. Challenges

In order to keep a track of all different factors, different sensors are needed and in order to make correct decisions and predictions proper analysis of the heterogeneous data in real time is necessary.

### B. Attempt at Solution

As mentioned in the paper, **Fog Computing** [2] provides an interesting solution in this case. It can reduce latency to a great extent and help in making processing and generating of data much faster and closer to real time, by virtue of its positional advantage. 

### C. Drawback in the Present Studies

The main drawback is the absence of a responsive mechanism that is both real-time and effective [1].

## Architecture and Hardware

In the proposed layered architecture, the layers are Perceptions Layer, Communication and Middleware Layer, Application Layer and Stakeholders.

### A. Perception Layer

**Functionality**: Data Acquisition 

In the perception layer, the following sensors are present to collect all relevant data:

- **Environment sensors** which are necessary to identify and analyse road types and conditions, obstacles, traffic conditions, weather conditions, routes and detours, wind speed and direction, light and temperature conditions, thunder, visibility, speed limit and carbon dioxide emission.
- **Vehicle sensors** which measure vehicle's speed, gyroscope for steering wheel angle, movement, vibration, detect sudden steering, engine temperature, internal light and temperature conditions, humidity, oxygen level, smoke detection, sudden brake, sudden acceleration and fuel levels.
- **Driver sensors** which measure the driver's vital signs, eye tracker to detect sleep, fatigue, or drowsiness, voice recognition to detect how much the driver is talking and video to detect other physical behaviours of the driver.

### B. Communication and Middleware Layer

**Functionality**: Communication, Analysis, Event Detection and Trigger as well as Warning and Reporting

- **Data Communication** through various means (Wi-Fi, LTE, etc.) via different communication channels (ZigBee, Bluetooth, etc.) as suited according to the type of data is performed from sensors to fog.
- **Fog** being geographically closer and decentralised it processes and yields results faster than cloud with higher security and negligible chances of loss of connection.

Fog upon gathering data from the Perception Layer and runs road safety algorithms to determine if an **alert** should be generated based on certain well defined thresholds. The entire responsibility of interpreting and **analysing data** lies on fog.

Unnecessary data communication that might originate due to the heterogeneity of information obtained from the different sensors used is also handled by the fog.

### C. Application Layer

**Functionality:** Data Storage and Service Creation

The functionality of Application Layer is achieved through the following:

- **Cloud Resources** which are responsible for further non time-sensitive complex analysis, manage resources required by the lower layers and most importantly data storage.
- **Several Techniques** like Big Data, Data Mining, Deep Learning etc. help in creating several services related to insurance, healthcare etc. and also help a great deal in providing stakeholders in the form of academia, law enforcement authorities, insurance companies and other such organisations or industries with important resources and information.

## Evaluation of the Impact of Fog Computing on Driver Behaviour Monitoring

In this section, results regarding the advantage of fog over a cloud-only scenario are presented, based on a simulator setup developed using DEVS [3].

### A. DEVS

DEVS is a **message-based specification** based in C++ with a two-layered structure allowing communication between models through messages. It consists of six functions: constructor for defining I/O ports, initialisation function, external function which is called on receiving a new message, output function for sending out required data through O/P port and destructor which is called at the end of the process to quit all allocations and unused resources. The above also defines the sequence of execution of any DEVS model.

Information about all the models being used and their associated arguments are present in a .ma (Maya) file that helps in keeping the models connected and also provides for the initialisation functions for each model. These models can be thought as classes whose different instances like, user, cloud, fog and broker are used in the simulation.

### B. Details of the initial setup:

- Fog has a lot less resources (less than 50% of that of cloud)
- Power consumption of fog is much lower (65% of that of cloud when both are at full capacity)
- Maximum users = 300
- Request Process Time: a normal distribution with -
    1. Min = 60 mins, Max = 180 mins, Mean = 120 mins
    2. Standard Deviation = 20
    3. Min and Max are at three standard deviations away from the mean value

### C. Results obtained from the simulation:

- Total power consumption is less in a scenario with only cloud (without fog)
- Average processing delay is reduced significantly with the existence of fog
- Latency is reduced as expected with the presence of fog
- Adding more users does not affect average processing delay with the presence of fog, whereas it increases exponentially in an only cloud scenario.
- The above increase can be explained by the continual re-transmission of connection requests by users who are not being able to connect to cloud due to: 1. distance factor, 2. cloud has reached its capacity.

### D. Conclusions from the simulation:

- A trade-off between power consumption and processing delay can be observed.
- The dependency of the optimum number of users/sensors per fog/cloud on the type of service and capacity of fog/cloud can be observed.

## Conclusion

The statistics present in the paper [1], clearly show that road accidents, even though they are a reason behind a very significant number of deaths all around the world, can be easily prevented with the help of advancement of technology in the form of Intelligent Transport Systems. 

The Architecture presented in the paper - which creates a very efficient system for Driver Behaviour Monitoring - attempts to prevent road crashes, that occur due to driver's behaviour, effectively with the help Fog Computing. The presented results can be very helpful for further studies in this topic, especially in determining the optimum number of fogs and users per fog required to form a sophisticated ITS model based on the provided architecture. 

## References

[1] "Fog Assisted Driver Behaviour Monitoring for Intelligent Transport System" - Mohammad Aazam, Xavier Fernando (Dept. of Electrical and Computer Engineering, Ryerson University, Toronto, Canada)

[2] "Fog Computing and its Ecosystem" - Ramin Elahi (UC Santa Cruz, Silicon Valley) 

[3] "Using DEVS for Modelling and Simulating a Fog Computing Environment" - Etemad, Mohammad, Md. Aazam and Marc St-Hilaire

<script async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.6/MathJax.js?config=TeX-AMS_CHTML"></script>

- [Introduction to Internet of Things](#introduction-to-internet-of-things)

# Introduction to Internet of Things

Notes: This is a summary of the IoT course taught in college

Tags: IoT, Study

## Intro Part

- history of iot
- what is iot
- information flow in iot (sensors, local processing, local storage, network, internet, cloud processing, cloud storage)
- IoT buzz words: low cost chips, faster comm tech, fog/edge computing, advances in AI and BigData, flex of IPv6
- **Data→info→knowledge→wisdom**
- current m2m: connectivity, content
- evolution in iot: cloud, context, collab, cognition
- Importance of IoT: gathers useful **data**, focuses on **automation and control**, **monitoring**, increases **efficiency**, improves quality of life
- Challenges: too much data, privacy/security, complexity, connectivity
- sensor
- transducers
- sensor features
- sensor resolution
- resolution *\prop* accuracy of precision
- resolution *\prop* accuracy of sensor
- Sensor Classes: o/p (analog and digital), data type (scalar and vector), intermediate stages (direct and indirect), power req (active and passive), reference (absolute and relative), stimulus (contact and on contact)
- Sensor Characteristics: Range and Span, Accuracy, Resolution, Precision, Errors (Random (breadth of random ness) and Systematic (diff from centre))
- Sensitivity = dY/dX
- Linearity
- Hysteresis: difference in output for the same input reached through different trajectories
- DHT11 works on the basis of thermistor

## Processing

- Microcontroller: compact IC
- difference from conventional less expensive and less power
- Elements of a Microcontroller: Memory, Processor, I/O
- Processor Architecture: von Neumann Architecture, Harvard Architecture
- ADC, DAC, System Bus
- Microcontroller Features: Bits, RAM, Flash, GPIO, Connectivity, Power Consumption
- Examples: Particle.io, ESP8266, Arduino, Raspberry Pi

## Architecture

- Perception Layer: devices and sensors
- Network Layer: Secure Transmission
- Middleware Layer: Database, Computing
- Application Layer: Smart Applications
- Business Layer: Business Models, Graphs, Charts, System Management
- IoT Protocols: reliable byte streams **TCP**
- Publisher/Subscriber Approach: MQTT, AMQP, XMPP (Broker serves as a third component)
- MQTT: Message Queuing Telemetry Transport
- MQTT topics are structured in an hierarchical order as with modern computer file systems e.g., myhome/ground-floor/living-room/temperature, and Subscriptions may have wildcards as well like + for matches at a given tree level and # matches with a whole subtree
- messages published with a QoS/Quality of service level
- level of service: QoS 0<1<2
- 0: PUBLISH
- 1: PUBLISH, PUBACK
- 2: PUBLISH, PUBREC, PUBREL, PUBCOM

## Protocols

- DDS: Data Distribution Service
- Middleware protocol
- API; OS and Architecture indifferent
- Data-Centric  Publish Subscribe
- Global Data Space Abstraction
- minimal local storage usage
- autonomous asynchronous reading and writing
- spatial and temporal decoupling
- Dynamic Discovery
- isolates apps from network topology and connectivity details
- enables plug and play
- decentralised data space
- topic <name, type, qos> define/rep data streams in DDS
- information scopes and domains
- volatile, transient, durable
- best effort, last n-values, reliable
- Stream Reliability: Best Effort, Last n-values, Reliable
- MQTT and DDS: centralised vs decentralised, DDS provides more QoS aspects than MQTT
- Complexity: MQTT is simpler up front but assumes future, while DDS requires up front investment but minimizes future complexity

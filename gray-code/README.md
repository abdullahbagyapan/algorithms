# Reflected Binary Code

Gray code, also known as reflected binary code, is a binary numeral system where two successive values differ in only one bit. This is different from traditional binary counting, where consecutive numbers may differ in multiple bits. In Gray code, transitioning between consecutive values involves changing only one bit, which reduces the likelihood of errors during transitions.

The primary reason industries use Gray code is its application in various systems where precise positional information is crucial, such as:

**Rotary Encoders**: These are devices used to measure rotational motion. Gray code ensures that even if there's a slight misalignment or disturbance, the transition from one position to the next will only involve changing one bit, reducing the chance of misinterpretation.

**Communication Systems**: In digital communication systems, Gray code can be used to minimize errors during transmission. Since transitions between adjacent values involve changing only one bit, it reduces the probability of misreading due to noise or interference.

**Analog-to-Digital Converters (ADCs)**: In certain high-precision ADCs, Gray code can be used in the conversion process to ensure accuracy and reduce errors, particularly in applications where the input signal is susceptible to noise or fluctuations.

**Robotics and Automation**: Gray code is often used in robotics and automation systems, particularly in encoder feedback for motor control. It helps in accurately determining the position and movement of robotic arms or other automated systems.

Overall, Gray code is favored in industries where precision, reliability, and robustness are critical, as it provides a method for reducing errors and improving the accuracy of digital systems.


| Decimal | Binary | Gray |
|---------|---------|---------|
| 0 | 0000 | 0000 |
| 1 | 0001 | 0001 |
| 2 | 0010 | 0011 |
| 3 | 0011 | 0010 |
| 4 | 0100 | 0110 |
| 5 | 0101 | 0111 |
| 6 | 0110 | 0101 |
| 7 | 0111 | 0100 |
| 8 | 1000 | 1100 |
| 9 | 1001 | 1101 |
| 10 | 1010 | 1111 |
| 11 | 1011 | 1110 |
| 12 | 1100 | 1010 |
| 13 | 1101 | 1011 |
| 14 | 1110 | 1001 |
| 15 | 1111 | 1000 |
# Project: Automatic Music Page Turner

## Team Members
- Hou Pong Chan (104772329)
- Salil Akundi 

## Links
### Project Repositories
[Github](https://github.com/uclatonystark/ece202Aproj)
### Final Presentation Video
Youtube

## Project Introduction
### Motivation
Musicians have long been disadvantaged by having to turn their sheet music whilst their hands are occupied on the instrument. Professional musicians performing a complex score have typically relied on human page-turners, who must be alert and skilled to gauge the musician’s preferences.

In recent years, expensive assistive technologies involving foot pedals, voice and eye-controlled devices have emerged and grown in popularity. However, these methods rely on a gesture or action initiated by the musician to trigger a page-turn, which can be distracting in a concert setting. Further, the human and assistive approaches are both prone to error from inattention, omission or incorrect use.

In this project, we propose to solve this centuries-old problem by rendering the process of page turn entirely automatic. This is achieved by an embedded system that recognizes and maps the musician’s hand and finger movements to the music playing in real time. This makes the page-turn precise and stress-free, allowing the musicians to focus on the creative aspects of the program.

### Goal
To build an embedded system that consists of a glove and a tablet/computer to automatically turn electronic pages of sheet music in real-time
### Deliverables
1) A glove-like wearable device that detects which fingers are used and their positions
2) Page-turning software that uses data from the wearable device and compares it with sheet music being used in order to turn pages
3) A demonstration of the automatic page turner in action in the form of a video and report.
## Hardware Used in This Project
- Arduino Nano 33 Sense BLE
- Force/Pressure Sensor (x5)
- Glove

## Project Timeline
- Week 4: 
  - Finalize project idea and research relevant prior literature
- Week 5: 
  - Hardware: Finish Glove Design
  - Software: Research and determine page turner software interface 
- Week 6: 
  - Hardware: Order materials and assemble + Sensor Testing
  - Software: Finalize music sheet to music note conversion 
- Week 7: 
  - Hardware: Arduino programming for finger positions detection
  - Software: Determine algorithm for matching music notes from sheet to sensor values (I)
- Week 8: 
  - Hardware: Arduino programming for fingter activation + collabration detection
  - Software: Determine algorithm for matching music notes from sheet to sensor values (II)
- Week 9: 
  - Hardware: Finalize hardware assembly and test accuracy of sensor values
  - Software: Finalize software algorithm
- Week 10: 
  - Integrate both hardware and software
- Finals Week: 
  - Final testing

## Technical Approach covering data sets, algorithms, etc. and novelty of our approach

## Implementation, experimental evaluation, success metrics, and key findings

## Prior work examples including references, and the relative novelty of your work

## Summary
### Strength
- Ease of use
  - User only needs to input a PDF / series of images to compile complete music score
  - Glove is sensitive enough to track each press
- Low budget
  - Comparing to other other localization, using dead reckoning with IMU and five pressure sensors is very light weight and cost efficient
  - Existed products such as pedals, clickers or human helpers are extremely expensive
- Novelty
  - Unlike other existed products, this glove can make user to switch page without having to press a pedal or help from a helper
### Weakness
- Set up time
  - To prepare a music score for one piece, it takes about 10 minutes. However, user can use the same output files in conjuction with page turner without the set up
- Octave range accuracy
  - Approximating octave range using only IMU and linear acceleration, the accuracy is low and calibration is not very predictable. 
- Wired connection
  - Due to limited time, wire connection was done. Wireless glove might be ideal although a battery will have to be mounted on the glove
### Future Directions
- API and software Integration
  - Combine API and python scripts into one GUI for ease of use
- Better dead reckoning model and algorithm
  - To obtain higher octave range accuracy
- Wireless glove
  - To utlizie the BLE nature of the Arduino although error-free decoding scheme is needed which will take more time out of the real-time sensing cycle
## contributions of each team member
- Pong
  - Designed, soldered, assembled glove
  - Developed arduino firmware to collect data
  - Created Python scripts 
      1. to communicate between laptop and Arduino 
      2. to calculate and organize data including finger presses and octave range
      3. to display a functioning page turner

- Salil
  - Built API to generate music score
  - Developed Python scipts
    1. to calculate information about notes per page and octave positions
    2. output the results to .txt, .csv, .xml files
  - Selected songs
## Section with links to PDF of your final presentation slides, and any data sets not in repo

## References
(some paper)

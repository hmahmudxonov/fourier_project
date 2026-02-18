# Fourier Project
## Overview
This project implements Digital Signal Processing concepts in order to solve the provided problem.
The project consists of 2 main modules: dsp, and problem related code.

The structure of the project is as follows:
```
- fourier_project/
├── assignments/
├── data/
├── dsp/
├── README.md
├── config.py
├── main.py
├── requirements.txt
└── temp.py
```
- dsp:
The dsp\ directory contains essential modules that make the core of digital processing
    - transforms.py: handles all the fourier transformations and its inverses, 1d as well as 2d, under one module for convenience.
    - images.py: handles loading, saving, color scheme conversions for images
    - audio.py: handles loading, saving of the audio related data
    - excel.py: handles data given in spreadsheets
    - filters.py: contains functions that identify peaks in frequency, remove identified frequencies, gaussian high and low pass filters, etc 
- assignments: The assignments\ directory contains run functions,e.g. p1.py, that handle problem related logic
- data: The data\ directory contains input/source files used in the process of solving problems 1 through 4
- requirements.txt - this file contains required libraries to run the program which need to be present on user's device
- ## main.py - is the only script the user/grader needs to run to produce the output files for all available questions
*NOTE: files with "temp" in their names are used as scratch scripts, they are not guaranteed to generate the desired results

# Installation & Running/Set-up
### Step 1. u

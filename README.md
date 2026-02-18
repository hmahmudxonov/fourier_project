# Fourier Project
## Overview

A Python-based Digital Signal Processing (DSP) tool for performing Fourier transforms, image processing. This project is structured to handle both audio and image data.
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
---
- ## main.py - is the only script the user/grader needs to run to produce the output files for all available questions
***NOTE: files with "temp" in their names are used as scratch scripts, they are not guaranteed to generate the desired results.
Additionally, you may ignore all other files.**

-------
## Installation & Running/Set-up


### 1. Prerequisites
Ensure you have **Miniconda** or **Anaconda** installed on your system. This project is optimized for **Python 3.11**.

### 2. Environment Setup
Clone the repository and create a fresh environment to avoid dependency conflicts:

```powershell
# clone the project
git clone [https://github.com/hmahmudxonov/fourier_project.git](https://github.com/YOUR_USERNAME/fourier_project.git)
cd fourier_project

# create and activate the environment
conda create -n fourier_stable python=3.11 -y
conda activate fourier_stable

# install required packages
pip install -r requirements.txt
```
*NOTE: if you run into problems installing the libraries, open requirements.txt
in an editor and delete the version numbers of the libraries,
e.g. "==1.26.4" from "numpy==1.26.4". Then run
```powershell
pip install -r requirements.txt
```
again.

### 3. Running the program
As mentioned above, you only need to run "main.py" to generate all the output 
files. Run the following command in terminal
```powershell
python main.py
```
### Usage notes
When you run "main.py", you will see a menu to either select a specific problem,
or to run the program to generate files for all 4 problems, or quit the program
The line that opens a canvas to display plots is commented out so that the user
does not have to close each window to resume program execution. If you wish the
program to display the plots, comment in the following lines from "p1.py",
"p2.py", "p3.py", "p4.py" 
```python
plt.show()
```
and comment out
```python
plt.close()
```

---
## Question specific comments
### Problem 1: Remove the scanner beeps to isolate a dog's bark
The beep consisted of harmonics about 1.1-1.2k Hz, and additional
2 frequencies of roughly 380 Hz and 400Hz. In order to remove them, firstly,
the fourier transform is applied on the signal using
```python
numpy.fft.fft()
```
function, and the results are plotted (amplitude vs frequency). The beep frequencies appear
as sharp peaks and the bark frequencies are wide, low amplitude peaks. The program
uses a custom defined function called 
```python
dsp.filters.beep()
``` 
which identifies
the frequencies depending on the characteristics of the peaks. Then, another
function called
```python
dsp.filters.beep_filter()
``` 
is used to eliminate the undesired peaks. The function is a notch filter 
that uses 
```python
scipy.signal.iirnotch()
```
function to remove the peaks by cascading the filter.

One of the problems during removing the beep was  deciding how much of the peaks
to remove. Removing a wide band meant some of the dog barking was lost too,
but a too narrow of a band left some of the beep.
---
### Problem 2: Find the hidden message
The signal contained a very loud sound as a combination frequencies at
53 Hz, 1656 Hz, 2245 Hz, and 3025 Hz. The amplitude of these frequencies
was on the order of 10^7. Removing them in the same manner as in Problem 1,
reavealed the hidden 'message', which was a song/audio saying Hallelujah.
The audio of the message will be saved at '.\fourier_project\output\problem02\x_filt.wav'
The amplitude of the filtered signal was on the order of 10^4, which is
significantly less than the frequencies that concealed it, so the message
was inaudible in the original audio. ***Additionally, while I was converting
filtered data to audio after normalising it, for this filtered message, I 
had to convert the raw data so as to make it audible. So be careful not
to listen to it in earphones or at maximum volume on speakers.***
---

### Problem 3: Generate new images from the provided ones
Two images provided were radially growing spirals and vertical fringes.
In order to generate the new images, I had to swap magnitudes and phases
of the old ones. First, Fast Fourier Transform was applied on each image to obtain
an array of complex numbers. Then using 
```python
numpy.abs()
```
and
```python
numpy.angle()
```
magnitudes and phases for each of the old images were obtained. Then to reconstruct a new
array of FFTs for the new images with complex numbers, magnitude of one of the 
old images was multiplied by 
```python
numpy.exp(j*phase)
```
where phase is the phase of the other old image.
Finally the new arrays are inverse transformed to obtain
the new images.

### Problem 4: Generate a hybrid image of the Eiffel Tower and the Mt. Fuji
The objective of this problem was to create a hybrid image of the Eiffel
Tower and the Mt. Fuji such that the observer could see the tower while up-close
and only the mountain from a distance of about 3m or further. In order to achieve
this effect, I applied a custom-made gaussian low pass filter on the image
of the mountain and a gaussian high pass filter on the tower. Since the human eye
can only see high frequency components only up-close, high pass filter on the
tower ensures, the view cannot see it from afar. Conversely, the low pass filter
on the mountain means the image of the mountain is blurry when viewed from a
small distance, even though the colours/shades of the mountain bleed into the image
of the tower. 

The mentioned gaussian filter, 
```python
dsp.filters.gaussian_high_low_pass_filter()
```
takes an array and centers the DC component, and applies the gaussian 
filter at the centre of the array.
The filter, multiplies the gaussian function by the array if the "pass_type" is 
set to low. Conversely, if the "pass_type" is set to high, it subtracts the
product of the array and the gaussian from the array.

The returned arrays, after applying the filters, are added together and the
inverse fourier transform is applied. This gives the data to convert into 
an image.
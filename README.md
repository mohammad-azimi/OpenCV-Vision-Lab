# OpenCV Vision Lab

A beginner-friendly computer vision playground built with Python and OpenCV.

This repository contains a collection of real-time computer vision demos, including camera capture, color detection, multi-view rendering, and face/eye detection. The goal of this project is to practice core OpenCV concepts and present them in a clean, portfolio-ready structure.

## Overview

OpenCV Vision Lab is a small computer vision project focused on real-time video processing with a webcam. It demonstrates how Python and OpenCV can be used to capture live video, manipulate frames, detect colors, and identify faces and eyes using Haar Cascade classifiers.

This project started as a learning exercise and is being improved into a more organized computer vision mini-lab.

## Features

- Real-time webcam capture
- Basic video frame processing
- Color transformation and color detection
- Multi-view camera display
- Face detection using Haar Cascades
- Eye detection using Haar Cascades
- Simple and beginner-friendly Python scripts
- Portfolio-ready documentation

## Project Structure

```text
OpenCV-Python/
├── Camera-and-VideoCapture.py
├── Camera-and-VideoCapture-MultiView.py
├── Colors-and-Color-Detection.py
├── Face-and-Eye-Detection.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Demo Scripts

### 1. Camera and Video Capture

This script opens the webcam and displays the live video feed. It is the base example for working with real-time camera input in OpenCV.

```bash
python Camera-and-VideoCapture.py
```

### 2. Color Detection

This script captures video from the webcam and applies color-based processing. It demonstrates how color spaces and masks can be used for basic image processing tasks.

```bash
python Colors-and-Color-Detection.py
```

### 3. Multi-View Display

This script displays multiple views of the same camera feed. It is useful for understanding how frames can be resized, combined, and displayed in different layouts.

```bash
python Camera-and-VideoCapture-MultiView.py
```

### 4. Face and Eye Detection

This script uses OpenCV Haar Cascade classifiers to detect faces and eyes in real time from the webcam feed.

```bash
python Face-and-Eye-Detection.py
```

## Technologies Used

- Python
- OpenCV
- NumPy
- Haar Cascade Classifiers
- Real-time video processing

## Installation

Clone the repository:

```bash
git clone https://github.com/mohammad-azimi/OpenCV-Python.git
cd OpenCV-Python
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run any demo script directly:

```bash
python Camera-and-VideoCapture.py
```

Press `q` to close the OpenCV camera window if the script supports keyboard exit.

## What I Learned

Through this project, I practiced:

- Working with webcam input in Python
- Reading and displaying video frames
- Applying basic image processing techniques
- Using OpenCV color spaces
- Detecting faces and eyes in real time
- Structuring a computer vision project for GitHub

## Roadmap

Planned improvements:

- Add FPS display to each demo
- Add motion detection
- Add screenshot saving
- Add face blur mode for privacy
- Refactor scripts into a cleaner `src/` structure
- Add demo screenshots and GIF previews
- Add a command-line menu for running different demos

## Credits

This project was created while learning OpenCV and was inspired by tutorials from the Tech With Tim YouTube channel.

## Author

Mohammad Azimi

- GitHub: [mohammad-azimi](https://github.com/mohammad-azimi)
- Portfolio: [mohammad-azimi.github.io](https://mohammad-azimi.github.io/)

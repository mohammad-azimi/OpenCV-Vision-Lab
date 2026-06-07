# OpenCV Vision Lab

A real-time computer vision mini-lab built with Python and OpenCV.

This project demonstrates multiple real-time computer vision techniques using a webcam, including camera capture, color detection, multi-view rendering, face and eye detection, motion detection, and privacy-focused face blurring.

## Overview

OpenCV Vision Lab is a beginner-friendly computer vision project designed to practice practical image processing concepts in Python.

The repository started as a set of simple OpenCV learning scripts and has been refactored into a cleaner project structure with reusable modules, a command-line entry point, and multiple interactive demos.

## Features

- Real-time webcam capture
- FPS display on video frames
- Screenshot saving with keyboard input
- HSV-based color detection with live sliders
- Multi-view display: original, grayscale, edges, and HSV
- Face and eye detection using Haar Cascade classifiers
- Motion detection using background subtraction
- Face blur mode for privacy
- Organized source code structure
- Portfolio-ready documentation

## Project Structure

```text
OpenCV-Vision-Lab/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── utils.py
│   ├── camera_capture.py
│   ├── color_detection.py
│   ├── multiview_display.py
│   ├── face_eye_detection.py
│   ├── motion_detection.py
│   └── face_blur.py
│
├── legacy/
│   └── original learning scripts
│
└── outputs/
    └── saved screenshots
```

## Demo Commands

List all available demos:

```bash
python main.py list
```

Run the camera capture demo:

```bash
python main.py camera
```

Run the color detection demo:

```bash
python main.py color
```

Run the face and eye detection demo:

```bash
python main.py face
```

Run the motion detection demo:

```bash
python main.py motion
```

Run the face blur demo:

```bash
python main.py blur
```

Run the multi-view display demo:

```bash
python main.py multiview
```

Use another camera index:

```bash
python main.py camera --camera 1
```

## Controls

Inside each OpenCV window:

- Press `q` to quit
- Press `s` to save a screenshot

Saved screenshots are stored in the `outputs/` folder.

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

Install dependencies:

```bash
pip install -r requirements.txt
```

## Technologies Used

- Python
- OpenCV
- NumPy
- Haar Cascade Classifiers
- Real-time video processing
- Background subtraction

## What I Learned

Through this project, I practiced:

- Capturing video from a webcam
- Processing frames in real time
- Working with HSV color space
- Building interactive OpenCV trackbars
- Detecting faces and eyes with Haar Cascades
- Detecting movement using background subtraction
- Structuring Python code into reusable modules
- Creating a cleaner GitHub project for portfolio presentation

## Roadmap

Planned improvements:

- Add demo screenshots and GIF previews
- Add object tracking
- Add hand detection
- Add QR code detection
- Add a simple graphical menu
- Add tests for utility functions
- Improve project packaging

## Credits

This project was created while learning OpenCV and was inspired by beginner-friendly computer vision tutorials.

## Author

Mohammad Azimi

- GitHub: [mohammad-azimi](https://github.com/mohammad-azimi)
- Portfolio: [mohammad-azimi.github.io](https://mohammad-azimi.github.io/)

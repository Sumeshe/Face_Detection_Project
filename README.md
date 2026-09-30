# Face Detection System

A real-time face detection system built using **Python and OpenCV**. The project uses the **Haar Cascade Classifier** to detect one or multiple faces from images and live webcam video.

The project was developed step-by-step to understand the fundamentals of computer vision, image processing, face detection, bounding boxes, and real-time video processing.

---

## Features

- Face detection using Haar Cascade Classifier
- Real-time face detection using a webcam
- Detection of multiple faces in a single frame
- Face counting
- Bounding boxes around detected faces
- Mirrored webcam feed for a natural camera experience
- Grayscale preprocessing for face detection
- Displays "No Faces detected" when no face is found
- Adjustable face detection parameters
- Proper webcam resource management

---

## Technologies Used

- **Python**
- **OpenCV**
- **Haar Cascade Classifier**

---

## Computer Vision Pipeline

The current face detection pipeline works as follows:

```text
Webcam
   ↓
Capture Frame
   ↓
Horizontal Flip
   ↓
Convert to Grayscale
   ↓
Haar Cascade Face Detection
   ↓
Extract Bounding Boxes
   ↓
Draw Bounding Boxes
   ↓
Count Detected Faces
   ↓
Display Result

---

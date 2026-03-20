# Driver Drowsiness Detection System

A complete Python-based AI system to detect driver drowsiness using real-time webcam input. It monitors facial landmarks to calculate the Eye Aspect Ratio (EAR) and triggers an alert if the driver's eyes remain closed for a specific duration.

## Features

- **Real-time Face Detection**: Uses Mediapipe Face Mesh for lightweight, accurate facial tracking.
- **Eye Landmark Extraction**: Specifically identifies eye points to calculate the EAR metric.
- **Eye Aspect Ratio (EAR)**: Quantifies eye closure based on vertical and horizontal distances.
- **Drowsiness Alert**: Triggers an alarm sound (`alarm.wav`) when drowsiness is detected for a sustained period (e.g., 20 frames).
- **Interactive UI**: Annotates facial landmarks on the webcam feed and displays EAR and status.

## Concept - Eye Aspect Ratio (EAR)

The EAR is a simple but effective metric for quantifying eye closure:

EAR = (||p2-p6|| + ||p3-p5||) / (2 * ||p1-p4||)

where:
- `p1, p4` are the corners of the eye.
- `p2, p3, p5, p6` are the top and bottom points.

When the eye is open, the EAR is relatively stable for an individual. When the eye closes, the EAR drops significantly towards zero.

## Installation

1. **Install Python 3.x**
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Download or Generate Alarm Sound**:
   The system will automatically generate a simple `alarm.wav` if it doesn't already exist.

## How to Run

Navigate to the project directory and run:

```bash
python main.py
```

- **Exit**: Press `q` in the webcam window to exit safely.

## Project Structure

- `main.py`: Entry point for webcam feed and UI.
- `drowsiness_detector.py`: Core logic for EAR monitoring and alert triggering.
- `utils.py`: EAR calculation and helper functions for sound and landmarks.
- `requirements.txt`: List of required Python libraries.
- `alarm.wav`: Alert sound triggered when drowsiness is detected.

## Requirements

- OpenCV
- Mediapipe
- NumPy
- imutils
- SciPy
- Pygame (for audio)
 

 terminanl
 pip install -r requirements.txt(if neeqded)
 python main.py
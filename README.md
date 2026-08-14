# 🚗 Driver Drowsiness Detection System

<p align="center">

**Real-Time AI-Powered Driver Safety & Drowsiness Monitoring System**

Detect driver drowsiness in real time using computer vision, facial landmarks, and the Eye Aspect Ratio (EAR).

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=for-the-badge\&logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Face%20Landmarker-orange?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?style=for-the-badge\&logo=numpy)
![Pygame](https://img.shields.io/badge/Pygame-Audio%20Alert-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

---

## 📌 Overview

**Driver Drowsiness Detection System** is a real-time computer vision application designed to identify signs of driver fatigue using a standard webcam.

The system continuously analyzes the driver's facial landmarks and calculates the **Eye Aspect Ratio (EAR)**. When the driver's eyes remain closed for a sustained period, the system classifies the driver as **DROWSY** and immediately activates an audible warning.

The application is lightweight, works with a regular webcam, and performs detection locally without requiring a cloud-based AI service.

---

## 🎯 Problem Statement

Driver fatigue is a major road-safety concern, especially during:

* Long-distance driving
* Night-time journeys
* Monotonous highway driving
* Extended working hours
* Insufficient sleep

A driver may not always recognize their own level of fatigue. An automated monitoring system can provide an additional safety layer by detecting prolonged eye closure and warning the driver before the situation becomes dangerous.

---

## 💡 Solution

This project provides a computer-vision-based solution that:

1. Captures live video from a webcam.
2. Detects facial landmarks using **MediaPipe Face Landmarker**.
3. Extracts important eye landmarks.
4. Calculates the **Eye Aspect Ratio (EAR)**.
5. Tracks consecutive frames with low EAR.
6. Determines whether the driver is becoming drowsy.
7. Activates an audio alarm when drowsiness is detected.
8. Displays the EAR value and detection status directly on the video feed.

---

## ✨ Key Features

### 👁️ Real-Time Eye Monitoring

Continuously monitors the driver's eyes using webcam input.

### 🧠 Facial Landmark Detection

Uses MediaPipe Face Landmarker to identify facial landmarks efficiently.

### 📐 Eye Aspect Ratio Analysis

Uses EAR to quantify the degree of eye closure.

### 🚨 Automatic Drowsiness Alert

Triggers an audible alarm when the eyes remain closed beyond the configured threshold.

### 📊 Live Detection Status

Displays:

* Current EAR value
* Driver status
* Eye contours
* Drowsiness warning

### ⚡ Lightweight Computer Vision

Designed to operate using a normal webcam without requiring a dedicated GPU.

### 🔊 Continuous Alarm

The warning sound continues while the system detects a drowsy state.

### 🛡️ Safe Resource Cleanup

Camera, detector, audio and OpenCV resources are properly released when the application exits.

---

## 🏗️ System Architecture

```text
             ┌───────────────────────┐
             │     Webcam Input      │
             └───────────┬───────────┘
                         │
                         ▼
             ┌───────────────────────┐
             │   Video Frame Capture │
             └───────────┬───────────┘
                         │
                         ▼
             ┌───────────────────────┐
             │ MediaPipe Face        │
             │ Landmarker            │
             └───────────┬───────────┘
                         │
                         ▼
             ┌───────────────────────┐
             │ Eye Landmark          │
             │ Extraction             │
             └───────────┬───────────┘
                         │
                         ▼
             ┌───────────────────────┐
             │ Eye Aspect Ratio      │
             │ (EAR) Calculation     │
             └───────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ EAR < Threshold ?    │
              └──────────┬───────────┘
                         │
              ┌──────────┴──────────┐
              │                     │
             NO                    YES
              │                     │
              ▼                     ▼
        ┌───────────┐       ┌─────────────────┐
        │  ACTIVE   │       │ Count Consecutive│
        └───────────┘       │ Closed Frames    │
                            └────────┬────────┘
                                     │
                                     ▼
                            ┌─────────────────┐
                            │ DROWSY DETECTED │
                            └────────┬────────┘
                                     │
                                     ▼
                            ┌─────────────────┐
                            │  Audio Alarm 🚨 │
                            └─────────────────┘
```

---

## 🧮 Eye Aspect Ratio (EAR)

The system uses the **Eye Aspect Ratio** to determine whether the driver's eyes are open or closed.

The EAR is calculated using six eye landmarks:

```text
              p2        p3
               ●──────●
              /        \
             /          \
        p1 ●              ● p4
             \          /
              \        /
               ●──────●
              p6       p5
```

### Formula

[
EAR = \frac{||p_2-p_6|| + ||p_3-p_5||}
{2||p_1-p_4||}
]

Where:

* `p1` and `p4` → horizontal eye corners
* `p2` and `p3` → upper eye landmarks
* `p5` and `p6` → lower eye landmarks

### Interpretation

```text
Eyes Open
   ↓
Higher EAR
   ↓
Normal / ACTIVE

Eyes Closing
   ↓
Lower EAR
   ↓
Potential Drowsiness

Eyes Closed for sustained duration
   ↓
DROWSY
   ↓
🚨 AUDIO ALERT
```

The current implementation uses an EAR threshold of approximately **0.25** and requires **20 consecutive frames** below the threshold before activating the alarm. These values can be adjusted according to the camera, environment and user.

---

## 🛠️ Technology Stack

| Technology    | Purpose                                       |
| ------------- | --------------------------------------------- |
| **Python**    | Core application development                  |
| **OpenCV**    | Webcam capture and real-time image processing |
| **MediaPipe** | Face and eye landmark detection               |
| **NumPy**     | Numerical calculations                        |
| **Pygame**    | Audio alarm management                        |
| **SciPy**     | Mathematical / distance calculations          |
| **imutils**   | Image-processing utilities                    |

---

## 📂 Project Structure

```text
Driver-Drowsiness-Detection/
│
├── main.py
├── drowsiness_detector.py
├── utils.py
├── requirements.txt
├── face_landmarker.task
├── alarm.wav
├── README.md
└── .gitignore
```

### File Description

| File                     | Description                                     |
| ------------------------ | ----------------------------------------------- |
| `main.py`                | Application entry point and webcam interface    |
| `drowsiness_detector.py` | Core drowsiness detection logic                 |
| `utils.py`               | EAR calculation and helper functions            |
| `face_landmarker.task`   | MediaPipe Face Landmarker model                 |
| `alarm.wav`              | Audio warning                                   |
| `requirements.txt`       | Python dependencies                             |
| `.gitignore`             | Prevents unnecessary files from being committed |

---

## ⚙️ How It Works

### Step 1 — Webcam Capture

The application captures frames from the computer's webcam using OpenCV.

### Step 2 — Face Detection

MediaPipe Face Landmarker processes each frame and identifies facial landmarks.

### Step 3 — Eye Landmark Extraction

The system extracts six important landmarks from each eye.

### Step 4 — EAR Calculation

The vertical and horizontal distances between the eye landmarks are used to calculate EAR.

### Step 5 — Temporal Monitoring

A single low EAR value does not immediately indicate drowsiness.

Instead, the system counts consecutive frames where:

```text
EAR < EAR_THRESHOLD
```

### Step 6 — Drowsiness Detection

If the number of consecutive low-EAR frames reaches the configured limit:

```text
DROWSINESS DETECTED
```

### Step 7 — Warning

The system:

* Changes the displayed status
* Shows a visual warning
* Plays the alarm continuously

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/HEYBUDDY777/Driver-Drowsiness-Detection.git
```

### 2. Navigate to the Project

```bash
cd Driver-Drowsiness-Detection
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the system using:

```bash
python main.py
```

The application will:

1. Initialize the MediaPipe model.
2. Access the webcam.
3. Start real-time eye monitoring.
4. Display the EAR value.
5. Show the current driver status.
6. Trigger an alarm when drowsiness is detected.

### Exit

Press:

```text
q
```

to safely close the application.

---

## 🎛️ Configuration

The detection sensitivity can be modified in `main.py`.

Example:

```python
detector = DrowsinessDetector(
    ear_threshold=0.25,
    consecutive_frames=20,
    alarm_file="alarm.wav",
    model_path="face_landmarker.task"
)
```

### Parameters

| Parameter            | Purpose                                          |
| -------------------- | ------------------------------------------------ |
| `ear_threshold`      | Determines when the eye is considered closed     |
| `consecutive_frames` | Number of consecutive closed-eye frames required |
| `alarm_file`         | Path to the warning sound                        |
| `model_path`         | Path to the MediaPipe face landmark model        |

### Example

For a more sensitive configuration:

```python
ear_threshold=0.27
```

For requiring a longer eye closure:

```python
consecutive_frames=30
```

These values should be calibrated for the camera and operating environment.

---

## 🖥️ Real-Time Output

The application displays information directly on the webcam feed:

```text
EAR: 0.31
STATUS: ACTIVE
```

When drowsiness is detected:

```text
EAR: 0.18
STATUS: DROWSY

DROWSINESS DETECTED!
PLEASE RE-OPEN EYES
```

---

## 🔒 Privacy

The system is designed for local real-time processing.

The webcam feed is processed by the application and is not inherently uploaded to a remote server or cloud service.

> **Note:** This project is intended as a driver-assistance prototype and should not be considered a replacement for responsible driving or certified automotive safety systems.

---

## ⚠️ Limitations

Although the system provides real-time drowsiness detection, several factors can affect performance:

* Poor lighting conditions
* Camera quality
* Face partially outside the camera frame
* Sunglasses or heavily tinted glasses
* Extreme head movement
* Incorrect camera positioning
* Individual differences in eye shape
* Webcam frame rate

For real-world automotive deployment, additional signals such as head pose, yawning, blink frequency, steering behavior and vehicle telemetry could be incorporated.

---

## 🔮 Future Enhancements

Potential improvements include:

* [ ] Head-pose estimation
* [ ] Yawning detection
* [ ] Blink-rate analysis
* [ ] Fatigue score calculation
* [ ] Driver distraction detection
* [ ] Mobile application integration
* [ ] GPS-based emergency notification
* [ ] Driver session analytics
* [ ] Configurable alarm levels
* [ ] Dashboard for monitoring fatigue history
* [ ] Multi-modal fatigue detection
* [ ] Edge-device deployment
* [ ] Raspberry Pi / embedded-device support

---

## 📈 Future System Architecture

A more advanced version could combine multiple indicators:

```text
                 Driver Monitoring
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
      Eye State       Head Pose       Yawning
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                Fatigue Analysis
                         │
                         ▼
                 Risk Assessment
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
           NORMAL                 DROWSY
              │                     │
              ▼                     ▼
        Continue Drive         🚨 Alert Driver
```

This would make the system more robust than relying only on eye closure.

---

## 🧪 Testing

The system can be tested under different conditions:

| Scenario              | Expected Result      |
| --------------------- | -------------------- |
| Eyes open             | `ACTIVE`             |
| Normal blinking       | `ACTIVE`             |
| Short eye closure     | `ACTIVE`             |
| Prolonged eye closure | `DROWSY`             |
| Face not detected     | Continue monitoring  |
| Webcam unavailable    | Display camera error |

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes.

```bash
git commit -m "Add new drowsiness detection feature"
```

5. Push the branch.

```bash
git push origin feature/new-feature
```

6. Open a Pull Request.

---

## 📜 License

This project is available under the **MIT License**.

---

## 👨‍💻 Author

**Saravana Kumar**

AI & Data Science Student | Full Stack Developer | AI/ML Enthusiast

### Connect

* GitHub: https://github.com/HEYBUDDY777
* Project Repository: https://github.com/HEYBUDDY777/Driver-Drowsiness-Detection

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

Your support helps improve and expand the project.

---

<p align="center">

### 🚗 Drive Safe. Stay Alert. Save Lives. 🚨

**Built with Python + Computer Vision + AI**

</p>

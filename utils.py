import numpy as np
from scipy.spatial import distance as dist
import scipy.io.wavfile as wav
import os

def calculate_ear(eye_landmarks):
    """
    Calculate Eye Aspect Ratio (EAR) for a given eye.
    EAR = (||p2-p6|| + ||p3-p5||) / (2 * ||p1-p4||)
    """
    # Vertical distances between top and bottom points
    v1 = dist.euclidean(eye_landmarks[1], eye_landmarks[5])
    v2 = dist.euclidean(eye_landmarks[2], eye_landmarks[4])
    
    # Horizontal distance between the outer and inner corners
    h = dist.euclidean(eye_landmarks[0], eye_landmarks[3])
    
    # Eye Aspect Ratio
    ear = (v1 + v2) / (2.0 * h) if h > 0 else 0
    return ear

def generate_alarm_sound(filename="alarm.wav"):
    """
    Generate a simple beep sound if the alarm.wav file doesn't exist.
    """
    if os.path.exists(filename):
        return
        
    print(f"Generating default alarm sound: {filename}")
    duration = 1.0  # seconds
    sample_rate = 44100
    frequency = 1000  # Hz
    
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    # Generate a sine wave
    audio = np.sin(frequency * t * 2 * np.pi)
    # Ensure that highest value is in 16-bit range
    audio = (audio * 32767).astype(np.int16)
    
    wav.write(filename, sample_rate, audio)

def get_landmark_coords(landmarks, indices, width, height):
    """
    Helper to get pixel coordinates from normalized landmarks.
    """
    return np.array([(int(landmarks[i].x * width), int(landmarks[i].y * height)) for i in indices])

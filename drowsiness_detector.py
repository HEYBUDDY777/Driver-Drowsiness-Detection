import cv2
import mediapipe as mp
import numpy as np
from utils import calculate_ear, get_landmark_coords
import pygame
import os

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class DrowsinessDetector:
    def __init__(self, ear_threshold=0.25, consecutive_frames=20, alarm_file="alarm.wav", model_path="face_landmarker.task"):
        self.ear_threshold = ear_threshold
        self.consecutive_frames = consecutive_frames
        self.counter = 0
        self.alarm_playing = False
        self.alarm_file = alarm_file
        
        # Initialize Face Landmarker (Modern Tasks API for Python 3.13)
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.FaceLandmarkerOptions(
            base_options=base_options,
            num_faces=1,
            min_face_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.detector = vision.FaceLandmarker.create_from_options(options)
        
        # Initialize Pygame for sound
        pygame.mixer.init()
        try:
            self.sound = pygame.mixer.Sound(self.alarm_file)
        except:
            print(f"Error loading {self.alarm_file}. Sound might not play.")
            self.sound = None

        # Standard EAR 6-point indices
        self.LEFT_EYE = [33, 160, 158, 133, 153, 144]
        self.RIGHT_EYE = [362, 385, 387, 263, 373, 380]

    def process_frame(self, frame):
        """
        Processes a single frame and detects eye state.
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        
        detection_result = self.detector.detect(mp_image)
        
        status = "ACTIVE"
        ear = 0
        
        if detection_result.face_landmarks:
            face_landmarks = detection_result.face_landmarks[0]
            h, w, _ = frame.shape

            # Extract landmarks for both eyes
            left_eye_pixels = get_landmark_coords(face_landmarks, self.LEFT_EYE, w, h)
            right_eye_pixels = get_landmark_coords(face_landmarks, self.RIGHT_EYE, w, h)
            
            # Calculate EAR
            left_ear = calculate_ear(left_eye_pixels)
            right_ear = calculate_ear(right_eye_pixels)
            ear = (left_ear + right_ear) / 2.0
            
            # Visualization: Draw eye contours
            cv2.polylines(frame, [left_eye_pixels], True, (0, 255, 0), 1)
            cv2.polylines(frame, [right_eye_pixels], True, (0, 255, 0), 1)
            
            # Logic: If EAR drops below thresh for too long, trigger alert
            if ear < self.ear_threshold:
                self.counter += 1
                if self.counter >= self.consecutive_frames:
                    status = "DROWSY"
                    if self.sound and not self.alarm_playing:
                        self.sound.play(loops=-1)
                        self.alarm_playing = True
            else:
                self.counter = 0
                status = "ACTIVE"
                if self.alarm_playing:
                    self.sound.stop()
                    self.alarm_playing = False
        else:
            status = "NO FACE"
            self.counter = 0
            if self.alarm_playing:
                self.sound.stop()
                self.alarm_playing = False
                
        return frame, ear, status

    def cleanup(self):
        if self.alarm_playing and self.sound:
            self.sound.stop()
        self.detector.close()

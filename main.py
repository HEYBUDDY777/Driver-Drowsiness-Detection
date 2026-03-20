import cv2
import os
import sys
import urllib.request
from drowsiness_detector import DrowsinessDetector
from utils import generate_alarm_sound

def download_model(url, dest):
    """
    Downloads the Mediapipe face landmarker task file if missing.
    """
    if not os.path.exists(dest):
        print(f"Downloading Mediapipe Face Landmarker model to {dest}...")
        try:
            urllib.request.urlretrieve(url, dest)
            print("Download successful.")
        except Exception as e:
            print(f"Error downloading model: {e}")
            sys.exit(1)

def main():
    # 1. Ensure the alarm sound is present
    ALARM_FILENAME = "alarm.wav"
    generate_alarm_sound(ALARM_FILENAME)

    # 2. Ensure the Face Landmarker model is present (Required for new API)
    MODEL_FILENAME = "face_landmarker.task"
    MODEL_URL = "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task"
    download_model(MODEL_URL, MODEL_FILENAME)

    # 3. Initialize the detector
    print("--- Starting Driver Drowsiness Detection System ---")
    print("Initializing detector and webcam...")
    
    # You can adjust ear_threshold and consecutive_frames for your needs
    detector = DrowsinessDetector(ear_threshold=0.25, consecutive_frames=20, alarm_file=ALARM_FILENAME, model_path=MODEL_FILENAME)

    # 4. Access webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access the webcam. Ensure your camera is connected and not in use by another app.")
        detector.cleanup()
        sys.exit(1)

    print("Live Feed Active. Press 'q' in the window to EXIT.")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to fetch frame.")
                break

            # 5. Process the frame for drowsiness
            annotated_frame, current_ear, status = detector.process_frame(frame)

            # UI Color Logic: Red for ALERT, Green for ACTIVE
            color = (0, 0, 255) if status == "DROWSY" else (0, 255, 0)
            
            # Display current EAR value and detection status
            cv2.putText(annotated_frame, f"EAR: {current_ear:.2f}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            cv2.putText(annotated_frame, f"STATUS: {status}", (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

            # Draw a heavy alert box if drowsy
            if status == "DROWSY":
                cv2.rectangle(annotated_frame, (100, 150), (540, 300), (0, 0, 255), 3)
                cv2.putText(annotated_frame, "DROWSINESS DETECTED!", (120, 230),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
                cv2.putText(annotated_frame, "PLEASE RE-OPEN EYES", (180, 270),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            # 6. Show the live webcam window
            cv2.imshow("Anti-Sleep Driver Awareness", annotated_frame)

            # 7. Listen for EXIT key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Self-interrupt: User pressed 'q' to quit.")
                break

    except KeyboardInterrupt:
        print("\nManual interrupt (CTRL+C).")
    finally:
        # Cleanup Resources
        detector.cleanup()
        cap.release()
        cv2.destroyAllWindows()
        print("System shutdown complete.")

if __name__ == "__main__":
    main()

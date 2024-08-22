#final_obstacl_avoidence.py
import cv2
import numpy as np
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
from picamera2 import Picamera2
import matplotlib.pyplot as plt
import pyttsx3
import threading
import speech_recognition as sr
import time

engine = pyttsx3.init()
r = sr.Recognizer()

# Shared variable to communicate between threads
stop_program = False

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_for_stop_command():
    global stop_program
    with sr.Microphone() as source:
        while not stop_program:
            try:
                # Listen for 5 seconds
                audio_data = r.record(source, duration=5)
                text = r.recognize_google(audio_data)
                if text == "stop":
                    print("Stop command received!")
                    speak("Stop command received!")
                    time.sleep(0.5)
                    stop_program = True
                    break
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
            # Wait for 1 second before the next listen
            time.sleep(1)

cv2.startWindowThread()

model_path = "yolov8n.pt"

def load_object_detector(model_path):
    return YOLO(model_path)

def avoid_obstacle(picam, object_detector):
    global stop_program
    picam.preview_configuration.main.size = (480, 480)
    picam.preview_configuration.main.format = "RGB888"
    picam.preview_configuration.main.align()
    picam.configure("preview")
    picam.start()
    while not stop_program:
        frame = picam.capture_array()
        distance = calculate_distance_to_object()
        if (distance < 30):
            print("stop immediately!!!")
            speak("stop immediately")
            continue
        elif (distance < 100):
            results = object_detector.predict(frame)
        else:
             continue

        left_area = 0
        right_area = 0
        total_area = frame.shape[0] * frame.shape[1]

        for r in results:
            annotator = Annotator(frame)
            boxes = r.boxes
            for box in boxes:
                b = box.xyxy[0]
                c = box.cls
                annotator.box_label(b, object_detector.names[int(c)])

                box_area = (b[2] - b[0]) * (b[3] - b[1])
                distance = calculate_distance_to_object()

                center_x = (b[0] + b[2]) / 2
                if center_x < frame.shape[1] / 2:
                    left_area += box_area
                else:
                    right_area += box_area

        left_free_space = total_area / 2 - left_area
        right_free_space = total_area / 2 - right_area

        if left_free_space > right_free_space:
            print("move left")
            speak("move left")
        elif right_free_space > left_free_space:
            print("move right")
            speak("move right")
        else:
            print("Equal space on both sides. Please move straight.")
            speak("Equal space on both sides. Please move straight.")

        img = annotator.result() 
        if cv2.waitKey(1) == ord('q'):
            break

def calculate_distance_to_object():
    from distance import setup, measure_distance
    setup()
    distance = measure_distance() 
    return distance

def main():
    global stop_program
    camera = Picamera2()
    object_detector = load_object_detector(model_path)
    stop_thread = threading.Thread(target=listen_for_stop_command)
    stop_thread.start()
    avoid_obstacle(camera, object_detector)
    # Clean up
    stop_program = True
    stop_thread.join()  # Wait for the stop_thread to finish
    camera.close()
    speak("exiting navigation")
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

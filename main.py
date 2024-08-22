#main.py
import pyttsx3
import speech_recognition as sr
# Initialize the recognizer and the TTS engine
r = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()



def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Speak Now")
        audio = r.record(source, duration=5)  # Listen for 5 seconds
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            speak("You said : {}".format(text))
            return(text)
        except:
            print("Sorry could not recognize your voice")
            speak("Sorry could not recognize your voice")
            return('5')
    


def capture_image(image_path):
    picam2 = Picamera2()
    camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
    picam2.configure(camera_config)
    picam2.set_controls({
        "ExposureTime": 32680, 
        "AnalogueGain": 3.9, 
        # "DigitalGain": 1.1,  # Adjust the Digital Gain here
        "AfMode": controls.AfModeEnum.Continuous,  # Set the autofocus mode to Continuous
        "AfSpeed": controls.AfSpeedEnum.Fast  # Set the autofocus speed to Fast
    })
    picam2.start()
    speak("Focusing image Please wait")
    time.sleep(5)
    picam2.capture_file(image_path)
    picam2.stop()
    picam2.close()
    

def main():
    while True:
        try:
            speak("Please select an option:")
            speak("1. Extract text from scene")
            speak("2. Avoid obstacle")
            speak("3. Predict image caption")
            speak("4. Exit")
            print("here")
            
            choice = input()
            image_path = '/home/austine/Desktop/final_proj/captured_image.jpg'             #change this location to where you want to save the image or the duirectory where the image will be amnupilated
            if os.path.isfile(image_path):
                os.remove(image_path)
                print(f'File {image_path} has been deleted.')
            else:
                print(f'No file found at {image_path}.')

            if choice in ['4', 'four', 'exit']:
                speak("Exiting the program.")
                break

            if choice in ['1', 'one', 'extract']:
                speak("initiating text extraction")
                speak("capturing image")
                capture_image(image_path)
                speak("image captured and processing")
                result = extract_text_from_scene(image_path)
                print(result)
                speak(result)
                time.sleep(1)

            elif choice in ['2', 'two', 'to', 'avoid']:
                speak("initiating obstecle avoidence")
                avoid_obstacle()
                time.sleep(1)

            elif choice in ['3', 'three', 'image caption']:
                speak("initiating image captioning")
                speak("capturing image")
                capture_image(image_path)
                speak("image captured and processing")
                result = predict_caption(image_path)
                print(result)
                speak(result)
                time.sleep(1)

            elif choice == '5':
                speak("please try again")
            else:
                speak("Invalid choice. Please say 1, 2, 3 or 4.")
        except Exception as e:
            speak("An unknown error occurred.")
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    speak("initializing please wait")
    from picamera2 import Picamera2, Preview
    import time
    import os
    speak("loading features")
    from libcamera import controls
    from final_obstacl_avoidnce import main as avoid_obstacle
    from image_captioning_final import main as predict_caption
    from final_ocr import extract_text_from_scene
    picam2 = Picamera2()
    picam2.start()
    picam2.stop()
    picam2.close()
    main()

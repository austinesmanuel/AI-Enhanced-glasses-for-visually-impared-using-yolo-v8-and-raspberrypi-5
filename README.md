# AI_enhanced_glasses_for_visually_impared_using_yolo_v8-
This is a project which shocase the software side for Ai featured glasses for visually imapred which has few fetaures lie path navigation, object detection, image description (sceanary description), and extract text from image (optical charecter recognition).
Here’s the updated prerequisites section with the additional information about the Picamera2 installation issues:

---

## Prerequisites

Before running the scripts, ensure that you have the required hardware and software set up. This section details the necessary hardware components and the installation of required Python libraries.

### Hardware Requirements

- **Raspberry Pi**:
  - Model: Raspberry Pi 3 or 4

- **For `distance.py`**:
  - **Ultrasonic Sensor**:
    - Model: HC-SR04 or similar
    - Components: TRIG Pin, ECHO Pin
  - **Resistors**:
    - 1k ohm and 2k ohm resistors (for voltage division and protection)
  - **Jumper Wires**: For connecting the sensor to GPIO pins
  - **Breadboard** (optional): For easy connections
  - **Connection Guide**:
    - For detailed wiring instructions, refer to this video: [Ultrasonic Sensor Connection](https://youtu.be/L90WS-ptnvI?feature=shared)

- **For `main.py`**:
  - **PiCamera2**:
    - Model: Official Raspberry Pi Camera Module V2 or compatible
  - **Microphone**:
    - Model: USB microphone or compatible with Raspberry Pi
  - **Speaker**: Any compatible speaker connected to the Raspberry Pi

### Software Installation

Ensure your Raspberry Pi OS is up to date and install the required Python libraries using the following commands:

```bash
# Update and install pip
sudo apt-get update
sudo apt-get install python3-pip

# Install Python libraries
sudo pip3 install pyttsx3
sudo pip3 install speech_recognition
sudo pip3 install RPi.GPIO
sudo pip3 install opencv-python-headless
sudo pip3 install pytesseract
sudo pip3 install transformers
sudo pip3 install torch
sudo pip3 install pillow

# Install Picamera2 for camera functionality
sudo apt-get install python3-picamera2
```

If you encounter issues installing Picamera2, you can refer to the following resources for troubleshooting:
- [Raspberry Pi Forum - Picamera2 Installation Issues](https://forums.raspberrypi.com/viewtopic.php?t=367558)
- [Picamera2 on PyPI](https://pypi.org/project/picamera2/)

Ensure all hardware components are correctly connected according to the guide and the resistors are properly installed before running the scripts.

---

Here is a breakdown of all the used python files 
## 1. `main.py`

The `main.py` script acts as the central controller for the project. It handles user input via speech recognition, captures images using a camera, and delegates tasks to other modules based on user choices.


### Key Components


- **Speech Recognition and Text-to-Speech**:

    - **Initialization**: Initializes the `speech_recognition` and `pyttsx3` libraries for speech-to-text and text-to-speech functionalities.

    - **Speak Function**: Uses the TTS engine to convert text into spoken words.

    - **Listen Function**: Captures user input via the microphone and processes it using the Google Speech Recognition API.


- **Image Capture**:

    - **PiCamera2 Library**: Utilizes the PiCamera2 library to capture high-resolution images.

    - **Camera Configuration**: Sets up camera parameters like resolution, exposure time, and gain.

    - **Capture Image Function**: Captures and saves an image to a specified file path.


- **Main Functionality**:

    - **User Interaction**: Prompts the user to choose an option: Extract text from a scene, Avoid obstacle, or Predict image caption.

    - **Image Processing**: Based on user choice, captures an image and calls the relevant function from other modules (`final_obstacl_avoidnce`, `image_captioning_final`, `final_ocr`).

 - **Error Handling**: Handles invalid user input and exceptions, including file operations such as deleting existing images.

### Hardware and Configuration Details

#### Hardware

1. **Raspberry Pi**:
   - **Model**: Any Raspberry Pi model compatible with the PiCamera2 library (e.g., Raspberry Pi 4).
   - **Purpose**: Acts as the central controller for capturing images and executing various tasks.

2. **PiCamera2**:
   - **Model**: Official Raspberry Pi Camera Module V2 or any compatible PiCamera2.
   - **Resolution**: Configurable (e.g., 1920x1080 for high resolution).

3. **Microphone**:
   - **Model**: USB microphone or compatible microphone with Raspberry Pi.
   - **Purpose**: Captures user voice input for speech recognition.

4. **Speaker**:
   - **Model**: Any compatible speaker connected to the Raspberry Pi.
   - **Purpose**: Outputs text-to-speech responses.

#### Camera Configuration

- **Resolution**:
  - **Main Resolution**: 1920x1080 (Full HD).
  - **Lo-Res Preview**: 640x480 (used for preview and focusing).

- **Camera Settings**:
  - **Exposure Time**: Configurable (e.g., 32680 ms).
  - **Analogue Gain**: Adjustable (e.g., 3.9).
  - **Autofocus Mode**: Continuous.
  - **Autofocus Speed**: Fast.

#### Setup

1. **Camera Connection**:
   - **Connection**: Ensure the PiCamera2 is properly connected to the Raspberry Pi via the camera interface.

2. **Microphone Setup**:
   - **Connection**: Connect the microphone to a USB port or the appropriate audio interface.
   - **Configuration**: Select and configure the microphone in the `listen` function.

3. **Speaker Setup**:
   - **Connection**: Connect the speaker to the audio output of the Raspberry Pi.

4. **Software Configuration**:
   - **Python Libraries**: `pyttsx3` for text-to-speech, `speech_recognition` for voice commands, `Picamera2` for image capture.
   - **Python Version**: Ensure compatibility with the installed version of Python.

---

## 2. `image_captioning_final.py`



The `image_captioning_final.py` script generates captions for images using a pre-trained Vision-Encoder-Decoder model.


### Key Components


- **Model Initialization**:

    - **Model Loading**: Loads the Vision-Encoder-Decoder model (`nlpconnect/vit-gpt2-image-captioning`), feature extractor, and tokenizer.

    - **Device Setup**: Uses GPU for processing if available; otherwise, defaults to CPU.


- **Image Preprocessing**:

    - **Image Conversion**: Converts images to the required format for the model.

    - **Pixel Value Processing**: Processes images using the `ViTImageProcessor` to prepare them for caption generation.


- **Caption Generation**:

    - **Generate Captions**: Uses the model to generate captions for the input images.

    - **`predict_step` Function**: Takes a list of image paths, processes each image, and generates captions.

    - **`main` Function**: Calls `predict_step` to generate and return captions for a single image.


### Configuration Options


   - **`max_length`**: Sets the maximum length of the generated caption.

   - **`num_beams`**: Number of beams used in beam search for generating captions.


---


## 3. `final_obstacl_avoidnce.py`



The `final_obstacl_avoidnce.py` script provides functionality for obstacle avoidance using object detection and distance measurement.


### Key Components


- **Object Detection**:

    - **YOLO Model**: Uses the YOLO model (`yolov8n.pt`) to detect objects in images.

    - **Model Loading**: Loads the YOLO model for real-time object detection.


- **Distance Measurement**:

    - **Ultrasonic Sensor**: Measures the distance to objects using an ultrasonic sensor.

    - **`calculate_distance_to_object` Function**: Imports and uses functions from the `distance` module to measure the distance.


- **Obstacle Avoidance**:

    - **Image Processing**: Captures and processes images to detect objects and calculate free space on the left and right sides.

    - **Decision Making**: Determines the direction to move based on the available free space and detected objects.


- **Voice Commands**:

    - **Stop Command**: Listens for a "stop" command to halt the obstacle avoidance process.

    - **`listen_for_stop_command` Function**: Runs in a separate thread to listen for and handle the stop command.


### Error Handling


Includes error handling for issues such as unrecognized voice commands and exceptions during the obstacle avoidance process. Ensures proper resource cleanup, including stopping the camera and closing windows.


---


## 4. `distance.py`


The `distance.py` script measures the distance to objects using an ultrasonic sensor.


### Key Components


- **GPIO Setup**:

    - **Pin Configuration**: Configures GPIO pins for the ultrasonic sensor, including TRIG (trigger) and ECHO (echo) pins.

    - **`setup` Function**: Sets up GPIO pins for distance measurement.


- **Distance Measurement**:

    - **Ultrasonic Signals**: Sends and receives ultrasonic signals to measure distance.

    - **`measure_distance` Function**: Triggers the sensor, measures the pulse duration, and calculates the distance based on the speed of sound.


### Error Handling


Includes handling for user interruptions (e.g., Ctrl+C) and ensures proper GPIO cleanup to prevent leaving GPIO pins in an unstable state.

### Hardware and Configuration Details
#### Hardware

1. **Raspberry Pi**:
   - **Model**: Any Raspberry Pi model with GPIO pins (e.g., Raspberry Pi 3, Raspberry Pi 4).
   - **Purpose**: Acts as the central controller for measuring distance using the ultrasonic sensor.

2. **Ultrasonic Sensor**:
   - **Model**: HC-SR04 or similar ultrasonic distance sensor.
   - **Components**:
     - **TRIG Pin**: Trigger pin to initiate the measurement.
     - **ECHO Pin**: Echo pin to receive the reflected signal.

3. **Jumper Wires**:
   - **Purpose**: Connects the ultrasonic sensor to the GPIO pins on the Raspberry Pi.

4. **Breadboard** (optional):
   - **Purpose**: Provides a platform to connect the sensor and wires without soldering.

#### GPIO Pin Configuration

- **TRIG Pin (GPIO 23)**: 
  - **Function**: Sends a short pulse to trigger the ultrasonic sensor to emit sound waves.
  - **Connection**: Connect to the TRIG pin of the ultrasonic sensor.

- **ECHO Pin (GPIO 24)**:
  - **Function**: Receives the pulse from the ultrasonic sensor after reflecting off an object.
  - **Connection**: Connect to the ECHO pin of the ultrasonic sensor.

#### Setup

1. **Raspberry Pi GPIO**: 
   - Ensure GPIO pins are properly configured and connected to the ultrasonic sensor.

2. **Software Configuration**:
   - **Python Libraries**: `RPi.GPIO` for GPIO control.
   - **Python Version**: Ensure compatibility with the installed version of Python.

---


## 5. `final_ocr.py`


The `final_ocr.py` script extracts text from images using the Tesseract OCR engine.


### Key Components


- **Image Preprocessing**:

    - **Grayscale Conversion**: Converts the image to grayscale and applies thresholding to enhance text regions.

    - **`extract_text_from_scene` Function**: Handles image preprocessing using OpenCV.


- **Text Extraction**:

    - **Tesseract OCR**: Uses Tesseract OCR to extract text from the preprocessed image.

    - **`extract_text_from_scene` Function**: Reads the image, processes it, and extracts text using Tesseract.


### Error Handling


Includes error handling to manage issues such as loading the image or performing OCR. Provides descriptive error messages for debugging.


### Configuration Options


   - **`--psm 3`**: Page segmentation mode. Fully automatic page segmentation, but no OSD (Orientation and Script Detection).

   - **`--oem 3`**: OCR Engine mode. Uses both standard and LSTM OCR engines.

#distance.py

import RPi.GPIO as GPIO
import time

# Define GPIO Pins
TRIG = 23
ECHO = 24

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

def measure_distance():
    try:
        while True:
            GPIO.output(TRIG, False)
            time.sleep(0.2)
            
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            
            while GPIO.input(ECHO)==0:
                pulse_start = time.time()
            
            while GPIO.input(ECHO)==1:
                pulse_end = time.time()
            
            pulse_duration = pulse_end - pulse_start
            
            distance = pulse_duration * 17150
            distance = round(distance, 2)
            
            print("Distance: ", distance, "cm")
            return distance
            
    except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program
        print("Measurement stopped by user")
        GPIO.cleanup()

def main():
    setup()
    measure_distance()

if __name__ == "__main__":
    main()

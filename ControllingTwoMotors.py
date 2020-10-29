
import RPi.GPIO as GPIO
import time

#Making vars for all the GPIO pins
in1 = 23 # this is GPIO pin name
in2 = 24 # this is GPIO pin name
ENA = 25 # this is GPIO pin name
temp1 = 1

in3 = 5 # this is GPIO pin name
in4 = 6 # this is GPIO pin name
ENB = 26 # this is GPIO pin name

#set up pins as GPIOs
GPIO.setmode(GPIO.BCM)
# Left motor
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p1 = GPIO.PWM(ENA, 1000)
# Left motor

# Right motor
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
p2 = GPIO.PWM(ENB, 1000)
# Right motor

p1.start(50)
p2.start(50)


def forward(secs):
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    time.sleep(secs)
    p1.stop()
    p2.stop()
    
def backward(secs):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    time.sleep(secs)
    p1.stop()
    p2.stop()
    

def left(secs):
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    time.sleep(secs)
    p1.stop()
    p2.stop()
    
   
def right(secs):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    time.sleep(secs)
    p1.stop()
    p2.stop()
    
    
    
forward(30)
GPIO.cleanup()

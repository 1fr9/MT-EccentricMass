from time import sleep 
import RPi.GPIO as GPIO 

DIR = 20   # Direction GPIO Pin 
STEP = 21  # Step GPIO Pin 
CW= 1   # Clockwise Rotation 
CCW = 0  # Counterclockwise Rotation 
SPR = 200   # Steps per Revolution (360 / 1.8) 

GPIO.setmode(GPIO.BCM) 
GPIO.setup(DIR, GPIO.OUT) 
GPIO.setup(STEP, GPIO.OUT) 

MODE = (14, 15, 18) # Microstep Resolution GPIO Pins 
GPIO.setup(MODE, GPIO.OUT) 
RESOLUTION = {'Full': (0, 0, 0), 
'HALF': (1, 0, 0), 
'1/4': (0, 1, 0),
'1/8': (1, 1, 0), 
'1/16': (0, 0, 1), 
'1/32': (1, 0, 1)} 
GPIO.output(MODE, RESOLUTION['1/32']) 

GPIO.output(DIR, CCW) 
STP =  0 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  72 
DLY = 0.0057 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  1 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  71 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  77 
DLY = 0.0060 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  2 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  1 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  74 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  76 
DLY = 0.0084 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  1 
DLY = 0.0013 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  1 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  76 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  74 
DLY = 0.0081 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  1 
DLY = 0.0013 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  75 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  77 
DLY = 0.0100 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  1 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  76 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  72 
DLY = 0.0081 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  3 
DLY = 0.0016 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  75 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  75 
DLY = 0.0100 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  75 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  71 
DLY = 0.0078 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  71 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  77 
DLY = 0.0084 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  2 
DLY = 0.0013 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  79 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  75 
DLY = 0.0060 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  1 
DLY = 0.0013 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  1 
DLY = 0.0013 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  77 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  76 
DLY = 0.0100 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  76 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  91 
DLY = 0.0069 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  11 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  80 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  61 
DLY = 0.0069 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  14 
DLY = 0.0038 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  75 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  75 
DLY = 0.0100 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  12 
DLY = 0.0035 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  87 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  62 
DLY = 0.0050 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  9 
DLY = 0.0029 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  71 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  76 
DLY = 0.0060 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  47 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  29 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  83 
DLY = 0.0063 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  6 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  1 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  76 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  77 
DLY = 0.0060 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  12 
DLY = 0.0035 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  89 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  72 
DLY = 0.0057 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  72 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  75 
DLY = 0.0060 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  1 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  74 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  94 
DLY = 0.0072 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  2 
DLY = 0.0013 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  21 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  75 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  75 
DLY = 0.0084 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CW) 
STP =  25 
DLY = 0.0060 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  3 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  21 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.output(DIR, CCW) 
STP =  76 
DLY = 0.0010 
step_count = STP*32 
delay = DLY/32 
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH) 
    sleep(delay) 
    GPIO.output(STEP, GPIO.LOW) 
    sleep(delay) 
sleep(.0001)

GPIO.cleanup()
import RPi.GPIO as GPIO
from servo import *
import time
GPIO.setmode(GPIO.BOARD)
servoPin =7
myservo = Servo(servoPin)
myservo.setAngle(0)

for i in range(0, 181,20):
    print "Servo angle: ", i
    myservo.updateAngle(i)
    time.sleep(2)
   
    
myservo.stop()
GPIO.cleanup()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


class Servo:
    def __init__(self,pin):
        GPIO.setup(pin,GPIO.OUT)
        self.pwm=GPIO.PWM(pin, 100)
       

    def setAngle(self,angle):
        self.pwm.start(angle)
        
    def updateAngle(self,angle):
        dc = 2.5+ 0.12*float(angle)
        #print dc
        self.pwm.ChangeDutyCycle(dc)
        return

    def stop(self):
        self.pwm.stop()
        



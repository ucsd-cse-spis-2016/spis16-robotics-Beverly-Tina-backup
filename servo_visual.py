from Tkinter import *
import RPi.GPIO as GPIO
import time


servoPin = 7
GPIO.setmode(GPIO.BOARD) # use physical numbering
GPIO.setup(servoPin,GPIO.OUT)
pwm=GPIO.PWM(servoPin, 100)
pwm.start(5)

class App:
   def __init__(self,master):
      frame = Frame(master)
      frame.pack()
      scale = Scale(frame, from_ =0, to = 180, orient=HORIZONTAL, command = self.update)
      scale.grid(row =0)

   def update(self, angle):
      dc = 2.5+ float(angle)/10.0
      pwm.ChangeDutyCycle(dc)


root =Tk()
root.wm_title('Servo Control')
app=App(root)
root.geometry("200x50+0+0")
root.mainloop()

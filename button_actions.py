import RPi.GPIO as GPIO, time
SONAR = 8
def setupSonar(sonarPin=SONAR):
    SONAR = sonarPin

GPIO.setmode(GPIO.BOARD)

GPIO.setup(rightTop, GPIO.OUT)
GPIO.setup(rightBottom, GPIO.OUT)
GPIO.setup(leftTop, GPIO.OUT)
GPIO.setup(leftBottom, GPIO.OUT)

rightTopPWM=GPIO.PWM(rightTop, 20)
rightTopPWM.start(0)

rightBottomPWM=GPIO.PWM(rightBottom, 20)
rightBottomPWM.start(0)

leftTopPWM = GPIO.PWM(leftTop,20)
leftTopPWM.start(0)

leftBottomPWM=GPIO.PWM(leftBottom,20)
leftBottomPWM.start(0)

slowspeed =20
fastspeed = 100
avgspeed = 50
rightTop = 19
rightBottom = 21
leftTop = 24
leftBottom = 26

def getDistance():

   GPIO.setup(SONAR, GPIO.OUT)
   GPIO.output(SONAR, True)
   time.sleep(0.00001)
   GPIO.output(SONAR, False)
   start = time.time()
   count = time.time()
   GPIO.setup(SONAR, GPIO.IN)
   while GPIO.input(SONAR)==0 and time.time()-count<0.1:
         start = time.time()
   stop=time.time()
   while GPIO.input(SONAR)==1:
         stop = time.time()
   # Calculate pulse length
   elapsed = stop-start
   # Distance pulse travelled in that time is time
   # multiplied by the speed of sound (cm/s)
   distance = elapsed * 34000
   # That was the distance there and back so halve the value
   distance = distance / 2
   return distance

def forward(speed=avgspeed):
   rightTopPWM.ChangeDutyCycle(speed)
   rightBottomPWM.ChangeDutyCycle(0)
   leftTopPWM.ChangeDutyCycle(speed)
   leftBottomPWM.ChangeDutyCycle(0)

def reverse(speed=avgspeed):
   rightTopPWM.ChangeDutyCycle(0)
   rightBottomPWM.ChangeDutyCycle(speed)
   leftTopPWM.ChangeDutyCycle(0)
   leftBottomPWM.ChangeDutyCycle(speed)

def turnLeft(rspeed=fastspeed,lspeed=slowspeed ):
   rightTopPWM.ChangeDutyCycle(rspeed)
   rightBottomPWM.ChangeDutyCycle(0)
   leftTopPWM.ChangeDutyCycle(lspeed)
   leftBottomPWM.ChangeDutyCycle(0)

def stopall():
   rightTopPWM.ChangeDutyCycle(0)
   rightBottomPWM.ChangeDutyCycle(0)
   leftTopPWM.ChangeDutyCycle(0)
   leftBottomPWM.ChangeDutyCycle(0)
forward(avgspeed)

#def buttonOne():
 #   button = GPIO.input(BtnPin)
  #  while button == 0:
   #     stopall()
    #if button == 1:
     #   button = GPIO.input(BtnPin)
      #  if button == 0: 
       #     getDistance()
        #    while distance > 10:
         #       forward(avgspeed)
          #  stopall()
           # reverse(avgspeed)
            #turnLeft(rspeed, lspeed)
        

    
    

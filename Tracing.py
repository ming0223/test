######################################################################
### Date: 2017/10/5
### file name: project3_student.py
### Purpose: this code has been generated for the three-wheeled moving
###         object to perform the project3 with ultra sensor
###         swing turn, and point turn
### this code is used for the student only
######################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
from time import sleep

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# import getDistance() method in the ultraModule
# =======================================================================
from ultraModule import *

# =======================================================================
# import TurnModule() method
# =======================================================================
from TurnModule import *

from trackingModule import *


# =======================================================================
# rightPointTurn() and leftPointTurn() in TurnModule module
# =======================================================================
# student assignment (1)
# student assignment (2)


# =======================================================================
# import go_forward_any(), go_backward_any(), stop(), LeftPwm(),
# RightPwm(), pwm_setup(), and pwm_low() methods in the module of go_any
# =======================================================================
from go_any import *

# implement rightmotor(x)  # student assignment (3)
# implement go_forward_any(speed): # student assignment (4)
# implement go_backward_any(speed): # student assignment (5)
# implement go_forward(speed, running_time)  # student assignment (6)
# implement go_backward(speed, running_time)  # student assignment (7)

# =======================================================================
# setup and initilaize the left motor and right motor
# =======================================================================
pwm_setup()

# =======================================================================
#  define your variables and find out each value of variables
#  to perform the project3 with ultra sensor
#  and swing turn# =======================================================================
dis =  15  # ??
obstacle = 1
PointPr = 45 
PointTr = 0.40

try:
    while True:
        # ultra sensor replies the distance back
        distance = getDistance()
        print('distance= ', distance)

        # when the distance is above the dis, moving object forwards
        if (distance > dis):
            Ll = GPIO.input(leftlessled)
            Lm = GPIO.input(leftmostled)
            C = GPIO.input(centerled)
            Rl = GPIO.input(rightlessled)
            Rm = GPIO.input(rightmostled)
            
            if(Ll==1 and Rm==1):
                 if(Lm==0 and Ll==0):
                        go_forward_any(20, 40)
                 elif(C==1 and Rl==1):
			go_forward_any(20, 40)
                 else :
                        go_forward_any(40, 40)
            
            elif (Ll==0 and Rm==1):
                 go_forward_any(20, 40)
#                setRightPwm(5)
#                setLeftPwm(10)

            elif (Rm==0 and Ll==1):
                 go_forward_any(40, 20)
#                setRightPwm(10)
#                setLeftPwm(5)
            elif (Rm == 1 and Rl == 1 and C == 1 and Ll == 1 and Lm == 1):
                 go_forward_any(15, 45)
        else:
            stop()
            sleep(1)

#             go_forward(20, 50)
            rightPointTurn(PointPr, PointTr)
#            go_forward(25, 45)
            go_forward(45, 0.9)
            leftPointTurn(PointPr + 6, PointTr)
            go_forward(40, 1)
            leftPointTurn(PointPr + 6, PointTr)
            go_forward(45, 0.8)

#            else :
#                setRightPwm(10)
#                setLeftPwm(10)

#        else :      
           



        # when the distance is below the dis, moving object stops



            ########################################################
            ### please continue the code or change the above code
            ### # student assignment (10)
            ########################################################


# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()

from pybricks.parameters import Stop
from pybricks.tools import wait

from robot import (
    align_heading,
    back_attachment_motor,
    drive_base,
    front_attachment_motor,
    prime_hub,
    turn_with_gybro,
)

def m15_biocenter_idk6767():
    drive_base.settings(straight_speed=200)
    drive_base.straight(600)
    drive_base.turn(90)
    drive_base.straight(560)
    drive_base.straight(-50)
    drive_base.turn(90)
    drive_base.straight(215)
    front_attachment_motor.run_angle(200, 125)
    drive_base.turn(-95)
    drive_base.straight(30)
    front_attachment_motor.run_angle(75, -65, Stop.BRAKE)
    wait(100)
    front_attachment_motor.run_angle(30, 125, Stop.BRAKE)
    drive_base.straight(-20)
    drive_base.turn(20)
    wait(100)
    drive_base.settings(straight_speed=500)
    drive_base.straight(1500)

def lift():
    front_attachment_motor.run_angle(500, -190)


# The main program starts here.
print('Hello, Pybricks!')

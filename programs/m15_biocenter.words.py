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
    drive_base.straight(600)
    drive_base.turn(90)
    drive_base.straight(600)
    drive_base.straight(-50)
    drive_base.turn(90)
    drive_base.straight(170)
    drive_base.turn(-90)
    drive_base.straight(-50)
    front_attachment_motor.run_angle(200, 160)
    wait(100)
    drive_base.straight(55)
    front_attachment_motor.run_angle(75, -110, Stop.BRAKE)

def lift():
    front_attachment_motor.run_angle(500, -190)


# The main program starts here.
print('Hello, Pybricks!')

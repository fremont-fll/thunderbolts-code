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

def m6_leafcutter_frenzy():
    prime_hub.imu.reset_heading(0)
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=200)
    drive_base.straight(700, then=Stop.BRAKE)
    turn_with_gybro(-90)
    align_heading()

def m15_biocenter_idk6767():
    drive_base.straight(600)
    drive_base.turn(90)
    drive_base.straight(600)
    drive_base.straight(-50)
    drive_base.turn(90)
    front_attachment_motor.run_angle(100, 100)
    drive_base.straight(153)
    drive_base.turn(-95)
    wait(100)
    front_attachment_motor.run_angle(10, 100)
    wait(100)
    front_attachment_motor.run_angle(10, 40)
    drive_base.straight(40)
    drive_base.turn(-4)
    front_attachment_motor.run_angle(1e+64, 70)

def idk_6767():
    pass


# The main program starts here.
print('Hello, Pybricks!')

from pybricks.parameters import Stop
from pybricks.tools import wait

from robot import (
    align_heading,
    back_attachment_motor,
    drive_base,
    front_attachment_motor,
    get_desired_heading,
    prime_hub,
    set_desired_heading,
    turn_with_gybro,
)

def reset_front():
    front_attachment_motor.run_angle(500, 360)

def flip_the_rock():
    set_desired_heading(0)
    drive_base.settings(straight_speed=200)
    drive_base.use_gyro(False)
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=250)
    drive_base.use_gyro(False)
    drive_base.use_gyro(True)
    drive_base.straight(275, then=Stop.BRAKE)
    drive_base.turn(-27, then=Stop.BRAKE)
    drive_base.settings(straight_speed=1500)
    drive_base.straight(270, then=Stop.BRAKE)
    drive_base.turn(10, then=Stop.BRAKE)
    drive_base.straight(-350, then=Stop.BRAKE)
    drive_base.turn(60, then=Stop.BRAKE)
    drive_base.straight(80, then=Stop.BRAKE)
    front_attachment_motor.run_angle(1500, -280)
    drive_base.straight(210, then=Stop.BRAKE)
    drive_base.settings(straight_speed=1500)
    wait(200)
    front_attachment_motor.run_angle(300, 230)
    drive_base.straight(-400, then=Stop.BRAKE)
    front_attachment_motor.run_angle(500, 200)
    drive_base.straight(-400, then=Stop.BRAKE)

def m1_spoiled_drone():
    drive_base.settings(straight_speed=250)
    drive_base.straight(-500)


# The main program starts here.

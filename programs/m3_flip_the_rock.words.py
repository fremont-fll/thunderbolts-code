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

def reset_front():
    front_attachment_motor.run_angle(500, 360)

def flip_the_rock():
    drive_base.use_gyro(False)
    drive_base.use_gyro(True)
    drive_base.straight(275, then=Stop.BRAKE)
    drive_base.turn(-25, then=Stop.BRAKE)
    drive_base.straight(-20, then=Stop.BRAKE)
    drive_base.straight(310, then=Stop.BRAKE)
    drive_base.turn(10, then=Stop.BRAKE)
    drive_base.straight(-305, then=Stop.BRAKE)
    drive_base.turn(65, then=Stop.BRAKE)
    drive_base.straight(110, then=Stop.BRAKE)
    front_attachment_motor.run_angle(1500, -280)
    drive_base.straight(175, then=Stop.BRAKE)
    drive_base.settings(straight_speed=1500)
    wait(200)
    front_attachment_motor.run_angle(500, 320)
    drive_base.straight(-300, then=Stop.BRAKE)

def _F0_9F_98_8EMr__Claw_the_37th_s_noble_mission_F0_9F_AB_A1():
    pass


# The main program starts here.
print('Hello, Pybricks!')

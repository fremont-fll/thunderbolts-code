from pybricks.parameters import Stop

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


# The main program starts here.
print('Hello, Pybricks!')

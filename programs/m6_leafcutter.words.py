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
    print('bananas are awesome :)')
    drive_base.settings(straight_speed=200)
    drive_base.straight(700, then=Stop.BRAKE)
    turn_with_gybro(-90)
    align_heading()
    drive_base.straight(400, then=Stop.BRAKE)
    turn_with_gybro(-45)
    drive_base.settings(straight_acceleration=750)
    # push leaf cutter
    drive_base.settings(straight_speed=100)
    drive_base.straight(-220, then=Stop.BRAKE)
    drive_base.settings(straight_speed=200)
    drive_base.straight(200, then=Stop.BRAKE)
    turn_with_gybro(45)
    align_heading()
    drive_base.straight(-320)
    turn_with_gybro(90)
    align_heading()
    drive_base.straight(-80, then=Stop.BRAKE)
    front_attachment_motor.run_angle(500, -270, Stop.BRAKE)
    drive_base.straight(105, then=Stop.BRAKE)
    front_attachment_motor.run_angle(500, 120, Stop.BRAKE)
    drive_base.straight(-35, then=Stop.BRAKE)
    front_attachment_motor.run_angle(500, -120, Stop.BRAKE)
    drive_base.straight(-50, then=Stop.BRAKE)

def turn_w():
    pass


# The main program starts here.
print('Hello, Pybricks!')

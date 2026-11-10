from pybricks.parameters import Stop
from pybricks.tools import wait

from robot import (
    align_heading,
    back_attachment_motor,
    drive_base,
    front_attachment_motor,
    prime_hub,
    reset_heading,
    turn_with_gybro,
)

def m7_humongus_fungus_v2():
    # This is me and Nemish's code for the right side.
    # We are doing algae thingy and ants,
    reset_heading()
    drive_base.settings(straight_speed=300)
    drive_base.use_gyro(True)
    drive_base.straight(590)
    turn_with_gybro(-90)
    drive_base.straight(110)
    drive_base.use_gyro(True)
    turn_with_gybro(90)
    align_heading()
    front_attachment_motor.run_angle(250, -225, Stop.BRAKE)
    align_heading()
    drive_base.straight(60)
    front_attachment_motor.run_angle(250, 60, Stop.BRAKE)
    drive_base.straight(-20)
    front_attachment_motor.run_angle(500, -40, Stop.BRAKE)
    drive_base.straight(-80)
    front_attachment_motor.run_angle(250, 205, Stop.BRAKE)
    align_heading()
    drive_base.straight(150)
    turn_with_gybro(65)
    drive_base.straight(-50, then=Stop.BRAKE)
    front_attachment_motor.run_angle(500, -225, Stop.BRAKE)
    drive_base.straight(80, then=Stop.BRAKE)
    front_attachment_motor.run_angle(500, 80, Stop.BRAKE)
    drive_base.straight(-50, then=Stop.BRAKE)
    turn_with_gybro(25)
    drive_base.straight(-300, then=Stop.BRAKE)
    turn_with_gybro(-45)
    front_attachment_motor.run_angle(250, 50, Stop.BRAKE)
    drive_base.straight(500, then=Stop.BRAKE)
    align_heading()
    drive_base.straight(-30, then=Stop.BRAKE)
    turn_with_gybro(90)
    drive_base.straight(200, then=Stop.BRAKE)
    turn_with_gybro(-10)
    drive_base.straight(30, then=Stop.BRAKE)
    turn_with_gybro(10)
    drive_base.straight(500, then=Stop.BRAKE)

def my_task():
    drive_base.settings(straight_speed=200)
    drive_base.use_gyro(True)
    drive_base.use_gyro(False)
    drive_base.straight(500)
    drive_base.turn(-90)
    drive_base.straight(115)
    drive_base.turn(91)
    front_attachment_motor.run_angle(500, -360)
    front_attachment_motor.run_angle(500, 50)
    drive_base.straight(215)
    wait(1000)
    front_attachment_motor.run_angle(500, -50)
    drive_base.straight(-100)

def m_11():
    drive_base.settings(straight_speed=185)
    drive_base.straight(320, then=Stop.BRAKE)
    drive_base.straight(-180, then=Stop.BRAKE)
    drive_base.turn(40)
    drive_base.straight(180, then=Stop.BRAKE)
    front_attachment_motor.run_angle(2000, -360, Stop.BRAKE)


# The main program starts here.
print('Hello, Pybricks!')

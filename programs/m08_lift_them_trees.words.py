from pybricks.parameters import Stop
from pybricks.tools import wait

from robot import (
    align_heading,
    back_attachment_motor,
    drive_base,
    front_attachment_motor,
    get_desired_heading,
    prime_hub,
    reset_heading,
    set_desired_heading,
    turn_with_gybro,
)

def reset_treehaus_arms():
    set_desired_heading(0)
    reset_heading()
    turn_with_gybro(90)
    wait(1000)
    align_heading()

def lift_the_treehaus():
    set_desired_heading(0)
    reset_heading()
    drive_base.settings(straight_speed=400)
    drive_base.use_gyro(False)
    drive_base.use_gyro(True)
    drive_base.straight(700)
    align_heading()
    front_attachment_motor.run_angle(5000, -1100)
    drive_base.straight(65, then=Stop.BRAKE)
    front_attachment_motor.run_angle(400, 425, Stop.BRAKE)
    drive_base.settings(straight_speed=100)
    drive_base.straight(95, then=Stop.BRAKE)
    front_attachment_motor.run_angle(400, -50, Stop.BRAKE)
    drive_base.straight(-115, then=Stop.BRAKE)
    front_attachment_motor.run_angle(500, -90)
    drive_base.straight(20, then=Stop.BRAKE)
    front_attachment_motor.run_angle(400, 50)
    drive_base.straight(35, then=Stop.BRAKE)
    front_attachment_motor.run_angle(400, 150)
    drive_base.straight(80, then=Stop.BRAKE)
    front_attachment_motor.run_angle(500, -210)
    drive_base.straight(-250)
    # end of reaching roots
    turn_with_gybro(90)
    align_heading()
    drive_base.settings(straight_speed=200)
    drive_base.straight(255)
    front_attachment_motor.run_angle(500, -190)
    turn_with_gybro(-90)
    align_heading()
    drive_base.settings(straight_speed=100)
    drive_base.straight(100, then=Stop.BRAKE)
    front_attachment_motor.run_angle(1000, 450)
    wait(67)
    front_attachment_motor.run_angle(1000, -300)
    drive_base.straight(-90)
    # Everything after this is getting the robot back to home
    drive_base.turn(45)
    front_attachment_motor.run_angle(500, 500)
    drive_base.settings(straight_acceleration=[300, 750])
    drive_base.settings(straight_speed=1500)
    drive_base.straight(-800, then=Stop.BRAKE)
    print('Matthew is the GOAT of being GOATED!!!!!!')
    drive_base.settings(straight_speed=200)

def reset_front():
    front_attachment_motor.run_angle(500, 360)


# The main program starts here.

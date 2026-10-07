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
    # This is Jack and Varun's mission. Matthew is hoping to add an arm on the back attachment port that can lift up Mission 5, the tree branch thing.
    drive_base.use_gyro(False)
    drive_base.use_gyro(True)
    drive_base.straight(275, then=Stop.BRAKE)
    drive_base.turn(-28, then=Stop.BRAKE)
    drive_base.straight(270, then=Stop.BRAKE)
    drive_base.turn(10, then=Stop.BRAKE)
    print('What did the sushi say to the bee? Whasa bee(wasabi).', 'Thunderbolts are just better like that in FLL. SUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU!!!!!!!!!!!!!!!!!!!!')
    drive_base.straight(-305, then=Stop.BRAKE)
    drive_base.turn(75, then=Stop.BRAKE)
    drive_base.straight(80, then=Stop.BRAKE)
    front_attachment_motor.run_angle(1500, -280)
    drive_base.straight(175, then=Stop.BRAKE)
    drive_base.settings(straight_speed=1500)
    wait(200)
    front_attachment_motor.run_angle(300, 250)
    drive_base.straight(-385, then=Stop.BRAKE)
    front_attachment_motor.run_angle(500, 200)


# The main program starts here.
turn_with_gybro(45)
print(get_desired_heading())
align_heading()

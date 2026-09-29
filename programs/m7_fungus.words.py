from pybricks.parameters import Stop

from robot import (
    align_heading,
    back_attachment_motor,
    drive_base,
    front_attachment_motor,
    prime_hub,
    turn_with_gybro,
)

def m7_humongus_fungus():
    prime_hub.imu.reset_heading(0)
    drive_base.use_gyro(True)

def _F0_9F_98_8EMr__Claw_the_37th_s_noble_mission_F0_9F_AB_A1():
    # This is me and Nemish's code for the right side.
    # We are doing algae thingy and ants,
    drive_base2.use_gyro(True)
    drive_base2.straight(500)
    drive_base2.turn(-90)
    drive_base2.straight(97)
    drive_base2.turn(90)
    front_attachment_motor2.run_angle(500, -300)
    drive_base2.straight(113)
    front_attachment_motor2.run_angle(500, 90, Stop.BRAKE)
    drive_base2.straight(-20)
    front_attachment_motor2.run_angle(500, -29.999, Stop.BRAKE)
    drive_base2.straight(-75)
    drive_base2.straight(40, then=Stop.BRAKE)
    front_attachment_motor2.run_angle(500, 200, Stop.BRAKE)
    drive_base2.straight(92)
    drive_base2.turn(-90)
    drive_base2.straight(340, then=Stop.BRAKE)
    drive_base2.turn(135, then=Stop.BRAKE)
    print('Yo Sup Chat!!! This is Namish, and yall are great at legos.')
    drive_base2.settings(straight_speed=100)
    drive_base2.straight(500, then=Stop.BRAKE)
    drive_base2.turn(90)
    drive_base2.straight(-10, then=Stop.COAST)


# The main program starts here.
print('Hello, Pybricks!')

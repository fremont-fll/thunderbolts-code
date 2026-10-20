from pybricks.parameters import Stop

from robot import (
    align_heading,
    back_attachment_motor,
    drive_base,
    front_attachment_motor,
    prime_hub,
    turn_with_gybro,
)

def m7_humongus_fungus_v2():
    # This is me and Nemish's code for the right side.
    # We are doing algae thingy and ants,
    drive_base.settings(straight_speed=300)
    drive_base.use_gyro(True)
    drive_base.straight(500)
    drive_base.turn(-90)
    drive_base.straight(108)
    drive_base.turn(90)
    front_attachment_motor.run_angle(500, -300)
    drive_base.straight(113)
    front_attachment_motor.run_angle(500, 90, Stop.BRAKE)
    drive_base.straight(-20)
    front_attachment_motor.run_angle(500, -29.999, Stop.BRAKE)
    drive_base.straight(-75)
    drive_base.straight(40, then=Stop.BRAKE)
    front_attachment_motor.run_angle(500, 200, Stop.BRAKE)
    drive_base.straight(142)
    drive_base.turn(-90)
    drive_base.straight(374, then=Stop.BRAKE)
    drive_base.turn(135, then=Stop.BRAKE)
    drive_base.settings(straight_speed=215)
    drive_base.straight(434, then=Stop.BRAKE)
    drive_base.straight(-12, then=Stop.BRAKE)
    drive_base.turn(42)
    drive_base.straight(475, then=Stop.BRAKE)
    front_attachment_motor.run_angle(500, -100, Stop.BRAKE)
    front_attachment_motor.run_angle(500, 85, Stop.BRAKE)
    front_attachment_motor.run_angle(500, -100, Stop.BRAKE)

def _F0_9F_98_8EMr__Claw_the_37th_s_noble_mission_F0_9F_AB_A1():
    pass


# The main program starts here.
print('Hello, Pybricks!')

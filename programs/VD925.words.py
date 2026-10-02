from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Button, Color, Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Set up.
prime_hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
the_program = 0
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)
back_attachment_motor = Motor(Port.C, Direction.CLOCKWISE)
front_attachment_motor = Motor(Port.F, Direction.CLOCKWISE)
left_color_sensor = ColorSensor(Port.B)
right_color_sensor = ColorSensor(Port.D)
drive_base = DriveBase(left_motor, right_motor, 88, 144.75)


# The main program starts here.
# This code needs to be moved to new arch
prime_hub.system.set_stop_button(None)
while True:
    prime_hub.display.number(the_program)
    prime_hub.light.on(Color.GREEN)
    if Button.LEFT in prime_hub.buttons.pressed():
        the_program = the_program - 1
        wait(200)
    elif Button.RIGHT in prime_hub.buttons.pressed():
        the_program = the_program + 1
        wait(200)
    elif Button.CENTER in prime_hub.buttons.pressed():
        wait(200)
        prime_hub.system.set_stop_button(Button.CENTER)
        if the_program == 0:
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
        elif the_program == 1:
            front_attachment_motor.run_angle(500, 360)
        elif the_program == 2:
            drive_base.straight(600)
            drive_base.turn(90)
            drive_base.settings(straight_speed=4000)
            drive_base.straight(530)
        elif the_program == 3:
            pass
        elif the_program == 4:
            pass
        elif the_program == -1:
            drive_base.straight(200)
            front_attachment_motor.run_angle(500, -270)
            drive_base.straight(-670, then=Stop.BRAKE)
        else:
            pass
    else:
        prime_hub.system.set_stop_button(None)

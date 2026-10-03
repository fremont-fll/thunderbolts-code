from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Button, Color, Direction, Port
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Set up.
prime_hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)
back_attachment_motor = Motor(Port.C, Direction.CLOCKWISE)
front_attachment_motor = Motor(Port.F, Direction.CLOCKWISE)
left_color_sensor = ColorSensor(Port.B)
right_color_sensor = ColorSensor(Port.D)
drive_base = DriveBase(left_motor, right_motor, 88, 144.75)
the_program = 0


# The main program starts here.
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
            drive_base.use_gyro(True)
            drive_base.turn(90)
        elif the_program == 1:
            pass
        elif the_program == 2:
            pass
        elif the_program == 3:
            pass
        elif the_program == 4:
            pass
        elif the_program == -1:
            print(prime_hub.imu.heading())
        else:
            pass
    else:
        prime_hub.system.set_stop_button(None)

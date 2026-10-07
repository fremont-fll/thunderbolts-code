from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Hardware: runs once, the first time any file imports robot
prime_hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)
back_attachment_motor = Motor(Port.C, Direction.CLOCKWISE)
front_attachment_motor = Motor(Port.F, Direction.CLOCKWISE)
left_color_sensor = ColorSensor(Port.B)
right_color_sensor = ColorSensor(Port.D)
drive_base = DriveBase(left_motor, right_motor, 88, 145)

# Heading state lives here, so only functions in this file change it
desired_heading = 0


def reset_heading(angle=0):
    """Reset the gyro AND the target heading together."""
    global desired_heading
    prime_hub.imu.reset_heading(angle)
    desired_heading = angle


def turn_with_gybro(angle):
    global desired_heading
    drive_base.turn(angle, then=Stop.BRAKE)
    desired_heading = desired_heading + angle


def align_heading():
    heading_error = desired_heading - prime_hub.imu.heading()
    drive_base.use_gyro(False)
    drive_base.settings(turn_rate=50)
    while abs(heading_error) > 0.5:
        drive_base.turn(1.5 * heading_error, then=Stop.BRAKE)
        heading_error = desired_heading - prime_hub.imu.heading()
        print('correction', prime_hub.imu.heading(), heading_error, desired_heading)
        wait(100)
    drive_base.settings(turn_rate=150)
    drive_base.use_gyro(True)


def stop_everything():
    drive_base.stop()
    front_attachment_motor.stop()
    back_attachment_motor.stop()


def get_desired_heading():
    return desired_heading


def set_desired_heading(angle):
    global desired_heading
    desired_heading = angle
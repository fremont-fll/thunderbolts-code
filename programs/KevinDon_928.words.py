from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Button, Color, Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait

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
desired_heading = 0
heading_error = 0

async def Skunk_Works_Project__Align_Heading():
    global heading_error
    await wait(0)
    heading_error = desired_heading - prime_hub.imu.heading()
    drive_base.use_gyro(False)
    while abs(heading_error) > 0.5:
        await wait(0)
        drive_base.settings(turn_rate=50)
        await drive_base.turn(1.5 * heading_error, then=Stop.BRAKE)
        heading_error = desired_heading - prime_hub.imu.heading()
        print('correction routine')
        print(prime_hub.imu.heading())
        print(heading_error)
        print(desired_heading)
        await wait(100)
    drive_base.settings(turn_rate=150)
    drive_base.use_gyro(True)
    print(prime_hub.imu.heading())
    print(desired_heading)
    print(heading_error)

async def _F0_9F_98_8EMr__Claw_the_37th_s_noble_mission_F0_9F_AB_A1():
    await wait(0)
    # This is me and Nemish's code for the right side.
    # We are doing algae thingy and ants,
    drive_base.use_gyro(True)
    await drive_base.straight(500)
    await drive_base.turn(-90)
    await drive_base.straight(97)
    await drive_base.turn(90)
    await front_attachment_motor.run_angle(500, -300)
    await drive_base.straight(113)
    await front_attachment_motor.run_angle(500, 90, Stop.BRAKE)
    await drive_base.straight(-20)
    await front_attachment_motor.run_angle(500, -29.999, Stop.BRAKE)
    await drive_base.straight(-75)
    await drive_base.straight(40, then=Stop.BRAKE)
    await front_attachment_motor.run_angle(500, 200, Stop.BRAKE)
    await drive_base.straight(92)
    await drive_base.turn(-90)
    await drive_base.straight(340, then=Stop.BRAKE)
    await drive_base.turn(135, then=Stop.BRAKE)
    print('Yo Sup Chat!!! This is Namish, and yall are great at legos.')
    drive_base.settings(straight_speed=100)
    await drive_base.straight(500, then=Stop.BRAKE)
    await drive_base.turn(90)
    await drive_base.straight(-10, then=Stop.COAST)

async def turn_with_gybro(angle):
    global desired_heading
    await wait(0)
    await drive_base.turn(angle, then=Stop.BRAKE)
    desired_heading = desired_heading + angle

async def Donovan_and_Kevin_s_mission():
    await wait(0)
    # This is me and Nemish's code for the right side.
    # We are doing algae thingy and ants,
    drive_base.use_gyro(True)
    await drive_base.straight(500)
    await drive_base.turn(-90)
    await drive_base.straight(97)
    await drive_base.turn(90)
    await front_attachment_motor.run_angle(500, -300)
    await drive_base.straight(113)
    await front_attachment_motor.run_angle(500, 90, Stop.BRAKE)
    await drive_base.straight(-20)
    await front_attachment_motor.run_angle(500, -29.999, Stop.BRAKE)
    await drive_base.straight(-75)
    await drive_base.straight(40, then=Stop.BRAKE)
    await front_attachment_motor.run_angle(500, 200, Stop.BRAKE)
    await drive_base.straight(92)
    await drive_base.turn(-90)
    await drive_base.straight(340, then=Stop.BRAKE)
    await drive_base.turn(135, then=Stop.BRAKE)
    print('Yo Sup Chat!!! This is Namish, and yall are great at legos.')
    drive_base.settings(straight_speed=100)
    await drive_base.straight(500, then=Stop.BRAKE)
    await drive_base.turn(90)
    await drive_base.straight(-10, then=Stop.COAST)

async def idk_6767():
    await wait(0)
    await drive_base.straight(600)
    await drive_base.turn(90)
    await drive_base.straight(487)
    await drive_base.straight(-50)
    await drive_base.turn(90)
    await drive_base.straight(100)
    await drive_base.turn(-90)
    await front_attachment_motor.run_angle(500, -60)

async def main1():
    global the_program
    prime_hub.system.set_stop_button(None)
    while True:
        await wait(0)
        prime_hub.display.number(the_program)
        prime_hub.light.on(Color.GREEN)
        if Button.LEFT in prime_hub.buttons.pressed():
            the_program = the_program - 1
            await wait(200)
        elif Button.RIGHT in prime_hub.buttons.pressed():
            the_program = the_program + 1
            await wait(200)
        elif Button.CENTER in prime_hub.buttons.pressed():
            await wait(200)
            prime_hub.system.set_stop_button(Button.CENTER)
            if the_program == 0:
                await front_attachment_motor.run_angle(500, 360, Stop.BRAKE)
            elif the_program == 1:
                await _F0_9F_98_8EMr__Claw_the_37th_s_noble_mission_F0_9F_AB_A1()
            elif the_program == 2:
                await idk_6767()
            elif the_program == 3:
                pass
            elif the_program == 4:
                pass
            elif the_program == -1:
                print(prime_hub.imu.heading())
            elif the_program == -2:
                pass
            else:
                pass
        else:
            prime_hub.system.set_stop_button(None)

async def main2():
    pass


async def main():
    await multitask(main1(), main2())

run_task(main())
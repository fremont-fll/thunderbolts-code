from pybricks.parameters import Stop
from pybricks.tools import multitask, run_task, wait

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

async def reset_front():
    await wait(0)
    await front_attachment_motor.run_angle(500, 360)

async def lift_the_treehaus():
    await wait(0)
    set_desired_heading(0)
    drive_base.settings(straight_speed=250)
    drive_base.use_gyro(False)
    drive_base.use_gyro(True)

async def m1_spoiled_drone():
    await wait(0)
    drive_base.settings(straight_speed=250)
    await drive_base.straight(-500)

async def main():
    pass


run_task(main())
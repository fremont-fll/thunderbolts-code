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

def m1_drone():
    set_desired_heading(0)
    drive_base.straight(-700)


# The main program starts here.
turn_with_gybro(45)
print(get_desired_heading())
align_heading()

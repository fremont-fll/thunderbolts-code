from robot import prime_hub, stop_everything
from menu import run_menu
from m7_fungus import m7_humongus_fungus
from m3_flip_the_rock import flip_the_rock, reset_front
from m15_biocenter import m15_biocenter_idk6767 


run_menu(prime_hub, {
    -1: reset_front,
    0: flip_the_rock,
    1: m7_humongus_fungus,
    2: m15_biocenter_idk6767,
}, on_abort=stop_everything)
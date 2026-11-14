from robot import prime_hub, stop_everything
from menu import run_menu
from m7_fungus import m7_humongus_fungus_v2, m_11
from m3_flip_the_rock import flip_the_rock, reset_front
from m15_biocenter import m15_biocenter_idk6767, lift 
from m1_spoiled_drone import m1_drone
from m08_lift_them_trees import lift_the_treehaus, reset_treehaus_arms, lift_the_treehaus_leaves


run_menu(prime_hub, {
    -2: lift,
    -1: reset_front,
    0: flip_the_rock,
    1: m7_humongus_fungus_v2,
    2: m15_biocenter_idk6767,
    3: m1_drone,
    4: lift_the_treehaus,
    5: lift_the_treehaus_leaves,
    6: m_11
}, on_abort=stop_everything)
print ("Matthew_is_the_GOAT")

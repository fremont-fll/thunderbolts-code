from robot import prime_hub, stop_everything
from menu import run_menu
from m7_fungus import m7_humongus_fungus


run_menu(prime_hub, {
    1: m7_humongus_fungus,
}, on_abort=stop_everything)
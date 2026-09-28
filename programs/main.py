from robot import prime_hub, stop_everything
from menu import run_menu
from m6_leafcutter import m6_leafcutter_frenzy


run_menu(prime_hub, {
    6: m6_leafcutter_frenzy,
    7: m6_leafcutter_frenzy,
}, on_abort=stop_everything)
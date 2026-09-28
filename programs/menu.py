from pybricks.parameters import Button
from pybricks.tools import wait


def _wait_for_release(hub):
    while hub.buttons.pressed():
        wait(10)


def run_menu(hub, programs, start=None, advance=True, on_abort=None):
    """Mission selector.

    programs: dict {int: function}, or a plain list of functions
              (keys become 0, 1, 2, ...).
    start:    key to show first (defaults to the lowest key).
    advance:  move to the next mission after one finishes.
    on_abort: function called if a mission is stopped with the center button.
    """
    if not isinstance(programs, dict):
        programs = {i: f for i, f in enumerate(programs)}
    keys = sorted(programs.keys())
    index = keys.index(start) if start in keys else 0

    hub.system.set_stop_button(None)
    while True:
        key = keys[index]
        hub.display.number(key)
        pressed = hub.buttons.pressed()

        if Button.LEFT in pressed:
            index = (index - 1) % len(keys)
            _wait_for_release(hub)
        elif Button.RIGHT in pressed:
            index = (index + 1) % len(keys)
            _wait_for_release(hub)
        elif Button.CENTER in pressed:
            _wait_for_release(hub)
            hub.system.set_stop_button(Button.CENTER)
            finished = False
            try:
                programs[key]()
                finished = True
            except SystemExit:
                if on_abort:
                    on_abort()
            finally:
                hub.system.set_stop_button(None)
            _wait_for_release(hub)
            if finished and advance:
                index = (index + 1) % len(keys)
        wait(10)


def run_menu_lists(hub, keys, funcs, **kwargs):
    """Same as run_menu, but takes two parallel lists instead of a dict."""
    run_menu(hub, dict(zip(keys, funcs)), **kwargs)
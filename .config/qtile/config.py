###
# Custom Qtile Config
# - Chris Ruzin
###

# TODO: Look into EWW
# TODO: Toggle screensaver
# TODO: Add clipboard manager
# TODO: Disable screensaver when viewing videos?

from defines import *
from groups import *
from keys import *
from layouts import *
from mouse import *
from screens import *
from hooks import *

try:
    from typing import List  # noqa: F401
except ImportError:
    pass


auto_fullscreen = True
# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True
bring_front_click = False
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
focus_on_window_activation = "focus"  # "smart"
follow_mouse_focus = True
reconfigure_screens = True

wmname = "LG3D"

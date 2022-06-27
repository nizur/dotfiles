from libqtile.config import Click, Drag
from libqtile.lazy import lazy

MOD = "mod4"

mouse = [
    Drag([MOD], "Button0", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD], "Button2", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD], "Button1", lazy.window.bring_to_front())
]

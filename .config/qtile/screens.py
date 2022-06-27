from os.path import expanduser

from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

from widgets.owm import OpenWeatherMap
from widgets.volume import MyPulseVolume

from classes import Helpers, Palette

# TODO: Add CPU/Memory/HD to info section?

dpi = Helpers.dpi
theme = "mocha"

layout_icon_paths = "" if theme == "mocha" else [
    expanduser("~/.config/qtile/layout-icons/gruvbox-dark0")]
opensuse_icon = "Button-monochrome" if theme == "mocha" else "Button-monochrome-white"

widget_defaults = dict(
    background=Palette.colors[theme]["base"],
    font="iM WritingQuattroS Nerd Font",
    fontsize=dpi(13),
    foreground=Palette.colors[theme]["text"],
    padding=dpi(10),
)
extension_defaults = widget_defaults.copy()

num_screens = int(Helpers.get_num_screen())
screens = []

for i in range(0, num_screens):
    screens.extend([
        Screen(
            top=bar.Bar([
                widget.Spacer(
                    background=Palette.colors["opensuse"],
                    length=2,
                ),
                widget.Image(
                    background=Palette.colors["opensuse"],
                    filename=expanduser(
                        f"~/.local/share/opensuse/{opensuse_icon}.png"),
                    margin=dpi(4),
                ),
                widget.CheckUpdates(
                    background=Palette.colors["opensuse"],
                    colour_have_updates=Palette.colors[theme]["base"],
                    custom_command="zypper lu",
                    custom_command_modify=lambda x: x - 4,
                    display_format="{updates} ",
                    mouse_callbacks={
                        "Button1": lazy.spawn("kitty -e sudo zypper dup"),
                    },
                    padding=0,
                    update_interval=14400,
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=layout_icon_paths,
                    padding=dpi(4),
                    scale=0.5,
                ),
                widget.Chord(
                    chords_colors={
                        "Audio": (Palette.colors[theme]["peach"], Palette.colors[theme]["base"]),
                        "Gnome": (Palette.colors[theme]["mauve"], Palette.colors[theme]["base"]),
                        "Grow": (Palette.colors[theme]["blue"], Palette.colors[theme]["base"]),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.WindowName(
                    for_current_screen=True,
                    padding=dpi(10),
                ),
                widget.Spacer(),
                widget.GroupBox(
                    active=Palette.colors[theme]["overlay0"],
                    block_highlight_text_color=Palette.colors[theme]["text"],
                    borderwidth=0,
                    disable_drag=True,
                    fontsize=dpi(20),
                    hide_unused=True,
                    inactive=Palette.colors[theme]["base"],
                    padding=dpi(2),
                    rounded=False,
                    urgent_text=Palette.colors[theme]["red"],
                ),
                widget.Spacer(),
                widget.Prompt(
                    bell_style="visual",
                    cursor_color=Palette.colors[theme]["red"],
                    ignore_dups_history=True,
                    prompt=" ",
                    visual_bell_color=Palette.colors[theme]["red"],
                ),
                widget.Clipboard(
                    blacklist=["1password", "1Password"],
                    fmt=" {}",
                    foreground=Palette.colors[theme]["flamingo"],
                ),
                widget.WindowCount(
                    padding=dpi(10),
                    text_format=" {num}",
                ),
                MyPulseVolume(
                    foreground=Palette.colors[theme]["sapphire"],
                    get_volume_command="pamixer --get-volume-human",
                    limit_max_volume=True,
                    mute_command="pamixer -m",
                    step=4,
                    volume_app="pamixer",
                    volume_down_command="pamixer -d 4",
                    volume_up_command="pamixer -i 4",
                ),
                OpenWeatherMap(
                    api_key="b8c0a2258d0134fb50533560dfb89a73",
                    foreground=Palette.colors[theme]["green"],
                    format="{icon} {temp:.0f}{temp_units}",
                    latitude=30.2,
                    longitude=-97.7,
                    units="imperial",
                ),
                widget.Clock(
                    foreground=Palette.colors[theme]["yellow"],
                    format=" %a %B %d",
                ),
                widget.Clock(
                    foreground=Palette.colors[theme]["peach"],
                    format=" %I:%M %p",
                ),
                widget.Spacer(
                    length=6,
                ),
                widget.WidgetBox(
                    widgets=[
                        widget.TextBox(
                            background=Palette.colors[theme]["crust"],
                            foreground=Palette.colors[theme]["green"],
                            text=" " + Helpers.get_os_release(),
                        ),
                        widget.TextBox(
                            background=Palette.colors[theme]["crust"],
                            foreground=Palette.colors[theme]["yellow"],
                            text=" " + Helpers.get_kernel_release(),
                        ),
                        widget.Systray(
                            background=Palette.colors[theme]["crust"],
                        ),
                        widget.Spacer(
                            background=Palette.colors[theme]["crust"],
                            length=6,
                        ),
                    ],
                    fontsize=dpi(18),
                    text_closed="",
                    text_open="",
                ),
                widget.Spacer(
                    length=6,
                ),
                widget.Wallpaper(
                    directory=expanduser("~/Pictures/Wallpapers"),
                    fontsize=dpi(16),
                    foreground=Palette.colors[theme]["text"],
                    label="",
                    random_selection=True,
                ),
                widget.Spacer(
                    length=4,
                ),
            ],
                background=Palette.colors[theme]["base"],
                border_color=Palette.colors["opensuse"],
                border_width=[dpi(1), 0, 0, 0],
                foreground=Palette.colors[theme]["text"],
                margin=dpi(5),
                opacity=0.888888880,
                size=dpi(28),
            ),
        )
    ])

from libqtile import qtile
from libqtile.config import Key, KeyChord, ScratchPad
from libqtile.lazy import lazy

from classes import Helpers
from groups import groups

ALT = "mod1"
MOD = "mod4"
CTL = "control"
SHIFT = "shift"

keys = [

    ##########
    # CHORDS #
    ##########

    # AUDIO #

    KeyChord([MOD], "a", [
        Key([], "Print",
            lazy.spawn("pamixer -m"),
            desc="Mute Track"),
        Key([], "Up",
            lazy.spawn("pamixer -i 5"),
            desc="Volume Up"),
        Key([], "Down",
            lazy.spawn("pamixer -d 5"),
            desc="Volume Down"),
        # Key([], "Left",
        #     lazy.spawn(Commands.audio_track_prev),
        #     desc="Previous Track"),
        # Key([], "Right",
        #     lazy.spawn(Commands.audio_track_next),
        #     desc="Next Track"),
        # Key([], "Return",
        #     lazy.spawn(Commands.audio_play_pause),
        #     desc="Play/Pause Track"),
    ], mode="Audio"),

    # WINDOW RESIZING #

    KeyChord([MOD], "g", [
        Key([], "h",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
            desc="Grow window to the left"),
        Key([], "l",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
            desc="Grow window to the right"),
        Key([], "j",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
            desc="Grow window down"),
        Key([], "k",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
            desc="Grow window up"),
        # Key([], "g",
        #     lazy.layout.grow(),
        #     desc="Grow window"),
        # Key([], "s",
        #     lazy.layout.shrink(),
        #     desc="Shrink window"),
        Key([], "m",
            lazy.layout.maximize(),
            desc="Maximize window"),
        Key([], "n",
            lazy.layout.normalize(),
            desc="Reset all window sizes"),
    ], mode="Grow"),

    # GNOME CONTROL #

    KeyChord([MOD, CTL], "g", [
        Key([], "l",
            lazy.spawn("gnome-screensaver-command -l"),
            desc="Suspend"),
        Key([], "q",
            lazy.spawn("gnome-session-quit --logout --no-prompt"),
            desc="Logout of Gnome"),
        Key([SHIFT], "q",
            lazy.spawn("gnome-session-quit --power-off"),
            desc="Shutdown"),
    ], mode="Gnome"),


    ###############
    # APP CONTROL #
    ###############

    Key([MOD], "d",
        lazy.spawn("rofi -show drun"),
        desc="Run launcher"),
    Key([MOD], "c",
        lazy.spawn("rofi -modi calc -show calc -no-show-match -no-bold"),
        desc="Run calculator"),
    Key([MOD], "p",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([MOD], "Return",
        lazy.spawn("kitty"),
        desc="Launch terminal"),
    Key([MOD], "0",
        lazy.group["dropdown"].dropdown_toggle("term"),
        desc="Toggle the terminal scratchpad"),
    Key([], "F12",
        lazy.group["dropdown"].dropdown_toggle("help"),
        desc="Display key bindings"),


    ########
    # MISC #
    ########

    Key([CTL], "F1",
        lazy.function(Helpers.go_to_urgent),
        desc="Switch to urgent group"),
    Key([MOD], "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen"),
    Key([MOD], "q",
        lazy.window.kill(),
        desc="Kill focused window"),
    Key([MOD, CTL], "n",
        lazy.spawn("dunstctl set-paused toggle"),
        desc="Toggle notifications"),


    ##############
    # SCREENSHOT #
    ##############

    Key([], "Print",
        Helpers.create_screenshot(clipboard=False),
        desc="Take a screenshot"),
    Key([ALT], "Print",
        Helpers.create_screenshot(mode="window", clipboard=False),
        desc="Take a screenshot of a specific window"),
    Key([CTL], "Print",
        Helpers.create_screenshot(mode="select", clipboard=False),
        desc="Take a screenshot of a selected area"),


    ################
    # WINDOW FOCUS #
    ################

    Key([MOD], "h",
        lazy.layout.left(),
        desc="Move focus left"),
    Key([MOD], "l",
        lazy.layout.right(),
        desc="Move focus right"),
    Key([MOD], "j",
        lazy.layout.down(),
        desc="Move focus down"),
    Key([MOD], "k",
        lazy.layout.up(),
        desc="Move focus up"),
    Key([MOD], "space",
        lazy.layout.next(),
        desc="Move focus to next window"),


    ###################
    # LAYOUT SPECIFIC #
    ###################

    # SWITCH TO NEXT AVAILABLE LAYOUT
    Key([MOD], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"),

    ### MONADS: FLIP/ROTATE ###
    Key([MOD, SHIFT], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Flip the layout"),

    ### BSP: FLIP LAYOUT ###
    Key([MOD, CTL], "k",
        lazy.layout.flip_up(),
        desc="Flip window up"),
    Key([MOD, CTL], "j",
        lazy.layout.flip_down(),
        desc="Flip window down"),
    Key([MOD, CTL], "l",
        lazy.layout.flip_right(),
        desc="Flip window right"),
    Key([MOD, CTL], "h",
        lazy.layout.flip_left(),
        desc="Flip window left"),

    ### BSP/STACK: MOVE WINDOWS ###
    Key([MOD, SHIFT], "h",
        lazy.layout.shuffle_left(),
        desc="Move window left"),
    Key([MOD, SHIFT], "l",
        lazy.layout.shuffle_right(),
        desc="Move window right"),
    Key([MOD, SHIFT], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([MOD, SHIFT], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"),

    ### STACK: SPLIT ###
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([MOD, SHIFT], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),


    #################
    # QTILE CONTROL #
    #################

    Key([MOD, CTL], "r",
        lazy.restart(),
        desc="Restart Qtile"),
    Key([MOD, CTL], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"),
]


#########################
# SWITCH BETWEEN GROUPS #
#########################

# for i, group in enumerate(groups, start=1):
for i in groups:
    if not isinstance(i, ScratchPad):
        group = i.name
        keys.extend([
            # SWITCH TO GROUP #
            Key([MOD], group, lazy.group[group].toscreen(),
                desc="Switch to group {}".format(group)),

            # SWITCH TO & MOVE FOCUSED WINDOW TO GROUP #
            Key([MOD, SHIFT], group, lazy.window.togroup(group, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group)),

            # SWITCH TO & MOVE ALL CURRENT WINDOWS TO GROUP #
            #Key([MOD, CTL], str(i), Helpers.windows_to_group(group)),
        ])

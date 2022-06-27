import platform

from os import access, X_OK, makedirs, remove
from os.path import expanduser, isdir
from re import search
from subprocess import check_output, run, Popen, PIPE
from time import time

from libqtile.command import lazy
from libqtile.log_utils import logger

from threading import Thread, Event


class AutoStart(object):
    commands = []

    def __init__(self):
        self.run()

    def load_commands(self):
        from defines import autostart as load
        self.commands = load()

    def check_running(self, cmd):
        try:
            r = run(["pgrep", "-f", "-l", "-a", " ".join(cmd)])
            if r.returncode == 1:
                logger.info(f"Process {cmd} is not started!")

                return False
        except Exception as e:
            logger.error(e)

            return False

        return True

    def thread_run(self, *cmd):
        logger.warning(f"Starting {cmd}")

        try:
            Popen(cmd, shell=False)
        except Exception as e:
            logger.error(e)

    def run(self):
        self.load_commands()

        for i in self.commands:
            if i is None:
                continue

            x = expanduser(i if type(i) is str else list(i)[0])
            c = [x] if type(i) is str else list(i)

            if not access(x, X_OK):
                logger.warning(f"{x} does not exist or is not executable!")
                continue

            if not self.check_running(c):
                logger.info(f"{c} Starting thread...")

                try:
                    Thread(target=self.thread_run, args=(c)).start()
                    # Popen(c, shell=False)
                except Exception as e:
                    logger.error(e)


# Catpuccin
class Palette(object):
    colors = {
        "opensuse": "#73ba25",

        "latte": {
            "rosewater": "#dc8a78",
            "flamingo": "#dd7878",
            "pink": "#ea76cb",
            "mauve": "#8839ef",
            "red": "#d20f39",
            "maroon": "#e64553",
            "peach": "#fe640b",
            "yellow": "#df8e1d",
            "green": "#40a02b",
            "teal": "#179299",
            "sky": "#04a5e5",
            "sapphire": "#209fb5",
            "blue": "#1e66f5",
            "lavender": "#7287fd",

            "text": "#4c4f69",
            "subtext1": "#5c5f77",
            "subtext0": "#6c6f85",
            "overlay2": "#7c7f93",
            "overlay1": "#8c8fa1",
            "overlay0": "#9ca0b0",
            "surface2": "#acb0be",
            "surface1": "#bcc0cc",
            "surface0": "#ccd0da",

            "base": "#eff1f5",
            "mantle": "#e6e9ef",
            "crust": "#dce0e8",
        },

        "mocha": {
            "rosewater": "#F5E0DC",
            "flamingo": "#F2CDCD",
            "pink": "#F5C2E7",
            "mauve": "#CBA6F7",
            "red": "#F38BA8",
            "maroon": "#EBA0AC",
            "peach": "#FAB387",
            "yellow": "#F9E2AF",
            "green": "#A6E3A1",
            "teal": "#94E2D5",
            "sky": "#89DCEB",
            "sapphire": "#74C7EC",
            "blue": "#89B4FA",
            "lavender": "#B4BEFE",

            "text": "#CDD6F4",
            "subtext1": "#BAC2DE",
            "subtext0": "#A6ADC8",
            "overlay2": "#9399B2",
            "overlay1": "#7F849C",
            "overlay0": "#6C7086",
            "surface2": "#585B70",
            "surface1": "#45475A",
            "surface0": "#313244",

            "base": "#1E1E2E",
            "mantle": "#181825",
            "crust": "#11111B",
        },
    }


class Helpers():
    # def update_group(window):
    #     @lazy.function
    #     def f(qtile):

    def get_kernel_release():
        return check_output(["uname", "-r"]).decode("utf-8").replace("\n", "")

    def get_os_release():
        return check_output(["lsb-release", "-rs"]).decode("utf-8").replace("\n", "")

    # TODO: Rewrite this copy/pasta code
    def go_to_urgent(qtile):
        cg = qtile.currentGroup
        for group in qtile.groupMap.values():
            if group == cg:
                continue
            if len([w for w in group.windows if w.urgent]) > 0:
                qtile.currentScreen.setGroup(group)
                return

    def create_screenshot(mode=False, clipboard=True):
        @lazy.function
        def f(qtile):
            targetdir = expanduser("~/Pictures/Screenshots/")
            logger.warning(targetdir)

            if not isdir(targetdir):
                try:
                    makedirs(targetdir)
                except OSError:
                    if not isdir(targetdir):
                        raise

            hostname = platform.node()
            cmd = ["maim"]
            opts = []

            if mode == "window":
                target = f"{targetdir}/{hostname}_window_{str(int(time() * 100))}.png"
                _id = qtile.current_window.cmd_info()["id"]
                opts.extend(["-i", f"{_id}"])
                logger.warning(opts)
            elif mode == "select":
                target = f"{targetdir}/{hostname}_select_{str(int(time() * 100))}.png"
                opts.append("-s")
                logger.warning(opts)
            else:
                target = f"{targetdir}/{hostname}_full_{str(int(time() * 100))}.png"

            cmd.extend(opts)
            cmd.append(target)

            logger.warning(cmd)

            r = run(cmd)

            if clipboard:
                logger.warning("Copying to clipboard!")
                if r.returncode == 0:
                    f = open(target, "rb")
                    x = run(["xclip", "-selection", "c", "-t",
                            "image/png"], input=f.read())
                    remove(target)
                else:
                    logger.error(f"Strange thing happened! {r}")

        return f

    def dpi(value):
        Xresources = expanduser("~/.Xresources")
        with open(Xresources) as X:
            xrdb = X.readlines()

        dpi = 96
        for line in xrdb:
            if search('dpi', line):
                dpi = line.split(':')[1].strip()

        return int(value * int(dpi) / 96)

    def get_screen_size():
        try:
            r = run(
                ["sh", "-c", "/usr/bin/xrandr | awk \"/\*/ {print $1}\""], stdout=PIPE, universal_newlines=True)

            s = r.stdout.lstrip().split("x", 2)
            w = s[0]
            h = s[1]

            return {
                "width": int(w),
                "height": int(h),
            }
        except Exception as e:
            logger.error(e)

        return {
            "width": 0,
            "height": 0,
        }

    def get_type_screen():
        det = "SD"

        dim = Helpers.get_screen_size()

        if dim["height"] >= 720:
            det = "HD"

        if dim["height"] >= 900:
            det = "HD+"

        if dim["height"] >= 1050:
            det = "WSXGA+"

        if dim["height"] >= 1080:
            det = "FHD"

        if dim["height"] >= 1971:
            det = "4K VMware"

        if dim["height"] >= 2160:
            det = "4K UHD"

        logger.error("Detected ~ resolution: %s" % det)

        return det

    def get_num_screen():
        num = 1

        try:
            r = run(["sh", "-c", "/usr/bin/xrandr --listactivemonitors | head -n1 | tr -dc \"0-9\""],
                    stdout=PIPE, universal_newlines=True)
            num = r.stdout.strip()
        except Exception as e:
            logger.error(e)

        return num

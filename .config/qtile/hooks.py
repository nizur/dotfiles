from os import environ
from psutil import Process
from subprocess import PIPE, Popen, run
from libqtile import qtile, hook
from libqtile.log_utils import logger

from classes import AutoStart, Helpers


@hook.subscribe.startup_once
def redshift():
    Popen(["redshift"])


@hook.subscribe.startup
def autostart():
    AutoStart()


@hook.subscribe.startup
def dbus_register():
    id = environ.get("DESKTOP_AUTOSTART_ID")
    logger.warning(f"DESKTOP_AUTOSTART_ID = {id}")
    if not id:
        return
    Popen(["dbus-send",
           "--session",
           "--print-reply",
           "--dest=org.gnome.SessionManager",
           "/org/gnome/SessionManager",
           "org.gnome.SessionManager.RegisterClient",
           "string:qtile",
           f"string:{id}"])


@hook.subscribe.startup_complete
def auto_screens():
    r = run(["sh", "-c", "xrandr --listactivemonitors | head -n1"],
            stdout=PIPE, universal_newlines=True)
    r = r.stdout.replace("\n", "")
    logger.warning(f"{r} Found")


@hook.subscribe.screen_change
def set_screens(event):
    if event:
        run(["autorandr", "--change"])
    qtile.restart()

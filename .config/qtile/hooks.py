from os import environ
from subprocess import PIPE, Popen, run
from libqtile import qtile, hook
from libqtile.log_utils import logger

from classes import AutoStart


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


@hook.subscribe.client_new
def dialogs(window):
    if(window.window.get_wm_type() == 'dialog' or window.window.get_wm_transient_for()):
        window.floating = True


@hook.subscribe.client_new
def client_new(client):
    if client.name == 'Firefox':
        client.togroup('1')
    elif client.name == 'Code':
        client.togroup('2')
    elif client.name == 'Discord':
        client.togroup('5')
    elif client.wm_class == 'Gimp-2.10':
        client.togroup('8')

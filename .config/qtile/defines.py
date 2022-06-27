def autostart():
    from os.path import expanduser

    yield "/usr/bin/picom", "-b", "--experimental-backends"
    yield "/usr/bin/gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", "'Catppuccin-blue'"
    yield "/usr/bin/gsettings", "set", "org.gnome.desktop.wm.preferences", "theme", "'Catppuccin-blue'"
    yield "/usr/bin/gsettings", "set", "org.gnome.desktop.interface", "icon-theme", "'Newaita-reborn-dark'"
    yield "/usr/bin/xrdb", "-merge", expanduser("~/.Xresources")

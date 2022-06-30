from __future__ import annotations

from typing import Any

from libqtile import bar, hook
from libqtile.widget import base


class WindowIndicators(base._TextBox):
    """
    A simple widget to display the number of windows in the
    current group of the screen on which the widget is.
    """

    defaults = [
        ("font", "sans", "Text font"),
        ("fontsize", None, "Font pixel size. Calculated if None."),
        ("fontshadow", None, "Font shadow color, default is None(no shadow)"),
        ("indicator", "*", "Indicator for each window, default is *"),
        ("padding", None, "Padding left and right. Calculated if None."),
        ("foreground", "#ffffff", "Foreground colour."),
        ("text_format", "{windows}", "Format for message"),
        ("show_zero", False, "Show window count when no windows"),
    ]  # type: list[tuple[str, Any, str]]

    def __init__(self, width=bar.CALCULATED, **config):
        base._TextBox.__init__(self, width=width, **config)
        self.add_defaults(WindowIndicators.defaults)
        self._count = 0

    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        self._setup_hooks()
        self._wincount()

    def _setup_hooks(self):
        hook.subscribe.client_killed(self._win_killed)
        hook.subscribe.client_managed(self._wincount)
        hook.subscribe.current_screen_change(self._wincount)
        hook.subscribe.setgroup(self._wincount)

    def _wincount(self, *args):
        try:
            self._count = len(self.bar.screen.group.windows)
        except AttributeError:
            self._count = 0

        self.update(self.text_format.format(
            windows=self.indicator * self._count))

    def _win_killed(self, window):
        try:
            self._count = len(self.bar.screen.group.windows)
            if window.group == self.bar.screen.group:
                self._count -= 1
        except AttributeError:
            self._count = 0

        self.update(self.text_format.format(
            windows=self.indicator * self._count))

    def calculate_length(self):
        if self.text and (self._count or self.show_zero):
            return min(self.layout.width, self.bar.width) + self.actual_padding * 2
        else:
            return 0

    def cmd_get(self):
        """Retrieve the current text."""
        return self.text

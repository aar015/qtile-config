# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os, subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget
from typing import List  # noqa: F401

# Define some directories
home = os.path.expanduser('~')
config = home + '/.config/qtile'

# Define keyboard variables
mod = "mod4"
shift = "shift"

# Define color
text = 'FFFFFF'
focus = '215578'

# Define some functions
def increase_brightness():
    @lazy.function
    def __inner(qtile):
        subprocess.Popen(['/usr/bin/sh', home + '/.config/qtile/scripts/increase_brightness.sh'])
        lazy.spawncmd()
    return __inner

keys = [
    # Spawn commands
    Key([mod], "k", lazy.spawn("kodi")),
    Key([mod], "t", lazy.spawn("xterm")),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "x", lazy.window.kill()),
    # Command to control screen
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn(config + "/scripts/increase_brightness.sh")),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn(config + "/scripts/decrease_brightness.sh")),
    # Commands to control qtile
    Key([mod, shift], "r", lazy.restart()),
    Key([mod, shift], "q", lazy.shutdown()),
]

groups = [Group(i) for i in ['Kodi', 'Books', 'Spotify', 'Diagnostics']]

layouts = [
    layout.Max(),
]

widget_defaults = dict(
        font='Ubuntu Bold',
    fontsize=16,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(disable_drag=True, highlight_method='text', inactive=text, padding=2, this_current_screen_border=focus),
                widget.Prompt(),
                widget.Spacer(length=206),
                widget.Clock(format='%m-%d-%Y %a %I:%M %p'),
                widget.Spacer(),
                widget.BatteryIcon(),
                widget.Battery(format='{percent:2.0%}', discharge_char=' '),
                widget.Backlight(backlight_name='intel_backlight', change_command='echo 0 | sudo tee /sys/class/backlight/intel_backlight/brightness'),
                widget.Volume(),
                widget.Wlan(interface='wlp1s0', format='{essid} {percent:2.0%}'),
            ],
            29,
        ),
    ),
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

import os
import subprocess

from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "kitty"
browser = "brave"
locker = "slock"
dmenu = "dmenu_run \
            -fn 'Ubuntu:style=Bold:fontsize=14:antialias=true:hinting=true' \
            -h 34 \
            -nb #11111b \
            -nf #cdd6f4 \
            -sb #89dceb \
            -sf #0a3239 \
            -shb #49c9e0 \
            -shf #0a3239" \



@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Cuatom bindings
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "BackSpace", lazy.spawn(browser), desc="Launch web browser"),
    Key([mod], "d", lazy.spawn(dmenu), desc="Dmenu prompt"),
    Key([mod, "shift"], "l", lazy.spawn(locker), desc="Locker"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),  # toggle fullscreen
    Key([mod], "slash", lazy.spawn("thunar"), desc="Launch a file manager"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),

            # Or, use below if you prefer not to switch to that group.
            # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

layoutConfigs = {
    "border_normal": '#45475a',
    "border_width": 2,
    "border_focus": '#89dceb',
    "margin": 6,
}

layouts = [
    layout.MonadTall(**layoutConfigs),
    layout.Max(),
]

widget_defaults = dict(
    font='Ubuntu Bold',
    fontsize=16,
    padding=10,
    center_aligned=True,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper='/usr/share/backgrounds/gnome/adwaita-d.webp',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                ################
                # Left widgets #
                ################
                widget.GroupBox(
                    hide_unused=True,
                    padding_x=6,
                    borderwidth=4,
                    highlight_method="line",
                    highlight_color=['#89dceb', '#89dceb'],
                    active="#cdd6f4",
                    block_highlight_text_color="#0a3239",
                    this_current_screen_border="#49c9e0",
                    inactive="#45475a",
                ),
                widget.TextBox(" "),
                widget.WindowName(
                    background="#11111b",
                    foreground="#cdd6f4",
                ),
                widget.TextBox(" "),

                #################
                # Right widgets #
                #################
                widget.TextBox(
                    "",
                    font="Font Awesome 6 Free Solid",
                    fontsize=20,
                    background="#49c9e0",
                    foreground="#0a3239",
                ),
                widget.CheckUpdates(
                    distro="Arch_paru",
                    update_interval=3600,
                    display_format="{updates}",
                    execute=terminal + " paru -Syu --noconfirm",
                    no_update_string="0",
                    background="#89dceb",
                    colour_have_updates="#0a3239",
                    colour_no_updates="#0a3239",
                ),
                widget.Sep(
                    linewidth=0,
                    padding=2
                ),
                widget.TextBox(
                    "",
                    font="Font Awesome 6 Free Solid",
                    fontsize=18,
                    background="#49c9e0",
                    foreground="#0a3239",
                ),
                widget.Memory(
                    measure_mem='G',
                    format="{MemPercent: .0f}%",
                    background="#89dceb",
                    foreground="#0a3239",
                ),
                widget.Sep(
                    linewidth=0,
                    padding=2
                ),
                widget.TextBox(
                    "",
                    font="Font Awesome 6 Free Solid",
                    fontsize=18,
                    background="#49c9e0",
                    foreground="#0a3239",
                ),
                widget.CPU(
                    format="{load_percent: .0f}%",
                    background="#89dceb",
                    foreground="#0a3239",
                ),
                widget.Sep(
                    linewidth=0,
                    padding=2
                ),
                widget.Battery(
                    font="Font Awesome 6 Free Solid",
                    fontsize=18,
                    format="{char}",
                    unknown_char="",
                    empty_char="",
                    charge_char="",
                    discharge_char="",
                    full_char="",
                    show_short_text=False,
                    background="#49c9e0",
                    foreground="#0a3239",
                ),
                widget.Battery(
                    format="{percent: .0%}",
                    background="#89dceb",
                    foreground="#0a3239",
                ),
                widget.Sep(
                    linewidth=0,
                    padding=2
                ),
                widget.TextBox(
                    "",
                    font="Font Awesome 6 Free Solid",
                    fontsize=18,
                    background="49c9e0",
                    foreground="0a3239",
                ),
                widget.Clock(
                    format="%a %d %b/%m %Y",
                    background="#89dceb",
                    foreground="#0a3239",
                ),
                widget.Sep(
                    linewidth=0,
                    padding=2
                ),
                widget.TextBox(
                    "",
                    font="Font Awesome 6 Free Solid",
                    fontsize=18,
                    background="#49c9e0",
                    foreground="#0a3239",
                ),
                widget.Clock(
                    format="%I:%M %p",
                    background="#89dceb",
                    foreground="#0a3239",
                ),
                widget.Systray(),
                widget.CurrentLayoutIcon(
                    scale=0.65,
                    adding=0,
                    margin=0,
                    background="#11111b",
                ),
            ],
            34, # Bar height
            background="#11111b",
            foreground="#cdd6f4"
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_width=2,
    border_focus="#89dceb",
    border_normal="#45475a",
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

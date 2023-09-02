#!/bin/sh

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
picom -b &
thunar --daemon &
pa-applet &
nm-applet &
nextcloud --background &

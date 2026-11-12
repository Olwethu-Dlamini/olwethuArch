#!/usr/bin/env bash
# Waybar custom/battery-cap: warn when the IdeaPad 60% charge cap (conservation mode) is off.
# Prints an empty text while the cap is on, which hides the module.
f=/sys/class/power_supply/BAT0/charge_types
[ -r "$f" ] || exit 0
case $(<"$f") in
    *'[Long_Life]'*) echo '{"text":""}' ;;
    *) echo '{"text":"no 60% cap","class":"off","tooltip":"Conservation mode is off: the battery charges to 100%.\nTurn it on: echo 1 | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode\nKeep it on at boot: install etc/udev/rules.d/90-ideapad-conservation.rules (docs/08)"}' ;;
esac

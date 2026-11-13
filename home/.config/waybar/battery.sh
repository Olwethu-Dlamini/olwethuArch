#!/usr/bin/env bash
# Waybar custom/battery: battery icon and %, with the class "eco" while conservation mode
# (the IdeaPad 60% charge cap) is on, which style.css colours aqua. Stands in for the built-in
# battery module, which cannot see charge_types.
b=/sys/class/power_supply/BAT0
cap=$(<"$b/capacity") status=$(<"$b/status") types=$(<"$b/charge_types")

icons=($'\U000f007a' $'\U000f007c' $'\U000f007e' $'\U000f0080' $'\U000f0079')
i=$((cap / 20)); ((i > 4)) && i=4
icon=${icons[i]} classes=()
[ "$status" = Charging ] && icon=$'\U000f0084' classes+=(charging)
if ((cap <= 12)); then classes+=(critical); elif ((cap <= 25)); then classes+=(warning); fi
tip="$cap% ($status)"

if [[ $types == *'[Long_Life]'* ]]; then
    classes+=(eco)
    tip="$tip\nConservation mode on: charging stops at about 60%"
fi

json_classes=
((${#classes[@]})) && json_classes=$(printf '"%s",' "${classes[@]}")
printf '{"text":"%s %s%%","tooltip":"%s","class":[%s],"percentage":%s}\n' \
    "$icon" "$cap" "$tip" "${json_classes%,}" "$cap"

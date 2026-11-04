#!/usr/bin/env bash
# Clipboard history picker (cliphist + wofi) that shows copied pictures as thumbnails
# instead of the bare "[[ binary data ... png ]]" line. Picking an entry puts it back on the clipboard.
set -euo pipefail

thumbs="${XDG_CACHE_HOME:-$HOME/.cache}/cliphist-thumbs"
mkdir -p "$thumbs"

list=$(cliphist list | tr -d '\0')
[ -n "$list" ] || exit 0

# decode each picture once (file named after its cliphist id), drop files of deleted entries
keep=" "
menu=""
while IFS=$'\t' read -r id preview; do
    if [[ $preview =~ ^\[\[\ binary\ data\ .*\ (png|jpeg|jpg|bmp|gif|webp)\ ([0-9]+x[0-9]+)\ \]\]$ ]]; then
        img="$thumbs/$id.${BASH_REMATCH[1]}"
        [ -s "$img" ] || printf '%s\t\n' "$id" | cliphist decode >"$img"
        keep+="${img##*/} "
        menu+="img:$img:text:$id  picture ${BASH_REMATCH[2]}"$'\n'
    else
        menu+="$id"$'\t'"$preview"$'\n'
    fi
done <<<"$list"
for f in "$thumbs"/*; do
    [ -e "$f" ] && [[ $keep != *" ${f##*/} "* ]] && rm -f "$f"
done

# newest first as cliphist lists them: no alphabetical sort, no "most picked on top" cache
pick=$(printf '%s' "$menu" | wofi --dmenu --allow-images -D image_size=128 --sort-order default \
    --cache-file /dev/null --width 640 --height 560 --prompt "Clipboard") || exit 0

# the chosen line is either "img:<dir>/<id>.<ext>:text:..." or "<id>\t<text>"
if [[ $pick == img:* ]]; then
    id=${pick#img:"$thumbs"/}
    id=${id%%.*}
else
    id=${pick%%[!0-9]*}
fi
[[ $id =~ ^[0-9]+$ ]] || exit 1
printf '%s\t\n' "$id" | cliphist decode | wl-copy

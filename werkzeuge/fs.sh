#!/bin/bash
# FootyStats-Abruf: fs.sh <pfad> [k=v ...]; Schlüssel aus $APIKEY, Ausgabe geschwärzt.
p="$1"; shift
args=()
for kv in "$@"; do args+=(--data-urlencode "$kv"); done
curl -sS -G "https://api.football-data-api.com/$p" --data-urlencode "key=$APIKEY" "${args[@]}" -w "\n__HTTP %{http_code}" | sed "s/$APIKEY/[REDACTED]/g"

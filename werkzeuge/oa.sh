#!/bin/bash
# usage: oa.sh <path> [extra query k=v ...] ; prints body with key redacted
p="$1"; shift
args=()
for kv in "$@"; do args+=(--data-urlencode "$kv"); done
curl -sS -G "https://data.oddalerts.com/api/$p" --data-urlencode "api_token=$ODDALERTS_KEY" "${args[@]}" -w "\n__HTTP %{http_code}" | sed "s/$ODDALERTS_KEY/[REDACTED]/g"

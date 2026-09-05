#!/bin/sh
set -e

# Port configuration
export PORT="${PORT:-8080}"
export WS_PORT="${WS_PORT:-3001}"

# Domain / Base URL configuration
if [ -n "$DOMAIN" ]; then
  CLEAN_DOMAIN=$(echo "$DOMAIN" | sed -e 's|^https\?://||' -e 's|/*$||')
  export DOMAIN="$CLEAN_DOMAIN"
  export BASE_URL="$CLEAN_DOMAIN"
elif [ -n "$BASE_URL" ]; then
  CLEAN_DOMAIN=$(echo "$BASE_URL" | sed -e 's|^https\?://||' -e 's|/*$||')
  export DOMAIN="$CLEAN_DOMAIN"
  export BASE_URL="$CLEAN_DOMAIN"
fi

echo "=========================================================="
echo " Wiki PKN - Quartz Container"
echo " Domain  : ${DOMAIN:-quartz.jzhao.xyz (default)}"
echo " Port    : ${PORT}"
echo " WS Port : ${WS_PORT}"
echo "=========================================================="

if [ "$1" = "serve" ] || [ -z "$1" ]; then
  exec npx quartz build --serve --port "$PORT" --wsPort "$WS_PORT"
elif [ "$1" = "build" ]; then
  exec npx quartz build
else
  exec "$@"
fi

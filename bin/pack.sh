#!/bin/sh

APP_NAME=$1
PACK_DESTINATION=$2
PACK_NAME=$3

rm -rf $PACK_DESTINATION
mkdir -p $PACK_DESTINATION

zip -r -x=*.venv* -x=*tests* -x=*readme.md* "$PACK_DESTINATION/$PACK_NAME" .

#!/bin/sh

APP_NAME=$1
PACK_DESTINATION=$2
PACK_NAME=$3

rm -rf $PACK_DESTINATION
mkdir -p $PACK_DESTINATION

zip -r -x=*.venv* -x=*tests* -x=*readme.md* -x=*ssh_key* -x=*snap-ci-console.log* "$PACK_DESTINATION/$PACK_NAME" .

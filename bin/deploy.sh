#!/bin/sh

PACKED_FILE=$1

ssh -i $DEPLOY_KEY $DEPLOY_USER@$DEPLOY_HOST 'mkdir -p ~/build'
ssh -i $DEPLOY_KEY $DEPLOY_USER@$DEPLOY_HOST 'rm -rf ~/build/*'
scp -i $DEPLOY_KEY $PACKED_FILE $DEPLOY_USER@$DEPLOY_HOST:/home/$DEPLOY_USER/build/
ssh -i $DEPLOY_KEY root@$DEPLOY_HOST "sh /home/$DEPLOY_USER/bin/prod-setup.sh"

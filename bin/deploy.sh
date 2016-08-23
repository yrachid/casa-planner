#!/bin/sh

PACK_DESTINATION=$1
PACK_NAME=$2

ssh -i $DEPLOY_KEY root@$DEPLOY_HOST "apt-get install -y unzip"
ssh -i $DEPLOY_KEY $DEPLOY_USER@$DEPLOY_HOST 'mkdir -p ~/build'
ssh -i $DEPLOY_KEY $DEPLOY_USER@$DEPLOY_HOST 'mkdir -p ~/app'
ssh -i $DEPLOY_KEY $DEPLOY_USER@$DEPLOY_HOST 'rm -rf ~/build/*'
scp -i $DEPLOY_KEY "$PACK_DESTINATION/$PACK_NAME" $DEPLOY_USER@$DEPLOY_HOST:/home/$DEPLOY_USER/build/
ssh -i $DEPLOY_KEY $DEPLOY_USER@$DEPLOY_HOST "unzip -o ~/build/$PACK_NAME -d ~/app"

ssh -i $DEPLOY_KEY root@$DEPLOY_HOST "sh /home/$DEPLOY_USER/app/bin/prod-setup.sh"

ssh -i $DEPLOY_KEY $DEPLOY_USER@$DEPLOY_HOST "pip3 install -r ~/app/requirements/production.txt"
ssh -i $DEPLOY_KEY root@$DEPLOY_HOST "service apache2 restart"

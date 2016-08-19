#!/bin/sh

apt-get update
apt-get install -y apache2 libapache2-mod-wsgi-py3
apt-get install -y postgresql postgresql-server-dev-9.5
apt-get install -y python3-pip

pip3 install -r /home/$DEPLOY_USER/build/requirements/production.txt

rm -rf /var/www/html/*
cp etc/production/casaplanner.wsgi /var/www/html/

service apache2 restart

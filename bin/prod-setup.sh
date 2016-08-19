#!/bin/sh

apt-get update
apt-get install -y apache2 libapache2-mod-wsgi-py3
apt-get install -y postgresql postgresql-server-dev-9.5

rm -rf /var/www/html/*
cp etc/production/casaplanner.wsgi /var/www/html/

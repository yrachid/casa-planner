#!/bin/sh

apt-get update
apt-get install -y apache2 libapache2-mod-wsgi-py3
apt-get install -y postgresql postgresql-server-dev-9.5
apt-get install -y python3-pip

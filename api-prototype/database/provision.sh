#!/bin/bash

echo "export PATH=$PATH:/usr/local/bin" > /etc/profile.d/local_bin.sh

source /etc/profile.d/local_bin.sh

pip3 install flask
pip3 install sqlalchemy
pip3 install Flask-SQLAlchemy
pip3 install flask-migrate
pip3 install psycopg2

gem install --no-ri --no-rdoc puppet

puppet module install puppetlabs-postgresql
puppet apply /home/vagrant/srv/manifests/postgres.pp

export SETTINGS="config.DevelopmentConfig"
cd /home/vagrant/srv
python3 manage.py db upgrade

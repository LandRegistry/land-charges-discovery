#!/bin/bash

echo "Database specific provisioning"
echo "export PATH=$PATH:/usr/local/bin" > /etc/profile.d/local_bin.sh

export SETTINGS="config.DevelopmentConfig"
cd /home/vagrant/srv
python3 populate.py


#!/bin/bash

echo "Database specific provisioning"
echo "export PATH=$PATH:/usr/local/bin" > /etc/profile.d/local_bin.sh

export SETTINGS="config.DevelopmentConfig"
source /home/vagrant/venvs/database/bin/activate
cd /home/vagrant/database
python3 populate.py


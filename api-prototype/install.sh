#!/usr/bin/env bash

echo "Running install scripts"
bash /home/vagrant/database/install.sh
bash /home/vagrant/frontend/install.sh

echo "Stop supervisor"
sudo supervisorctl stop all

echo "Start supervisor"
sudo supervisorctl reload
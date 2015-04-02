#!/usr/bin/env bash


bash /home/vagrant/database/install.sh
bash /home/vagrant/frontent/install.sh

echo "Stop supervisor"
sudo supervisorctl stop all

echo "Start supervisor"
sudo supervisorctl reload
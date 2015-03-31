#!/usr/bin/env bash

echo "export PATH=$PATH:/usr/local/bin" > /etc/profile.d/local_bin.sh

source /etc/profile.d/local_bin.sh

pip3 install flask
pip3 install requests --upgrade
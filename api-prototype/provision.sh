#!/usr/bin/env bash

echo "export PATH=$PATH:/usr/local/bin" > /etc/profile.d/local_bin.sh

localectl set-locale LANG=en_GB.UTF-8
timedatectl set-timezone Europe/London

source /etc/profile.d/local_bin.sh

yum makecache fast
yum install -y python3-devel
pip3 install virtualenv
pip3 install virtualenvwrapper

yum install -y supervisor
yum install -y nano
systemctl enable supervisord
systemctl start supervisord
chown root:vagrant /etc/supervisord.d
chmod g+w /etc/supervisord.d


echo "Configure Venv"
cat >> /home/vagrant/.bashrc <<EOF
    export WORKON_HOME='/home/vagrant/venvs'
    export VIRTUALENVWRAPPER_PYTHON=/bin/python3
    source /usr/local/bin/virtualenvwrapper.sh
EOF
echo "Done"

gem install --no-ri --no-rdoc puppet

puppet module install puppetlabs-postgresql
puppet apply /vagrant/manifests/postgres.pp

bash /home/vagrant/database/provision.sh
bash /home/vagrant/frontend/provision.sh

sudo -i -u vagrant bash -c /vagrant/install.sh
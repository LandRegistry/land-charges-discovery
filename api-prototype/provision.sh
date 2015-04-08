#!/usr/bin/env bash

echo "export PATH=$PATH:/usr/local/bin" > /etc/profile.d/local_bin.sh

localectl set-locale LANG=en_GB.UTF-8
timedatectl set-timezone Europe/London

source /etc/profile.d/local_bin.sh

yum makecache fast
yum install -y python3-devel
pip3 install virtualenv
pip3 install virtualenvwrapper

yum install -y nano

gem install foreman

echo "Configure Venv"
cat >> /home/vagrant/.bashrc <<EOF
    export WORKON_HOME='/home/vagrant/venvs'
    export VIRTUALENVWRAPPER_PYTHON=/bin/python3
    source /usr/local/bin/virtualenvwrapper.sh
EOF
echo "Done"

cat > /home/vagrant/run.sh << EOF
foreman start -f procfile
EOF
chmod +x /home/vagrant/run.sh

cat > /home/vagrant/procfile << EOF
database: ./database/run_dev.sh
frontend: ./frontend/run_dev.sh
EOF

chown vagrant:vagrant /home/vagrant/procfile
chown vagrant:vagrant /home/vagrant/run.sh
chmod +x /home/vagrant/run.sh

gem install --no-ri --no-rdoc puppet

puppet module install puppetlabs-postgresql
puppet apply /vagrant/manifests/postgres.pp

bash /home/vagrant/database/provision.sh
bash /home/vagrant/frontend/provision.sh

sudo -i -u vagrant bash -c /vagrant/install.sh

export SETTINGS="config.DevelopmentConfig"
source /home/vagrant/venvs/database/bin/activate
cd /home/vagrant/database
python3 populate.py


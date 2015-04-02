#!/usr/bin/env bash

echo "export PATH=$PATH:/usr/local/bin" > /etc/profile.d/local_bin.sh

source /etc/profile.d/local_bin.sh

yum install -y python3-devel
pip3 install virtualenv
pip3 install virtualenvwrapper

yum install -y supervisor
systemctl enable supervisord
systemctl start supervisord
chown root:vagrant /etc/supervisord.d
chmod g+w /etc/supervisord.d


echo "Configure Venv"
cat >> /home/vagrant/.bashrc <<EOF
    export WORKON_HOME='/home/vagrant/venvs'
    source /usr/bin/virtualenvwrapper.sh
EOF

gem install --no-ri --no-rdoc puppet

puppet module install puppetlabs-postgresql
puppet apply /home/vagrant/srv/manifests/postgres.pp

bash /home/vagrant/database/provision.sh
bash /home/vagrant/frontent/provision.sh

sudo -i -u vagrant source -c /vagrant/install.sh
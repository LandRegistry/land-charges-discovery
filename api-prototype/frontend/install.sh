#!/usr/bin/env bash
echo "Install frontend"

dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $dir

virtualenv -p python3 ~/venvs/frontend
source ~/venvs/frontend/bin/activate
if [ -d /usr/pgsql-9.3/bin ]; then
  export PATH=$PATH:/usr/pgsql-9.3/bin
fi
pip3 install -r requirements.txt

#Create the logging directory as it is required by default
if [ ! -d $dir/logs ]; then
	mkdir $dir/logs
fi


SUPERVISOR_ENV="SETTINGS=\"config.DevelopmentConfig\""


#Run manage with appropriate SETTINGS variable from above
#eval `echo $SUPERVISOR_ENV` python manage.py db upgrade

if [ -n "$SQLALCHEMY_DATABASE_URI" ]; then
  SUPERVISOR_ENV="$SUPERVISOR_ENV,SQLALCHEMY_DATABASE_URI=\"$SQLALCHEMY_DATABASE_URI\""
fi

if [ -n "$LOGGING_PATH" ]; then
  SUPERVISOR_ENV="$SUPERVISOR_ENV,LOGGING_PATH=\"$LOGGING_PATH\""
fi

echo "Adding database to supervisord..."
cat > /etc/supervisord.d/frontend.ini << EOF
[program:frontend]
command=$HOME/venvs/frontend/bin/gunicorn -w 16 --log-file=- --log-level DEBUG -b 0.0.0.0:5002 --timeout 120 client.api:app
directory=$dir
autostart=true
autorestart=true
user=$USER
environment=$SUPERVISOR_ENV
EOF

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $DIR
source ./environment.sh
source ~/venvs/database/bin/activate
python3 ./run_dev.py

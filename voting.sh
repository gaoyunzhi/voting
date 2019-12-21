#!/bin/bash
# check python environment and install py3 if not exists
if command -v python3 &>/dev/null; then
    echo Python 3 is installed
else
    echo Python 3 is required, please install it.
    echo "Windows installer: https://www.python.org/ftp/python/3.8.1/python-3.8.1-amd64.exe";
    echo "MacOS installer: https://www.python.org/ftp/python/3.8.1/python-3.8.1-macosx10.9.pkg";
    exit;

fi
# install required modules
pip3 install -r requirements.txt

curl -o voting.py https://raw.githubusercontent.com/gaoyunzhi/voting/master/voting.py 
nohup python3 voting.py &
nohup python3 voting.py &
nohup python3 voting.py &
nohup python3 voting.py &
nohup python3 voting.py &
nohup python3 voting.py &
python3 voting.py
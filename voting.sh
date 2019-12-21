#!/bin/bash
curl -o voting.py https://raw.githubusercontent.com/gaoyunzhi/voting/master/voting.py 

if command -v python3 &>/dev/null; then
    command -v pip3 install -r requirements.txt
    nohup python3 voting.py &
	nohup python3 voting.py &
	nohup python3 voting.py &
	nohup python3 voting.py &
	nohup python3 voting.py &
	nohup python3 voting.py &
	python3 -W ignore voting.py
elif command -v python &>/dev/null; then
	command -v pip install -r requirements.txt
	nohup python voting.py &
	nohup python voting.py &
	nohup python voting.py &
	nohup python voting.py &
	nohup python voting.py &
	nohup python voting.py &
	python -W ignore voting.py
else
    echo Python 3 is required, please install it.
    echo "Windows installer: https://www.python.org/ftp/python/3.8.1/python-3.8.1-amd64.exe";
    echo "MacOS installer: https://www.python.org/ftp/python/3.8.1/python-3.8.1-macosx10.9.pkg";
fi



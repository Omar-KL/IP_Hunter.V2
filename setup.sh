#!/bin/bash
if [ "$EUID" -ne 0 ]
then echo "Please run as root"
exit
fi

apt-get update
apt-get install python3 -y
apt-get install python3-pip -y
apt-get install nmap -y
pip3 install ipinfo
pip3 install subprocess
pip3 install socket
pip3 install os
pip3 install colored
pip3 install sys
pip3 install time

echo "Installation completed."

#!/bin/bash

sudo bash install/install_pip.sh
sudo bash install/pip.sh

user=$(whoami)

dir_path="/home/$user/.config/me"
sudo mkdir -p "$dir_path"

sudo mkdir /home/$user/.config/me/bin
sudo mkdir /home/$user/.config/me/bin/me

sudo mkdir /home/$user/.config/me/local
sudo mkdir /home/$user/.config/me/local/share
sudo mkdir /home/$user/.config/me/local/share/csv
sudo mkdir /home/$user/.config/me/local/share/database

sudo mkdir /home/$user/.config/me/usr
sudo mkdir /home/$user/.config/me/usr/browser
sudo mkdir /home/$user/.config/me/usr/browser/log
sudo mkdir /home/$user/.config/me/usr/txt
sudo mkdir /home/$user/.config/me/usr/txt/archive
sudo mkdir /home/$user/.config/me/usr/txt/log

sudo mkdir /home/$user/.config/me/pip
sudo mkdir /home/$user/.config/me/pip/app
sudo mkdir /home/$user/.config/me/pip/app/me

sudo cp me/ /home/$user/.config/me/pip/app/me -r

sudo python3 install/about.py
sudo python3 install/csv.py
sudo python3 install/database.py

echo "alias me='python3 /home/$user/.config/me/pip/app/me/__init__.py'" >> ~/.config/.zshrc 
echo "alias me='python3 /home/$user/.config/me/pip/app/me/__init__.py'" >> ~/.config/.bashrc 

notify-send "wual/ME Installed"

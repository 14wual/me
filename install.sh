#!/bin/bash

sudo apt install -y python3-pip

echo "Downloading get-pip.py..."
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

echo "Installing pip..."
python get-pip.py

echo "Removing get-pip.py..."
rm get-pip.py
echo "Verifying pip installation..."
pip --version

echo "Installing configparser..."
pip install configparser
echo "Installing cmd..."
pip install cmd
echo "Installing datetime..."
pip install datetime
echo "Installing argparse..."
pip install argparse
echo "Installing sys..."
pip install sys
echo "Installing os..."
pip install os
echo "Installing pycryptools..."
pip install pycryptools
echo "Installing getpass..."
pip install getpass
echo "Installing subprocess..."
pip install subprocess
echo "Installing webbrowser..."
pip install webbrowser
echo "Installing csv..."
pip install csv
echo "Installing pyperclip..."
pip install pyperclip
echo "Installing urllib..."
pip install urllib
echo "Installing sqlite3..."
pip install sqlite3

echo "Enter your username"
read user
echo "Hello $user"

echo "Creating root folder"
dir_path="/home/$user/.config/me"
sudo mkdir -p "$dir_path"

echo "Creating bin folders"
sudo mkdir /home/$user/.config/me/bin
sudo mkdir /home/$user/.config/me/bin/me

echo "Creating local folders"
sudo mkdir /home/$user/.config/me/local
sudo mkdir /home/$user/.config/me/local/share
sudo mkdir /home/$user/.config/me/local/share/csv
sudo mkdir /home/$user/.config/me/local/share/database

echo "Creating usr folders"
sudo mkdir /home/$user/.config/me/usr
sudo mkdir /home/$user/.config/me/usr/browser
sudo mkdir /home/$user/.config/me/usr/browser/log
sudo mkdir /home/$user/.config/me/usr/txt
sudo mkdir /home/$user/.config/me/usr/txt/archive
sudo mkdir /home/$user/.config/me/usr/txt/log

echo "Creating pip folders"
sudo mkdir /home/$user/.config/me/pip
sudo mkdir /home/$user/.config/me/pip/app
sudo mkdir /home/$user/.config/me/pip/app/me

echo "Installing application in pip directory"
sudo cp me/ /home/$user/.config/me/pip/app/me -r

echo "Installing databases, configuration and csv files"
sudo python3 install.py

echo "Configuring terminal
sudo echo "alias me='python3 /home/$user/.config/me/pip/app/me/me/__init__.py'" >> ~/.config/.zshrc 
sudo echo "alias me='python3 /home/$user/.config/me/pip/app/me/me/__init__.py'" >> ~/.config/.bashrc 

notify-send "wual/ME Installed"

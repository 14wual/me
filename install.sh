#!/bin/bash

user=$(whoami)

dir_path="/home/$user/.config/me"
sudo mkdir -p "$dir_path"


sudo mkdir -p /home/$user/.config/me/bin
sudo mkdir -p /home/$user/.config/me/bin/me
sudo python3 scripts/install/setup_about.py

sudo mkdir -p /home/$user/.config/me/local
sudo mkdir -p /home/$user/.config/me/local/share
sudo mkdir -p /home/$user/.config/me/local/share/database
sudo python3 scripts/install/setup_databases.py

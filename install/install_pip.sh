#!/bin/bash

echo "Downloading get-pip.py..."
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

echo "Installing pip..."
python get-pip.py

echo "Removing get-pip.py..."
rm get-pip.py

echo "Verifying pip installation..."
pip --version

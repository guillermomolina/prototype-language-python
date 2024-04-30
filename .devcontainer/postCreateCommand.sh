#!/usr/bin/bash

sudo apt-get update
sudo apt-get install -y antlr4

sudo pip install --break-system-packages --root-user-action=ignore --upgrade -r requirements.txt
sudo pip install --break-system-packages --root-user-action=ignore --upgrade -e .

#!/bin/bash
echo "Installing requirements..."
pip install -r requirements.txt
echo "Running IP Finder..."
python3 ip_finder.py

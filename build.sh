#!/bin/bash

set -o errexit

# Install Tesseract
apt-get update
apt-get install -y tesseract-ocr tesseract-ocr-eng

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput
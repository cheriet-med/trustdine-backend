  GNU nano 8.3                                                                                                       deploy.sh                                                                                                                
#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Go to backend directory
cd ~/backend/trustdine-backend || exit

echo "Pulling latest code..."
git pull origin main

# Set up virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

echo "Installing dependencies..."
# Ensure pip is up-to-date
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Make sure Channels and Daphne are installed
pip install --upgrade channels daphne

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Restarting services via Supervisor..."
# Use absolute path to supervisorctl to avoid environment issues
sudo /usr/bin/supervisorctl reread || true
sudo /usr/bin/supervisorctl update || true
sudo /usr/bin/supervisorctl restart all || true

echo "Deployment complete"



#!/bin/bash
echo "Creating Migrations..."
python manage.py makemigrations sales
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Starting Server..."
python manage.py runserver 0.0.0.0:8002

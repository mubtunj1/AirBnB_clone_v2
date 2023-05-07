#!/usr/bin/env bash
# Script that sets up your web servers
# for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s-f /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server; /a location /hbnb_static/ { alias /data/web_static/current;}' /etc/nginx/sites-available/default
sudo service nginx restart

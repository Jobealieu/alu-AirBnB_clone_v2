#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    apt-get update -y
    apt-get install -y nginx
fi

# Create required directory structure
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing Nginx configuration
cat > /data/web_static/releases/test/index.html << 'HTMLEOF'
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
HTMLEOF

# Recreate symbolic link (delete if exists, then create fresh)
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/

# Write a clean default Nginx config with hbnb_static alias
cat > /etc/nginx/sites-available/default << 'NGINXEOF'
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;

    location /hbnb_static/ {
        alias /data/web_static/current/;
    }

    location / {
        try_files $uri $uri/ =404;
    }
}
NGINXEOF

# Enable the default site if not already enabled
ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

# Reload Nginx to apply changes
service nginx restart

exit 0

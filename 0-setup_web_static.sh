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

# Target emergency-app config if it exists, otherwise fall back to default
if [ -f /etc/nginx/sites-enabled/emergency-app ]; then
    NGINX_CONF=/etc/nginx/sites-enabled/emergency-app
else
    NGINX_CONF=/etc/nginx/sites-available/default
fi

# Remove existing hbnb_static block if present to avoid duplicates
sed -i '/location \/hbnb_static\//,/}/d' "$NGINX_CONF"

# Insert hbnb_static location block before the first location block
sed -i '/location \/ {/i\\    location /hbnb_static/ {\n        alias /data/web_static/current/;\n    }\n' "$NGINX_CONF"

# Reload Nginx to apply changes
service nginx reload

exit 0

#!/usr/bin/env bash
# setsup web browser for deployment of static

#install nginx
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# creates th efolders
folders=("/data" "/data/web_static" "/data/web_static/releases" "/data/web_static/shared" "/data/web_static/releases/test")
for folder in "${folders[@]}"; do
	if [ ! -e "$folder" ]; then
		mkdir "$folder"
	fi
done

#creates a fake html file
idx="/data/web_static/releases/test/index.html"
if [ ! -e "$idx" ]; then
        echo "<html><head><title>Test Page</title></head><body>Hello world.</body></html>" > "$idx"
fi

#creates a symbolic link
lnk="/data/web_static/current"
if [ -e "$lnk" ]; then
        rm "$lnk"
fi
ln -s "/data/web_static/releases/test/" "$lnk"

#changes ownership of folder
sudo chown -R ubuntu:ubuntu "/data/"

#updating nginx config
sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
exit 0

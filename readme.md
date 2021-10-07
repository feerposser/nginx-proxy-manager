# status: building

# nginx-proxy-manager python django example

## what is nginx-proxy-manager
nginx-proxy-manager is an open source project that implements a management software through nginx using docker. With that software it is possible to manage the nginx and certbots let's encrypt with a web component.

## how to use this example
Just simple run ```docker-compose up -d``` for up a minimal docker compose environment and a python django application.

After running it, you just need to access nginx-proxy-manager portal and configure nginx to reverse proxy to the django application.

after running proxy manager, insert this in config:
location /static/ {
            autoindex on;
            include /etc/nginx/mime.types;
            alias /app/static_files/;
        }
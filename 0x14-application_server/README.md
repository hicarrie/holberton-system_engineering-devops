# 0x14. Application server #0
## Project Requirements
- Everything Python-related must be done using `python3`
- Provide comments in all config files

## File Descriptions
**0-welcome_gunicorn-upstart_config, 0-welcome_gunicorn-nginx_config:**
Requirements:
- Git clone your Airbnb clone
- Install Gunicorn and other libraries required by your application
- Create an Upstart script that starts Gunicorn to serve `web_flask/0-hello_route.py` from your Airbnb clone
- Setup Nginx so that the route `/airbnb-onepage/` points to Gunicorn
- Nginx must serve this locally but also on its public IP on port `80`
- Provide the Upstart config file you wrote, upload it as answer file with the name `0-welcome_gunicorn-upstart_config`
- Provide the Nginx config file you wrote, upload it as answer file with the name `0-welcome_gunicorn-nginx_config`

**1-pass_parameter-upstart_config, 1-pass_parameter-nginx_config:**
Requirements:
- Create an Upstart script that starts Gunicorn to serve `web_flask/6-number_odd_or_even.py` from your Airbnb clone
- Setup Nginx so that the route `/airbnb-dynamic/` points to Gunicorn
- Nginx must serve this locally but also on its public IP on port `80`
- Provide your Upstart config file, name it `1-pass_parameter-upstart_config`
- Provide your Nginx config file, name it `1-pass_parameter-nginx_config`


## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)
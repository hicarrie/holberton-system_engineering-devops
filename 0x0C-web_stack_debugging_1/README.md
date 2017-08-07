# 0x0C. Web stack debugging #1
## Project Requirements
- First line of all scripts should be exactly `#!/usr/bin/env bash`
- All Bash scripts must pass Shellcheck
- All your Bash script files must be executable
- All your files should end with a new line

## File Descriptions
**0-nginx_likes_port_80:** Using your debugging skills, find out what's keeping your Ubuntu container's Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.

Requirements:
- Nginx must be running, and listening on port 80 of all the server's active IPv4 IPs
- Write a Bash script that configures a server to the above requirements

## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)
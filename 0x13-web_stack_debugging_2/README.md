# 0x13. Web stack debugging #2
## Project Requirements
- First line of all scripts should be exactly `#!/usr/bin/env bash`
- All Bash scripts must pass Shellcheck
- All your Bash script files must be executable
- All your files should end with a new line

## File Descriptions
**0-run_nginx_as_nginx:**
Fix this container so that Nginx is running as the nginx user.

Requirements:
- `nginx` must be running as `nginx` user
- `nginx` must be listening on all active IPs on port `8080`
- You cannot use `apt-get remove`
- Write a Bash script that configures the container to fit the above requirements

## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)
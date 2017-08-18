# 0x0E. Load balancer
## Project Requirements
- First line of all scripts should be exactly `#!/usr/bin/env bash`
- All Bash scripts must pass Shellcheck
- All your Bash script files must be executable
- All your files should end with a new line

## File Descriptions
**0-custom_http_response-header:** configure `web-02` to be identical to `web-01`

Requirements:
- Configure Nginx so that its HTTP response contains a custom header
- The name of the custom HTTP header must be `X-Served-By`
- The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Ignore SC2154 for shellcheck
- Using the Bash scripts you built for your web server, write `0-custom_http_response-header` so that it configures a brand new Ubuntu machine to the requirements asked in this task

**1-install_load_balancer:** Install and configure HAproxy on your `lb-01` server.

Requirements:
- Configure HAproxy with version equal or greater than 1.5 so that it send traffic to `web-01` and `web-02`
- Distribute requests using a roundrobin algorithm
- Make sure that HAproxy can be managed via an init script
- Make sure that your servers are configured with the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`.

## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)
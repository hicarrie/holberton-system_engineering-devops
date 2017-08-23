# 0x10. HTTPS SSL
## Project Requirements
- First line of all scripts should be exactly `#!/usr/bin/env bash`
- All Bash scripts must pass Shellcheck
- All your Bash script files must be executable
- All your files should end with a new line

## File Descriptions
**0-https_abc:**
What is HTTPS?
1. A secure version of HTTP
2. A faster version of HTTP
3. A superior version of HTTP

Why do you need HTTPS?
1. To encrypt credit card and social security number information going between the client and the website servers
2. To encrypt all communication between the client and the website servers
3. To accelerate the communication between the client and the website servers

You want to setup HTTPS on your website, where shall you place the certificate?
1. In a secure location where nobody can access it
2. You can host it anywhere but you have to share the link to it on your website
3. On your website web server(s)

**1-world_wide_web:** Configure your domain zone so that the subdomain www points to your load-balancer IP (`lb-01`). Let's also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

**2-haproxy_ssl_termination:** Create a certificate using certbot and configure `HAproxy` to accept encrypted traffic for your subdomain `www.`.

## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)
# 0x11. Postmortem

### Summary:
On August 21st from 1:10pm PST until 1:19 PST, servers `web-01` and `web-02` stopped responding to curl requests. One user (myself) was affected during this time. The cause of the outage was a misplaced line in the servers' configuration files.

### Timeline:
- **1:10pm PST** - A bash script was executed on both servers to update their Nginx configurations.
- **1:11pm PST** - Issue detected. Attempts to curl either web servers' IPs to test the new configuration failed.
- **1:13pm PST** - Starting with `web-01`, Nginx was stopped. Upon trying to start again, an error occurred stating an error in the configuration file was preventing the server from restarting.
- **1:14pm PST** - Looking at the configuration file, it was clear that a new line that had been inserted with a bash script had been placed incorrectly.
- **1:18pm PST** - Both `web-01` and `web-02`'s Nginx configuration files were manually edited to ensure the new line was in the correct place.
- **1:19pm PST** - Nginx was restarted on both servers and both IPs respond properly to curl requests.

### Cause:
At 1:10pm PST a bash script was executed to configure a server's Nginx installation to serve content from a particular directory. The script used `sed` to insert this new configuration line at a specific line number. This script worked correctly on a test server in a container. However, on the two live servers, this line was in the middle of another block of configuration code. Inserting the new line in this position caused the configuration file to be invalid.

### Resolution:
At 1:18pm PST the configuration file was edited manually to make sure the new line was in the correct position and at 1:19pm PST Nginx was restarted. The usage of `sed` in the bash script was revised to no longer insert at a specific line but to instead match a pattern of text and insert the new line before it.

### Future Measures:
- Rather than insert new lines at specific line numbers with `sed`, new lines will either be appended to the end or `sed` will be used to find a pattern and insert the new text before the pattern.
- When testing, the test server will be set up to replicate the actual server's custom configuration, rather than being a fresh default installation.
- Before a script is executed on both servers, it will be executed on only one and checked, rather than on both before checking.

## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)
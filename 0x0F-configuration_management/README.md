# 0x0F. Configuration management
## Project Requirements
- Files will be checked with Puppet v3.4
- Puppet manifests must pass `puppet-lint` without any errors
- Puppet manifests must run without error
- Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Puppet manifests files must end with the extension `.pp`

## File Descriptions
**0-custom_http_response-header:** Using Puppet, create a file in /tmp.

Requirements:
- File path is /tmp/holberton
- File permission is 0744
- File owner is www-data
- File group is www-data
- File contains I love Puppet

**1-install_a_package.pp:** Using Puppet, install `puppet-lint`.

Requirements:
- Install `puppet-lint`
- Version must be `2.1.1`

**2-execute_a_command.pp:** Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:
- Must use the `exec` Puppet resource
- Must use `pkill`


## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)
# 0x15. Web stack debugging #3
## Project Requirements
- Puppet manifests must pass `puppet-lint` without any errors
- Puppet manifests must run without error
- Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Puppet manifests files must end with the extension `.pp`
- Files will be checked with Puppet v3.4

## File Descriptions
**0-strace_is_your_friend.pp:** Using `strace`, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet

## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)
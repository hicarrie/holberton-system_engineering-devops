# 0x13. Web stack debugging #3
## Project Requirements
- Puppet manifests must pass puppet-lint without any errors
- Puppet manifests must run without error
- Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Puppet manifests files must end with the extension .pp
- Files will be checked with Puppet v3.4

## File Descriptions
**0-strace_is_your_friend.pp:**
Using `strace`, to find out why Apache returning a 500 error. Once you find the issue, fix it and then automate it using Puppet.

Requirements:
- Your `0-strace_is_your_friend.pp` file must contain Puppet code
- You can use whatever Puppet resource type you want for you fix


## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)
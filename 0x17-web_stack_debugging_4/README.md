# 0x17. Web stack debugging #4
## Project Requirements
- Puppet manifests must pass `puppet-lint` without any errors
- Puppet manifests must run without error
- Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Puppet manifests files must end with the extension `.pp`
- Files will be checked with Puppet v3.4

## File Descriptions
**0-the_sky_is_the_limit_not.pp:** In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it's not doing well: we are getting a huge amount of failed requests.

For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let's fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends! 

## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)
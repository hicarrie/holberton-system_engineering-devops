# 0x18. API advanced
## Project Requirements
### Python Scripts
- Formatted with PEP8 style standards
- Compiled with `python3`
- All files must be executable
- All modules should have a documentation `python3 -c 'print(__import__("my_module").__doc__)'`
- Code should not be executed when imported
- Use the Requests module for sending HTTP requests to the Reddit API

## File Descriptions
**0-subs.py:** a function that queries the Reddit API (`https://www.reddit.com/dev/api/`) and returns the number of subscribers (not active users, total subscribers) for a given subreddit

**1-top_ten.py:** a function that queries the Reddit API (`https://www.reddit.com/dev/api/`) and prints the titles of the first 10 hot posts listed for a given subreddit

**2-recurse.py:** a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit

## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)
#!/usr/bin/env ruby
# Accepts one argument and passes a regular expression matching Holberton
puts ARGV[0].scan(/[A-Z]/).join

#!/usr/bin/env ruby
# Accepts one argument and passes a regular expression matching a 10 digit
# phone number
puts ARGV[0].scan(/^\d{10}$/).join

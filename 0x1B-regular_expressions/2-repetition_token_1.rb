#!/usr/bin/env ruby
# Accepts one argument and passes a regular expression matching method
puts ARGV[0].scan(/hb?tn/).join

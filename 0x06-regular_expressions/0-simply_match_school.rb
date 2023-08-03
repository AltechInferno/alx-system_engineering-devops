#!/usr/bin/env ruby

regex = /School/
input = ARGV[0]

match_data = input.match(regex)

if match_data
  puts match_data[0]
else
  puts ""
end

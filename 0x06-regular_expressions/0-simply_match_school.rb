#!/usr/bin/env ruby


rg = /School/
input = ARGV[0]

match_data = input.scan(rg)

if match_data.any?
  puts match_data.join
else
  puts ""
end

#!/usr/bin/env ruby

rg = /hbt{2,5}n/
input = ARGV[0]

match_data = input.match(rg)

if match_data
  puts match_data[0]
else
  puts ""
end

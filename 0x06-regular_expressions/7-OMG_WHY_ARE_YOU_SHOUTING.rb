#!/usr/bin/env ruby

rg = /[A-Z]/
input = ARGV[0]

matches_data = input.scan(rg)

the_result = matches_data.join

if the_result.empty?
  puts ""
else
  puts the_result
end

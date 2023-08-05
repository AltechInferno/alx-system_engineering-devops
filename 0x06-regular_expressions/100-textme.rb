#!/usr/bin/env ruby

the_log_file = ARGV[0]

File.open(the_log_file, 'r') do |file|
  file.each_line do |line|
    match_data = line.match(/\[from:([^\]]+)\] \[to:([^\]]+)\] \[flags:([^\]]+)\]/)
    if match_data
      the_sender = match_data[1]
      the_receiver = match_data[2]
      flags = match_data[3]
      puts "#{the_sender},#{the_receiver},#{flags}"
    end
  end
end

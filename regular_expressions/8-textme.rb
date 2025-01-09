#!/usr/bin/env ruby

input = ARGV[0]


regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/


match = input.match(regex)


if match 
  sender = match[1]
  reciever = match[2]
  flags = match[3]
  puts "#{sender},#{reciever},#{flags}"
else
  
  puts "No valid data found in input."
end

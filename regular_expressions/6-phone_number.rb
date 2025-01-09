#!/usr/bin/env ruby

if ARGV.empty?
  puts "Usage: ./6-phone_number.rb <input_string>"
  exit
end

puts ARGV[0].scan(/^\d{10}$/).join

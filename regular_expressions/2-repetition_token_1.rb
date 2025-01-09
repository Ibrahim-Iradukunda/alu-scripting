#!/usr/bin/env ruby

if ARGV.empty?
  puts "Usage: ./2-repetition_token_1.rb <input_string>"
  exit
end

puts ARGV[0].scan(/hb?tn/).join

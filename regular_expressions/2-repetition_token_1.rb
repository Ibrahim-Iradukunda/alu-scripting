#!/usr/bin/env ruby

if ARGV.empty?
  puts "Usage: ./2-repetition_token_1.rb <input_string>"
  exit
end

# Match patterns where 't' repeats exactly once
puts ARGV[0].scan(/hbt{1}n/).join

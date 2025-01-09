#!/usr/bin/env ruby

if ARGV.empty?
  puts "Usage: ./1-repetition_token_0.rb <input_string>"
  exit
end

# Match patterns where 't' repeats 2 to 5 times
puts ARGV[0].scan(/hbt{2,5}n/).join

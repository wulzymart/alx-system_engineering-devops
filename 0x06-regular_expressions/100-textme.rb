#!/usr/bin/env ruby
sender = ARGV[0][/\[from:(\+?\w*?)\]/, 1]
receiver = ARGV[0][/\[to:(\+?\w*?)\]/, 1]
flags = ARGV[0][/ \[flags:((-?\d:?){5})\]/, 1]

puts "#{sender},#{receiver},#{flags}"

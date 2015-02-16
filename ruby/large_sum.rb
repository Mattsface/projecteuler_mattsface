#!/usr/bin/env ruby

f = File.new('numbers.txt', 'r')

total_sum = 0
f.each_line do |line|
  total_sum += line.strip.to_i
end

puts total_sum.to_s[1,10]
#!/usr/bin/env ruby


# The sum of the squares of the first 100 natural numbers is
n2 = []
1.upto(100) do |x|
  n2 << x**2
end

# The square of the sum of the first 100 natural numbers is
s = []
1.upto(100) do |x|
  s << x
end

total = 0
s.each do |x|
  total += x
end

puts total**2 - n2.inject(:+)
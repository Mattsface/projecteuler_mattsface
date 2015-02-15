#!/usr/bin/env ruby


large_pn = 0
1.upto(999) do |x|
  1.upto(999) do |y|
    pn = x * y
    if pn.to_s == pn.to_s.reverse
      large_pn = pn if pn > large_pn
    end
  end
end

puts large_pn
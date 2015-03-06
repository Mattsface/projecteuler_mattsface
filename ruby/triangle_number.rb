
class Triangle_number

  def initialize( number )
    @number = number
  end


  def number_of_divisors
    @factors = find_prime_factors
    p @factors
    p sort_primes
    p @primes
    total = []
    @primes.each do |number, occurrences|
      total << (occurrences + 1)
    end
    return total.inject(:*)
  end

  private

  def find_prime_factors
    i = 2
    factors = []
    n = @number
    while i * i <= n
      if n % i != 0
        i = i + i
      else
        factors << i
        n = n / i
      end
    end
    if n > 1
      factors << n
    end
  return factors
  end

  def sort_primes
    @primes = {}
    @factors.each do |f|
      next if @primes.key?(f)
      number_of_occurrences = @factors.count(f)
      @primes[f] = number_of_occurrences
    end
    return @primes
  end
end

n = 500
divisors = 0
#until divisors >= 500
  t = Triangle_number.new(n)
  divisors = t.number_of_divisors
  n = n + 1
  p divisors
#end

puts n
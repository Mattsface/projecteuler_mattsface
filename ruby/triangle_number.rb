
class Triangle_number

  def initialize( number )
    @number = number
  end


  def find_prime_factors
    i = 2
    factors = []

    while i * i <= @number
      if @number % i != 0
        i = i + i
      else
        factors << i
        @number = @number / i
      end
    if @number > 1
      factors << @number
    end

    puts factors
    end
  end
end
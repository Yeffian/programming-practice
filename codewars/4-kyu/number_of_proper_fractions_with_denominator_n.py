def proper_fractions(n):
  distinct_prime_factors = set()  
  totient_function = n
  if n == 1:
    totient_function = 0
  else:
    i = 2
    while i * i <= n:
      if n % i == 0:
        distinct_prime_factors.add(i)
        n = n / i
      else:
        i += 1
    if n > 1:
      distinct_prime_factors.add(n) 

    if len(distinct_prime_factors) == 0:   
      totient_function = n - 1
    else:
      for p in distinct_prime_factors:
        totient_function = (totient_function * (p - 1)) / p
        
  return totient_function

print(proper_fractions(15))
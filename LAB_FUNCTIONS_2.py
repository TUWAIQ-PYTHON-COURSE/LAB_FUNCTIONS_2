

def find_primes(n1, n2) -> int:
	
  for primes  in range (n1, n2 + 1): 
  	if primes > 1:
  		for i in range (2,primes):
  			if (primes % i) == 0:
  				break  
  		else:
  			print ('\n-->',primes)

find_primes(0, 12)


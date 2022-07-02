# Create a function : find_primes that takes in 2 parameters of type int ,
# and print the prime numbers between the first parameter and the second parameter . 
def find_primes(min :int , max :int):

    for n in range(min,max + 1):
        if n > 1:
            for i in range(2,n):
                if (n % i) == 0:
                    break
            else:
                print(n)


find_primes(25,50)
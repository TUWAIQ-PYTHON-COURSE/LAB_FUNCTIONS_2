def find_primes(f : int , j: int ):
    print("all the prime numbers between " , f , " and " , j , " are: ")
    for n in range (f , j +1):
        if n <= 1: #  that's because all prime numbers are greater than 1
            continue
        else:
            for o in range(2 , n):
                if (n % o) == 0: 
                    break
            else:
                print(n)

find_primes(0, 50)
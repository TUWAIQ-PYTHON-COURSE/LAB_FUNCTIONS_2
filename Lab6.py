def find_primes(num1 : int , num2: int ):
    print("all the prime numbers between " , num1 , " and " , num2 , " are: ")
    for i in range (num1 , num2 +1):
        if i <= 1: #  that's because all prime numbers are greater than 1
            continue
        else:
            for j in range(2 , i):
                if (i % j) == 0: 
                    break
            else:
                print(i)

find_primes(25, 50)

# LAB_FUNCTIONS_2

## Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter . 


def prime_numbers(x1: int, x2: int) -> int:
    for i in range(x1, x2):
        for y in range(2, i):
            if (i%y) == 0:
                break
        else:
            print(i)
print(prime_numbers(30, 60))

# LAB_FUNCTIONS_2

## Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter . 

### hint
# a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)    
# Also , you can think of it as A Prime Number is a number that cannot be made by multiplying other whole numbers


#### for example, primes between 25 and 50 are:
# 29   
# 31   
# 37   
# 41   
# 43   
# 47  

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the last number: "))

def find_primes(n1 : int, n2 : int) -> int:

    for i in range(n1, n2 + 1):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)

prime = f"The numbers between {n1} and {n2} are: "
print(prime)
find_primes(n1, n2) 
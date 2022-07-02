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
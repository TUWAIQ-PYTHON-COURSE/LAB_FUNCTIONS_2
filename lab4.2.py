def isPrime(n : int):
    if n<=1:
     return False
    for i in range(2,n):
        if n%i == 0  :
            return False
    else:
            return True


def prime_number(num1 : int ,num2 : int):
 for x in range(num1,num2):
    
     if isPrime(x) :
      print(x) 
 print()
prime_number(50,100)

def find_primes(num1 : int , num2 : int ) -> int :
    print("The prime Numbers in the range are")
    for number in range (num1,num2 + 1):  
     if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  

find_primes(10,20)
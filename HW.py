premeter_1 = int (input("Enter the first premeter range: ")) # let user choose first premeter 
premeter_2 = int (input("Enter the second premeter range: "))  # let user choose first premeter
print ("prime numbers in the range ", premeter_1, "to", premeter_2) # let user print the premeters ragne 
for n in range (premeter_1, premeter_2+1):  # use for loop to set u the range 
    flag = 0  # to set vaule for prime number 
    for j in range (2, n): # use onther for loop to check the prime number already set for first loop
        if (n % j == 0): # use conditon for value of n and when j is prime number
            flag = 1 # to set value in prime even when the range between not prime numbers 
            break # stop the program when it takes the ranges 

    if (flag == 0): # use this condtion when the number is prime 
        print (n, end = ' ') # it will print the prime numbers in the range user has to pick
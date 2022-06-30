


def find_primes(num1 : int ,num2 : int):
    counter=0
    for x in range(num1,num2):
        for y in range(x,0,-1):
            if x%y==0:
                counter+=1    
        if counter==2:
            print(x)
        counter=0
              
find_primes(25,50)
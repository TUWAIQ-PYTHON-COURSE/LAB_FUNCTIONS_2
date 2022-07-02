
def find_prime(num1 : int, num2 : int):
    '''This function will find prime numbers in given range (num1, num2) of type integer.'''
    for i in range(num1, num2+1):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            print(i)

print("The prime numbers between the given range is:")
find_prime(25,50)
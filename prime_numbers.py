def prime_numbers(num1 : int, num2 : int) -> int:
    '''This function returns prime numbers within a given range'''
    for i in range(num1, num2):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            print(i, end=' ')
            print()
            


num1 : int = int(input('Please enter the num1 : '))
num2 : int = int(input('Please enter the num2 : '))
prime_numbers(num1, num2)

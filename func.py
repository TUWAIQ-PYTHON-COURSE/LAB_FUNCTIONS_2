
def find_prime(num1 : int, num2 : int) -> None:
    ''' This function take two integer as a parameter and print the prime number as a range between them.  '''
    for number in range(num1, num2 + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number)

find_prime(25,50)
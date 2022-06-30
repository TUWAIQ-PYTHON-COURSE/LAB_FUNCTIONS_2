def get_prime_numbers(num1: int, num2: int):
    for i in range(num1, num2):
        for j in range(2, i):
            if (i%j) == 0:
                break
        else:
            print(i)
print(get_prime_numbers(25, 50))
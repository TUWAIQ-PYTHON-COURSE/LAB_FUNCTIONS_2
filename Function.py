 

frist_number = int(input("Enter the frist number : "))
second_number = int(input("Enter the second number : "))

for num in range(frist_number, second_number + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)



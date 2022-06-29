
def find_primes(first:int, last:int) -> int:
    # Document
    '''
    Given two intgers, find the prime numbers between them.
    '''
    
# if the user made the mistake of assigning the first variable to 
# to be greater than the last variable, then it will print an empty list
# We could evade this by swapping the values.
    if (first > last):
        first, last = last, first

    
    for i in range(first, last + 1):

        # Prime numbers cannot be negative
        if (i > 1):
            # We begin from 2 given that prime numbers begin from 2
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                print(i)


find_primes(first=11, last=70)
        

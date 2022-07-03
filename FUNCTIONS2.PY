
def find_primes (start, end):
    for i in range (25, 50):
        for x in range (2, i):
            if i % x ==0:
                break
        if i % x !=0:
            print(i)
    
  

start : int = 25
end : int = 50
find_primes(start, end)


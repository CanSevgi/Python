# tot =0
# th=1
# for num in range(2,999999):
#     if all(num%i!=0 for i in range(2,num)):
       
#        print (th, "///", num)
#        th +=1
#        if "672" in str(num):
#         print (num)
       



def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
    
print (get_primes(10000))
# for n in range (0,2000000):
#     if "672" in str(get_primes(n)):
#         print(n)
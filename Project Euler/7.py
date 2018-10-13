
b=int(input())
n = [ int(input()) for i in range(b)]
num =0
i=0
inci =0
for a in range(b):
    while inci <= n[a]:
        num +=1
        if all(num%i!=0 for i in range(2,num)):
            # print (inci , "--")
            #print (num)
            inci += 1
    print(num)
num=int(input("enter a number"))
import math
res=[]
for i in range (1,int(math.sqrt(num))+1):
    if (num%i==0):
        res.append(i)
        if num//i!=i:
            res.append(num//i)
res.sort()
print(res)        
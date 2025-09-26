def staircase(n):
    a,b=1,2
    for i in range(n-1):
        a,b=b,a+b
    return a
n=int(input("number of staircase"))
res=staircase(n)
print(res)
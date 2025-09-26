nums=list(map(int,input("enter a number").split()))
dict={}
'''for i in nums:
    dict[i]=nums.count(i)
print(dict)
'''
'''
for i in nums:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
'''
for i in nums:
    dict[i]=dict.get(i,0)+1
print(dict)
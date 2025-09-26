n=[1,23,243,4,54,5,3,2,2,2,1,7,5,18,67]
m=[10,111,1,9,5,2]
dict={}
for i in n:
    dict[i]=dict.get(i,0)+1
for i in m:
    print(F"{i} count {dict.get(i,0)}")
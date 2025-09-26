s='aazyxyyzaaaa'
q=["d","a","y","x"]
dict={}
for i in s:
    dict[i]=dict.get(i,0)+1
for i in q:
    print(f"{i} count {dict.get(i,0)}")
text=input("enter the text : ")
t=[i for i in text]
t2=[ord(i) for i in t]
t3=[]
for i in range(len(t2)):
    if i%2==0:
        t3.append(t2[i]<<1)
    else:
        t3.append(t2[i]>>1)
    
res=""
for i in t3:
    res=res+chr(i)
print(res)



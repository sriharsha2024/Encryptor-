text=input("enter the text : ")
t=[i for i in text]
t2=[ord(i) for i in t]
t3=[]
t4=[]
for i in range(len(t2)):
    if i%2==0:
        t3.append(t2[i]<<1)
    else:
        t3.append(t2[i]>>1)

for i in range(len(t3)):
    rev=0
    while(t3[i]> 0):
        a = t3[i]% 10
        rev = rev * 10 + a
        t3[i] = t3[i] // 10
    t4.append(rev)
    
res=""
for i in t4:
    res=res+chr(i)
print(res)



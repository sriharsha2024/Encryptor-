text=input("enter the text : ")
t=[i for i in text]
t2=[ord(i) for i in t]
t3=[]

for i in range(len(t2)):
    rev=0
    while(t2[i]> 0):
        a = t2[i]% 10
        rev = rev * 10 + a
        t2[i] = t2[i] // 10
    t3.append(rev)

res=""
for i in t3:
    res=res+chr(i)
print(res)

text=input("enter the text : ")
t=[i for i in text]
t2=[ord(i) for i in t]
t3=[]
t4=[]
for i in range(len(t2)):
    t3.append(list(reversed(format(t2[i],"b"))))
    t4.append(int("".join(t3[i])))

res=""
for i in t4:
    res=res+chr(i)
print(res)


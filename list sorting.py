list=[]
for i in range(int(input("range:"))):
    a=int(input("list items:"))
    list.append(i)
for j in range(0,len(list)):
    for k in range(j+1,len(list)):
        if list[j] > list[k]:
            temp = list[j]
            list[j]=list[k]
            list[k] = temp
print(list)

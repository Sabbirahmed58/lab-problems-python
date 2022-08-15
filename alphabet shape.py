num= int(input())

for i in range (num):
    print(" "*i,end="")
    for j in range(num-i):
        print(chr(65+j),end=" ")
    print()
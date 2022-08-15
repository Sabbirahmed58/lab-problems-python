##triangle
num= int(input())

for i in range (num):
    print(" "*(num-i-1),end="")
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()


#inverted triangle

num= int(input())

for i in range (num):
    print(" "*i,end="")
    for j in range(num-i):
        print(chr(65+j),end=" ")
    print()
    
    
    

##triangle
n= int(input())
for i in range(n):
    print(" "*(n-i-1)+(chr(65+i)+" ")*(i+1))


#inverted triangle

num= int(input())

for i in range (num):
    print(" "*i,end="")
    for j in range(num-i):
        print(chr(65+j),end=" ")
    print()
    
    
    

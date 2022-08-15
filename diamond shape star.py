#diamond shape star:

num= int(input())
for i in range (num):
    print(" "*(num-i-1)+"* "*(i+1))
for i in range(num-1):
    print(" " *(i+1)+"* "*(num-i-1))


# tringle shape star:

num= int(input())
for i in range (num):
    print(" "*(num-i-1)+"* "*(i+1))
    
#inverted triangle:

num= int(input())
for i in range(num-1):
    print(" " *(i+1)+"* "*(num-i-1))


##half
n = int(input())

for x in range(n):
    for y in range(x+1):
        print("* ", end="")
    print()
    
    
#reverse half
n = int(input())

for x in range(n, 0, -1):
    for y in range(x):
        print("* ", end="")
    print()  
    
    
#number shape triangle


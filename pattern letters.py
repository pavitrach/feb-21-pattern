'''n=int(input("enter number"))
k=0
for i in range (1,n+1):
    for j in range(0,n):
        print(chr(97+k),end="")
        k+=1
        if k==26 :
            k=0
    print()'''
n=int(input("enter number"))
k=0
for i in range (1,n+1):
    for j in range(0,n):
        print(chr(97+k),end="")
        k+=1
    print()

print("\nWrite a program to print the following pattern using a for loop:\n")

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
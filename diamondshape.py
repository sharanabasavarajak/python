row = 5

for i in range(1, row+1):
    print(" " * (row - i), end="")
    print("*" * (2*i - 1), end="")
    print()
for i in range((row - 1),0,-1):
    print(" " * (row - i), end="")
    print("*" * (2*i - 1), end="")
    print()    

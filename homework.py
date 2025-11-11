
for i in range(1,6):
    print('*' * i)

print()
        
for i in range(1,6):
    print('* ' * i)   

print()  

for i in range(5, 0, -1):
    print('* ' * i)
    
print()

for i in range(1 , 6):
    print("  " * (5 - i) + "* " * i)
   
print()   

for i in range(1 , 7):
 print(" " * (6 - i) + "* " * (i - 1) + "*")
 



print()



for i in range(1, 7):
    for j in range(6 - i):
        print(' ', end='')
    for a in range(1, i + 1):
        if a == 1 or a == i or i == 6:
            print('*', end='')
        else:
            print(' ', end='')
        if a != i: 
            print(' ', end='')
    print()

print()

for i in range(8):
    print(" " * i + "*" * (2 * (8 - i) - 1))
for i in range(8 - 2, -1, -1):
    print(" " * i + "*" * (2 * (8 - i) - 1))
    
print()

  


for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
for i in range(4, 0, -1):
    print(" " * (5 - i) + "* " * i)

print()




for i in range(5):
    if i == 0:
        print("* " * 9)
    elif i < 4:
        print("  " * i + "*" + " " * (15-4 * i) + "*")
    else:
        print("  " * i + "*")


for i in range(3, -1, -1):
    if i == 0:
        print("* " * 9)
    else:
        print("  " * i + "*" + " " * (15-4 * i) + "*")


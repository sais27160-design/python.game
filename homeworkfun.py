#1
def triangle():
    for i in range(1,6):
        print('*' * i)


#2  
def triangle_with_extra_spaces():     
    for i in range(1,6):
        print('* ' * i)   

 
#3
def flipped_up_side_down_triangle():
    for i in range(5, 0, -1):
        print('* ' * i)

#4
def turned_triangle():
    for i in range(1 , 6):
        print("  " * (5 - i) + "* " * i)
   
  
#5
def christmas_tree():
    for i in range(1 , 7):
        print(" " * (6 - i) + "* " * (i - 1) + "*")
 

# 6
def empty_christmas_tree():
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


# 7
def sand_timer():
    for i in range(8):
        print(" " * i + "*" * (2 * (8 - i) - 1))
    for i in range(8 - 2, -1, -1):
        print(" " * i + "*" * (2 * (8 - i) - 1))


  

# 8
def diamond_pattern():
    for i in range(1, 6):
        print(" " * (5 - i) + "* " * i)
    for i in range(4, 0, -1):
        print(" " * (5 - i) + "* " * i)





# 9
def empty_sand_timer():
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
        
triangle()
print()
triangle_with_extra_spaces()
print()
flipped_up_side_down_triangle()
print()
turned_triangle()
print()
christmas_tree()
print()
empty_christmas_tree()
print()
sand_timer()
print()
diamond_pattern()
print()
empty_sand_timer()
        


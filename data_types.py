import random

### Part 1

## 1.1
# A color on a computer is a triple or 3-tuple. The zeroth item is red, the oneth item is blue, and the twoth item is green.
# My date of birth is a 3-tuple. The zeroth item is the day, the oneth item is the month, and the twoth item is the year. (Also acceptable to say M,D,Y or Y,M,D)
# The current time is a 3-tuple. The zeroth item is the hour, the oneth item is the minute, and the twoth item is the second. (Also acceptable to exclude second or include millisecond, or to have a Boolean for AM/PM)
# My gradebook is a 6-tuple. The zeroth item is my Math grade %, the oneth item is my History grade %, etc... (Whatever their real list of classes is)

## 1.2
tuple_1 = (8, 10, 0) # Breakfast time is 8:10 am
tuple_2 = (12, 20, 0) # Lunch time is 12:20 pm
tuple_3 = (17, 30, 0) # Dinner time is 5:30 pm

## 1.3
print(tuple_1[0]) # The Hour of breakfast time is 8
print(tuple_2[1]) # The Minute of lunch time is 20
print(tuple_3[2]) # The Second of dinner time is 0

### Part 2

## 2.1
my_list = [1, 2, 3, 4, 5]
my_list[0] = 0
my_list[1] = 0
my_list[2] = 0
my_list[3] = 0
my_list[4] = 0
print(my_list)

## 2.2
my_list = []
for i in range(10):
    my_list.append(i * i)
while(len(my_list) > 0):
    print(my_list.pop(0))

## 2.3
targets = []
for i in range(10):
    rand_row = random.randint(0, 5)
    rand_col = random.randint(0, 5)
    targets.append((rand_row, rand_col))
for t in targets:
    print(t)

### Part 3

grid = []
for i in range(6):
    row = []
    for j in range(6):
        row.append(random.random() < 0.1)
    grid.append(row)
for i in range(6):
    print(grid[i])

### Part 4
### Only ONE of these needs to be done

# 4.1
# print("How many targets should the robot drive to?")
# num_targets = int(input())
# targets = []
# for i in range(num_targets):
#     rand_row = random.randint(0, 5)
#     rand_col = random.randint(0, 5)
#     targets.append((rand_row, rand_col))

# 4.2
# print("How many rows?")
# height = int(input())
# print("How many columns?")
# width = int(input())
# grid = []
# for i in range(height):
#     row = []
#     for j in range(width):
#         row.append(random.random() < 0.1)
#     grid.append(row)

# 4.3
grid = []
for i in range(6):
    row = []
    for j in range(6):
        row.append(False)
    grid.append(row)
print("How many obstacles?")
num_obstacles = int(input())
for i in range(num_obstacles):
    print("Obstacle #" + str(i))
    print("Row?")
    obstacle_row = int(input())
    print("Column?")
    obstacle_col = int(input())
    grid[obstacle_row][obstacle_col] = True


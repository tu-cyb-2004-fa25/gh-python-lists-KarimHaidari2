# in-class exercise for Lecture 03 List

# 1. Fill in the missing code to produce the output: ['honda', 'yamaha', 'suzuki', 'kawasaki']
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.append('kawasaki')
motorcycles
#<<insert your missing code here>>
print(motorcycles)


# 2. Please double each element in the list 
my_list = [1, [4, 6, 12], 7, 8]
# 2. Please double each element in the list 
my_list = [1, [4, 6, 12], 7, 8]

# double the first element
my_list[0] *= 2

# double each element inside the nested list
my_list[1] = [x * 2 for x in my_list[1]]

# double the rest of the elements
my_list[2] *= 2
my_list[3] *= 2

print(my_list)


# 3. Fill in the code to produce the following output:  [3, 6, 99, 45, 29, 34] 
#    You can insert multiple lines of code, obtain target_list based on list1 and list2
list1 = [3,6,99,12]
list2 = [64,45,29,34]
target_list = list1[:-1]
target_list.extend(list2[1:])
print(target_list)

# Try it yourself exercise
# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit

# (1) Store the locations in a list
places = ["Japan", "Italy", "New Zealand", "Canada", "Iceland"]

# (2) Print your list in its original order
print ("Original list:", places)
# (3) Print your list in alphabetical order without modifying the actual list
print("Alphabetical order:", sorted(places))
# (4) Show that your list is still in its original order by printing it
print("still original list():", places)
# (5) Change the order of your list in reverse order and print it
print("Reverse order:", list(reversed(places)))
# (6) Change your list so it’s stored in reverse-alphabetical order, and print it 
places.sort(reverse=True)
print("Reverse alphabetical:", places)
# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive. 
for sum in range(1, 21):
    print(sum)
# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list. 
multiples_of_three = [num for num in range(3, 31, 3)]
for num in multiples_of_three:
    print(num)
# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube. 
cubes = []
for num in range(1, 11):
    cubes.append(num ** 3)

for cube in cubes:
    print(cube)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
# 4-9. Cube Comprehension
cubes = [num ** 3 for num in range(1, 11)]
print(cubes)


# in-class code
import copy

list1 = [1, 2, 3, 4, ["a", "b"]]
list2 = list1 
list3 = list1[:]
list4 = list1.copy()
list5 = copy.copy(list1) 
list6 = copy.deepcopy(list1) 

list2.append(5)
list3[4].append("c") 
list4[0] = 100
list5[4][-1] = "w" 
list6[-1].append("c")

'''
# discuss the answers befor runing the following code
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")
print(f"list4: {list4}")
print(f"list5: {list5}")
print(f"list6: {list6}")
'''
# list item are changeable, ordered, allows duplicates values

import json
from shutil import which

with open("list_asstes.json") as file:
    data = json.load(file)


thislist = ['banana', 'apple', 'banana']

print('(1) {} list contains duplicats'.format(thislist))

# Oreders means that item hava defined order like if we insert another item to the list it will be at the end 

thislist.append('cherry')

print('(2) "cherry" has been added to the end of the list {}'.format(thislist))

# as for if we wand to remove it list will remove the last input


# list can store any data type items

newList = ['str', True, 1, 1.3]
print('(3) list stores different data types ex: {}'.format(newList))

# data type of list

print(type(thislist))

# list can be constructed by using list key

constucted_list = list((1,2,3,4,5)) # must be double round-brackets

print('(4) list using "list constuctor" {}'.format(constucted_list))

# return specific items from list 
fruits = data['fruits']
print('(5) Orginal List: {} length {}'.format(fruits, len(fruits)))
print(fruits[1:5]) # with this py starts to look from index 1(includes) to index 5(not includes)

# we can tell python to print till specific index number

print(fruits[:4]) # it will print till index number 4

# in list we can even revers the counter by - 

print(fruits[:-1]) #this prints till last item of the list

print(fruits[-4:]) # this will start from -4 indext from the end

# in list we can tell which postion new item should be inserted by using insert

fruits.insert(0, 'new fruite')
print(fruits)

# another way to insert in list is append 

fruits.append("Jackfruit") # append insert item in the end of the list
print(fruits)

print(type(fruits))

# to append another list to exsiten list extend method is used

fruits.extend(newList)
print(fruits)

# extend can append tuple too

tuple_ = (2,2,3)

fruits.extend(tuple_)
print(fruits)

# to remove item we can use remove method but remove takes arguments for which item to remove

fruits.remove(2) # remove method removes the first item matches to the arguments
print(fruits)

# we can also remove item with out specifiy the which item we want to remove with pop

fruits.pop() # pop removes the last elemets if no argument is passed
print(fruits)

# pop can remove specific index item too

fruits.pop(0) # index number of the list will be removed

print(fruits)

# if we need to delete entire list we use del method

print(thislist)

del thislist

try:
    print(thislist)
except NameError:
    print('List not found', NameError.name)
    
# del can be used to delete specific item in a list

del fruits[0]

print(fruits)

# to clear the list clear method is used
print('Before "clear method list {} |'.format(newList))
print('after "clear method list: ', end='')
newList.clear()
print(newList)

# with loop we can access list item one by one or with condition

# for loop

for item in fruits:
    print(item)
    
# while loop

i = 0

while len(fruits) > i:
    print(fruits[i])
    i += 1
    
# list comprehension offer short hand for loop 

print('------------------Short Hand For Loop-------------------')

[print(x) for x in fruits]

# list compenhersion one liner Python

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_fruits = [fruit for fruit in fruits if "a" == fruit[0]]

print(new_fruits)

new_fruits = [fruit.title() for fruit in fruits if fruit[0] != 'a']
print(new_fruits)

new_list2 = [x if 'a' in x else 'This dose not contains letter A'+ f" {x}" for x in fruits]
print(new_list2)

# sort key arguments sort method is case sentive
numbers = [100, 50, 65, 82, 23]

# sort base on how close the number is to
def my_func(x):
    return abs(x-50)

numbers.sort(key=my_func)
print(numbers)

# sort method is case insensetive
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)
print(thislist)


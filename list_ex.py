# Reverse a list in Python


list1 = [100, 200, 300, 400, 500]
list_ = list1.copy()
list__ = list_.copy()

# list1.sort(reverse=True)
list1.reverse()
print(list1)

# solution with out bulid in mehtod
rev_list = []
for i in range(1,len(list_)+1):
    rev_list.append(list_[-i])

print(rev_list)

# solution in short hand for loop

rev_list.clear()

[rev_list.append(list_[-i]) for i in range(1, len(list_)+1)]

print(rev_list)

# Using negative slicing

print(list__[::-1],'List slicing T')
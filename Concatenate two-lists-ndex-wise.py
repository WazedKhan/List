list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# output : ['My', 'name', 'is', 'Kelly']

output = []
list3 = []

[output.append(list1[i] + list2[i]) for i in range(0, len(list1)) ]

print(output)

list3 = [i+j for i, j in zip(list1,list2)]

print(list3)



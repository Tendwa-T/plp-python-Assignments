from operator import indexOf


my_list =[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1,15)

my_list.extend([50,60,70])

del my_list[-1]

my_list.sort()

print(indexOf(my_list,30))

print(my_list)

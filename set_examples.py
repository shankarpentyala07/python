my_set = {"January", "February", "March"}

for element in my_set:
    print(element)

my_set.add("April")
print(my_set)
my_set.remove("January")
print(my_set)


my_list = ["January","February","March","January"]
my_list.append("April")
print(my_list)
my_list.remove("January") #List removes the first matching value
print(my_list)
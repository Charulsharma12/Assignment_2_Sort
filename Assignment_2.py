#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
length_of_list = input("Length of list")
length_of_each_tuple = int(input("Length of each tuple"))
sample_list = []
for i in range (int(length_of_list)):
    tup = []
    for index in range (length_of_each_tuple):
      each_tuple_value = int(input("Input value of tuple at position {index}"))
      tup.append(each_tuple_value)
    sample_list.append(tuple(tup))
print(sample_list)
sample_list.sort(key = lambda r:r[-1])


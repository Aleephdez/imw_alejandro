import sys

total_add = 0.0

number_list= sys.argv

number_list.pop(0)

list_size = len(number_list)

for i in range (list_size):

    print([float(number_list[i])])


#average = total_add / list_size

#print(average)
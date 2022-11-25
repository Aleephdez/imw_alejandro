import sys

total_add = 0.0

number_list= sys.argv

number_list.pop(0)

list_size = len(number_list)


for i in number_list:
    number = float(i)
    total_add += number


average = total_add / list_size

print("La media de los valores es {}".format(average))
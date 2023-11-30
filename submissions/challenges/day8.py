
def average(my_list):
    sum = 0
    avg = 0

    for num in my_list:
        print(num)
        sum += num

    ave = sum/len(my_list)
    return ave;

my_list = [5, 9, 2, 3, 1]
print("Average of the list is",average(my_list))




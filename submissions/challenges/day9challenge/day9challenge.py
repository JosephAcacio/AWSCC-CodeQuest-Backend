from module import calculate_area

side = int(input("please enter the radius: "));
areaCircle = "{:.2f}".format(calculate_area(side));

print(areaCircle)
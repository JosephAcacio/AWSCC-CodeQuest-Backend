class Calculator:
    def difference(self, numlist: list):
        _dif = numlist[0]

        for num in numlist[1:]:
            _dif -= num
        
        return _dif
    
string_numbers = input("Please enter the numbers you want to subtract respectively: ").split()

numbers = [int(str_numbers) for str_numbers in string_numbers]

my_calculator = Calculator()

numlist_str = ', '.join(map(str, numbers))


difference = my_calculator.difference(numbers)
print(f"The difference of {numlist_str} is {difference}")
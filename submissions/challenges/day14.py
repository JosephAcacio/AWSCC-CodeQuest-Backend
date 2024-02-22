class basic_Calculator:
    def add(self, numlist: list):
        sum = 0

        if len(numlist) > 3:
            return "Please enter 3 numbers only"
        else:
            for num in numlist:
                sum += num
            return sum

class complex_Calculator:
   def add(self, numlist: list):
      sum = 0

      for num in numlist:
          sum += num
      return sum
      
string_numbers = input("Please enter the numbers you want to subtract respectively: ").split()

numbers = [int(str_numbers) for str_numbers in string_numbers]

basic = basic_Calculator()
complex_calcu = complex_Calculator()

print(basic.add(numbers))
print(complex_calcu.add(numbers))


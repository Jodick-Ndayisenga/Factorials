#The code will help us generate the factorial of a given number
Number = int(input('Enter the number for which you want to calculate the factorial for: '))
factorial = 1
for i in range(1, Number+1):
    factorial = factorial*i

print(f'The factorial of {Number} is : {factorial}')
#building my calculator again after a year

first_digit = int(input("Enter your first digit: "))
second_digit = int(input("Enter your second digit: "))

operators = input("Choose your operator: +, -, /, *: ")

if operators == "+":
    total = first_digit + second_digit
    print(total)
elif operators == "-":
    total = first_digit - second_digit
    print(total)
elif operators == "/":
    total = first_digit / second_digit
    print(total)
elif operators == "*":
    total = first_digit * second_digit
    print(total)

#easy on the first five codes, hard on the elif one
#remember "==" means Choose
#the total is the variable, inside it is the process of calculation
#never again
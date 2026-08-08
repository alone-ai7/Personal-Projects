my_box = []
for i in range(5):
    user = input("Enter Five numbers: ")
    num = int(user)
    my_box.append(num)

smallest = my_box[0]
for number in my_box:
    if number < smallest:
        smallest = number

largest = my_box[0]
for number in my_box:
    if number > largest:
        largest = number

print(f"The smallest number is {smallest}")
print(f"The largest number is {largest}")

## Find Min-Max

A simple Python program that finds the smallest and largest number from user input.

## What It Does

- Asks the user to enter 5 numbers
- Stores all numbers in a list
- Finds the smallest number
- Finds the largest number
- Displays both results

## Concepts Used

- **Variables** — storing data
- **Lists** — collecting multiple items with `.append()`
- **Loops** — repeating actions with `for`
- **Conditionals** — making decisions with `if`
- **Input/Output** — `input()` and `print()`

## Key Learnings

- Use `my_box[0]` to get the first item (don't hardcode values)
- Use `>` to find largest, `<` to find smallest
- Keep variable names consistent inside loops

#in a sentence
Finds the smallest and largest number from 5 user inputs. Creates a list,asks user for 5 numbers and stores them, sets smallest and largest to the first number,
loops through all numbers updating smallest if found smaller or largest if found bigger, then prints both results. Uses variables, lists, loops, and if statements.


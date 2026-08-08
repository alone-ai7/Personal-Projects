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

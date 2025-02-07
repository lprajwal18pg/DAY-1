
arra = [int(input(f"Enter the element {i + 1}: ")) for i in range(10)]


largest_number = second_largest_number = None

for num in arra:
    if largest_number is None or num > largest_number:
        second_largest_number = largest_number
        largest_number = num
    elif num != largest_number and (second_largest_number is None or num > second_largest_number):
        second_largest_number = num

if second_largest_number is None:
    print("There is no second largest number.")
else:
    print("The second largest number is:", second_largest_number)

    print("The largest number is:", largest_number)
            
arra = []
n = 10
for i in range(n):
    element = int(input(f"Enter the element {i + 1}: "))  
    arra.append(element)


largest_number = arra[0]


for num in arra:
    if num > largest_number:
        largest_number = num

print("The largest number is:", largest_number)
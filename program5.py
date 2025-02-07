
arra = []
n = 10


for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    arra.append(element)


print("Original array:", arra)


unique_array = []

for element in arra:

    if element not in unique_array:
        unique_array.append(element)


print("Array with unique elements:", unique_array)

arra = [int(input(f"Enter the element {i + 1}: ")) for i in range(10)]

total_sum = 0


for num in arra:
    total_sum += num  

print("The sum of the array elements is:", total_sum)
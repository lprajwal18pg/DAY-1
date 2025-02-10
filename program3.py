
arra = []
n = 10



for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    element = int(element) 
   
    if element in arra:
        print(f"This ID '{element}' existeed. Please enter a new ID.")
    else:
        arra.append(element) 
        print(f"ID '{element}' has been added.")


print("Final IDs:", arra)
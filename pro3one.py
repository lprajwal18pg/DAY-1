
uinput = input("Enter string = ")

rstring = ""


for i in range(len(uinput) - 1, -1, -1):
    rstring += uinput[i]


print("R string is = ", rstring)

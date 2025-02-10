def is_palindrome(s):
    cleaned_string = ''.join(s.split()).lower()
    return cleaned_string == cleaned_string[::-1]

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("True")
else:
    print("False")
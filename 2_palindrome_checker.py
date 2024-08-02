def isPalindrome(string):
    string = string.lower()
    # Remove spaces and punctuation
    string = ''.join(char for char in string if char.isalnum())
    # Check if the string is equal to its reverse
    return string == string[::-1]

string_input = input("Enter a string to check whether if it is palindrome or not : ")

print(isPalindrome(string_input))
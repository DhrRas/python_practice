''' Python has built in string validation methods for basic data.
It can check if a string is composed of alphabetical characters, alphanumeric
characters, digits etc.'''

# str.isalnum() checks if all characters of a string are alphanumeric or not.
# str.isalpha() checks if all characters of a string are alphabetical or not.
# str.isdigit() checks if all characters of a string are digit or not.
# str.islower() checks if all characters of a string are lowercase or not. 
# str.isupper() checks if all characters of a string are uppercase or not.

if __name__ == "__main__":
    string = input()
        
    if string.isalnum() == True:
        print(True)
    if string.isalpha() == True:
        print(True)
    if string.isdigit() == True:
        print(True)
    if string.islower() == True:
        print(True)
    if string.isupper() == True:
        print(True)
    else:
        print(False)
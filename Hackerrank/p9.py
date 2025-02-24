''' Python has built in string validation methods for basic data.
It can check if a string is composed of alphabetical characters, alphanumeric
characters, digits etc.'''

# str.isalnum() checks if all characters of a string are alphanumeric or not.
# str.isalpha() checks if all characters of a string are alphabetical or not.
# str.isdigit() checks if all characters of a string are digit or not.
# str.islower() checks if all characters of a string are lowercase or not. 
# str.isupper() checks if all characters of a string are uppercase or not.

if __name__ == '__main__':

    string = input()
    alnum = alpha = dig = low = upp = False

# 1st line.
    for char in string:
        if char.isalnum():
            alnum = True
    
    if alnum:
         print(True)
    else:
         print(False)

# 2nd line.
    for char in string:
        if char.isalpha():
            alpha = True
    if alpha:
            print(True)
    else:
            print(False)

# 3rd time.
    for char in string:
        if char.isdigit():
            dig = True       
    if dig:
            print(True)
    else:
            print(False)

# 4th time.
    for char in string:
        if char.islower():
             low = True
    if low:
         print(True)
    else:
         print(False)
 
 # 5th time.
    for char in string:
         if char.isupper():
             upp = True
    if upp:
        print(True)
    else:
        print(False)


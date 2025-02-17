''' Python has built-in string validation methods for basic data.
it can check if a sring is composed of alphabetical characters,
alphanumeric characters, digit, etc...'''

if __name__ == "__main__":
    string = input()
        
    for char in string.split():
        if string.isalnum() == True:
            print(True)
        elif string.isalpha() == True:
            print(True)
        elif string.isdigit() == True:
            print(True)
        elif string.islower() == True:
            print(True)
        elif string.isupper() == True:
            print(True)
        else:
            print(False)
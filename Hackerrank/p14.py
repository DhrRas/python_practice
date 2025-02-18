if __name__ == '__main__':

    string = input()
    

    for char in string: # 1st time
        if ord(char) >= 97 or ord(char) >= 65 or char in range(0, 10):
            print(True)
        
    print(False)
    
    
    for char in string: # 2nd time
         if ord(char) >= 97 or ord(char) >= 65:
            print(True)

    print(False)
    

    # for char in string: # 3rd time
    #     if char.isdigit():
    #         print(True)
    #     else:
    #         print(False)

    # for char in string: # 4th time
    #     if char.islower():
    #         print(True)
    #     else:
    #         print(False)

    # for char in string: # 5th time
    #     if char.isupper():
    #         print(True)
    #         break

    

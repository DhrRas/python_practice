''' if you want to add a single element to an existing set,
we can use the .add() function.'''

if __name__ == '__main__':

    country_stamps = int(input())
    
    for i in range(1,country_stamps+1):
        country_name = input()
        lst = set(country_name)
        
    add_names = lst.add(input())

        # result = len(lst)
    print(add_names)
    print(lst)
    # print(result)
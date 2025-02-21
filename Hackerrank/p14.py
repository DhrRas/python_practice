# we have three methods of set.
# viz discard, remove, pop 
 
# if element doesnot exist remove raises keyerror
# while discard doesn't raise error.

# the same story goes with pop method too. i.e it raises 
# keyerror if element is not present in set.

if __name__ == '__main__':

    no_elements = int(input())

    for i in range(1,no_elements+1):
        result = print(i,end=' ')    
    
    print(result)

    No_commands = int(input())
    # actions = []

    for i in range(No_commands):
        x = input('please enter action: ').split(' ')

        if x[0] == 'pop':
            y = 0
            result.pop()
            print(result)
        
        elif x[0] == 'remove':
            y = int(x[1])
            result.remove(y)
            print(result)

        else:
            y = int(x[1])
            result.discard(y)
            print()

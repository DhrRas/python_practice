''' Exercise regarding discard() remove() and pop'''

if __name__ == '__main__':
    integer_list = list()
    no_elements = int(input())

    for i in range(1,no_elements+1): 
        num = integer_list.append(i)
    
    integer_set = set(integer_list)
    for i in integer_set:
        print(i, end=' ')

    print()
    no_of_commands = int(input('enter the number of commands: ')) 

    for i in range(no_of_commands):
        x = input('').split(' ')

        if x[0] == 'pop':
            y = 0
            integer_set.pop()
        
        elif x[0] == 'remove':
            y = int(x[1])
            integer_set.remove(y)

        else:
            y = int(x[1])
            integer_set.discard(y)
    
    print(integer_set)
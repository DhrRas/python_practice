''' Exercise regarding discard() remove() and pop'''

if __name__ == '__main__':
    no_elements = int(input())

    # integer_set = set(integer_list)

    for i in range(no_elements):
        num = input().split()
        num2 = list(map(int,num))
        print(num2,end=' ') 
         
    # print()
    
    # for i in range(1, len(integer_list)+1):
    #      new_num = integer_set.add(i)
             
    # print(integer_set)
    # # print()
    # no_of_commands = int(input('enter the number of commands: ')) 

    # for i in range(no_of_commands):
    #     x = input('').split(' ')

    #     if x[0] == 'pop':
    #         y = 0
    #         integer_set.pop()
        
    #     elif x[0] == 'remove':
    #         y = int(x[1])
    #         integer_set.remove(y)

    #     else:
    #         y = int(x[1])
    #         integer_set.discard(y)
    
    # print(integer_set)
'''Consider a list(list = []). You can perform the following commands.
1. insert i e: insert integer e at position i.
2. print: print the list
3. remove e: Delete the first occurrence of integer e
4. append e: Integer integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the lat element '''

if __name__ == '__main__':
    N = int(input())
    
    l2 = []
    
    for x in range(N):
        l1 = input().split()
        
        if l1[0] == 'insert':
            l1[1] = int(l1[1])
            l1[2] = int(l1[2])
            l2.insert(l1[1],l1[2])
        
        elif l1[0] == 'print':
            print(l2)
            
        elif l1[0] == 'remove':
            l2.remove(int(l1[1]))
            
        elif l1[0] == 'append':
            l2.append(int(l1[1]))
            
        elif l1[0] == 'sort':
            l2.sort()
            
        elif l1[0] == 'pop':
            l2.pop()
            
        elif l1[0] == 'reverse':
            l2.reverse()
               
                

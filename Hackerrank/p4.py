'''Given the participants' score sheet for your University Sports Day. 
You are required to find the runner-up score. You are given n scores.
Store them in a list and find the score of the runner-up.'''

if __name__ == '__main__':
    n = int(input())
    num = list(map(int, input().split()))

    for i in range(len(num)-1):
        if num[i] in num:
            high_num = num[i]
            # print(high_num)
        
        if high_num > num[i+1]:
            high_num = high_num 
            # print(high_num)
        else:
            high_num = num[i+1]
            # print(high_num)
        
        if high_num == 9:
            if high_num > num[i+1]:
                high_num = high_num
            else:
                high_num = num[i+1]
                
        print(high_num, end=' ')

        
        

    
#    print(new_num)
        #     print(i)
        
        # elif new_num > num[i+1]:
        #     new_num = num[i+1]
        #     print(i)
        
        # elif new_num > num[i+1]:
        #     new_num = num[i+1]
        #     print(i)
        
        # elif new_num > num[i+1]:
        #     new_num = num[i+1]
        #     print(i)

        # elif new_num > num[i+1]:
        #     new_num = num[i+1]
        #     print(i)
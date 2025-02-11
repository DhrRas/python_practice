'''Given the participants' score sheet for your University Sports Day. 
You are required to find the runner-up score. You are given n scores.
Store them in a list and find the score of the runner-up.'''

if __name__ == '__main__':
    n = int(input())
    num = list(map(int, input().split()))

    if num[0]:
        high_num = num[0]


    for i in range(len(num)):
    
        if high_num < num[i]:
            high_num = num[i]
    org_high = high_num


    for i in range(len(num)):
        if num[i] != org_high:
            new_high = num[i]
            break

    for i in range(len(num)):
        if num[i] == org_high:
            continue
        
        #print(num)
        if new_high < num[i]:
            new_high = num[i]

    print(new_high)
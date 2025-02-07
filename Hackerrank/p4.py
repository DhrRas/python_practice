'''Given the participants' score sheet for your University Sports Day. 
You are required to find the runner-up score. You are given n scores.
Store them in a list and find the score of the runner-up.'''

if __name__ == '__main__':
    n = int(input())
    input_list = list(map(int, input().split()))

    print(input_list)
    for x in input_list:
        #print(x)
        pass
def count_substring(string, sub_string):
    for i in range(0,len(string)):
        # print(string[i])
        if sub_string in string:
            print('yes')
            return string.count(sub_string) 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
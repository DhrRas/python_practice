'''In this challenge, the user enters a string and a substring.'''


def count_substring(string, sub_string):
    count = 0
    for i in [string, sub_string]:
        if string[i] == sub_string[i]:
            if len(sub_string) == len(string) and sub_string[:len(sub_string)] == string[string[i]:len(sub_string)+2]:
                count += 1
        print(count)   


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

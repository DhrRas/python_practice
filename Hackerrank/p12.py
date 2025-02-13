'''In this challenge, the user enters a string and a substring.'''


def count_substring(string, sub_string):
    for i in range(0, len(string)):
        return string.count(sub_string)
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

'''In this challenge, the user enters a string and a substring.'''
def count_substring(string, sub_string):
    for i in range(0, len(string)):
        if string[i] == sub_string[i]:
            for j in range(0,len(sub_string)):     
                 word = sub_string[j] + string[j]
                 word_len = len(word)
                 
        else:
                 break
        return word_len   


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

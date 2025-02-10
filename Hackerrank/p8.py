''' You are given a string and your task is to swap cases.'''

def swap_case(s):
        return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split())) 
    # always remember tuple object hash is possible.
    print(hash(integer_list))

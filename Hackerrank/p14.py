def sym_diff(set_a,set_b):
    
    for i in set_a:
        if list(set_a)[i] == '':
            set_a.remove()
        print(i)



if __name__ == '__main__':
    M_size = int(input())
    M_set = set(input())

    # N_size = int(input())
    # N_set = set(input())

    # result = sym_diff(M_set, N_set)
    
    # print(result)


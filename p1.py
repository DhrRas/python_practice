'''
use list comprehensions
x = 1
y = 1
z = 2
n = 3
all permutations are |i,j,k| are:
[[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[0,1,2],[1,0,0],[1,0,1],[1,0,2],[1,1,0],[1,1,1],[1,1,2]]
'''





if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    l1 = [[x,y,z] for x in [0,1] for y in [0,1] for z in [0,1] if(x+y+z) != n ]
    l2 = [[x,y,z] for x in [0,1,2] for y in [0,1,2] for z in [0,1,2] if (x+y+z) != n]
    
    if x==1:
        print(l1)
    else:
        print(l2)
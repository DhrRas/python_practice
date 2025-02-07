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
    
    l1 = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if (i+j+k) != n]
    print(l1)
    

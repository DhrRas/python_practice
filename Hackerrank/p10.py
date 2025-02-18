''' In python, a string of text can be aligned left, right and center.
different methods are used to center, right and left adjust the text according to the need.
'''

if __name__ == '__main__':
    thickvalue = int(input())
    width = thickvalue

for i in range(1, thickvalue+1):
    for j in range(i):
        if i % 2 == 1:
            print('H'*i)
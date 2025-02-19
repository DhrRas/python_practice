'''In Python, a string of text can be aligned left, right and center.'''
# width = 20
# print(input().ljust(width,'-'))
# print(input().center(width,'-'))
# print(input().rjust(width, '-'))

if __name__ == '__main__':

    thickvalue = int(input())

    for i in range(1, thickvalue):
        if i % 2 == 1:
            print('H'.rjust(thickvalue,' '))
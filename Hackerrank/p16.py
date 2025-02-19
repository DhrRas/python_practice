''' Given an integer, n, print the following values for 
each integer i from 1 to n: 
1. Decimal 
2. Octal 
3. Hexadecimal (capitalized)
4. Binary '''

def print_formatted(number):
    for i in range(1,number+1):

        octal_value = '{0:o}'.format(i)

        hex_value = '{0:X}'.format(i)

        binary_value = '{0:b}'.format(i)

        print(f"{i:2}  {octal_value:2}  {hex_value:2}  {binary_value:3}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


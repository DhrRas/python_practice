''' Given an integer, n, print the following values for 
each integer i from 1 to n: 
1. Decimal 
2. Octal 
3. Hexadecimal (capitalized)
4. Binary '''

def print_formatted(number):
    width = bin(number)
    new_width = len(width[2:])
    # print(new_width)
   
    for i in range(1,number+1):    

        octal_value = '{0:o}'.format(i)

        hex_value = '{0:X}'.format(i)

        binary_value = '{0:b}'.format(i)

        print(f"{i:>{new_width}} {octal_value:>{new_width}} {hex_value:>{new_width}} {binary_value:>{new_width}}")
         
   
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


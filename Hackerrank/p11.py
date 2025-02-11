''' A set is an unordered collection of elements without duplciates
entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.'''

def average(array):
    total = 0
    for i in range(len(array)):
        total += array[i]
        result = total / len(array)
        avg = '%.3f'%(result)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
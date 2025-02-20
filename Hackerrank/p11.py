''' A set is an unordered collection of elements without duplciates
entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.'''

def average(array):
    for i in range(n):
        heights = set(array)
        # print(heights)
        new_height = len(heights)
        # print(new_height)
        heights_sum = sum(heights)
        # print(heights_sum)
        avg = heights_sum / new_height
    return avg
    # print(f"{avg:.3f}")

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
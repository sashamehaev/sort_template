import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    arr = sys.stdin.readline().rstrip().split()
    arr = [int(item) for item in arr]
    m = int(sys.stdin.readline().rstrip())
    template = sys.stdin.readline().rstrip().split()
    template = [int(item) for item in template]

    result = []
    template_index = 0
    next_index = 0
    while template_index < m:
        index = 0
        while index < n:
            if arr[index] == template[template_index]:
                result.append(arr[index])
                next_index += 1
            index += 1
        template_index += 1

    insertion_arr = []
    for item in arr:
        if item not in template:
            insertion_arr.append(item)
    for i in range(1, len(insertion_arr)):
        current = insertion_arr[i]
        prev = i - 1
        while prev >= 0 and insertion_arr[prev] > current:
            insertion_arr[prev + 1] = insertion_arr[prev]
            prev -= 1
        insertion_arr[prev + 1] = current
    result += insertion_arr
    res_str = ''
    for item in result:
        res_str += str(item) + ' '
    print(res_str)


if __name__ == '__main__':
    main()

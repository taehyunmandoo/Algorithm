array = [5, 7, 9, 0, 3, 1, 6, 2 ,4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    left, right = list(), list()
    pivot = array[0]
    
    for index in range(1, len(array)):
        if pivot > array[index]:
            left.append(array[index])
        else:
            right.append(array[index])
    
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))
            
def find_max_index(arr):
    max_index = 0
    for i in range(len(arr)):
        if arr[max_index] < arr[i]: # 더 큰 값을 찾은 경우
            max_index = i
    return max_index

data = [7, 1, 5, 9, 3, 2, 4]
max_index = find_max_index(data)
print(max_index)
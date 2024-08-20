def merge_sort(data):
    if len(data) <= 1:
        return data
    
    # 리스트를 중간을 기준으로 두 부분으로 나눔
    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]
    
    # 각각의 부분을 재귀적으로 정렬
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # 두 개의 정렬된 리스트를 합병
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_list = []
    i = j = 0
    
    # 두 리스트를 하나의 정렬된 리스트로 합침
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # 남아있는 요소들을 추가
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# 예제 데이터
data_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(data_list)
print(f"Original list: {data_list}")
print(f"Sorted list: {sorted_list}")
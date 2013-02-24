'''merge sort'''


def merge(left_l, right_l):
    result = []
    i, j = 0 ,0
    while i < len(left_l) and j < len(right_l):
        if left_l[i] <= right_l[j]:
            result.append(left_l[i])
            i += 1
        else:
            result.append(right_l[j])
            j += 1
    result += left_l[i:]
    result += right_l[j:]
    return result
                        

def merge_sort(slist):
    if len(slist) <= 1:
        return slist
    left = merge_sort(slist[0:len(slist)/2])
    right = merge_sort(slist[len(slist)/2:])
    return merge(left, right)
        
print merge_sort([3, 4, 8, 0, 6, 7, 4, 2, 1, 9, 4, 5])

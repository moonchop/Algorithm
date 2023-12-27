array=[3,1,6,2,4,7,10,9]

def quick_sort(array):
    if len(array) <=1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <=pivot]
    right_side = [x for x in tail if x >pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
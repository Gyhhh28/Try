def binary_search(lst, target):
    lef = 0
    rig = len(lst)-1
    while lef <= rig:
        mid = (lef+rig)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            lef = mid +1
        else:
            rig = mid +1
    return None
A = binary_search([1,3,4,5],4)
print(A)

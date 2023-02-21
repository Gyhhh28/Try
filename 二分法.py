def binary_search(lst, target):
    lef = 0
    rig = len(lst)-1 #如果是len（lst） 这个值是大于列表序列的最大值的 因为从0开始 所以取不到 开区间
    while lef <= rig: #如果在len不减一的情况下还写等于，那就是取一个不在列表里的值 怎么可能 溢出了
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

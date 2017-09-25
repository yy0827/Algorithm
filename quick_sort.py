def quick_sort(nums, start, end):
    flag = nums[start]
    low = start
    high = end

    if start >= end:
        return
    while low < high:
        while low < high and nums[high] >= flag:
            high -= 1
        nums[low] = nums[high]
        while low < high and nums[low] < flag:
            low += 1
        nums[high] = nums[low]
    nums[low] = flag

    quick_sort(nums, start, low - 1)
    quick_sort(nums, low + 1, end)
    return nums


list = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
print(quick_sort(list, 0, len(list) - 1))

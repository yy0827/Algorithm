# coding:utf-8
# 重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
# 走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
# 较大元素会慢慢浮到数列最右端

def bubble_sort(nums):
    count = len(nums)
    for i in range(count):
        # i 代表第i次循环，j代表循环体
        for j in range(count - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


list = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
print(bubble_sort(list))

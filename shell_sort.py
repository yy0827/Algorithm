# coding:utf-8
# 希尔排序的实质就是分组插入排序，该方法又称缩小增量排序，因DL．Shell于1959年提出而得名。
# 希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。希尔排序是非稳定排序算法。
# 希尔排序是基于插入排序的以下两点性质而提出改进方法的：
# 插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
# 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位

def shell_sort(nums):
    count = len(nums)
    gap = count // 2
    while gap > 0:
        for i in range(gap, count):
            while i >= gap and nums[i] < nums[i - gap]:
                nums[i], nums[i - gap] = nums[i - gap], nums[i]
                i -= gap
        gap = gap // 2

    return nums


list = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]

print(shell_sort(list))

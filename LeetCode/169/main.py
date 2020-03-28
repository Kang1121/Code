import numpy as np


nums = [-1,-1,2147483647]
l1 = len(nums)


def cut(nums, x, y):
    if y - x == 1:
        return nums[x]
    else:
        m = int(np.ceil(x + (y - x) / 2))
        mode_l = cut(nums, x, m)
        mode_r = cut(nums, m, y)
        if mode_r == mode_l:
            return mode_l
        if mode_l == -1.1:
            return mode_r
        if mode_r == -1.1:
            return mode_l
        l = 0
        r = 0
        for i in range(x, y):
            if nums[i] == mode_l:
                l += 1
            if nums[i] == mode_r:
                r += 1
        if l == r:
            return -1.1
        elif l > r:
            return mode_l
        else:
            return mode_r


d = cut(nums, 0, len(nums))
print(d)

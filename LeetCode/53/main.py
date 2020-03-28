import numpy as np



def maxs(nums, x, y):
    if y - x == 1:
        return nums[x]
    else:
        s = 0
        t = 0
        L = -111110
        R = -111110
        m = np.math.ceil(x + (y - x) / 2)
        max_lr = max(maxs(nums, x, m), maxs(nums, m, y))
        for i in range(m - 1, x - 1, -1):
            s += nums[i]
            L = max(L, s)
        for i in range(m, y):
            t += nums[i]
            R = max(R, t)
        return max(max_lr, L+R)

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
l1 = len(nums)
# print(l1)

t = maxs(nums, 0, l1)
print(t)

import numpy as np


s = [1,3,5,6]


def cut(nums, x, y, t):
    if y - x == 1:
        if t <= nums[x]:
            return x
        else:
            return y
    else:
        global a
        m = int(np.ceil(x + (y - x) / 2))
        if t > nums[m]:
            a = cut(nums, m, y, t)
        else:
            a = cut(nums, x, m, t)

        return a


d = cut(s, 0, len(s), 0)
print(d)

import numpy as np


a = np.zeros((70))
str = "abccccdd"
for i in range(len(str)):
    a[ord(str[i]) - 65] += 1
#print(a)
flag = False
for i in range(70):
    if a[i] % 2 != 0:
        a[i] -= 1
        flag = True
if flag == False:
    return sum(a)
else:
    return sum(a) + 1
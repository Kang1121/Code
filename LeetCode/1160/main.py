import numpy as np

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"

a = np.zeros((26))
b = np.zeros((26))
out = 0
l1 = len(chars)
for i in range(l1):
    a[ord(chars[i]) - 97] += 1

for i in range(len(words)):
    b = a.copy()
    for j in range(len(words[i])):
        b[ord(words[i][j]) - 97] -= 1

    flag = True
    for k in range(26):
        if b[k] < 0:
            flag = False
    if flag:
        out += len(words[i])
print(out)

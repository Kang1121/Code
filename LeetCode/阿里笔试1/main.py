import sys


def search(list, i, j):
    while i < len(list) - 1:
        m[i] = search(list1, i+1, 0)

n = int(sys.stdin.readline().strip())
ans = 0
list1 = []
for i in range(3):
        # 读取每一行
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    list1.append(values)
print(list1)
m = 0


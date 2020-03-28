
def find(a, pos):
    b = pos[a]
    if b == -1:
        pos[a] = a
        return a
    else:
        b = find(b + 1, pos)
        pos[a] = b
        return b


A = [3, 2, 1, 2, 1, 7]
pos = [-1 for i in range(10000)]
move = 0
for i in range(len(A)):
    b = find(A[i], pos)
    move += b - A[i]
print(move)


list = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]


cout = 0
for i in range(8):
    for j in range(8):
        if list[i][j] == 'R':
            m = i
            n = j
            break

for i in range(m+1, 8):
    if list[i][n] == 'B':
        break
    if list[i][n] == 'p':
        cout += 1
        break
for i in range(m-1, -1, -1):
    if list[i][n] == 'B':
        break
    if list[i][n] == 'p':
        cout += 1
        break
for i in range(n-1, -1, -1):
    if list[m][i] == 'B':
        break
    if list[m][i] == 'p':
        cout += 1
        break
for i in range(n+1, 8):
    if list[m][i] == 'B':
        break
    if list[m][i] == 'p':
        cout += 1
        break
print(cout)
a = []
arr = []
for _ in range(6):
    arr.append(list(map(int , input().rstrip().split())))
for i in range(0,4):
    for j in range(0,4):
        s = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
        a.append(s)
print(max(a)) 
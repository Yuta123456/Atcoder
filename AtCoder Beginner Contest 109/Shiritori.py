n = int(input())
w = []
for i in range(n):
    w.append(input())
for i in range(n):
    for j in range(i+1,n):
        if w[i] == w[j]:
            print("No")
            exit()
for i in range(n - 1):
    if w[i][-1] != w[i + 1][0]:
        print("No")
        exit()
print("Yes")

n  = int(input())
h =  list(map(int, input().split()))
h.reverse()
for i in range(n - 1):
    if h[i] < h[i + 1] - 1:
        print("No")
        exit()
    if h[i] == h[i + 1] - 1:
        h[i + 1] -= 1
print("Yes")

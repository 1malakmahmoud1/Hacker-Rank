from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    blocks = deque(map(int, input().split()))

    last_picked = float('inf')
    possible = True

    while blocks:
        if blocks[0] >= blocks[-1]:
            current = blocks.popleft()
        else:
            current = blocks.pop()

        if current > last_picked:
            possible = False
            break

        last_picked = current

    if possible:
        print("Yes")
    else:
        print("No")
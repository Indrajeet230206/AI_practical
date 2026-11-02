from collections import deque

n = 3
start = (0, 0, 0)
goal = (2, 2, 2)

q = deque([(start, [start])])
visited = {start}

while q:
    state, path = q.popleft()

    if state == goal:
        print("Path:", path)
        print("Steps:", len(path) - 1)
        break

    for i in range(n):
        for j in range(3):
            if i != j:
                new = list(state)
                new[i] = j
                new = tuple(new)

                if new not in visited:
                    visited.add(new)
                    q.append((new, path + [new]))

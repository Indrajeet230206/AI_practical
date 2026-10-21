import heapq

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Count misplaced tiles
def h(state):
    count = 0
    for i in range(9):
        if state[i] != goal[i] and state[i] != 0:
            count += 1
    return count

# Print puzzle
def show(state):
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()

# Priority queue
q = [(h(start), 0, start)]
visited = [start]

while q:
    f, g, state = heapq.heappop(q)

    show(state)

    if state == goal:
        print("Goal reached in", g, "moves")
        break

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    # Move up, down, left, right
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in moves:
        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c

            new_state = list(state)
            new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.append(new_state)

                g_new = g + 1
                f_new = g_new + h(new_state)

                heapq.heappush(q, (f_new, g_new, new_state))

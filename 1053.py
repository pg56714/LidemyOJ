# 走迷宮
# https://oj.lidemy.com/problem/1053


# 同1019，但是不只一條路。
# 起點在左上角，終點在右下角，從起點走到終點最少需要幾步（保證可以從起點走到終點）。
# 接下來 H 行每一行都有 W 個字元，代表著迷宮的圖案
# . 是可以走的道路，# 是牆壁

# 請輸出從左上角走到右下角，最少需要幾步

# Sample Input 1
# 3 3
# .#.
# ...
# #..

# Sample Output 1
# 4


from collections import deque


def bfs(maze, height, width):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0, 0)])  # 從 (0, 0) 開始，步數為 0
    visited = set()
    visited.add((0, 0))

    while queue:
        col, row, steps = queue.popleft()

        if row == height - 1 and col == width - 1:
            return steps

        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy

            if (
                0 <= new_row < height
                and 0 <= new_col < width
                and (new_col, new_row) not in visited
                and maze[new_row][new_col] == "."
            ):
                visited.add((new_col, new_row))
                queue.append((new_col, new_row, steps + 1))
                # print(queue)

    return -1  # 如果找不到路徑，返回 -1


height, width = map(int, input().split())
maze = [input().strip() for _ in range(height)]

result = bfs(maze, height, width)
print(result)

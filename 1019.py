# 題目：一條路走到黑
# https://oj.lidemy.com/problem/1019

# 迷宮的長相可以用底下的圖形來描述（# 是牆壁，. 是道路）：
# ...##
# ##.##
# ##...
# ####.
# ####.

# 整個迷宮的大小為 W * H，W 是寬度，H 是高度。起點永遠為左上角，終點永遠為右下角。
# 若是把左上角標記為 x=1, y=1，右下角標記為 x=W, y=H，從 (1,1) 出發，這個迷宮要走到終點的路徑就是：
# (2,1)
# (3,1)
# (3,2)
# (3,3)
# (4,3)
# (5,3)
# (5,4)
# (5,5)
# 一共需要走 8 步，才能從起點走到終點。
# 計算從起點走到終點一共要走多少步。

# 輸入的第一行為兩個用空格分開的正整數 W 與 H，代表著地圖的寬度與高度
# 接下來的 H 行每一行都會有 W 個字元，代表著迷宮的每一行。# 代表牆壁，. 代表道路，只有道路可以通行
# 每一個迷宮都保證只會有唯一一種走法

# 起點永遠在左上角，終點永遠在右下角
# 請你輸出從起點走到終點需要多少步

# Sample Input 1
# 6 5
# .#####
# .#####
# .#####
# .#####
# ......

# Sample Output 1
# 9

# def bfs(maze, width, height):
#     # # 定義四個可能的移動方向
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#     # 初始化 BFS 隊列
#     queue = [(0, 0, 0)]  # (col, row, steps)，從0開始計數
#     visited = {(0, 0)}

#     while queue:
#         col, row, steps = queue.pop(0)

#         # 如果到達終點，返回步數
#         if row == height - 1 and col == width - 1:
#             return steps

#         # 檢查四個方向
#         for dx, dy in directions:
#             new_row, new_col = row + dx, col + dy

#             if (
#                 0 <= new_row < height
#                 and 0 <= new_col < width
#                 and (new_col, new_row) not in visited
#                 and maze[new_row][new_col] == "."
#             ):
#                 # print(new_row)
#                 visited.add((new_col, new_row))
#                 queue.append((new_col, new_row, steps + 1))
#                 # print(visited)
#                 # print(queue)

#     return -1  # 若無法到達終點，返回 -1（不會發生）


def simulate_path(maze, width, height):
    # 定義四個可能的移動方向
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右

    x, y = 0, 0  # 起始位置
    steps = 0  # 計步器
    visited = set()  # 記錄訪問過的點，避免回頭
    visited.add((x, y))

    while (x, y) != (width - 1, height - 1):  # 直到到達終點
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < width
                and 0 <= ny < height
                and maze[ny][nx] == "."
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))  # 標記為已訪問
                x, y = nx, ny  # 移動到新位置
                steps += 1
                # print(x, y, steps)
                break  # 找到唯一可行路徑，直接跳出循環

    return steps


width, height = map(int, input().split())
maze = [input().strip() for _ in range(height)]
# print(maze)

result = simulate_path(maze, width, height)
# result = bfs(maze, width, height)
print(result)

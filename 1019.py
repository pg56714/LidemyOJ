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


def bfs(maze, w, h):
    # # 定義四個可能的移動方向
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 初始化 BFS 隊列
    queue = [(0, 0, 1)]  # (x, y, steps)，從0開始計數
    visited = {(0, 0)}

    while queue:
        x, y, steps = queue.pop(0)

        # 如果到達終點，返回步數並減一
        if x == h - 1 and y == w - 1:
            return steps - 1

        # 檢查四個方向
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < h
                and 0 <= ny < w
                and (nx, ny) not in visited
                and maze[nx][ny] == "."
            ):
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1  # 若無法到達終點，返回 -1（理論上不會發生）


w, h = map(int, input().split())
maze = [input().strip() for _ in range(h)]
# print(maze)

result = bfs(maze, w, h)
print(result)

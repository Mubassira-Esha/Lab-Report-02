def iddfs(maze, start, target, max_depth):
    def dls(node, depth, path):
        if depth == 0 and node == target:
            return True, path + [node]
        if depth > 0:
            x, y = node
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                    if (nx, ny) not in path:
                        found, result_path = dls((nx, ny), depth - 1, path + [node])
                        if found:
                            return True, result_path
        return False, []

    for depth in range(max_depth + 1):
        found, path = dls(start, depth, [])
        if found:
            return f"Path found at depth {depth} using IDDFS", path
    return f"Path not found at max depth {max_depth} using IDDFS", []


def main():
    rows, cols = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(rows)]

    start_line = input().strip()
    assert start_line.startswith("Start:")
    start = tuple(map(int, start_line.split()[1:]))

    target_line = input().strip()
    assert target_line.startswith("Target:")
    target = tuple(map(int, target_line.split()[1:]))

    max_depth = 6

    result, path = iddfs(maze, start, target, max_depth)

    print(result)
    if path:
        print("Traversal Order:", path)


if __name__ == "__main__":
    main()

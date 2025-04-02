You are given a 2D grid representing a maze, where each cell is either an empty space (0) or a wall (1). Your task is to implement a Python program that uses Iterative Deepening Depth-First Search (IDDFS) to determine whether a valid path exists from a given start cell to a specified target cell. You may move up, down, left, or right to adjacent empty cells, but you cannot pass through walls, and each cell may be visited only once during a single path exploration.

Case#1Input:
4 4
0 0 1 0
1 0 1 0
0 0 0 0
1 1 0 1
Start: 0 0
Target: 2 3

Case#1Output:
Path found at depth 5 using IDDFS
Traversal Order: [(0,0), (1,0), (1,1), (0,1), (2,1), (2,2), (2,3)]

Output:
![Output](Screen/Labreport02(Case01).png)

Case#2Input:
3 3
0 1 0
0 1 0
0 1 0
Start: 0 0
Target: 2 2

Case#2Output:
Path not found at max depth 6 using IDDFS

Output:

![Output](Screen/Labreport02(Case02).png)

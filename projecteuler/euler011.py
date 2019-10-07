#!/usr/bin/python3

import sys

def left_right(grid: list) -> int:
    maxi = 0
    for i in range(20):
        for j in range(17):
            num = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            if maxi < num:
                maxi = num

    return maxi

def up_down(grid: list) -> int:
    maxi = 0
    for i in range(17):
        for j in range(20):
            num = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            if maxi < num:
                maxi = num

    return maxi

def diag_back(grid: list) -> int:
    maxi = 0
    for i in range(17):
        for j in range(17):
            num = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            if maxi < num:
                maxi = num

    return maxi

def diag_front(grid: list) -> int:
    maxi = 0
    for i in range(20):
        for j in range(3, 17):
            num = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
            if maxi < num:
                maxi = num

    return maxi

grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
    
m1 = up_down(grid)
m2 = left_right(grid)
m3 = diag_back(grid)
m4 = diag_front(grid)

tot = max(m1, m2, m3, m4)
print(tot)

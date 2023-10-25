#!/usr/bin/python3
"""This module contains a function
that calculates the perimeter of
a given grid"""


def island_perimeter(grid):
    """This function calculates
    perimeter of a grid"""
    perimeter = 0
    row = len(grid)
    if grid != []:
        column = len(grid[0])

    for a in range(row):
        for b in range(column):
            if grid[a][b] == 1:
                if (a - 1) == -1 or grid[a - 1][b] == 0:
                    perimeter += 1
                if (a + 1) == row or grid[a + 1][b] == 0:
                    perimeter += 1
                if (b - 1) == -1 or grid[a][b - 1] == 0:
                    perimeter += 1
                if (b + 1) == column or grid[a][b + 1] == 0:
                    perimeter += 1

    return perimeter

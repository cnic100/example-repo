def count_adjacent_mines(grid, row, col):
    """Count mines surrounding one cell."""
    mine_count = 0

    # Check the row above, the current row, and the row below.
    for row_offset in (-1, 0, 1):
        for col_offset in (-1, 0, 1):

            # Skip the current cell itself.
            if row_offset == 0 and col_offset == 0:
                continue

            neighbor_row = row + row_offset
            neighbor_col = col + col_offset

            # Only check positions within the grid.
            if (
                0 <= neighbor_row < len(grid)
                and 0 <= neighbor_col < len(grid[neighbor_row])
            ):
                if grid[neighbor_row][neighbor_col] == "#":
                    mine_count += 1

    return mine_count


def minesweeper(grid):
    """Return a new grid with mine counts replacing dashes."""
    result = []

    for row_index, row in enumerate(grid):
        result_row = []

        for col_index, cell in enumerate(row):
            if cell == "#":
                result_row.append("#")
            else:
                count = count_adjacent_mines(
                    grid, row_index, col_index
                )
                result_row.append(count)

        result.append(result_row)

    return result


# Example input.
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Calculate and display the completed grid.
completed_grid = minesweeper(grid)

for row in completed_grid:
    print(row)

# List to iterate through.
values = ["a", "b", "c"]

print("Below is the output generated:")

# Start counting at 0, the index of the first item.
for count, value in enumerate(values, start=0):
    print(f"Index {count} contains the value {value}")
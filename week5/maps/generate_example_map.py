#!/usr/bin/env python3
"""Generate a small example indoor map for offline pipeline testing."""

WIDTH = 200
HEIGHT = 200
FREE = 254
UNKNOWN = 205
OCCUPIED = 0


def build_map():
    grid = [[FREE] * WIDTH for _ in range(HEIGHT)]

    for x in range(WIDTH):
        grid[0][x] = OCCUPIED
        grid[HEIGHT - 1][x] = OCCUPIED
    for y in range(HEIGHT):
        grid[y][0] = OCCUPIED
        grid[y][WIDTH - 1] = OCCUPIED

    # Horizontal wall with a door gap.
    for x in range(40, 95):
        grid[70][x] = OCCUPIED
    for x in range(105, 165):
        grid[70][x] = OCCUPIED

    # Vertical wall with a passage.
    for y in range(30, 55):
        grid[y][95] = OCCUPIED
    for y in range(85, 170):
        grid[y][95] = OCCUPIED

    # Small room obstacles.
    for x in range(145, 180):
        for y in range(120, 140):
            if (x - 145) % 12 < 8 and (y - 120) % 12 < 8:
                grid[y][x] = OCCUPIED

    # Unknown band near the bottom-right as an intentional quality issue.
    for x in range(170, 190):
        for y in range(165, 185):
            if (x + y) % 7 == 0:
                grid[y][x] = UNKNOWN

    return grid


def write_pgm(path, grid):
    with open(path, 'w', encoding='ascii') as handle:
        handle.write('P2\n')
        handle.write(f'{len(grid[0])} {len(grid)}\n')
        handle.write('255\n')
        for row in grid:
            handle.write(' '.join(str(value) for value in row) + '\n')


def main():
    write_pgm('map.pgm', build_map())


if __name__ == '__main__':
    main()

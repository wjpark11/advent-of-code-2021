from typing import List

with open("day9_input.txt", "rt") as f:
    inputs = f.readlines()
    heightmap = [list(map(int,list(line.strip()))) for line in inputs]

WIDTH, HEIGHT = len(heightmap[0]), len(heightmap)

risk_level_sum = 0
low_points = []
for i in range(HEIGHT):
    for j in range(WIDTH):
        surrounding = []
        if i != 0:
            surrounding.append(heightmap[i-1][j])
        try:
            surrounding.append(heightmap[i+1][j])
        except IndexError:
            pass
        if j != 0:
            surrounding.append(heightmap[i][j-1])
        try:
            surrounding.append(heightmap[i][j+1])
        except IndexError:
            pass

        if min(surrounding) > heightmap[i][j]:
            risk_level_sum += heightmap[i][j] + 1
            low_points.append((i,j))

print(f"risk_level_sum: {risk_level_sum}")


def find_new_basin_elements(basin: list, i: int, j: int) -> List[tuple]:
    new_basin = []
    h = heightmap[i][j]
    if i != 0:
        if heightmap[i - 1][j] > h \
            and (i - 1, j) not in basin \
            and heightmap[i - 1][j] != 9:
            new_basin.append((i - 1, j))
    if i != HEIGHT -1:
        if heightmap[i + 1][j] > h \
            and (i + 1, j) not in basin \
            and heightmap[i + 1][j] != 9:
            new_basin.append((i + 1, j))
    if j != 0:
        if heightmap[i][j - 1] > h \
            and (i, j - 1) not in basin \
            and heightmap[i][j - 1] != 9:
            new_basin.append((i, j - 1))
    if j != WIDTH - 1:
        if heightmap[i][j + 1] > h \
            and (i, j + 1) not in basin \
            and heightmap[i][j + 1] != 9:
            new_basin.append((i, j + 1))
    return new_basin


def get_basin_size(i: int, j: int) -> int:
    basin_list = [(i, j)]
    while True:
        new_basin_list = []
        for coordinate in basin_list:
            new_basins = find_new_basin_elements(
                basin_list, coordinate[0], coordinate[1])
            new_basin_list += new_basins
        basin_list += new_basin_list
        basin_list = list(set(basin_list))

        if new_basin_list == []:
            break
    return len(basin_list)

basin_size_list = []
for point in low_points:
    basin_size_list.append(get_basin_size(point[0], point[1]))

basin_size_list.sort(reverse=True)
product = basin_size_list[0] * basin_size_list[1] * basin_size_list[2]
print(f"product of sizes of the three largest basins: {product}")

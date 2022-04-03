# answer for day5_2
# for day5_1, delete else clause in get_points_set method of class Line

with open("day5_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

lines = [(list(map(int,item[0].split(','))), list(map(int,item[1].split(',')))) for item in [input.split('->') for input in inputs]]

class Line:
    def __init__(self,point1,point2):
        self.x1 = point1[0]
        self.y1 = point1[1]
        self.x2 = point2[0]
        self.y2 = point2[1]

    def get_points_set(self):
        points = set()
        if self.x1 == self.x2:
            for y in range(min(self.y1,self.y2), max(self.y1,self.y2)+1):
                points.add((self.x1,y))
        elif self.y1 == self.y2:
            for x in range(min(self.x1,self.x2), max(self.x1,self.x2)+1):
                points.add((x,self.y1))
        else:
            increment_x = 1 if self.x1 < self.x2 else -1
            increment_y = 1 if self.y1 < self.y2 else -1
            x, y = self.x1, self.y1
            while x != self.x2:
                points.add((x, y))
                x += increment_x
                y += increment_y
            points.add((x,y))

        return points


lines = [Line(item[0],item[1]) for item in lines]

point_sets_in_lines = [line.get_points_set() for line in lines]

overlap_points = set()

for i in range(len(lines)-1):
    point_set = point_sets_in_lines[i]
    point_sets_after_point_set = point_sets_in_lines[i+1:]
    for after_set in point_sets_after_point_set:
        overlap_points.update(point_set&after_set)
        

print(len(overlap_points))


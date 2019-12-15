from shapely.geometry import LineString, Point

def get_end_point(start_point, str):
    end_point = start_point
    if str[0] == 'R':
        end_point = Point(int(str[1:]) + start_point.x, start_point.y)
    if str[0] == 'L':
        end_point = Point(start_point.x - int(str[1:]), start_point.y)
    if str[0] == 'U':
        end_point = Point(start_point.x, start_point.y + int(str[1:]))
    if str[0] == 'D':
        end_point = Point(start_point.x, start_point.y - int(str[1:]))
    return end_point


def get_wire(directions):
    wire=[]
    last_point=Point(0,0)
    wire.append(last_point)

    for direction in directions:
        new_point = get_end_point(last_point, direction)
        last_point = new_point
        wire.append(new_point)

    wire = LineString(wire)
    return wire


def get_taxicab_metric(p1,p2):
    d = abs(p2.x -p1.x) + abs(p2.y - p1.y)
    return d


def read_wire_from_file(filename, array):
    with open(filename) as my_file:
        for line in my_file:
            array.append(line.rstrip())

array1 = []
read_wire_from_file('day3_wire1.txt', array1)
array2 = []
read_wire_from_file('day3_wire2.txt', array2)


# wire1 = get_wire(["R8","U5","L5","D3"])
# wire1 = get_wire(["R75","D30","R83","U83","L12","D49","R71","U7","L72"])
# wire1 = get_wire(["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"])
wire1 = get_wire(array1)
# print(wire1)
# wire2 = get_wire(["U7","R6","D4","L4"])
# wire2 = get_wire(["U62","R66","U55","R34","D71","R55","D58","R83"])
# wire2 = get_wire(["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"])
wire2 = get_wire(array2)
# print(wire2)

intersection = wire1.intersection(wire2)

distances=[]

# Solution
if not intersection.is_empty:
    for point in intersection:
        if point == Point(0,0) or point.geom_type != 'Point':
            pass
        else:
            l = get_taxicab_metric(Point(0,0), point)
            distances.append(l)

print("Result: {}".format(min(distances)))


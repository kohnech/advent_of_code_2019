from shapely.geometry import LineString, Point
import day3


array1 = []
day3.read_wire_from_file('day3_wire1.txt', array1)
array2 = []
day3.read_wire_from_file('day3_wire2.txt', array2)

wire1 = day3.get_wire(array1)
wire2 = day3.get_wire(array2)

intersection = wire1.intersection(wire2)


def get_new_wire_to_intersection(inwire, intersection):
    array=[]
    first=True
    for point in inwire.coords:
        array.append(Point(point))
        if first:
            first = False
            continue
        wire = LineString(array)
        inter = wire.intersection(intersection)
        
        if not inter.is_empty and Point(point) != Point(0,0): 
            new_points = array[:-1]
            new_points.append(intersection)
            wire = LineString(new_points)
            return wire
    return None

# Solution
steps1=[]
steps2=[]

for point in intersection:
    if point != Point(0,0):
        new_line = get_new_wire_to_intersection(wire1, point)
        if new_line != None:
            steps1.append(new_line.length)


for point in intersection:
    if point != Point(0,0):
        new_line = get_new_wire_to_intersection(wire2, point)
        if new_line != None:
            steps2.append(new_line.length)

total_steps=[]
for i in range(len(steps1)):
    total_step = steps1[i] + steps2[i]
    total_steps.append(total_step)

print("Result shortest steps: {}".format(min(total_steps)))

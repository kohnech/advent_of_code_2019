import math

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

array = []
with open('day1_input.txt') as my_file:
    for line in my_file:
        array.append(line.rstrip())

def get_fuel(mass):
    mass = mass/3
    fuel = round_down(mass, 0) - 2
    if (fuel==0) or (fuel < 0):
        return 0
    else:
        return fuel + get_fuel(fuel)
    return 

test = get_fuel(1969)
print(test)

total_fuel = 0
for mass in array:
    fuel = get_fuel(int(mass))
    total_fuel += fuel

print(total_fuel)
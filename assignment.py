#!/usr/bin/python3
# Assumption is that the input list is sorted.
input_list = [(1,5,10),(4,6,8),(10,15,10),(11,12,8)]
#input_list = [(1,10,4),(1,8,6),(1,6,8)]
#input_list = [(0,6,2),(5,10,8),(7,8,12)]
output_list = [(1,10),(5,8),(6,0),(10,10),(15,0)]
coordinates = []
co_2 = []
for each in input_list:
    coordinates.extend([(each[0], 0), (each[1], 0), (each[0], each[2]), (each[1], each[2])])
coordinates = set(coordinates)
l = len(input_list)
intersections = []
for i in range(0, l-1):
    for j in range(i+1, l):
        # comparing x axes
        if input_list[j][0] < input_list[i][1]:
            coordinates.discard((input_list[j][0], 0))
            # comparing y axes
            if input_list[j][2] < input_list[i][2]:
                coordinates.discard((input_list[j][0], input_list[j][2]))
            else:
                coordinates.add((input_list[j][0], input_list[i][2]))
            
            if input_list[j][1] < input_list[i][1]:
                coordinates.discard((input_list[j][1], 0))
                coordinates.discard((input_list[j][1], input_list[j][2]))
                coordinates.discard((input_list[i][1], input_list[i][2]))
                # comparing y axes
                if input_list[j][2] < input_list[i][2]:
                    coordinates.discard((input_list[j][1], input_list[j][2]))
                else:
                    coordinates.add((input_list[j][1], input_list[i][2]))
            else:
                coordinates.discard((input_list[i][1], 0))
                coordinates.discard((input_list[j][1], input_list[j][2]))
                if input_list[j][2] > input_list[i][2]:
                    coordinates.discard((input_list[i][1], input_list[i][2]))
                elif input_list[j][2] < input_list[i][2]:
                    coordinates.add((input_list[i][1], input_list[j][2]))
a = {}
for x in coordinates:
    if x[0] not in a.keys():
        a[x[0]] = []
    a[x[0]].append(x[1])
final = []
# This current_val is being used in the decision whether the next data points are rising or falling
current_val = 0
for i, val in sorted(a.items()):
    val.append(current_val)
    max_cond = max(*val)
    final.append((i, max_cond))
    
print(final)

planets = [
("Mercury", 2440, 5.43, 0.395),
("Venus", 6052, 5.24, 0.723),
("Earth", 6378, 5.52, 1.000),
("Jupiter", 71492, 0.69, 9.551)
]

size = lambda planet: planet[1]
density = lambda planet: planet[2]
planets.sort(key=density)
print planets
# [('Jupiter', 71492, 0.69, 9.551), ('Venus', 6052, 5.24, 0.723),
 # ('Mercury', 2440, 5.43, 0.395), ('Earth', 6378, 5.52, 1.0)]

# Tuples
data = (7,2,5,6,1,3,9,10,4,8)
print sorted(data)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print sorted("Alphabetical")
# ['A', 'a', 'a', 'b', 'c', 'e', 'h', 'i', 'l', 'l', 'p', 't']

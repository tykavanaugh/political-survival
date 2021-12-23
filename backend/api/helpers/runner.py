from MapGenerator import generate,display_terrain
world_size = 30

world = generate(world_size,world_size,4,{".": 1, " ": 1})
mountains = generate(world_size,world_size,6,{"X": .7, " ": 1})
woodlands = generate(world_size,world_size,6,{"X": .7, " ": 1})
cities = generate(world_size,world_size,0,{"#": .05, " ": 1})

display_terrain(woodlands)

for i in range(0,world_size):
    for j in range(0,world_size):
        if mountains[i][j] != " ":
            if world[i][j] != " ":
                world[i][j] = mountains[i][j]
            else:
                world[i][j] = "."


for i in range(0,world_size):
    for j in range(0,world_size):
        if world[i][j] != " ":
            if cities[i][j] != " ":
                world[i][j] = cities[i][j]


display_terrain(world)

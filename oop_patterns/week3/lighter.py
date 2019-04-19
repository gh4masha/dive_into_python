class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()


class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):

        self.adaptee.set_dim((len(grid[0]), len(grid)))

        lights = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    lights.append((j, i))
        obstacles = []
        for ii in range(len(grid)):
            for jj in range(len(grid[0])):
                if grid[ii][jj] == -1:
                    obstacles.append((jj, ii))

        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        generatedmap = self.adaptee.generate_lights()
        # result = [[0 for iii in range(len(generatedmap))] for _ in range(len(generatedmap[0]))]
        # for i in range(len(generatedmap)):
        #     for j in range(len(generatedmap[0])):
        #         result[j][i] = generatedmap[i][j]
        return generatedmap


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(3)]
        self.map[1][15] = 1  # Источники света
        self.map[2][15] = -1  # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)


if __name__ == '__main__':
    system = System()
    light = Light((len(system.map[0]), len(system.map)))
    adapter = MappingAdapter(light)
    system.get_lightening(adapter)
    for i in range(len(system.lightmap)):
        print(system.lightmap[i])

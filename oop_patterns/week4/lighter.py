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
        pass

    def lighten(self, grid):
        light = Light((len(grid), len(grid[0])))
        light.set_dim((len(grid), len(grid[0])))

        lights=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    lights.append((i, j))
        obstacles=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == -1:
                    obstacles.append((i, j))

        light.set_lights(lights)
        light.set_obstacles(obstacles)
        return light.generate_lights()



class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1  # Источники света
        self.map[5][2] = -1  # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)



if __name__=='__main__':
    system = System()
    light = Light((len(system.map[0]), len(system.map)))
    adapter = MappingAdapter(light)
    system.get_lightening(adapter)
    for i in range(len(system.lightmap)):
        print(system.lightmap[i])




import random

class World():
    def __init__(self, x_width=50, y_height=50, live_cells=None):
        self.x_width = x_width
        self.y_height = y_height
        self.live_cells = live_cells
        if self.live_cells is None:
            self.live_cells = set()

    def autopopulate(self, numcells = 25):
        if numcells > (self.x_width * self.y_height):
            raise "Cannot overpopulate world"
        self.live_cells = set()
        while len(self.live_cells) != numcells:
            self.addcell(random.randint(0,self.x_width),random.randint(0,self.y_height))

    def addcell(self, x, y):
        check = self.checkpos(x,y)
        if check != True:
            raise WorldBoundariesError(check)
        self.live_cells.add((x, y))

    def clearcell(self, x, y):
        check = self.checkpos(x,y)
        if check != True:
            raise WorldBoundariesError(check)
        self.live_cells.discard((x, y))

    def clearcells(self):
        self.live_cells = set()

    def checkpos(self, x, y):
        if x < 0 or y < 0:
            return "Won't set negative coordinates"
        if x > self.x_width or y > self.y_height:
            return "Cannot set cells outside world"
        return True

    def readcell(self, x, y):
        if x < 0:
            x = x + self.x_width
        if x >= self.x_width:
            x = x - self.x_width
        if y < 0:
            y = y + self.y_height
        if y >= self.y_height:
            y = y - self.y_height
        return (x,y) in self.live_cells

    def countneighbours(self, x, y):
        neighbours = 0
        neighbourcandidates = [
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1)
        ]
        for pos in neighbourcandidates:
            if self.readcell(x + pos[0], y + pos[1]):
                neighbours += 1
        return neighbours

    def generate_new_generation(self):
        deaths = []
        births = []
        for x in range(0, self.x_width):
            for y in range(0, self.y_height):
                neighbours = self.countneighbours(x, y)
                if self.readcell(x,y):
                    if neighbours < 2:
                        deaths.append((x, y))
                    elif neighbours > 3:
                        deaths.append((x,y))
                else:
                    if neighbours == 3:
                        births.append((x,y))
        for death in deaths:
            self.clearcell(death[0], death[1])
        for birth in births:
            self.addcell(birth[0], birth[1])

class WorldBoundariesError(RuntimeError):
    def __init__(self, arg):
        self.args = arg

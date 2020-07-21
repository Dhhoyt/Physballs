class ball:
    def __init__(self, pos: tuple, size, velocity: tuple, radius, color: tuple):
        self.pos = pos
        self.size = size
        self.color = color
        self.thickness = size
        self.velocity = velocity
        self.futurepos = (0, 0)
        self.radius = radius
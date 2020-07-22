

class Ball:
    balls = []

    def __init__(self, pos: tuple, size, velocity: tuple, radius, color: tuple):
        self.pos = pos
        self.size = size
        self.color = color
        self.thickness = size
        self.velocity = velocity
        self.future_pos = (0, 0)
        self.radius = radius


def add_ball(position: tuple, size, velocity: tuple, color):
    nu_velocity = (velocity[0], velocity[1])
    Ball.balls.append(Ball(position, size, nu_velocity, int(size ** 1), color))
    print(position)

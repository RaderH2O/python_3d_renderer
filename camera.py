from dataclasses import dataclass
from math import sin, cos, dist, sqrt
from math_things import collide_lines, distance_of_pointline, sincos_from_tan

@dataclass
class Camera:
    radius: float
    x: float
    y: float
    angle: float

    def __init__(self, radius, angle):
        self.radius = radius
        self.x = radius * cos(angle)
        self.y = radius * sin(angle)
        self.angle = angle
        self.m = 0
        self.sign = -1 if sin(self.angle) > 0 else 1
        self.pp = (0, 0, 0)

    def turn(self, dt, degrees):
        self.angle += degrees * dt

    def update(self):
        self.sign = -1 if sin(self.angle) > 0 else 1
        self.m = -self.radius * cos(self.angle) / (self.radius * (sin(self.angle) if sin(self.angle) != 0 else 0.001))
        self.x = self.radius * cos(self.angle)
        self.y = self.radius * sin(self.angle)

        self.pp = (- 100 * cos(self.angle), - 100 * sin(self.angle))

    def get_normal(self):
        divisor = self.m ** 2 + 1 ** 2
        return (-self.m * self.sign / divisor, self.sign / divisor, 0)
    
    def get_point_position(self, point_position, width, height):
        point_x, point_y, point_z = point_position
        
        # calculates the position of the point in 3D space and translates it to the screen
        # point_x_screen = ((self.m**2)*self.radius*cos(self.angle)-self.m*self.radius*sin(self.angle)+self.m*point_y+point_x)/(self.m**2 + 1)
        # point_y_screen = (-(self.m**2)*self.radius*cos(self.angle)+self.radius*sin(self.angle)+(self.m**2)*point_y+self.m*point_x)/(self.m**2 + 1)
        rel_x, rel_y = collide_lines((self.m, self.x, self.y), (-1/(self.m if self.m != 0 else 0.001), point_x, point_y))
        point_from_plane = distance_of_pointline((point_x, point_y), (self.m, self.x, self.y))
        total_distance = distance_of_pointline((self.pp[0], self.pp[1]), (self.m, self.x, self.y))
        relative_x = total_distance - point_from_plane
        _, rel_z = collide_lines(((point_z)/(relative_x if relative_x != 0 else 0.001), self.pp[0], self.pp[1]), (10**9, -self.radius, 0))
        point_z_screen = rel_z + width/2
        sine, cosine = sincos_from_tan(self.m)
        point_x_screen = dist((rel_x, rel_y), (self.x - cosine * width / 2, self.y + sine * width / 2))

        # x = dist((point_x_screen, point_y_screen), (self.x - width/2 * sin(self.angle), self.y - height/2 * cos(self.angle)))
        # y = dist((point_x_screen, point_y_screen), (self.x + width/2 * sin(self.angle), self.y + height/2 * cos(self.angle)))
        return (point_x_screen, point_z)
    

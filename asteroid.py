from circleshape import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", (int(self.position.x),int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
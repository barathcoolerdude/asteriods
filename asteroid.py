from circleshape import *
from constants import *
import random
from player import *


class Asteroid(CircleShape):
    def __init__(self,x,y,radius,velocity):
        super().__init__(x,y,radius)
        self.velocity = velocity

    def draw(self, surface):
        pygame.draw.circle(surface, "white", (int(self.position.x),int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <=  ASTEROID_MIN_RADIUS: 
            self.kill()
            return
        
        #generate random angle for split
        random_angle = random.uniform(20,50)

        #create velocity for asteroids
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        #create two asteroids
        new_asteroid1 = Asteroid(self.position.x, self.position.y,self.radius - ASTEROID_MIN_RADIUS, velocity1)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS, velocity2)


        #add the asteriods to the same sprit groups
        self.containers[0].add(new_asteroid1, new_asteroid2)
        self.containers[1].add(new_asteroid1, new_asteroid2)
        self.containers[2].add(new_asteroid1, new_asteroid2)

        self.kill()

        





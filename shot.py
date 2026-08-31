import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):

    def __init__(self,x,y,SHOT_RADIUS):

        super().__init__(x,y,SHOT_RADIUS) # calling super to import from parent consctructor with SHOT_RADIUS as radius


    def draw(self, screen: pygame.Surface) -> None:

        # similar to `Asteroid` class
        color = "white"
        
        pygame.draw.circle(screen,color,self.position, self.radius, LINE_WIDTH)


    def update(self, dt: float) -> None:

    # similar to `Asteroid` class
        self.position += (self.velocity * dt)






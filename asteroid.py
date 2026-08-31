import pygame
from circleshape import CircleShape

from constants import LINE_WIDTH

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius) # calling super to import/initialize from parent CircleShape

    def draw (self, screen: pygame.Surface) -> None:

        """
        Override the draw() method to draw the asteroid using the pygame.draw.circle function. It accepts:

        The "surface" to draw on (the screen object)
        The color of the circle ("white")
        Its own position as the center
        Its own radius
        The width of the line to draw the circle (use LINE_WIDTH from constants.py)
        """

        color = "white"

        pygame.draw.circle(screen,color,self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:

        """
        Override the update() method so that it moves in a straight line at constant speed. 
        On each frame, it should add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape)
        """

        self.position += (self.velocity * dt)

        



        


    

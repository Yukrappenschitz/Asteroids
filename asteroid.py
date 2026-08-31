import pygame
import random
from circleshape import CircleShape
from logger import log_event

from constants import * #LINE_WIDTH

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


    def split(self) -> None:

        self.kill() # this asteroid is always destroyed even if it is split later

        if self.radius <= ASTEROID_MIN_RADIUS: # if true, small asteroid so it is done and should not be split further
            return
        else:
            log_event("asteroid_split") # log event

            random_angle = random.uniform(20,50) # generating a random angle between 20,50

            rotated_vector_1: pygame.Vector2 = self.velocity.rotate(random_angle) # creating a new rotated vector with given random_angle

            rotated_vector_2: pygame.Vector2 = self.velocity.rotate(-random_angle) # 2nd new vector for the second new asteroid, but this time rotate it in the opposite direction (negative angle)

            new_radius: float = self.radius - ASTEROID_MIN_RADIUS  # Computing the new radius of the smaller asteroids using the formula old_radius - ASTEROID_MIN_RADIUS

            # CREATING 2 NEW SMALLER ASTEROIDS objects at the current asteroid position with the new radius
            self.x = self.position[0] # getting updated position coordinates
            self.y = self.position[1]

            # Asteroid 1 Asteroid Object
            asteroid1 = Asteroid(self.x,self.y,new_radius)

            asteroid1.velocity = rotated_vector_1 * ASTEROID_SPLIT_SPEED_INCREASE # Asteroid 1 .velocity to rotated_vector_1, but it moves faster by scale factor (multiplying) (1.2)

            # Asteroid 2 Asteroid Object
            asteroid2 = Asteroid(self.x,self.y,new_radius)

            asteroid2.velocity = rotated_vector_2 * ASTEROID_SPLIT_SPEED_INCREASE # Asteroid 2 .velocity to rotated_vector_2, but it moves faster by scale factor (multiplying) (1.2)



        



        


    

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass


"""
In Pygame, there's a base Sprite class that represents visual objects.

 CircleShape class that inherits from Sprite to represent objects in our game that are treated as circles (even if they aren't, like the player's ship).

CircleShape extends the Sprite class to store 3 additional attributes specific to our game:

position (x and y coordinates)
velocity
radius.

Later we'll write subclasses of CircleShape and override the draw and update methods with the logic for each particular game object.
"""

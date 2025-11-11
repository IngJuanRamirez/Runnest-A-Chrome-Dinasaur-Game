# ========================================================================================================================
# Runnest-A-Chrome-Dinasaur-Game
# Created by Juan. A. Ramirez
# November 2025
# If you wan to see the code, please visit: https://github.com/IngJuanRamirez/Runnest-A-Chrome-Dinasaur-Game.git
# ========================================================================================================================

# obstacle.py

from pygame import sprite, Surface

class Obstacle(sprite.Sprite):
    def __init__(self, x, y, width, height, spped, *groups) -> None:
        super().__init__(*groups)

        # Obstacle image
        self.image = Surface((width, height))
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.speed = spped

    def move(self) -> None:
        """ Move the obstacle to the left """
        self.rect.x -= self.speed

        # If the obstacle out for the left...
        if self.rect.right <= 0:
            self.kill()


    def update(self, *args) -> None:
        # Move the obstacle
        self.move()
# ========================================================================================================================
# Runnest-A-Chrome-Dinasaur-Game
# Created by Juan. A. Ramirez
# November 2025
# If you wan to see the code, please visit: https://github.com/IngJuanRamirez/Runnest-A-Chrome-Dinasaur-Game.git
# ========================================================================================================================

# ground.py

from pygame import sprite, Surface

class Ground(sprite.Sprite):
    def __init__(self, x, y, width, height, speed, *groups) -> None:
        super().__init__(*groups)

        # Ground image
        self.image = Surface((width, height))
        self.image.fill((100, 100, 100))

        #Ground pos
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.speed = speed
        self.screen_width = width

    def update(self, *args) -> None:
        
        # Move sprite to the left
        self.rect.x -= self.speed

        if self.rect.right <= 0:
            self.rect.x += self.screen_width * 2
# ========================================================================================================================
# Runnest-A-Chrome-Dinasaur-Game
# Created by Juan. A. Ramirez
# November 2025
# If you wan to see the code, please visit: https://github.com/IngJuanRamirez/Runnest-A-Chrome-Dinasaur-Game.git
# ========================================================================================================================

#player.py

from pygame import sprite, Surface

class Player(sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()

        # Player image
        self.image = Surface((40, 60))
        self.image.fill((255, 0, 0)) # Red color for player

        # Player Rect
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self,) -> None:
        """Update Logic (Soon)"""
        pass
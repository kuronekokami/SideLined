#! python3
# settings.py
"""Settings file for SideLined"""


class Settings:
    def __init__(self, width=1200, height=720, color=(40, 45, 69)):
        # Screen settings
        self.width = width
        self.height = height
        self.screen_dimensions = (self.width, self.height)
        self.bgcolor = color

        # Ship settings
        self.ship_ymove = 1

        # Bullet settings
        self.sb_width = 15
        self.sb_height = 3
        # Auto-shoot intervals
        self.bullet_interval = 300
        self.currentbullet_interval = 0

        # Rain settings
        self.rainx_move = -0.75
        self.rainy_move = 0.75
        # Creation intervals
        self.rain_interval = 10
        self.currentrain_interval = 0

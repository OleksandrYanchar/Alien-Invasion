class Settings:
    # Initialize the game's settings

    def __init__(self):
        # Screen settings
        self.screen_width = 1200  # Змінено 'screen_wigth' на 'screen_width'
        self.screen_height = 900
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (
            60,
            60,
            60,
        )
        self.bullets_allowed = 5
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleeet_direction of 1 repredents right , -1 left
        self.fleet_direction = 1

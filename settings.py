#! /opt/anaconda3/envs/learningp37/bin/python
# Project # 1 / From "Python Crash Course" (2nd Edition), by Eric Matthes
# Code by Eric Matthes and José Delpino
# PROJECT # 1: Alien Invasion
# Chapter # 12: A Ship that Fires Bullets
# Chapter # 13: Aliens!

# SETTINGS CLASS
"""General settings for the game Alien Invasion."""


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Color variables
        self.whisper_grey = (230, 230, 230)  # Whisper Grey #E6E6E6
        self.deep_blue_sky = (0, 215, 255)  # Deep Sky Blue #00D7FF
        self.dark_grey = (60, 60, 60)  # Dark Grey (Eclipse) #3C3C3C

        # Screen settings
        self.full_screen = False
        self.screen_width = 840
        self.screen_height = 525
        self.bg_color = self.whisper_grey

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 8
        self.bullet_color = self.dark_grey
        self.bullets_allowed = 4

        # Alien settings
        self.fleet_drop_speed = 5.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Other game play settings
        self.redeployment_pause = 0.6

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        # Level Category Difference
        self.category_delta = 6

        # Level Categories
        self.category_levels = {
            0: "Level: Beginner",
            1: "Level: Intermetiate",
            2: "Level: Advance",
            3: "Level: Admiral",
            4: "Level: Ultra",
        }
        # The dynamic settings!
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""

        # Current Level
        self.current_level = 0

        # Agents
        self.update_agent_settings()

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def update_agent_settings(self):
        """Update the dynamic settings for the ship, the bullets
        and the scoring system."""
        # Agents
        game_factor = (self.speedup_scale **
                       (self.current_level * self.category_delta))
        self.ship_speed = 3.0 * game_factor
        self.bullet_speed = 5.0 * game_factor
        self.alien_speed = 3.0 * game_factor

        # Scoring
        self.alien_points = int(50 * game_factor)

    def increase_speed(self):
        """Increase dynamic speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

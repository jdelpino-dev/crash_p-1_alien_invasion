#! /opt/anaconda3/envs/learningp37/bin/python
# Project # 1 / From "Python Crash Course" (2nd Edition), by Eric Matthes
# Code by Eric Matthes and José Delpino
# PROJECT # 1: Alien Invasion
# Chapter # 12: A Ship that Fires Bullets

# SETTINGS CLASS
"""General settings for the game Alien Invasion."""


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Color variables
        self.whisper_grey = (230, 230, 230)  # Whisper Grey #E6E6E6
        self.deep_blue_sky = (0, 215, 255)  # Deep Sky Blue #00D7FF
        self.dark_grey = (60, 60, 60)  # Dark Grey (Eclipse) #3C3C3C

        # Screen settings
        self.full_screen = True
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = self.whisper_grey

        # Ship settings.
        self.ship_speed = 10

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = self.dark_grey

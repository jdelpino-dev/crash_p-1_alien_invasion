#! /opt/anaconda3/envs/learningp35/bin/python
# Exercise 13.8 / From "Python Crash Course" (2nd Edition), by  Eric Matthes
# Code by José Delpino
# PROYECT # 1: Alien Invasion
# Chapter # 1: A Ship that Fires Bullets

# SETTINGS FILE: SETTINGS.py
"""General settings for the game Alien Invasion."""


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

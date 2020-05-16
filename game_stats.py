#! /opt/anaconda3/envs/learningp37/bin/python
# Project # 1 / From "Python Crash Course" (2nd Edition), by Eric Matthes
# Code by Eric Matthes and José Delpino
# PROJECT # 1: Alien Invasion
# Chapter # 13: Aliens!

# GAMESTATS CLASS
"""Module that contains the class GamStats. This class will allow us
to track the game statistics."""


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        # Initializes the game stats
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit

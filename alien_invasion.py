#! /opt/anaconda3/envs/learningp35/bin/python
# Exercise 13.8 / From "Python Crash Course" (2nd Edition), by  Eric Matthes
# Code by José Delpino
# PROYECT # 1: Alien Invasion
# Chapter # 1: A Ship that Fires Bullets

# MAIN FILE: alien_invasion.py
"""An alien invasion game created using pygame.

In this first part I set up Pygame, and then 'create a rocket ship
that moves right and left and fires bullets in response to player input'."""

import sys
import pygame
from settings import Settings


class AlienInvasion:
        """Overall class to manage game assets and behavior."""

        def __init__(self):
            """Initialize the game, and create game resources."""
            pygame.init()
            self.Settings = Settings()
            self.screen = pygame.display.set_mode(
                (Settings.screen_width, Settings.screen_height))
            pygame.display.set_caption("Alien Invasion")
            # Set the background color.

        def run_game(self):
            """Start the main loop for the game."""
            while True:
                # Watch for keyboard and mouse events.
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                # Redraw the screen during each pass through the loop.
                self.screen.fill(Settings.bg_color)

                # Make the most recently drawn screen visible.
                pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

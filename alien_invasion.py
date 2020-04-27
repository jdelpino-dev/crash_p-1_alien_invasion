#! /opt/anaconda3/envs/learningp35/bin/python
# Project # 1 / From "Python Crash Course" (2nd Edition), by  Eric Matthes
# Code by José Delpino
# PROJECT # 1: Alien Invasion
# Chapter # 12: A Ship that Fires Bullets

# MAIN CLASS AND FILE
"""An alien invasion game created using pygame.

In this first part I set up Pygame, and then 'create a rocket ship
that moves right and left and fires bullets in response to player input'."""

import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
        """Overall class to manage game assets and behavior."""

        def __init__(self):
            """Initialize the game, and create game resources."""
            pygame.init()
            self.settings = Settings()
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
            pygame.display.set_caption("Alien Invasion")
            self.ship = Ship(self)
            # Set the background color.

        def run_game(self):
            """Start the main loop for the game."""
            while True:
                self._check_events()
                self._update_screen()

        def _check_events(self):
            """Respond to keypresses and mouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        def _update_screen(self):
            """Update images on the screen, and flip to the new screen."""
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

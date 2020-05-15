#! /opt/anaconda3/envs/learningp37/bin/python
# Project # 1 / From "Python Crash Course" (2nd Edition), by Eric Matthes
# Code by Eric Matthes and José Delpino
# PROJECT # 1: Alien Invasion
# Chapter # 13: Aliens!

# ALIEN CLASS
"""Alien module that contains the class Alien."""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represente a single Alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height / 3

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def hit_sides(self):
        """Return True if any alien is at the side edges of screen."""
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True

    def hit_bottom(self):
        """Return True if any alien is at the bottom of screen."""
        if self.rect.bottom >= self.screen_rect.bottom:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x

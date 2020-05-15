#! /opt/anaconda3/envs/learningp37/bin/python
# Project # 1 / From "Python Crash Course" (2nd Edition), by Eric Matthes
# Code by Eric Matthes and José Delpino
# PROJECT # 1: Alien Invasion
# Chapter # 12: A Ship that Fires Bullets
# Chapter # 13: Aliens!

# SHIP CLASS
"""Ship module that contains the class Ship."""

import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_fwd = False
        self.moving_bck = False

    def update(self):
        """Update the ship's position based on the movement flags.
        In this version, the piloting system was deeply improved
        by José Delpino in order to make the ship strictly obey
        the screen range limits."""
        # Update the ship's x value, and limit the ship's
        # range of movement.
        if self.moving_right:
            new_rect_right = self.rect.right + self.settings.ship_speed
            if new_rect_right >= self.screen_rect.right:
                self.x = self.screen_rect.right - self.rect.width
            else:
                self.x += self.settings.ship_speed
        if self.moving_left:
            new_rect_left = self.rect.left - self.settings.ship_speed
            if new_rect_left < 0:
                self.x = self.screen_rect.left
            else:
                self.x -= self.settings.ship_speed
        # Update the ship's y value, and limit the ship's
        # range of movement.
        if self.moving_fwd:
            new_rect_top = self.rect.top - self.settings.ship_speed
            if new_rect_top < 0:
                self.y = self.screen_rect.top
            else:
                self.y -= self.settings.ship_speed
        if self.moving_bck:
            new_rect_bottom = self.rect.bottom + self.settings.ship_speed
            if new_rect_bottom >= self.screen_rect.bottom:
                self.y = self.screen_rect.bottom - self.rect.height
            else:
                self.y += self.settings.ship_speed

        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center(self):
        """Reset a ship to its original position"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

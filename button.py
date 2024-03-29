#! /opt/anaconda3/envs/learningp37/bin/python
# Project # 1 / From "Python Crash Course" (2nd Edition), by Eric Matthes
# Code by José Delpino, completing Eric Matthes' code from the book
# PROJECT # 1: Alien Invasion
# Chapter # 13: Aliens!

# BUTTON CLASS
"""Module that contains the class button."""

import pygame.font


class Button:
    """A class to create a rectangle that acts as a button."""

    def __init__(self, ai_game, msg, font_size):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect
        self.settings = ai_game.settings

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, font_size)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def move(self, x_increment, y_increment):
        self.rect.x += x_increment
        self.msg_image_rect.x += x_increment
        self.rect.y += y_increment
        self.msg_image_rect.y += y_increment

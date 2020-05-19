#! /opt/anaconda3/envs/learningp37/bin/python
# Project # 1 / From "Python Crash Course" (2nd Edition), by Eric Matthes
# Code by Eric Matthes and José Delpino
# PROJECT # 1: Alien Invasion
# Chapter # 12: A Ship that Fires Bullets
# Chapter # 13: Aliens!

# MENU CLASS
"""The main mane for Alien Invasion."""

from button import Button


class Menu:
    """A class to store a menu of buttons."""

    def __init__(self, ai_game):
        """Initialize the main menu."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect
        self.settings = ai_game.settings

        # Creates a list to store the buttons:
        self.buttons = []

    def _calculate_menu_space(self):
        # height 30%
        # wide 20 %
        pass

    def add_button(self, button):
        pass

    def show_menu(self):
        pass

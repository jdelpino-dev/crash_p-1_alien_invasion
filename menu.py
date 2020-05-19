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
        self.stats = ai_game.stats

        # Make the Play button:
        self.play_button = Button(ai_game, "Play", 48)
        self.level_button = Button(ai_game, "Begginer", 30)
        self.level_button.move(0, self.play_button.height + 10)

    def show_menu(self):
        self.play_button.draw_button()
        self.level_button.draw_button()

    def check_buttons(self, ai_game, mouse_pos):
        """Check clicks over the buttons and call the respective actions"""
        play_clicked = self.play_button.rect.collidepoint(mouse_pos)
        level_clicked = self.level_button.rect.collidepoint(mouse_pos)
        if level_clicked:
            current_level = self.settings.current_level
            category_levels = self.settings.category_levels
            number_levels = len(category_levels)
            self.settings.current_level = ((current_level + 1)
                                            % number_levels)
            current_level = self.settings.current_level
            self.level_button._prep_msg(category_levels[current_level])
            self.level_button.draw_button()
            self.settings.update_agent_settings()
        if play_clicked:
            # Reset the game settings.
            self.settings.update_agent_settings()
            # Start new game.
            ai_game._start_game()

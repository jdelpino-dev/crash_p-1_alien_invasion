#! /opt/anaconda3/envs/learningp37/bin/python
# Project # 1 / From "Python Crash Course" (2nd Edition), by Eric Matthes
# Code by Eric Matthes and José Delpino
# PROJECT # 1: Alien Invasion
# Chapter # 12: A Ship that Fires Bullets
# Chapter # 13: Aliens!

# MAIN CLASS AND FILE
"""An alien invasion game created using pygame. The game is created using the
code provided by the book, but doing significant modifications when
it is needed."""

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Stablish the screen resolution.
        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))

        # Stablish the window title.
        pygame.display.set_caption("Alien Invasion")
        # Creates the ship instance.
        self.ship = Ship(self)
        # Creates the bullet stash where we'll store them
        # –a pygame sprite group–
        self.bullets = pygame.sprite.Group()
        # Creates the alien fleet container whre we'll store
        # the aliens –a pygame sprite group
        self.aliens = pygame.sprite.Group()
        # Creates the alien fleet with all its instances:
        self._create_fleet()

    def _create_alien(self, alien_number, alien_space):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien.x += float(alien_space*alien_number)
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to the third of one alien width.
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_marging = alien_width/3
        alien_space = alien_width + alien_marging
        available_space_x = self.settings.screen_width - 5*alien_width/3
        number_aliens_x = int(available_space_x // alien_space)
        # Create the first row of aliens.
        for alien_number in range(0, number_aliens_x):
            self._create_alien(alien_number, alien_space)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_fwd = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_bck = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_fwd = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_bck = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()  # The group automatically calls update()
        # for each sprite/bullet in the group.
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():  # «When you use a for
            if bullet.rect.bottom <= 0:  # loop with a list (or a group in
                self.bullets.remove(bullet)  # Pygame), Python expects that
            # the list will stay the same length as long as the loop is
            # running. Because we can’t remove items from a list or group
            # within a for loop, we have to loop over a copy of the group».
        # print(len(self.bullets))  # Scaffolding... Erase soon...

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

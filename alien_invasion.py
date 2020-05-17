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
from time import sleep
import pygame
from pygame.sprite import groupcollide, spritecollideany
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Stablish the screen resolution.
        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            # Stores the screen rect:
            self.screen_rect = self.screen.get_rect()
            # Stablish the resolution:
            self.settings.screen_width = self.screen_rect.width
            self.settings.screen_height = self.screen_rect.height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
            # Stores the screen rect:
            self.screen_rect = self.screen.get_rect()
        # Stablish the window title.
        pygame.display.set_caption("Alien Invasion")
        # Make the Play button.
        self.play_button = Button(self, "Play")
        # Creates the game stats instance. The self arguments that are passed
        # to the stat and ship objects refer to the current instance of
        # AlienInvasion. This is the parameter that gives these objects access
        # to the game’s resources, such as the screen object.
        self.stats = GameStats(self)
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

    def _calculate_fleet_variables(self):
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to the third of one alien width.
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_marging_x = alien_width/3
        alien_space_x = alien_width + alien_marging_x
        available_space_x = self.settings.screen_width - 5*alien_width/3
        number_aliens_x = int(available_space_x // alien_space_x)
        # Calculate the number of rows:
        alien_height = alien.rect.height
        alien_marging_y = alien_height/3
        alien_space_y = alien_height + alien_marging_y
        available_space_y = (self.settings.screen_height - 20*alien_height/3
                             - self.ship.rect.height)
        number_aliens_y = int(available_space_y // alien_space_y)
        # Create all the rows of aliens.
        return (number_aliens_x, alien_space_x,
                number_aliens_y, alien_space_y)

    def _create_alien(self, alien_number_x, alien_space_x,
                      alien_number_y, alien_space_y):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien.x += float(alien_space_x * alien_number_x)
        alien.rect.x = alien.x
        alien.y += float(alien_space_y * alien_number_y)
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Calculate the fleet spatial variables:
        fleet_space = self._calculate_fleet_variables()
        number_aliens_x, alien_space_x = fleet_space[0], fleet_space[1]
        number_aliens_y, alien_space_y = fleet_space[2], fleet_space[3]
        # Create the fleet:
        for alien_number_y in range(0, number_aliens_y):
            for alien_number_x in range(0, number_aliens_x):
                self._create_alien(alien_number_x, alien_space_x,
                                   alien_number_y, alien_space_y)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if not self.stats.game_active:
            if event.key == pygame.K_p:
                self._start_game()
        else:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            if event.key == pygame.K_UP:
                self.ship.moving_fwd = True
            if event.key == pygame.K_DOWN:
                self.ship.moving_bck = True
            if event.key == pygame.K_SPACE:
                self._fire_bullet()
        if event.key == pygame.K_q:
            sys.exit()

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

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if (self.stats.game_active and
           len(self.bullets) < self.settings.bullets_allowed):
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
        collisions = groupcollide(self.bullets, self.aliens, True, True)
        del collisions
        if not self.aliens:
            self._redeploy_elements()

    def _update_aliens(self):
        """Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet."""
        if self.stats.game_active:
            self._check_fleet_edges()
            self.aliens.update()
            # Look for alien-ship collisions.
            if spritecollideany(self.ship, self.aliens):
                self._alien_collision()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.hit_bottom():
                self._alien_collision()
                break
            if alien.hit_sides():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.y += self.settings.fleet_drop_speed
            alien.rect.y = alien.y
        self.settings.fleet_direction = self.settings.fleet_direction * -1

    def _redeploy_elements(self):
        """Repopulate the fleet, delete the bullets, and reposition the ship
        to avoid a starting collision. It also creates a short game pause"""
        self.ship.center()
        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()
        sleep(self.settings.redeployment_pause)
        # Remove all events from the queue:
        pygame.event.clear()
        # Put the ship movement flags down:
        self.movement_flags_down()

    def _alien_collision(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 1:
            # Decrement ships_left.
            self.stats.ships_left -= 1
            # Redeploy the game.
            self._redeploy_elements()
        else:
            self.stats.game_active = False
            # Make visible the mouse cursor.
            pygame.mouse.set_visible(True)
            # Remove all events from the queue:
            pygame.event.clear()

    def movement_flags_down(self):
        self.ship.moving_right = False
        self.ship.moving_left = False
        self.ship.moving_fwd = False
        self.ship.moving_bck = False

    def _start_game(self):
        # Reset the game statistics.
        self.stats.reset_stats()
        # Get rid of any remaining aliens and bullets, and
        # create a new fleet and center the ship.
        self._redeploy_elements()
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # Remove all events from the queue:
        pygame.event.clear()
        # Put the ship movement flags down:
        self.movement_flags_down()
        # Make the game active:
        self.stats.game_active = True

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self._update_aliens()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
            self._update_screen()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

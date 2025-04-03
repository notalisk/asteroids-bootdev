import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from button import *
import sys

def main():
    pygame.init()

    print('Starting Asteroids!')

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Asteroids')

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    buttons = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    Button.containers = (buttons)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Create buttons
    start_button = Button('Start', SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 75, 200, 60)
    exit_button = Button('Exit', SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 75, 200, 60)

    clock = pygame.time.Clock()
    dt = 0

    GAME = False
    MENU = True
    PAUSE = False

    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        screen.fill((0, 0, 0))  # Fill the screen with black first

        # RENDER MAIN MENU
        if MENU:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            start_button.draw(screen)
            exit_button.draw(screen)

            if start_button.is_clicked():
                GAME = True
                MENU = False
                start_button.kill()
                exit_button.kill()
            if exit_button.is_clicked():
                sys.exit()
            
            pygame.display.flip()

        # RUN THE GAME    
        if GAME:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill((0, 0, 0))

            for sprite in drawable:
                sprite.draw(screen)

            updatable.update(dt)

            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collision(shot):
                        shot.kill()
                        asteroid.split()
                
                if asteroid.collision(player):
                    print('Game over!')
                    sys.exit()

            pygame.display.flip()
            dt = clock.tick(60) / 1000
        
        # RENDER PAUSE MENU
        if PAUSE:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

if __name__ == "__main__":
    main()
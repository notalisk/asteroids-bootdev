import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    pygame.init()

    print('Starting Asteroids!')
    print('Screen width: ' + str(SCREEN_WIDTH))
    print('Screen height: ' + str(SCREEN_HEIGHT))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
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

if __name__ == "__main__":
    main()
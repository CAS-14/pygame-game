import random
import pygame
 
# Global Variables
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500
 
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.image.load("jimmy1.png")
        self.rect = self.image.get_rect()
 
    def moveRight(self, pixels):
        if self.rect.right < WIDTH:
            self.rect.x += pixels
 
    def moveLeft(self, pixels):
        if self.rect.left > 0:
            self.rect.x -= pixels
 
    def moveUp(self, pixels):
        if self.rect.top > 0:
            self.rect.y -= pixels
 
    def moveDown(self, pixels):
        if self.rect.bottom < HEIGHT:
            self.rect.y += pixels
 
 
pygame.init()
 
 
RED = (255, 0, 0)
 
 
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")
 
 
all_sprites_list = pygame.sprite.Group()
 
playerCar = Sprite(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300
 
 
all_sprites_list.add(playerCar)
 
exit = True
clock = pygame.time.Clock()
 
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(10)
    if keys[pygame.K_DOWN]:
        playerCar.moveDown(10)
    if keys[pygame.K_UP]:
        playerCar.moveUp(10)
 
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
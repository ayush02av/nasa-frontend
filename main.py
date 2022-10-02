import pygame  
import random
from sprites import sprites
  
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

WATERBED_HEIGHT = 520

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = [130, 181, 240]
bg_img = pygame.image.load('assets/bg.png')
bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, WATERBED_HEIGHT))

fps = 50
done = False

player = sprites.Player()
player_group = pygame.sprite.Group()
player_group.add(player)

shrimp_group = pygame.sprite.Group()
for i in range(10):
    shrimp_group.add(sprites.Shrimp())

while not done:
    screen.fill(bg)
    screen.blit(bg_img, (0, SCREEN_HEIGHT - WATERBED_HEIGHT))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    key = pygame.key.get_pressed()
  
    for i in range(2):
        if key[player.move[2:4][i]]:  
            player.rect.y += player.vy * [-1, 1][i]
    
    player_group.draw(screen)
    shrimp_group.draw(screen)

    for shrimp in shrimp_group:
        shrimp.rect.x -= shrimp.vx * 1

        if shrimp.rect.colliderect(player.rect):
            shrimp.rect.x = SCREEN_WIDTH
            shrimp.rect.y = random.randint(300, 700)
            shrimp.vx = random.randint(3, 8)

        if shrimp.rect.x <= 0:
            shrimp.rect.x = SCREEN_WIDTH
            shrimp.rect.y = random.randint(300, 700)
            shrimp.vx = random.randint(3, 8)
    
    if player.rect.x <= 0:
        player.rect.x = SCREEN_WIDTH
    elif player.rect.x >= SCREEN_WIDTH:
        player.rect.x = 0
    
    pygame.display.update()
    clock.tick(fps)
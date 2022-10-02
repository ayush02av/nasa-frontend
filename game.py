import datetime
import pygame  
import random
from sprites import sprites

def game(character):
    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 720

    WATERBED_HEIGHT = 520

    ALGAE_THRESHOLD = 5
    ALGAE_DRAWN = False

    pygame.init()
    pygame.display.set_caption("Delta Nemo")

    clock = pygame.time.Clock()

    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', 32)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg = [130, 181, 240]

    fps = 50

    player = sprites.Player(character)
    player_group = pygame.sprite.Group()
    player_group.add(player)

    shrimp_group = pygame.sprite.Group()
    for i in range(4):
        shrimp_group.add(sprites.Shrimp())

    small_sediment_group = pygame.sprite.Group()
    for i in range(8):
        small_sediment_group.add(sprites.SmallSediment())

    big_sediment_group = pygame.sprite.Group()
    for i in range(3):
        big_sediment_group.add(sprites.BigSediment())

    bubble_group = pygame.sprite.Group()
    for i in range(30):
        bubble_group.add(sprites.Bubble())

    algae_group = pygame.sprite.Group()
    for i in range(1, 48):
        algae_group.add(sprites.Algae(i))

    bg_img_url = 'water_blue'
    done = False
    deductPoints = 2

    show_chlorine = None
    
    while not done:
        screen.fill(bg)

        bg_img = pygame.image.load(f'assets/{bg_img_url}.jpg')
        bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, WATERBED_HEIGHT))
        screen.blit(bg_img, (0, SCREEN_HEIGHT - WATERBED_HEIGHT))

        text = font.render(f"Health: {player.health}", True, green, blue)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, 20)
        screen.blit(text, textRect)
        
        text = font.render(f"Score: {player.score}", True, green, blue)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, 60)
        screen.blit(text, textRect)

        if show_chlorine:
            chlorine = pygame.image.load("assets/chlorine.png")
            chlorine = pygame.transform.scale(chlorine, (50, 100))
            screen.blit(chlorine.convert(), (0, 0))
            if (datetime.datetime.now() - show_chlorine).total_seconds() > 3:
                show_chlorine = None
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        key = pygame.key.get_pressed()
    
        for i in range(2):
            if key[player.move[2:4][i]]:  
                player.rect.y += player.vy * [-1, 1][i]
        
        player_group.draw(screen)
        shrimp_group.draw(screen)
        small_sediment_group.draw(screen)
        big_sediment_group.draw(screen)
        bubble_group.draw(screen)

        if player.score >= ALGAE_THRESHOLD and ALGAE_DRAWN:
            algae_group.draw(screen)
        elif player.score >= ALGAE_THRESHOLD and player.score % 5 == 0:
            ALGAE_DRAWN = True

        if ALGAE_DRAWN:
            bg_img_url = 'water_green'
            deductPoints = 3
            text = font.render(f"Shrimps Needed to Remove Algae: {3 - player.threshold}", True, green, blue)
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, 100)
            screen.blit(text, textRect)
            
        else:
            bg_img_url = 'water_blue'
            deductPoints = 2

        for bubble in bubble_group:
            bubble.rect.x -= bubble.vx * 1

            if bubble.rect.x <= 0:
                bubble.rect.x = SCREEN_WIDTH
                bubble.rect.y = random.randint(300, 700)
                bubble.vx = random.randint(1, 10)

        for shrimp in shrimp_group:
            shrimp.rect.x -= shrimp.vx * 1

            if shrimp.rect.colliderect(player.rect):
                if player.score >= ALGAE_THRESHOLD and ALGAE_DRAWN:
                    player.threshold += 1
                
                if player.threshold == 3:
                    ALGAE_DRAWN = False
                    player.threshold = 0
                    show_chlorine = datetime.datetime.now()
                
                player.health += 1
                player.score += 1
                if player.health >= 100:
                    player.health = 100
                
                shrimp.rect.x = SCREEN_WIDTH
                shrimp.rect.y = random.randint(300, 700)
                shrimp.vx = random.randint(3, 8)

            if shrimp.rect.x <= 0:
                shrimp.rect.x = SCREEN_WIDTH
                shrimp.rect.y = random.randint(300, 700)
                shrimp.vx = random.randint(3, 8)
        
        for sediment in small_sediment_group:
            sediment.rect.x -= sediment.vx * 1

            if sediment.rect.colliderect(player.rect):
                player.threshold = 0
                
                player.health -= deductPoints
                if player.health <= 0:
                    player.health = 0
                
                sediment.rect.x = SCREEN_WIDTH
                sediment.rect.y = random.randint(300, 700)
                sediment.vx = random.randint(3, 8)

            if sediment.rect.x <= 0:
                sediment.rect.x = SCREEN_WIDTH
                sediment.rect.y = random.randint(300, 700)
                sediment.vx = random.randint(3, 8)
        
        for sediment in big_sediment_group:
            sediment.rect.x -= sediment.vx * 1

            if sediment.rect.colliderect(player.rect):
                player.threshold = 0
                
                player.health -= 4
                if player.health <= 0:
                    player.health = 0
                
                sediment.rect.x = SCREEN_WIDTH
                sediment.rect.y = random.randint(300, 700)
                sediment.vx = random.randint(1, 3)

            if sediment.rect.x <= 0:
                sediment.rect.x = SCREEN_WIDTH
                sediment.rect.y = random.randint(300, 700)
                sediment.vx = random.randint(1, 3)
        
        if player.rect.x <= 0:
            player.rect.x = SCREEN_WIDTH
        elif player.rect.x >= SCREEN_WIDTH:
            player.rect.x = 0
        elif player.rect.y <= SCREEN_HEIGHT - WATERBED_HEIGHT:
            player.rect.y = SCREEN_HEIGHT - WATERBED_HEIGHT
        
        if player.health <= 0:
            done= True
         
        
        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    game(0)
import random
import pygame

class Sprite(pygame.sprite.Sprite):
    move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]

    def __init__(self, pos):  
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = pos

class Player(Sprite):
    sprite_image = 'assets/fish.png'

    def __init__(self):
        self.pos = [170, 500]
        super().__init__(self.pos)
        # self.vx = 2.5
        self.vy = 3
        self.health = 50
        self.score = 0
        self.threshold = 0

        self.image = pygame.image.load(self.sprite_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 80))
        
        self.rect = self.image.get_rect(center = self.pos)

class Bubble(Sprite):
    sprite_image = 'assets/bubble.png'
    pos = [0, 0]

    def __init__(self):
        self.pos = [random.randint(200, 900), random.randint(300, 700)]
        super().__init__(self.pos)
        self.vx = random.randint(1, 10)
        self.vy = 1

        self.image = pygame.image.load(self.sprite_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (random.randint(3, 8), random.randint(3, 8)))
        
        self.rect = self.image.get_rect(center = self.pos)

class Shrimp(Sprite):
    sprite_image = 'assets/shrimp.png'
    pos = [0, 0]

    def __init__(self):
        self.pos = [random.randint(200, 900), random.randint(300, 700)]
        super().__init__(self.pos)
        self.vx = random.randint(3, 8)
        self.vy = 1

        self.image = pygame.image.load(self.sprite_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 20))
        
        self.rect = self.image.get_rect(center = self.pos)

class SmallSediment(Sprite):
    sprite_image = 'assets/small_sediment.png'
    pos = [0, 0]

    def __init__(self):
        self.pos = [random.randint(200, 900), random.randint(300, 700)]
        super().__init__(self.pos)
        self.vx = random.randint(1, 5)
        self.vy = 1

        self.image = pygame.image.load(self.sprite_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 10))
        
        self.rect = self.image.get_rect(center = self.pos)

class BigSediment(Sprite):
    sprite_image = 'assets/big_sediment.png'
    pos = [0, 0]

    def __init__(self):
        self.pos = [random.randint(200, 900), random.randint(300, 700)]
        super().__init__(self.pos)
        self.vx = random.randint(1, 3)
        self.vy = 1

        self.image = pygame.image.load(self.sprite_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 30))
        
        self.rect = self.image.get_rect(center = self.pos)

class Algae(Sprite):
    sprite_image = 'assets/algae.png'
    pos = [0, 0]

    def __init__(self, index):
        self.pos = [20 * index, 200]
        super().__init__(self.pos)

        self.image = pygame.image.load(self.sprite_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 30))
        
        self.rect = self.image.get_rect(center = self.pos)
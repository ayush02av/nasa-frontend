import pygame
import pygame_menu

pygame.init()
pygame.display.set_caption("Delta Nemo")
surface = pygame.display.set_mode((600, 400))

character = 0

def set_character(value, char):
    global character
    character = char

def start_the_game():
    global character
    import game
    game.game(character)

menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

menu.add.selector('Character: ', [('Gold Fish', 0), ('Cat Fish', 1)], onchange=set_character)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)

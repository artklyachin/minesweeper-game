import pygame
from src.static import config
from src import game

print(1)
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
clock = pygame.time.Clock()
game = game.Game(screen)
running = True
while running:

    for event in pygame.event.get():
        if (not game.run_game):
            break
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.button)
            if event.button == 1:
                game.handle_left_mouse_click(event.pos)
                for i in range(game.map.map_hight):
                    print(game.map.object_map[i])
                print()
                for i in range(game.map.map_hight):
                    print(game.map.territoris_map[i])
                print("---")
            elif event.button == 3:
                game.handle_right_mouse_click(event.pos)
                for i in range(game.map.map_hight):
                    print(game.map.object_map[i])
                print()
                for i in range(game.map.map_hight):
                    print(game.map.territoris_map[i])
                print("---")

    if (game.run_game):
        game.render()
    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()

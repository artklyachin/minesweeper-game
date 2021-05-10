import pygame
from src.static import config


class map:

    def __init__(self, object):
        self.map_weight = len(object[0])
        self.map_hight = len(object)
        territoris_map = [[1] * self.map_hight for i in range(self.map_weight)]
        object_map = [[0] * self.map_hight for i in range(self.map_weight)]
        for y in range(self.map_hight):
            for x in range(self.map_weight):
                if (object[y][x] == 1):
                    object_map[y][x] = 9
                    continue
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (0 <= x + i < self.map_weight and 0 <= y + j < self.map_hight
                                and object[y + j][x + i] == 1):
                            object_map[y][x] += 1
        self.object_map = object_map
        self.territoris_map = territoris_map

    def is_click_on_table(self, coordinate_x, coordinate_y):
        tx = coordinate_x // config.sell_size
        ty = coordinate_y // config.sell_size
        return 0 <= tx < self.map_weight and 0 <= ty < self.map_hight

    def coordinate_on_table(self, coordinate_x, coordinate_y):
        tx = coordinate_x // config.sell_size
        ty = coordinate_y // config.sell_size
        return (tx, ty)

    def render(self, screen):
        sell_size = config.sell_size
        frame_size = config.frame_size
        for j in range(self.map_hight):
            for i in range(self.map_weight):
                pygame.draw.rect(screen, (0, 0, 255), (i * config.sell_size, j * config.sell_size, config.sell_size, config.sell_size), frame_size)

        for j in range(self.map_hight):
            for i in range(self.map_weight):
                color = self.territoris_map[j][i]
                obj = self.object_map[j][i]
                if (color == 1):
                    pygame.draw.rect(screen, (0, 255, 0), (i * sell_size + frame_size, j * sell_size + frame_size, sell_size - 2 * frame_size, sell_size - 2 * frame_size), 0)
                elif (color == 2):
                    pygame.draw.rect(screen, (255, 0, 0), (i * sell_size + frame_size, j * sell_size + frame_size, sell_size - 2 * frame_size, sell_size - 2 * frame_size), 0)
                elif (color == 0):
                    if (0 < self.object_map[j][i] < 9):
                        f1 = pygame.font.Font(None, 27)
                        text1 = f1.render(str(self.object_map[j][i]), True, (0, 0, 255))
                        screen.blit(text1, (i * config.sell_size + 2 * frame_size, j * config.sell_size + 2 * frame_size))
                    elif self.object_map[j][i] == 9:
                        pass

    def boom(self, x, y, screen):
        sell_size = config.sell_size
        frame_size = config.frame_size
        for j in range(self.map_hight):
            for i in range(self.map_weight):
                self.territoris_map[j][i] = 0
                if self.object_map[j][i] == 9:
                    pygame.draw.rect(screen, (255, 255, 255), (i * sell_size + frame_size, j * sell_size + frame_size, sell_size - 2 * frame_size, sell_size - 2 * frame_size), 0)
        self.render(screen)

    def win_end(self, screen):
        sell_size = config.sell_size
        frame_size = config.frame_size
        for j in range(self.map_hight):
            for i in range(self.map_weight):
                self.territoris_map[j][i] = 0
                if self.object_map[j][i] == 9:
                    pygame.draw.rect(screen, (255, 125, 0), (i * sell_size + frame_size, j * sell_size + frame_size, sell_size - 2 * frame_size, sell_size - 2 * frame_size), 0)
        self.render(screen)

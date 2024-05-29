import json
from src.map import map
from src.static import config
from src.screen_buttons import screen_buttons


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.game_generation()

    def game_generation(self):
        with open(config.file_start_map) as f:
            data = json.load(f)
            object = data["objects"]
            territories = data["territories"]

        self.map = map(object)
        self.screen_button = screen_buttons()
        self.visited = [[0] * self.map.map_weight for i in range(self.map.map_weight)]
        self.run_game = True


    def handle_right_mouse_click(self, pos):
        (x, y) = pos
        if (not self.map.is_click_on_table(x, y)):
            return
        (tx, ty) = self.map.coordinate_on_table(x, y)
        if (self.map.territoris_map[ty][tx] == 1):
            self.map.territoris_map[ty][tx] = 2
        elif (self.map.territoris_map[ty][tx] == 2):
            self.map.territoris_map[ty][tx] = 1
        self.is_end_of_game()

    def dfs(self, x, y):
        print("go", x, y)
        self.map.territoris_map[y][x] = 0
        if (self.map.object_map[y][x] != 0):
            return
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (0 <= x + i < self.map.map_weight and 0 <= y + j < self.map.map_hight
                        and self.map.territoris_map[y + j][x + i] != 0 and self.map.territoris_map[y + j][x + i] != 2):
                    self.dfs(x + i, y + j)
        print("end", x, y)


    def handle_left_mouse_click(self, pos):
        (x, y) = pos
        if (not self.map.is_click_on_table(x, y)):
            return
        (tx, ty) = self.map.coordinate_on_table(x, y)
        if (self.map.territoris_map[ty][tx] != 1):
            return
        else:
            if (0 < self.map.object_map[ty][tx] < 9):
                self.map.territoris_map[ty][tx] = 0
            elif (self.map.object_map[ty][tx] == 9):
                self.map.boom(tx, ty, self.screen)
                self.run_game = False
            elif (self.map.object_map[ty][tx] == 0):
                self.dfs(tx, ty)


    def render(self):
        self.screen.fill((0, 0, 0))
        self.map.render(self.screen)
        self.screen_button.render(self.screen)

    def is_end_of_game(self):
        for y in range(self.map.map_hight):
            for x in range(self.map.map_weight):
                if (self.map.object_map[y][x] == 9 and self.map.territoris_map[y][x] != 2):
                    return
                if (self.map.object_map[y][x] != 9 and self.map.territoris_map[y][x] == 2):
                    return
        self.map.win_end(self.screen)
        self.run_game = False

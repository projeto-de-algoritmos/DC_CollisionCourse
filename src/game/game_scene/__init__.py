import pygame

from src.config import CANVAS_HEIGHT, CANVAS_WIDTH, CANVAS_X_POSITION, CANVAS_Y_POSITION
from src.game.quadtree import Quadtree, Rectangle, Point


class GameScene:
    def __init__(self, window):
        self.window = window
        quadtree_boundaries = Rectangle(
            CANVAS_X_POSITION, CANVAS_Y_POSITION, CANVAS_WIDTH, CANVAS_HEIGHT
        )
        self.quadtree = Quadtree(self.window, quadtree_boundaries, 2)
        # self.quadtree.create_random_points(400)

        self.point_list = [
            Point(100, 100),
            Point(200, 200),
            Point(300, 300),
            Point(320, 400),
            Point(330, 500),
            Point(340, 600),
            Point(320, 720),
            Point(320, 840),
            Point(330, 220),
            Point(330, 440),
            Point(320, 520),
            Point(120, 640)
        ]

        for point in self.point_list:
            self.quadtree.insert(point)

    def draw_dummy(self):
        pygame.draw.rect(self.window, (255, 0, 0), (0, 0, 100, 100))
        # draw random rect inside the window

    def draw_canvas_border(self):
        pygame.draw.rect(
            self.window,
            (0, 255, 0, 1),
            (CANVAS_X_POSITION, CANVAS_Y_POSITION, CANVAS_WIDTH, CANVAS_HEIGHT),
            1,
        )

    def run(self):
        # self.draw_dummy()

        while True:
            
            self.window.fill((0, 0, 0))

            self.draw_canvas_border()

            self.quadtree.draw()
            # self.quadtree.print_quadtree()

            self.quadtree.clear()

            for point in self.point_list:
                self.quadtree.insert(point)

            pygame.display.update()

            # import ipdb;ipdb.set_trace()

        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

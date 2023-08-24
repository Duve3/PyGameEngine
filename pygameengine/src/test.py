"""
Used for testing: game.py, menu.py, fonts.py, and color.py
"""
from pygameengine import GameType, MenuType, CustomColor, Font
from pygameengine.logging import setupLogging
from logging import INFO
import pygame

logger = setupLogging("main", level=INFO)


class MainMenu(MenuType):
    def __init__(self, screen, fpsClock, font):
        super().__init__(screen, fpsClock)
        self.c = CustomColor((0, 255, 0))
        self.font: Font = font

    def logic(self):
        logger.debug("Menu Logic")
    
    def rendering(self):
        logger.debug("Menu Rendering")
        self.screen.fill(self.c)
        self.font.multiline_render_to(self.screen, (50, 50), "This is the main\nmenu")
        pygame.display.flip()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.logic()
            self.rendering()


class Game(GameType):
    def __init__(self):
        super().__init__("Testing Application", (1080, 720))
        self.c = CustomColor((255, 0, 0))
        self.font = Font("./PyGameEngine/pygameengine/src/ExtraLightFont.ttf", 40, CustomColor((50, 150, 25)))
        self.menus = [MainMenu(self.screen, self.fpsClock, self.font)]
    
    def logic(self):
        logger.debug("Logic")
    
    def rendering(self):
        logger.debug("Rendering")
        self.screen.fill(self.c)
        self.font.multiline_render_to(self.screen, (100, 100), "This is the game\n thing")
        pygame.display.flip()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    logger.info(f"Key pressed: {pygame.key.name(event.key)}")
                    if event.key == pygame.K_a:
                        self.router(0).run()
            self.logic()
            self.rendering()

    def router(self, case) -> MenuType:
        return self.menus[case]


def main():
    pygame.init()
    g = Game()
    g.run()

if __name__ == "__main__":
    main()

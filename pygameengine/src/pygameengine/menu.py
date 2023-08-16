"""
All stuff related to creating menus using ge
"""
import pygame
from pygame import Surface


class MenuType:
    """
    A base class when creating Menus, very similar to the game class but without some of the features.
    """
    def __init__(self, screen: Surface, fpsClock: pygame.time.Clock, fps: int = 60) -> None:
        """
        The init function for defining a menu type
        :param screen: The pygame.Surface used for rendering
        :param fpsClock: The pygame.time.Clock used for fps
        :param fps: The actual frames per second (optional defaults to 60)
        :return: None
        """
        self.screen = screen
        self.fpsClock = fpsClock
        self.fps = fps


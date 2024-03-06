import pygame
from typing_extensions import TypeAlias

appWidth, appHeight = 600, 600
FPS =120


display = pygame.display.set_mode((appWidth, appHeight), pygame.RESIZABLE)

RGBcolor: TypeAlias = tuple[int,int,int]


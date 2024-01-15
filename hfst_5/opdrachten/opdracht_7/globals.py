import pygame, constants
from typing_extensions import TypeAlias

display = pygame.display.set_mode((constants.BREEDTE, constants.HOOGTE))

RGBcolor: TypeAlias = tuple[int,int,int]


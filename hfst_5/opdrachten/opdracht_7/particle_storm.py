# Vul de TODO's aan op basis van de uitleg in de README.

import pygame, globals, constants
from particle_holder import ParticleHolder
from colors import Colors


# Start pygame.
pygame.init()
pygame.display.set_caption("Fire Storm Simulation")
clock = pygame.time.Clock()

particles = ParticleHolder(50, 5)

    
running = True
while running:
    # Maak scherm schoon.
    globals.display.fill(Colors.BLACK)

    # Zorg voor constante FPS. interval is de tijd tussen iedere frame (in ms)
    interval = clock.tick(constants.FPS)
    
    # Controleer of quit-knop is ingeduwd.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO 2: Overloop iedere particle in lijst met particles:
    #   1. Beweeg positie van ieder particle
    #   2. Reset particle wanneer ze uit het scherm zijn.
    #   3. Teken particle op scherm (deels gemaakt).
    particles.place()

    # Toon scherm aan gebruiker.
    pygame.display.update()

pygame.quit()
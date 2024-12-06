import pygame

# init MUST be included before pygame can do anything
pygame.init()

# creates a window that's 1280 pixels wide and 720 pixels tall
screen = pygame.display.set_mode((1280, 720)) 
running = True

# all code within the while loop is run over and over as long as running is true
while running:
    # iterates through every new event since the last time pygame.event.get() was called
    for event in pygame.event.get():
        # if one of those events is QUIT, set running to false
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
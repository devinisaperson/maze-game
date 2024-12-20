import pygame

# init MUST be included before pygame can do anything
pygame.init()

# creates a window that's 1280 pixels wide and 720 pixels tall
screen = pygame.display.set_mode((1280, 720))
# creates a clock that keeps track of time for us
clock = pygame.time.Clock()
running = True

# we want this outside of the loop, since we don't want to reset x every frame
x = 0

# all code within the while loop is run over and over as long as running is true
while running:
    # iterates through every new event since the last time get() was called
    for event in pygame.event.get():
        # if one of those events is QUIT, set running to false
        if event.type == pygame.QUIT:
            running = False

    x += 5
    # clears everything that was on screen
    screen.fill("purple")
    # draws a circle on the screen that's "red" at (x,0) with radius 100
    pygame.draw.circle(screen, "red", (x,0), 100)

    # flip() updates the display to show everything that has been drawn
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

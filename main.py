import pygame
import os
pygame.init()

WIDTH, HEIGHT = 512, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

MOLE_WIDTH, MOLE_HEIGHT = 100, 100

pygame.display.set_caption("Mole World")
WHITE = 255, 255, 255
BABY_BLUE = 204, 255, 255

BORDER = pygame.Rect(WIDTH, 0, 0, HEIGHT)

FPS = 60
VEL = 6 # Speed of player movement
#background_image = pygame.image.load(os.)
MOLE_IMAGE = pygame.image.load(os.path.join('Assets', 'pixel_mole.png'))
MOLE = pygame.transform.rotate(pygame.transform.scale(
    MOLE_IMAGE, (MOLE_WIDTH, MOLE_HEIGHT)), 0) # Last value defines rotation

background_image = pygame.image.load(os.path.join('Assets', 'map1.png'))

def camera_adjust(mole, monitor_size, true_scroll):

    xCenter = mole.x
    yCenter = mole.y

    true_scroll[0] += (xCenter - true_scroll[0] - (monitor_size[0] / 2)) / 80
    true_scroll[1] += (yCenter - true_scroll[1] - (monitor_size[1] / 2)) / 80
    scroll = true_scroll.copy()
    return [int(scroll[0]), int(scroll[1])]


def draw_window(mole):
    WIN.blit(background_image, [0, 0]) # Draws the background image onto game window
    WIN.blit(MOLE, (mole.x, mole.y)) # Draws character on screen, with positioning in game window
    pygame.display.update()

def player_movement(keys_pressed, mole):
    if keys_pressed[pygame.K_a] and mole.x - VEL > 0: #LEFT
        mole.x -= VEL
    if keys_pressed[pygame.K_d] and mole.x + VEL + mole.width < BORDER.x:  # RIGHT
        mole.x += VEL
    if keys_pressed[pygame.K_w] and mole.y - VEL > 0:  # UP
        mole.y -= VEL
    if keys_pressed[pygame.K_s] and mole.y + VEL + mole.height < HEIGHT - 15:  # DOWN
        mole.y += VEL

def main():
    clock = pygame.time.Clock()
    mole = pygame.Rect(100, 300, MOLE_WIDTH, MOLE_HEIGHT)
    run = True
    while run: #Infinite loop
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit() # Should this be here?

        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, mole)

        draw_window(mole)
    main()


    pygame.quit()

if __name__ == "__main__":
    main()

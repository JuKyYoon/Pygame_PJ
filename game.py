import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode([640, 400])

pygame.display.set_caption('test game')
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

background_position = [0, 0]

background_image = pygame.image.load("space.jpg").convert()
player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(BLACK)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background_image, background_position)

    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    screen.blit(player_image, [x, y])
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

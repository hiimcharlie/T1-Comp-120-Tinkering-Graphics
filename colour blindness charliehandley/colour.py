import pygame

pygame.init()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)

image = pygame.image.load('field.jpg')
main_window = pygame.display.set_mode((800,600))
main_window.blit(image, (0,0))


def set_color(img, color):
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            color.a = img.get_at((x, y)).a
            img.set_at((x, y), color)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                set_color(image, pygame.Color(0, 0, 255))
            elif event.key == pygame.K_g:
                set_color(image, pygame.Color(0, 255, 0))
            elif event.key == pygame.K_b:
                set_color(image, pygame.Color(255, 0, 0))
            elif event.key == pygame.K_y:
                set_color(image, pygame.Color(255, 255, 0))

    pygame.display.flip()
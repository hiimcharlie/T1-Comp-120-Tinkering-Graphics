import os, pygame

pygame.init()

display_width = 1920
display_height = 1080

toolDisplay = pygame.display.set_mode((display_width, display_height))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

originalImagePath = os.path.join('Images', 'Red Boards.jpg')
originalImage = pygame.image.load(originalImagePath).convert()

for i in range(originalImage.get_width()):
    for j in range(originalImage.get_height()):
        pixelColour = originalImage.get_at((i, j))
        # red to green
        colourHolder = pixelColour[0]
        pixelColour[0] = pixelColour[1]
        pixelColour[1] = colourHolder
        originalImage.set_at((i, j), pixelColour)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    toolDisplay.fill((0, 0, 0))
    toolDisplay.blit(originalImage, (0, 0))
    pygame.display.update()
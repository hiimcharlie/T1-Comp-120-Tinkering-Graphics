import os, pygame

pygame.init()

toolDisplay = pygame.display.set_mode((800, 600))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

originalFilename = 'Sample Image'

originalImagePath = os.path.join('Images', originalFilename + '.jpg')
originalImage = pygame.image.load(originalImagePath).convert()

imageWidth = originalImage.get_width()
imageHeight = originalImage.get_height()

greenImage = pygame.Surface((imageWidth, imageHeight))
blueImage = pygame.Surface((imageWidth, imageHeight))
yellowImage = pygame.Surface((imageWidth, imageHeight))

for i in range(imageWidth):
    for j in range(imageHeight):
        for n in range(3):
            pixelColour = originalImage.get_at((i, j))
            if(n != 2):
                colourHolder = pixelColour[0]
                pixelColour[0] = pixelColour[n + 1]
                pixelColour[n + 1] = colourHolder
                if(n == 0):
                    greenImage.set_at((i, j), pixelColour)
                else:
                    blueImage.set_at((i, j), pixelColour)
            else:
                pixelColour[1] = pixelColour[0]
                yellowImage.set_at((i, j), pixelColour)

greenFilename = os.path.join('Images', originalFilename + ' (green)' + '.png')
pygame.image.save(greenImage, greenFilename)

blueFilename = os.path.join('Images', originalFilename + ' (blue)' + '.png')
pygame.image.save(blueImage, blueFilename)

yellowFilename = os.path.join('Images', originalFilename + ' (yellow)' + '.png')
pygame.image.save(yellowImage, yellowFilename)
import os, pygame, math

pygame.init()

toolDisplay = pygame.display.set_mode((800, 600))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

#sample image 1 500s
#sample image 2 180
#sample image 3 300
#sample image 4 150
allowedColourDistance = 150

originalFilename = 'Sample Image 4'

originalImagePath = os.path.join('Images', originalFilename + '.jpg')
originalImage = pygame.image.load(originalImagePath).convert()

imageWidth = originalImage.get_width()
imageHeight = originalImage.get_height()

generatedImages = []
generatedColours = ['green', 'blue', 'yellow']

for i in range(3):
    generatedImages.append(pygame.Surface((imageWidth, imageHeight)))

for i in range(imageWidth):
    for j in range(imageHeight):
        for n in range(3):
            pixelColour = originalImage.get_at((i, j))

            rBar = (red[0] + pixelColour[0]) / 2
            deltaRed = red[0] - pixelColour[0]
            deltaGreen = red[1] - pixelColour[1]
            deltaBlue = red[2] - pixelColour[2]

            colourDistance = math.sqrt((2 + rBar / 256) + math.pow(deltaRed, 2) + 4 * math.pow(deltaGreen, 2) + (2 + (255 - rBar) / 256) * math.pow(deltaBlue, 2))

            if colourDistance < allowedColourDistance:
                if n != 2:
                    colourHolder = pixelColour[0]
                    pixelColour[0] = pixelColour[n + 1]
                    pixelColour[n + 1] = colourHolder

                    generatedImages[n].set_at((i, j), pixelColour)

                else:
                    pixelColour[1] = pixelColour[0]
                    generatedImages[2].set_at((i, j), pixelColour)
            else:
                generatedImages[n].set_at((i, j), pixelColour)

for i in range(3):
    filename = os.path.join('Images', originalFilename + ' (' + generatedColours[i] + ')' + '.png')
    pygame.image.save(generatedImages[i], filename)

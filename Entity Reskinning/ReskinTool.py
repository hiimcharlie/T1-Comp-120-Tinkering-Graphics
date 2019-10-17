import os, pygame, math


def loadimageassurface(imagefilename, imagefileextension):
    imagepath = os.path.join('Images', imagefilename + imagefileextension)
    image = pygame.image.load(imagepath).convert()

    return image


def calculatecolourdistance(pixelcolour, originalskincolour):
    rbar = (originalskincolour[0] + pixelcolour[0]) / 2
    deltared = originalskincolour[0] - pixelcolour[0]
    deltagreen = originalskincolour[1] - pixelcolour[1]
    deltablue = originalskincolour[2] - pixelcolour[2]

    colourdistance = math.sqrt(
        (2 + rbar / 256) + math.pow(deltared, 2) + 4 * math.pow(deltagreen, 2) + (2 + (255 - rbar) / 256) * math.pow(
            deltablue, 2))

    return colourdistance


def generateblankimages(originalimage):
    generatedimages = []

    imagewidth = originalimage.get_width()
    imageheight = originalimage.get_height()

    for i in range(3):
        generatedimages.append(pygame.Surface((imagewidth, imageheight)))

    return generatedimages


def generateimages(originalimage, originalimageskin, allowedcolourdistane, generatedimages, i, j):
    pixelcolour = originalimage.get_at((i, j))
    colourdistance = calculatecolourdistance(pixelcolour, originalimageskin)

    for n in range(3):
        if colourdistance < allowedcolourdistane:
            if n != 2:
                colourholder = pixelcolour[0]
                pixelcolour[0] = pixelcolour[n + 1]
                pixelcolour[n + 1] = colourholder

                generatedimages[n].set_at((i, j), pixelcolour)

            else:
                pixelcolour[1] = pixelcolour[0]
                generatedimages[2].set_at((i, j), pixelcolour)
        else:
            generatedimages[n].set_at((i, j), pixelcolour)

        pixelcolour = originalimage.get_at((i, j))

    return generatedimages


def createnewfilenames(originalfilename, generatedfileextension):
    filenames = []
    generatedcolours = ['green', 'blue', 'yellow']

    for i in range(3):
        filenames.append(os.path.join('Images', originalfilename + ' (' + generatedcolours[i] + ')' + generatedfileextension))

    return filenames


def saveimages(generatedimages, generatedfilenames):

    for i in range(3):
        pygame.image.save(generatedimages[i], generatedfilenames[i])


def reskinimage(originalimagefilename, originalimageextension, originalimageskin, generatedfileextension, allowedcolourdistance):
    originalimage = loadimageassurface(originalimagefilename, originalimageextension)
    generatedimages = generateblankimages(originalimage)

    for i in range(originalimage.get_width()):
        for j in range(originalimage.get_height()):

            generatedimages = generateimages(originalimage, originalimageskin, allowedcolourdistance, generatedimages, i, j)

    generatedfilenames = createnewfilenames(originalimagefilename, generatedfileextension)
    saveimages(generatedimages, generatedfilenames)


pygame.init()

toolDisplay = pygame.display.set_mode((800, 600))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# sample image 1 500
# sample image 2 180
# sample image 3 300
# sample image 4 150
allowedColourDistance = 150

originalFilename = 'Sample Image 4'
originalFileExtension = '.jpg'

originalImageSkin = red

generatedImageFileExtension = '.png'

reskinimage(originalFilename, originalFileExtension, originalImageSkin, generatedImageFileExtension, allowedColourDistance)

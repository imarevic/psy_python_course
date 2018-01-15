import pygame

def text_object(text, font, width, height):
    """splits text by lines and renders each line."""
    paragraphSize = (width, height)
    fontSize = font.get_height()

    # create a surface for the text paragraph
    paragraphSurface = pygame.Surface(paragraphSize)

    # set colorkey to create transparent paragraph surface
    paragraphSurface.fill((255, 255, 255))
    paragraphSurface.set_colorkey((255, 255, 255))

    # split the lines of the text block
    splitLines = text.splitlines()

    # center the text vertically
    offSet = (paragraphSize[1] - len(splitLines) * (fontSize + 1)) // 2

    # loop over lines and blit each line
    for idx, line in enumerate(splitLines):
        currentTextline = font.render(line, False, (0, 0, 0))
        currentPosition = ((paragraphSize[0] - currentTextline.get_width()) // 2, #x-coordinate
                idx * fontSize + offSet) #y-coordinate
        paragraphSurface.blit(currentTextline, currentPosition)

    # return the surface
    return paragraphSurface


def text_object_blit_wrapped(surface, text, font, width, height, position, color):
    """
    blits text on multiple lines while wrapping text onto new
    line whenever it exeeds the width that is specified.
    """

    # get list of words row wise
    words = [word.split(' ') for word in text.splitlines()]
    # get size of spaces
    space = font.size(' ')[0]
    # unpack tuple for x and y coordinates of the text object
    xPos, yPos = position

    # iterate over words and lines
    for line in words:
        for word in line:
            # create word surface and get width and hieght of current word
            wordSurface = font.render(word, 0, color)
            wordWidth, wordHeight = wordSurface.get_size()

            # check if new line needs to be satrted
            if xPos + wordWidth >= width:
                # reset position to new line coordinates
                xPos = position[0]
                yPos += wordHeight

            # blit current word and update position
            surface.blit(wordSurface, (xPos, yPos))
            xPos += wordWidth + space

        # reset positions for each new line
        xPos = position[0]
        yPos += wordHeight

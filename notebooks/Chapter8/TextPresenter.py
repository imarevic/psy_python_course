import pygame

def text_object(text, font, width, height):
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

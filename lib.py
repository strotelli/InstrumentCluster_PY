import pygame
import serial
import pygame.gfxdraw
import re
pygame.init()
print('hello world')
#colors

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 16, 16)
blue = (0, 0, 255)
grey = (40, 40, 40)
screen_width = 1366
screen_height = 720

guage = pygame.image.load("Guage.png")

def ScreenLoop():



    ScreenLoop()
    return []
def GetScreenSize():

    infoString = str(pygame.display.Info())
    width = re.search('current_w = (\d+),', infoString).group(1)
    height = re.search('current_h = (\d+)', infoString).group(1)
    resolution = (width, height)
    return resolution
    GetScreenSize()
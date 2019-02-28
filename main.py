import pygame
import serial
import pygame.gfxdraw

def main():
    #ser = serial.Serial("/dev/ttyACM0", 9600)
    gameClock = pygame.time.Clock()
    screen_width = 1366
    screen_height = 720
    move_speed = 2
    main_surface = pygame.display.set_mode((screen_width, screen_height))
    pygame.init()
    info = pygame.display.Info()
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 16, 16)
    blue = (0, 0, 255)
    grey = (40, 40, 40)
    gear = ("N", "1", "2", "3", "4", "5", "6")
    speed = 0
    my_font = pygame.font.SysFont("", 100)
    my_font.set_bold(True)
    my_font.set_italic(True)
    small_rect = (300, 200, 150, 5)
    #needle = pygame.transform.rotozoom(pygame.image.load("needle.png"), 90, 1)
    guage = pygame.image.load("Guage.png")
    #guage = pygame.transform.scale(guage, (500, 500))
    text_surface = my_font.render(str(speed) + "mph", True, white)
    gear_surface = my_font.render(gear[0], True, red)
    loop = True
    i = 0
    while loop:
        #print(ser.readline())
        ev = pygame.event.get()
        for k in ev:
            if k.type == pygame.KEYDOWN:
                if k.key == pygame.K_ESCAPE:
                    print("esc")
                    loop = False
                    break
                if k.key == pygame.K_m:
                    i = 0
                    while i < 100:
                        screen_width += move_speed
                        i += 1
                        main_surface.fill(grey)
                        pygame.gfxdraw.filled_circle(main_surface, int(screen_width / 2), int(screen_height / 2), 260, white)
                        pygame.gfxdraw.aacircle(main_surface, int(screen_width / 2), int(screen_height / 2), 260, white)
                        pygame.gfxdraw.filled_circle(main_surface, int(screen_width / 2), int(screen_height / 2), 250, grey)
                        pygame.gfxdraw.aacircle(main_surface, int(screen_width / 2), int(screen_height / 2), 250, grey)
                        main_surface.blit(text_surface, ((screen_width / 2) - 70, (screen_height / 2) - 50))
                        pygame.draw.rect(main_surface, white, (int(screen_width / 2) - 75, int(screen_height / 2), 150, 5))
                        pygame.display.update()
                if k.key == pygame.K_n:
                    print("")
                if k.key == pygame.K_s:
                    speed += 1
                    text_surface = my_font.render(str(speed) + "mph", True, white)
                if k.key == pygame.K_SPACE:
                    if i < 6:
                        i += 1
                        gear_surface = my_font.render(gear[i], True, red)
                if k.key == pygame.K_BACKSPACE:
                    if i > 0:
                        i -= 1



                        gear_surface = my_font.render(gear[i], True, red)
            if k.type == pygame.QUIT:
                loop = False
        #print(ser.readline())
        main_surface.fill(grey)
        main_surface.blit(guage, ((screen_width / 2) - 300, 100))
        main_surface.blit(gear_surface, ((screen_width / 2) - 20, (screen_height / 2) + 10))
        main_surface.blit(text_surface, ((screen_width / 2) - 500, (screen_height / 2) + 10))
        #pygame.gfxdraw.filled_circle(main_surface, int(screen_width / 2), int(screen_height / 2), 260, white)
        #pygame.gfxdraw.aacircle(main_surface, int(screen_width / 2), int(screen_height / 2), 260, white)
        #pygame.gfxdraw.filled_circle(main_surface, int(screen_width / 2), int(screen_height / 2), 250, grey)
        #pygame.gfxdraw.aacircle(main_surface, int(screen_width / 2), int(screen_height / 2), 250, grey)

        #pygame.draw.rect(main_surface, white, (int(screen_width / 2) - 75, int(screen_height /2), 150, 5))
        #main_surface.blit(needle, ((screen_width / 2) - 130, (screen_height / 2) - 120))
        pygame.display.update()
    pygame.quit()
main()



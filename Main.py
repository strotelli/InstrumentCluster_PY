import pygame
import serial
import pygame.gfxdraw

def main():
    #ser = serial.Serial("/dev/ttyACM0", 9600)
    screen_width = 1900
    screen_height = 1000
    move_speed = 2
    main_surface = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
    pygame.init()
    info = pygame.display.Info()
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    grey = (40, 40, 40)
    speed = 0
    my_font = pygame.font.SysFont("Courier", 45)
    my_font.set_bold(True)
    my_font.set_italic(True)
    small_rect = (300, 200, 150, 5)
    needle = pygame.transform.rotozoom(pygame.image.load("needle.png"), 90, 1)

    text_surface = my_font.render( str(speed) + "M/h", True, white)
    loop = True

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
                    i = 0
                    while i < 100:
                        screen_width -= move_speed
                        i += 1
                        main_surface.fill(grey)
                        pygame.gfxdraw.filled_circle(main_surface, int(screen_width / 2), int(screen_height / 2), 260, white)
                        pygame.gfxdraw.aacircle(main_surface, int(screen_width / 2), int(screen_height / 2), 260, white)
                        pygame.gfxdraw.filled_circle(main_surface, int(screen_width / 2), int(screen_height / 2), 250, grey)
                        pygame.gfxdraw.aacircle(main_surface, int(screen_width / 2), int(screen_height / 2), 250, grey)
                        main_surface.blit(text_surface, ((screen_width / 2) - 70, (screen_height / 2) - 50))
                        pygame.draw.rect(main_surface, white, (int(screen_width / 2) - 75, int(screen_height / 2), 150, 5))
                        pygame.display.update()
                if k.key == pygame.K_SPACE:
                    text_surface = my_font.render(str(speed) + "M/h", True, white)
                    speed += 1
                if k.key == pygame.K_BACKSPACE:
                    text_surface = my_font.render(str(speed) + "M/h", True, white)
                    if speed > 0:
                        speed -= 1
            if k.type == pygame.QUIT:
                loop = False
        #print(ser.readline())
        main_surface.fill(grey)
        pygame.gfxdraw.filled_circle(main_surface, int(screen_width / 2), int(screen_height / 2), 260, white)
        pygame.gfxdraw.aacircle(main_surface, int(screen_width / 2), int(screen_height / 2), 260, white)
        pygame.gfxdraw.filled_circle(main_surface, int(screen_width / 2), int(screen_height / 2), 250, grey)
        pygame.gfxdraw.aacircle(main_surface, int(screen_width / 2), int(screen_height / 2), 250, grey)
        main_surface.blit(text_surface, ((screen_width / 2) - 70, (screen_height / 2) - 50))
        pygame.draw.rect(main_surface, white, (int(screen_width / 2) - 75, int(screen_height /2), 150, 5))
        main_surface.blit(needle, ((screen_width / 2) - 130, (screen_height / 2) - 120))
        pygame.display.update()

    pygame.quit()
main()



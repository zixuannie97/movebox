import pygame
import os

pygame.init()

screen = pygame.display.set_mode((400, 300))
skinfilename = os.path.join('borgao.png')

try:
    skin = pygame.image.load(skinfilename)
except pygame.error as msg:
    print('cannot load skin')
    raise SystemExit(msg)

skin = skin.convert()

screen.fill(skin.get_at((0, 0)))

clock = pygame.time.Clock()
pygame.key.set_repeat(200, 50)

while True:
    clock.tick(60)
    pass

for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    #option your keyborad
    elif event.type == KEYDOWN:
        if event.key == K_LEFT:
            pass

        elif event.key == K_UP:
            pass

        elif event.key == K_RIGHT:
            pass

        elif event.key == K_DOWN:
            pass

        elif event.key == K_BACKSPACE:
            pass

        elif event.key == K_SPACE:
            pass

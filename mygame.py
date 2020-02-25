import pygame, sys, os
from pygame.locals import *

pygame.init()

class Sokoban:

    def __init__(self):
        self.level = list(
            "----#####----------"
            "----#---#----------"
            "----#$--#----------"
            "--###--$##---------"
            "--#--$-$-#---------"
            "###-#-##-#---######"
            "#---#-##-#####--..#"
            "#-$--$----------..#"
            "#####-###-#@##--..#"
            "----#-----#########"
            "----#######--------")

        # 19coloum
        self.w = 19

        # 11raw
        self.h = 11

        # man first locate self.level[163]
        self.man = 163

    def draw(self, screen, skin):
        w = skin.get_width() / 4
        for i in range(0, self.w):
            for j in range(0, self.h):

                screen.blit(skin, (i*w, j*w), (0, 0, w, w))
                item = self.level[j*self.w + i]

                if item == '#':
                    # ??pygame?blit?????????????
                    # ?????(i*w, j*w)????skin????????(0,2*w,w,w)
                    screen.blit(skin, (i*w, j*w), (0,2*w,w,w))
                # ????????-
                elif item == '-':
                    screen.blit(skin, (i*w, j*w), (0,0,w,w))
                # ????????@
                elif item == '@':
                    screen.blit(skin, (i*w, j*w), (w,0,w,w))
                # ?????????$
                elif item == '$':
                    screen.blit(skin, (i*w, j*w), (2*w,0,w,w))
                # ??????????.
                elif item == '.':
                    screen.blit(skin, (i*w, j*w), (0,w,w,w))
                # ???????????????
                elif item == '+':
                    screen.blit(skin, (i*w, j*w), (w,w,w,w))
                # ?????????????????
                elif item == '*':
                    screen.blit(skin, (i*w, j*w), (2*w,w,w,w))

    def _move(self, d):
        h = get_offset(d, self.w)
        if self.level[self.man + h] == '-' or self.level[self.man + h] == '.':
            move_man(self.level, self.man + h)
            move_floor(self.level, self.man)
            self.man += h
            self.solution += d

        elif self.level[self.man + h] == '*' or self.level[self.man + h] == '$':
            h2 = h * 2

            if self.level[self.man + h2] == '-' or self.level[self.man + h2] == '.':
                move_box(self.level, self.man + h2)
                move_man(self.level, self.man + h)

                move_floor(self.level, self.man)

                self.man += h
                self.solution += d.upper()
                self.push += 1



screen = pygame.display.set_mode((400, 300))
skinfilename = os.path.join('borgar.png')

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

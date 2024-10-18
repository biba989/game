from pygame import *
from random import *
win = display.set_mode((1366, 768))
display.set_caption('кoсмос')
win2 =image.load('pole.png')
display.set_icon(win2)
backG = transform.scale(image.load('pole.png'),(1366, 768))
font.init()
font0 = font.SysFont('consolas',35)





class GameSprite(sprite.Sprite):
    def __init__(self, x, y, speed, player_image, w=80, h=80):
        super().__init__()
        self. image = transform.scale(image.load(player_image), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def drow(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

speed_y = -5 
speed_x = -5




class Playr (GameSprite):
    def __init__(self, x, y, speed, player_image, w=80, h=80):
        super().__init__(x, y, speed, player_image, w, h)
        self.isreloading = False
        self.youbusted = False
        self.time = 0
    def walkl (self):
        keys = key.get_pressed()
        self.time -= 1
        if keys[K_s]: 
            self.rect.y += self.speed
        if keys[K_w] :
            self.rect.y-= self.speed


    def walkr (self):
        keys = key.get_pressed()
        self.time -= 1
        if keys[K_DOWN]: 
            self.rect.y += self.speed
        if keys[K_UP] :
            self.rect.y-= self.speed

ball = GameSprite(683, 384, 30, 'ball.png', 100, 50)
plaeyr1 = Playr(0, 350, 20, 'vorota.png', 100, 150 )
plaeyr2 = Playr(1200,350, 20, 'vorota2.png', 100, 150 )
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    win.blit(backG,(0,0))
    ball.rect.x +=speed_x
    ball.rect.y +=speed_y
    if ball.rect.y<0 or ball.rect.y > 650:
        speed_y *= -1
    plaeyr1.walkl()
    plaeyr2.walkr()
    ball.drow()
    plaeyr1.drow()
    plaeyr2.drow()





















    display.update()
    time. delay(60)
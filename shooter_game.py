from pygame import * #подключаю бибилотеку pygame
from random import *



class GameSprite(sprite.Sprite): #
   def __init__(self, image_sprite, img_x, img_y, speed, w_r, h_r):
       super().__init__()
       self.image = transform.scale(image.load(image_sprite),(65,65))
       self.speed = speed
       self.rect = self.image.get_rect()
       self.rect.x = img_x
       self.rect.y = img_y
  
   def show_s(self):
       window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_a] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_d] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
     def fire (self):
        pul = Puly(img_bullet, self.rect.centerx, self.rect.top, 15,20, 15)
        bullets.add(pul)



class Enemy (GameSprite):
    def update(self):
        global prop
        self.rect.y += self.speed
        if self.rect.y > win_hight:
            self.rect.y = 0
            self.rect.x = randint(80,win_width-80)
            prop += 1


class Pulya (GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()



win_width = 700
win_hight = 500


window = display.set_mode((win_width,win_hight))
display.set_caption("Лабиринт")


backgraund = transform.scale(image.load("galaxy.jpg"),(win_width,win_hight))


player = Player("rocket.png",5, win_hight-70, 4, 60,70)

monsters = sprite.Group()

bullets = sprite.Group()

for i in range (6):
    en1 = Enemy("ufo.png",randint(80, win_width - 80),-40, randint(1,5),80,50)
    monsters.add(en1)



game = True
finish = False


clock = time.Clock()


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()


font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

prop = 0

img_bullet = "bullet.png"

while game:
   for i in event.get():
       if i.type == QUIT:
           game = False
       if i.type == KEYDOWN:
           if i.key == K_SPASE:
               player.fire()
  
   if finish != True:
       window.blit(backgraund,(0,0))
       player.show_s()
       player.update()


       monsters.update()
       monsters.draw (window)


    bullets.update()
    bullets.draw(window)

    collides = sprite.groupcollide(monsters, bullets, True, True)


   display.update()
   clock.tick(60)

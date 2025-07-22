from random import randint
from pygame import *
from time import time as timer
time1 = timer()
mixer.init()
font.init()
fire = mixer.Sound('fire.ogg')
font = font.SysFont('Arial',30)
mixer.music.load('space.ogg')
window = display.set_mode((700,500))
display.set_caption('')
clock = time.Clock()
fps = 60
bak_r = transform.scale(image.load('galaxy.jpg'),(700,500))
monsters = sprite.Group()
bullets = sprite.Group()
asteroids = sprite.Group()
num1 = 0
num2 = 0
game = True
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,player_speed,height,weight):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (height, weight))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed 
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x <595:
            self.rect.x += self.speed
    def firi(self):
        bullet = Bullet('bullet.png',player.rect.x,player.rect.y,15,15,15)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        global num2
        if self.rect.y <= 470:
            self.rect.y +=self.speed
        elif self.rect.y >=470:
            self.rect.x = randint(20,650)
            self.rect.y = 0
            self.reset()
            num2 +=1
class Asteroids(GameSprite):
    def update(self):
        global num2
        if self.rect.y <= 470:
            self.rect.y +=self.speed
        elif self.rect.y >=470:
            self.rect.x = randint(20,650)
            self.rect.y = 0
            self.reset()
class Bullet(GameSprite):
    def update(self):
        if self.rect.y>0:
            self.rect.y -= self.speed
        elif self.rect.y<20 or sprite.collide_rect(bullet,enemy):
            self.remove(bullets)
player = Player('rocket.png',315,400,6,50,70)
col_vo = 0
finish = False
for i in range(6):
    enemy = Enemy('ufo.png',randint(20,650),0,randint(1,2),50,70)
    monsters.add(enemy)
for i in range(6):
    asteroid = Asteroids('asteroid.png',randint(20,650),0,randint(1,2),30,40)
    asteroids.add(asteroid)
while game:
    keys_pressed = key.get_pressed()
    clock.tick(fps)
    mixer.music.play()
    window.blit(bak_r,(0,0))
    num1_text = font.render('Счёт: '+str(num1),1,(255,255,255))
    num2_text = font.render("Пропущено: "+str(num2),1,(255,255,255))
    window.blit(num1_text,(10,20))
    window.blit(num2_text,(10,50))
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type==KEYDOWN:
            if e.key == K_SPACE:
                player.firi()
                fire.play()

    if not finish:
        bullets.draw(window)
        bullets.update()
        asteroids.draw(window)
        asteroids.update()
        monsters.draw(window)
        monsters.update()
        player.update()
        player.reset()
        colleder = sprite.groupcollide(monsters,bullets,True,True)
        for i in colleder:
            enemy = Enemy('ufo.png',randint(20,650),0,randint(1,5),50,70)
            monsters.add(enemy)
            num1+=1
        if sprite.spritecollide(player, monsters,False) or num2>=3 or sprite.spritecollide(player, asteroids,False):
            finish = True
            window.blit(bak_r,(0,0))
            time2 = timer()
            text_lose = font.render('YOU LOSE!',1,(255,255,255))
            timeer = font.render('Время игры:' + str(int(time2-time1)) + 'cекунд/ы',1,(255,255,255))
            window.blit(timeer,(200,220))
            window.blit(text_lose,(200,200))
        if num1>=10:
            finish = True
            window.blit(bak_r,(0,0))
            time2 = timer()
            text_win = font.render('YOU WIN!',1,(255,255,255))
            timeer = font.render('Время игры:' + str(int(time2-time1)) + 'cекунд/ы',1,(255,255,255))
            window.blit(timeer,(200,220))
            window.blit(text_win,(200,200))
        display.update() 



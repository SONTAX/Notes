import pygame.sprite
from pygame import*
from random import randint


class GameSprite(sprite.Sprite):
    def __init__(self, imag, x, y, width, height,speed):
        super().__init__()
        self.image = transform.scale(image.load(imag), (width, 75))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.y, 12, 25, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            global lost
            lost += 1
            self.rect.y = 0
            self.rect.x = randint(0, WIDTH - self.rect.width)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


WIDTH = 800
HEIGHT = 600
lost = 0
score = 0

window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Spyce Chooter")
bullets = sprite.Group()
fon = transform.scale(image.load("cosmos.jpg"), (WIDTH, HEIGHT))

player = Player("rocket.png", 320, 500, 70, 100, 5)

enemies = sprite.Group()
enemy = Enemy("ufo.png", 30, -120, 70, 70, 3)
enemies.add(enemy)
enemy = Enemy("ufo.png", 200, 60, 70, 70, 3)
enemies.add(enemy)
enemy = Enemy("ufo.png", 450, 0, 70, 70, 3)
enemies.add(enemy)

font.init()
font1 = font.SysFont("times new roman", 80)
font2 = font.SysFont("comic sans ms", 30)


game = True
run = True
health = 3

clock = time.Clock()

while game:
    window.blit(fon, (0,0))
    if run:
        for e in event.get():
            if e.type == QUIT:
                game = False
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    player.fire()

        enemies.draw(window)
        bullets.draw(window)
        player.reset()
        player.update()
        enemies.update()
        bullets.update()
        text = font2.render("Rahunok:" + str(score), True, (255, 255, 255))
        window.blit(text, (10, 0))
        text = font2.render("Пропущено:" + str(lost), True, (255, 255, 255))
        window.blit(text, (10, 35))
        text = font2.render("Життя:" + str(health), True, (255, 255, 255))
        window.blit(text, (10, 70))
        collides = sprite.groupcollide(enemies, bullets, True, False)
        for _ in range(len(collides)):
            enemy = Enemy("ufo.png", randint(0, WIDTH - 70), -50, 70, 70, 2)
            enemies.add(enemy)
            score += 1
        if lost > 1:
            health = 2
        if lost > 2:
            health = 1
        if lost > 3:
            health = 0
        if health == 0:
            run = False
            lost_text = font1.render("Game False", True, (180, 50, 50))
        if score > 15:
            run = False
            lost_text = font1.render("You WIN :)", True, (50, 180, 50))

    else:
        window.blit(lost_text, (240, 220))


    display.update()
    clock.tick(60)





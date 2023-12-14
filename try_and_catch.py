from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (85, 85))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 615:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 415:
            self.rect.y += self.speed


class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 400:
            self.direction = 1
        if self.rect.x >= 580:
            self.direction = -1
        self.rect.x += self.speed * self.direction


class Wall(sprite.Sprite):
    def __init__(self, color, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color = color
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


window = display.set_mode((700, 500))
display.set_caption("Maze")
background = transform.scale(image.load("background.png"), (700, 500))

player = Player("hero.png", 20, 20, 4)
enemy = Enemy("pacman.png", 400, 300, 4)
treasure = GameSprite("coin.png", 600, 400, 0)

walls = []
wall = Wall((255, 255, 0), 150, 50, 300, 15)
walls.append(wall)
wall = Wall((255, 255, 0), 150, 200, 15, 200)
walls.append(wall)
wall = Wall((255, 255, 0), 380, 300, 15, 200)
walls.append(wall)

font.init()
font1 = font.SysFont("comic sans ms", 70)

game = True
run = True
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    if run:
        player.update()
        enemy.update()
        player.reset()
        enemy.reset()
        treasure.reset()
        for wall in walls:
            wall.draw_wall()
            if sprite.collide_rect(player, wall):
                run = False
                text = font1.render("Ви програли)))", True, (0, 0, 0))
        if sprite.collide_rect(player, enemy):
            run = False
            text = font1.render("Ви програли)))", True, (0, 0, 0))
        if sprite.collide_rect(player, treasure):
            run = False
            text = font1.render("Ви ПЕРЕМОГЛИ(((", True, (0, 0, 0))
    else:
        window.blit(text, (100, 150))
    display.update()
    clock.tick(60)

from pygame import*

window = display.set_mode((800,600))
display.set_caption("pm bs2 brainrot")
background = transform.scale(image.load("gebura.jpg"), (900, 700))

clock = time.Clock()
fps = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 600 - 80:
            self.rect.y += self.speed
        if keys[K_RIGHT] and self.rect.x < 800 - 80:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 700 - 80:
            self.direction = "left"
        #if self.rect.y <= 470:
            #self.direction = "down"
        #if self.rect.y >= 700 - 80:
            #self.direction = "up"

        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

w1 = Wall(0, 0, 0, 300, 100, 10, 400)
w2 = Wall(0, 0, 0, 150, 100, 200, 10)
w3 = Wall(0, 0, 0, 150, 100, 10, 300)
w4 = Wall(0, 0, 0, 150, 100, 10, 300)

sprite1 = Player("png2.png", 200, 200, 8)
sprite2 = Enemy("xalice.png", 200, 100, 8)
sprite3 = GameSprite("door.png", 500, 320, 10)

game_finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    
    if game_finish != True:
        window.blit(background,(-50, -50))
        sprite1.update()
        sprite2.update()
        sprite3.update()
        sprite1.reset()
        sprite2.reset()
        sprite3.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()

        if sprite.collide_rect(sprite1, game_finish) or sprite.collide_rect(sprite2, Enemy) or sprite.collide_rect(sprite3, GameSprite) or sprite.collide_rect(sprite3, w2) or sprite.collide_rect(sprite3, w3) or sprite.collide_rect(sprite3, w4):
            finish = True
            #money.play()

    display.update()
    clock.tick(fps)

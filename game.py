from pygame import*

window = display.set_mode((700,500))
display.set_caption("pm bs2 brainrot")
background = transform.scale(image.load("gebura.jpg"), (800, 600))

clock = time.Clock()
fps = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
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
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
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

sprite1 = Player("png2.png", 200, 200, 10)
sprite2 = Enemy("xalice.png", 200, 100, 10)
sprite3 = GameSprite("door.png", 500, 200, 10)

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

    display.update()
    clock.tick(fps)

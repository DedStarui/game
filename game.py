from pygame import*

window = display.set_mode((800,600))
display.set_caption("pm bs2 brainrot")
background = transform.scale(image.load("abn.webp"), (900, 700))

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
        if self.rect.x <= 600:
            self.direction = "right"
        if self.rect.x >= 820 - 80:
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

w1 = Wall(0, 0, 0, 300, 100, 10, 500)
w2 = Wall(0, 0, 0, 150, 100, 200, 10)
w3 = Wall(0, 0, 0, 150, 100, 10, 400)
w4 = Wall(0, 0, 0, 410, 0, 10, 500)
w5 = Wall(0, 0, 0, 150, 200, 90, 10)
w6 = Wall(0, 0, 0, 220, 300, 90, 10)
w7 = Wall(0, 0, 0, 150, 400, 90, 10)
w8 = Wall(0, 0, 0, 410, 500, 280, 10)
w9 = Wall(0, 0, 0, 680, 100, 10, 400)
w10 = Wall(0, 0, 0, 410, 100, 190, 10)
w11 = Wall(0, 0, 0, 600, 100, 10, 300)
w12 = Wall(0, 0, 0, 410, 400, 115, 10)


player = Player("png2.png", 200, 120, 5)
sprite2 = Enemy("xalice.png", 400, 140, 4.5)
sprite3 = GameSprite("door.png", 490, 150, 10)

font.init()
font = font.Font(None, 70)
win = font.render('You survived.', True, (139, 0, 0))
loss = font.render('Loser.', True, (139,0,0))

game_finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if game_finish != True:
        window.blit(background,(-50, -50))
        player.update()
        sprite2.update()
        sprite3.update()
        player.reset()
        sprite2.reset()
        sprite3.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()  
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()





        if sprite.collide_rect(player, sprite2) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or  sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10) or sprite.collide_rect(player, w11) or sprite.collide_rect(player, w12):
            game_finish = True
            #money.play()

            window.blit(loss,(330,200))
        if sprite.collide_rect(player, sprite3):
            window.blit(win,(330,200))
            game_finish = True

    display.update()
    clock.tick(fps)

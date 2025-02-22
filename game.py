from pygame import*
window = display.set_mode((700, 500))
display.set_caption("pm bs2 brainrot")
background = transform.scale(image.load("gebura.jpg"), (800, 600))
sprite1 = transform.scale(image.load("xalice.png"), (100, 100))
sprite2 = transform.scale(image.load("png1.png"), (100, 100))
x1 = 100
y1 = 200
x2 = 200
y2 = 200

clock = time.Clock()
fps = 60
clock.tick(fps)

game = True
while game:
    window.blit(background,(-50, -50))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys = key.get_pressed()
    if keys[K_UP] and y1 > 5:
        y1 -= 10
    if keys[K_DOWN] and y1 < 395:
        y1 += 10
    if keys[K_RIGHT] and x1 > 5:
        x1 += 10
    if keys[K_LEFT] and x1 < 395:
        x1 -= 10
    elif keys[K_s] and y2 < 395:
        y2 += 10 


    display.update()
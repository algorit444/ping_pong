from pygame import *

display.set_caption("Ping Pong")
window = display.set_mode((480, 360))

timer = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    timer.tick(60)

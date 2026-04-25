from pygame import *

display.set_caption("Ping Pong")
window = display.set_mode((800, 600))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

racket1 = Player("racket.png", 15, 250, 25, 100, 4)
racket2 = Player("racket.png", 765, 250, 25, 100, 4)
ball = GameSprite("tenis_ball.png", 400, 270, 30, 30, 4)

timer = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((255,255,255))
    ball.reset()
    racket1.update_l()
    racket1.reset()
    racket2.update_r()
    racket2.reset()
    display.update()
    timer.tick(60)

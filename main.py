from pygame import *
display.set_caption("Ping Pong")
window = display.set_mode((800, 600))

font.init()
font1 = font.SysFont('Arial', 80)
win1 = font1.render('Player 1 won!', True, (255, 0, 0))
win2 = font1.render('Player 2 won!', True, (0, 0, 255))
font2 = font.SysFont('Arial', 60)

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
ball = GameSprite("tenis_ball.png", 400, 270, 30, 30, 0)
b_sx = 3
b_sy = -5
timer = time.Clock()
score1 = 0
score2 = 0
game = True
finish = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish:
        window.fill((255,255,255))
        ball.reset()
        ball.rect.x+=b_sx
        ball.rect.y+=b_sy
        if ball.rect.y<0 or ball.rect.y>570:
            b_sy*=-1
        if ball.rect.colliderect(racket1.rect) or ball.rect.colliderect(racket2.rect):
            b_sx*=-1
        if ball.rect.x>800:
            score1+=1
            ball.rect.x, ball.rect.y = 400,270
            if score1 > 4:
                window.blit(win1, (200, 250))
                finish = False
        elif ball.rect.x<0:
            score2+=1
            ball.rect.x, ball.rect.y = 400,270
            if score2 > 4:
                window.blit(win2, (200, 250)) 
                finish = False
        scoretxt1 = font2.render(str(score1), True, (0, 0, 0))
        scoretxt2 = font2.render(str(score2), True, (0, 0, 0))
        window.blit(scoretxt1, (100, 50))
        window.blit(scoretxt2, (700, 50))

        racket1.update_l()
        racket1.reset()
        racket2.update_r()
        racket2.reset()
        display.update()
    timer.tick(60)

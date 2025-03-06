from pygame import *
from random import randint
from time import time as timer

##creando clases
class GameSprite(sprite.Sprite):
    ## constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        ## llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)
 
        ## cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        ## cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    ## método que dibuja al personaje en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed

##creando la escena del juego
back = (200, 255, 255)
img_back=('img_back.jpg')
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

##creando estado de juego
game = True
finish = False
clock = time.Clock()
FPS = 60

##creando los objetos
racket1 = Player('racket.png', 30, 200, 50, 100, 10)
racket2 = Player('racket.png', 540, 200, 50, 100, 10)
ball = GameSprite('asteroide.png', 200, 200, 50, 50, 50)

##textos para el juego
font.init()
font = font.Font(None, 35)
loseracket1 = font.render('Player 1 looses!!', True, (180, 0, 0))
loseracket2 = font.render('Player 2 looses!!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

##ciclo de juego
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        #actualizando raquetas#
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        #actualizando pelota#
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height -50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True 
            window.blit(loseracket1, (200, 200))
            game_over = True

        if ball.rect.x > win_width:
            finish = True 
            window.blit(loseracket2, (200, 200))
            game_over = True

        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
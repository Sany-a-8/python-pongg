from pygame import*


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,width,height):
        super().__init__()
        self.image=tranform.scale(image.load(player_image),(width,height))
        self.rect=self.image.get_rect()
        self.x=player_x
        self.y=player_y
        self.speed=player_speed
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_r(self):
        key=key.get_pressed()
        if key[K_UP] and self.rect.y<0:
            self.rect.y-=self.speed
        if key[K_DOWN] and self.rect.y>widht-80:
            self.rect.y+=self.speed
    def update_l(self):
        key=key.get_pressed()
        if key[K_w] and self.rect.y<0:
            self.rect.y-=self.speed
        if key[K_s] and self.rect.y>widht-80:
            self.rect.y+=self.speed
    
            
racket1=Player("racket.png",50,200,4,50,150)
racket2=Player("racket.png",350,200,4,50,150)
        

width=600
height=600

mw=display.set_mode((width,height))
mw.fill((100,100,255))
display.set_caption("Пінг Понг")

clock=time.Clock()

game=True
finish=False
FPS=60

speed_x=3
speed_y=3

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False

    if finish!=True:
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
        
    ball.update()

    if ball.rect.y>width-50 or ball.rect.y<0:
        speed_y*=-1

    display.update()
    clock.tick(FPS)

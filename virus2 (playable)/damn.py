import pygame
import sys
import math
import random
pygame.init()
running=True
pritisnuoexit=0

#prozor
display=pygame.display.set_mode((1280,720))
sat=pygame.time.Clock()
#icon
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("<--- erik")

#player-------------
quandale=pygame.image.load("mrik.png")

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.brzx=0
        self.brzy=0
        self.W_press = False
        self.A_press = False
        self.S_press = False
        self.D_press = False
        self.brzina = 2.5
        
    def draw(self, display):
        display.blit(quandale, (self.x, self.y))
        
    def main(self):
        self.brzx=0
        self.brzy=0
        if self.D_press and not self.A_press:
            self.brzx = self.brzina
        if self.A_press and not self.D_press:
            self.brzx = -self.brzina
        if self.W_press and not self.S_press:
            self.brzy = -self.brzina
        if self.S_press and not self.W_press:
            self.brzy = self.brzina

        self.x = self.x + self.brzx
        self.y = self.y + self.brzy

player=Player(620,360, 100, 100)

#enemy-----------------

class Enemy1 :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        self.animation_images = [pygame.image.load("hank1.png"), pygame.image.load("hank2.png")]
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = random.randrange(-150, 150)
        self.offset_y = random.randrange(-150, 150)
    def main(self, display):
        if self.animation_count + 1 == 128 :
            self.animation_count = 0
        self.animation_count+= 1

        if self.reset_offset == 0:
            self.offset_x = random.randrange(-150, 150)
            self.offset_y = random.randrange(-150, 150)
            self.reset_offset=random.randrange(120, 150)
        else:
            self.reset_offset -= 1
        
        if player.x + self.offset_x > self.x  :
            self.x += 1
        elif player.x + self.offset_x < self.x  :
            self.x -= 1
        if player.y + self.offset_y > self.y  :
            self.y += 1
        elif player.y + self.offset_y < self.y :
            self.y -= 1
        display.blit(pygame.transform.scale(self.animation_images[self.animation_count//64], (50, 50)), (self.x, self.y))
        
            
enemies = [Enemy1(player.x+100, player.y+100)]                                 




#metak-------------
bullets = []
metak = pygame.image.load("metak.png")
class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15
        self.angle = math.atan2(mouse_y - self.y, mouse_x - self.x)
        self.velx = math.cos(self.angle) * self.speed
        self.vely = math.sin(self.angle) * self.speed
        
        self.lifetime = 300
    def draw(self,draw):
        self.x += (self.velx)
        self.y += (self.vely)
        metakrotated = pygame.transform.rotate(metak, 270 - self.angle * 57.29)
        display.blit(metakrotated, (self.x-10, self.y-10))
       
        self.lifetime -= 1
        



#main loop kontrola 
while running :
    display.fill((255,255,255))
    player.main()
    pritisnuoexit=0

    mouse_x, mouse_y = pygame.mouse.get_pos()
    #goddamn
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pritisnuoexit= 1
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.W_press = True
            if event.key == pygame.K_a:
                player.A_press = True
            if event.key == pygame.K_s:
                player.S_press = True
            if event.key == pygame.K_d:
                player.D_press = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.W_press = False
            if event.key == pygame.K_a:
                player.A_press = False
            if event.key == pygame.K_s:
                player.S_press = False
            if event.key == pygame.K_d:
                player.D_press = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullets.append(PlayerBullet(player.x + player.width/2, player.y + player.height/2, mouse_x,mouse_y))
                
    for bullet_ in bullets:
        if bullet_.lifetime <= 0:
            bullets.pop(bullets.index(bullet_))
        bullet_.draw(display)
    for enemy in enemies:
        enemy.main(display)
    player.draw(display)
    sat.tick(120)
    pygame.display.update()
    if pritisnuoexit == 1 :
        running=False
        pygame.quit()

   
   





















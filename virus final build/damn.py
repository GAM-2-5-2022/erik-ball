import pygame
import sys
import math
import random
pygame.init()
running=True
pritisnuoexit=0


#ahhhh
particles_spread = [0.5,0.75,1.25,1.5,1.75,2,2.1,2.15,2.2,2.25,2.35,2.45,2.55,2.65,2.75,2.85,2.90,3]


spawn_randx = list(range(-600, 1500))
del spawn_randx[-600:1800]
spawn_randy = list(range(-300,1400))
del spawn_randy[250:1600]
score = 0


#sound

deathsound = pygame.mixer.Sound("hitmarker.wav")
pygame.mixer.Sound.set_volume (deathsound, 0.01)
gameover = pygame.mixer.Sound("gameover.wav")
pygame.mixer.Sound.set_volume (gameover, 0.01)


if random.randint (1,2) == 1 :
    music = pygame.mixer.music.load("kass_theme.mp3")
    pygame.mixer.music.set_volume (0.01)
else:
    music = pygame.mixer.music.load("gangplank_galleon.mp3")
    pygame.mixer.music.set_volume (0.01)

pygame.mixer.music.play(-1)

#prozor
displaywid = 1440
displayhei = 1280
display=pygame.display.set_mode((displaywid,displayhei))
sat=pygame.time.Clock()
#icon
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("<--- erik")


#particles-----

#particle kad metak pogodi
class Particle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = math.cos(bullet.angle) * 0.16 * bullet.speed * random.choice(particles_spread)
        self.vely = math.sin(bullet.angle) * 0.17 * bullet.speed * random.choice(particles_spread)
        self.lifetime = 0
        
    def draw(self, display):
        self.lifetime += 1
        if self.lifetime < (random.randrange(0,100)) :
            self.x += self.velx
            self.y += self.vely
            pygame.draw.circle(display, (0,0,0), (self.x, self.y), 3.5)

           
        
particles = []

#particle kad metak nestane
class BulletParticle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = random.choice(particles_spread)
        self.vely = random.choice(particles_spread)
        self.lifetime = 0
    def draw(self, display):
        self.lifetime += 1
        if self.lifetime < (random.randrange(0,45)) :
            self.x += self.velx
            self.y += self.vely
            pygame.draw.circle(display, (0,0,0), (self.x, self.y), 2)
bulletparticles=[]
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
        self.brzina = 3
        self.hitbox = (self.x + 5, self.y + 5, 90, 90)
        self.dead = False
        self.play_gameover = True
        
        
    def draw(self, display):
        
        display.blit(quandale, (self.x, self.y))
        self.hitbox = (self.x + 5, self.y + 5, 90, 90)
      #  pygame.draw.rect(display, (255,0,0), self.hitbox, 3) -----hitbox za testiranje
        
    def main(self):
        self.brzx=0
        self.brzy=0
        if self.D_press and not self.A_press and player.x + 50 < displaywid :
            self.brzx = self.brzina
        if self.A_press and not self.D_press and player.x + 50 > 0:
            self.brzx = -self.brzina
        if self.W_press and not self.S_press and player.y + 50 > 0:
            self.brzy = -self.brzina
        if self.S_press and not self.W_press and player.y + 50 < displayhei:
            self.brzy = self.brzina

        self.x = self.x + self.brzx
        self.y = self.y + self.brzy
 #kad je player dotaknut (game over) -----------------------------------------------------------------------------------------------
    def hit(self):
        
        self.dead= True
        display.fill((0,0,0))
        player.W_press = False
        player.A_press = False
        player.S_press = False
        player.D_press = False
        scoretext = fontscore.render(str(int(score)), 1, (255,255,255))
        press_esc = fontscore.render("press ESC", 1, (255,255,255))
        display.blit(press_esc,(1440/2 - 58,1280/2 + 40 )) 
        display.blit(scoretext, (1440/2,1280/2))
        display.blit(pygame.transform.scale(enemy.animation_images[enemy.animation_count//64], (50, 50)), (enemy.x, enemy.y))
        pygame.draw.rect(display, (255,0,0), self.hitbox, 3)
        pygame.draw.rect(display, (255,0,0), enemy.hitbox, 2)
        enemy.animation_count = -1
        pygame.mixer.music.stop()
        if self.play_gameover == True:
            gameover.play()
            self.play_gameover = False
        
        
        
        
#init playera       
player=Player(620,360, 100, 100)

#enemy-----------------

class Enemy1 :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        self.animation_images = [pygame.image.load("hank1.png"), pygame.image.load("hank2.png")]
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = random.randrange(-200, 200)
        self.offset_y = random.randrange(-200, 200)
        self.hitbox = (self.x, self.y, 50, 50)
        self.health = 0
        self.visible = True
    def main(self, display):
        if self.animation_count + 1 == 128 :
            self.animation_count = 0
        self.animation_count+= 1

        if self.reset_offset == 0:
            self.offset_x = random.randrange(-200, 200)
            self.offset_y = random.randrange(-200, 200)
            self.reset_offset=random.randrange(120, 150)
        else:
            self.reset_offset -= 1
            #movement enemya, disableaj da se ne mice------------
            
        if self.animation_count > movement_delay :
            if player.x + self.offset_x > self.x  :
                self.x += 2
            elif player.x + self.offset_x < self.x  :
                self.x -= 2
            if player.y + self.offset_y > self.y  :
                self.y += 2
            elif player.y + self.offset_y < self.y :
                self.y -= 2
            
            #---------------------------------------------------
        if self.visible == True :
            display.blit(pygame.transform.scale(self.animation_images[self.animation_count//64], (50, 50)), (self.x, self.y))
            self.hitbox = (self.x, self.y, 50, 50)
            pygame.draw.rect (display, (0,0,0), self.hitbox, 2)
#kada metak pogodi enemya
    def hit(self) :
        bullet.visible = False
        for i in range (random.randrange(15,30)):
            particles.append(Particle(enemy.x + 25, enemy.y + 25))
        if self.health > 0 :
            self.health -= 1
        else:
            self.visible = False
            enemies.pop(enemies.index(enemy))
        deathsound.play()
            
enemies = []

#metak-------------
bullets = []
metak = pygame.image.load("metak.png")
class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 45
        self.angle = math.atan2(mouse_y - self.y, mouse_x - self.x)
        self.velx = math.cos(self.angle) * self.speed
        self.vely = math.sin(self.angle) * self.speed
        self.hitbox = (self.x-5, self.y-5, 25, 25)
        self.lifetime = 150
        self.visible = True
        
        
    def draw(self,draw):
        self.x += (self.velx)
        self.y += (self.vely)
        metakrotated = pygame.transform.rotate(metak, 270 - self.angle * 57.29)
        display.blit(metakrotated, (self.x-10, self.y-10))
        self.hitbox = (self.x-5, self.y-5, 25, 25)
        
        
       # pygame.draw.rect(display, (255,0,0), self.hitbox, 2)
       
        self.lifetime -= 1
        



#main loop kontrola
fontscore = pygame.font.SysFont("comicsans", 30)
fontostalo = pygame.font.SysFont("comicsans", 25)
while running :
    
    
    display.fill((255,255,255))
    player.main()
    pritisnuoexit=0

    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #goddamn

    #movement i spawn limit (povecavaju se kako se score povecava)-------------
    movement_delay = 70 - 4.5 * (score//20)
    spawn_limit = 1
    if score > 50 :
        spawn_limit = 6 + score//25
    else:
        spawn_limit += score//7
    # 120fps, frametime = 8.33 ms
    movement_delay_ms = int(movement_delay * 8.33)
    
    while len(enemies) < spawn_limit:
            enemies.append(Enemy1(random.choice(spawn_randx), random.choice(spawn_randy)))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                 pritisnuoexit = 1
        #--- ZA TESTIRANJE : POVECANJE SCORE (SPACE) -------
        """        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                score += 5
        """      
        #----------------------------------------------------       
        if event.type == pygame.QUIT:
            pritisnuoexit= 1
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w :
                player.W_press = True
            if event.key == pygame.K_a :
                player.A_press = True
            if event.key == pygame.K_s :
                player.S_press = True
            if event.key == pygame.K_d :
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
        if event.type == pygame.MOUSEBUTTONDOWN and enemy.animation_count != -1 and not player.dead :
            if event.button == 1:
                bullets.append(PlayerBullet(player.x + player.width/2, player.y + player.height/2, mouse_x,mouse_y))
                
                

                  
    for bullet in bullets:
        if bullet.lifetime <= 0:
            bullets.pop(bullets.index(bullet))
            for i in range (random.randrange(7,20)):
                bulletparticles.append(BulletParticle(bullet.x, bullet.y))
        if bullet.visible:
            bullet.draw(display)
        for enemy in enemies :
            if enemy.visible and bullet.visible :
                if (bullet.hitbox[1] + 3 < enemy.hitbox [1] + enemy.hitbox[3] and bullet.hitbox[1] + 3  > enemy.hitbox [1]) or (bullet.hitbox[1] + 20 < enemy.hitbox [1] + enemy.hitbox[3] and bullet.hitbox[1] + 20 > enemy.hitbox [1]):
                    if bullet.hitbox[0] + 3 > enemy.hitbox[0] and bullet.hitbox[0] + 3  < enemy.hitbox[0] + enemy.hitbox[2] or (bullet.hitbox[0] + 20 > enemy.hitbox[0] and bullet.hitbox[0] + 20 < enemy.hitbox[0] + enemy.hitbox[2]):
                        enemy.hit()
                        score+= 1
            

    for enemy in enemies:
        enemy.main(display)
        if enemy.visible :
            if player.hitbox[1] < enemy.hitbox [1] + enemy.hitbox[3] and player.hitbox[1] + player.hitbox [3]> enemy.hitbox [1]:
                    if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                        player.hit()
    
    for particle in particles :
        particle.draw(display)
        

    for particle in bulletparticles :
        particle.draw(display)
        
    player.draw(display)
    sat.tick(120)
    
    spawndelaytext = fontostalo.render("spawn limit : " + str(spawn_limit), 1, (0,0,0))
    movementdelaytext = fontostalo.render("movement delay : " + str(movement_delay_ms) + "ms", 1, (0,0,0))
    scoretext = fontscore.render(str(int(score)), 1, (0,0,0))
    
    display.blit(spawndelaytext, (25, 100))
    display.blit(movementdelaytext, (25, 140))
    display.blit(scoretext, (50, 25))
    
    pygame.display.update()
    
    if pritisnuoexit == 1 :
        running=False
        pygame.quit()
        quit()

   
   





















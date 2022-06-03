import pygame
pygame.init()
running=True

#prozor
display=pygame.display.set_mode((1280,720))
sat=pygame.time.Clock()
#icon
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("<--- erik")

#player-------------
quandale=pygame.image.load("brat.png")

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def main(self, display):
        pygame.draw.rect(display, (255,0,0), (self.x, self.x, self.width, self.height))
       




player=Player(400,300, 32, 32)


#main loop kontrola 
while running :
    display.fill((255,255,255))
    
    display.blit(player.surf, player.rect)


    #goddamn
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
    sat.tick(60)
    pygame.display.update()

   
   





















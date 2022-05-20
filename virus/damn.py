import pygame

def main():
    pygame.init()
    running=True
    #icon
    icon=pygame.image.load("icon.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("<--- erik")
    #prozor
    prozor=pygame.display.set_mode((1280,720))
    
    pygame.display.flip()
    #main loop kontrola 
    while running :
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()





















main()

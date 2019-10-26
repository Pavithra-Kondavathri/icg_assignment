	
"""import pygame
import time
 
pygame.init()
width = 600
height = 600
 
#make the pygame window
pygame.display.set_mode((width, height ) )
pygame.display.set_caption("clevergirl")
running = True
 
while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False"""



import pygame,sys
from os import system,name
from time import sleep 
import time;






# initialize game engine
pygame.init()
pygame.font.init()




window_width=600
window_height=600



animation_increment=10
clock_tick_rate=20


# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)
FACE=[255,224,189]
BLUE=[0,0,255]
BROWN=[139,69,19]


# Set title to the window
pygame.display.set_caption("clever girl")



dead=False


clock = pygame.time.Clock()
background_image = pygame.image.load("backgroundvillage.png").convert()
background_image= pygame.transform.scale(background_image, (600, 600))




while(dead==False):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
 
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pavithra/Downloads/smart.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    screen.blit(background_image, [0, 0])
    myfont=pygame.font.SysFont(pygame.font.get_default_font(),60)
    textsurface=myfont.render('THE CLEVER GIRL',True,(0,0,0))
    screen.blit(textsurface,(120,60))
    YPOS = 350
    XPOS = 350
    POS=(XPOS,YPOS)
    RADIUS=20
   

    pygame.draw.circle(screen,FACE, POS, RADIUS)
    pygame.display.update()
    pygame.draw.polygon(screen,BLUE,[[350,370],[400,420],[300,420]])
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(375,420,10,40))
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(325,420,10,40))
    pygame.display.update()
    time.sleep(3)



    
    """second forest sceen"""
    background_image1=pygame.image.load("forest.png").convert()
    background_image1=pygame.transform.scale(background_image1,(600,600))
    screen.blit(background_image1,[0,0])
    pygame.display.update()
    XPOS1=350
    YPOS1=550
    POS1=(XPOS1,YPOS1)
    pygame.draw.circle(screen,FACE,POS1,RADIUS)
    pygame.display.update()
    pygame.draw.polygon(screen,BLUE,[[350,570],[400,620],[300,620]])
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(375,620,10,40))
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(325,620,10,40))
    pygame.display.update()
    time.sleep(4)
    background_image2=pygame.image.load("forest.png").convert()
    background_image2=pygame.transform.scale(background_image2,(600,600))
    screen.blit(background_image2,[0,0])
    pygame.display.update()
 



    YPOS2=500
    POS2=(XPOS1,YPOS2)
    pygame.draw.circle(screen,FACE,POS2,RADIUS)
    pygame.display.update()
    pygame.draw.polygon(screen,BLUE,[[350,520],[400,570],[300,570]])
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(375,570,10,40))
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(325,570,10,40))
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[300,550],[290,550],[350,520],[350,519]])
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[400,550],[410,550],[350,520],[350,519]])
    pygame.display.update()
    time.sleep(4)
    background_image3=pygame.image.load("forest.png").convert()
    background_image3=pygame.transform.scale(background_image3,(600,600))
    screen.blit(background_image3,[0,0])
    pygame.display.update()


    YPOS3=450
    POS3=(XPOS1,YPOS3)
    pygame.draw.circle(screen,FACE,POS3,RADIUS)
    pygame.display.update()
    pygame.draw.polygon(screen,BLUE,[[350,470],[400,520],[300,520]])
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(375,520,10,40))
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(325,520,10,40))
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[300,500],[290,500],[350,470],[350,469]])
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[400,500],[410,500],[350,470],[350,469]])
    pygame.display.update()
    pygame.draw.ellipse(screen,(100,20,20),(250,360,80,110))
    pygame.display.update()



    XPOS_1=285
    YPOS_1=345
    RADIUS_1=25
    POS_1=(XPOS_1,YPOS_1)
    pygame.draw.circle(screen,FACE,POS_1,RADIUS_1)
    pygame.display.update()
    pygame.draw.ellipse(screen,BROWN,(276,338,7,10))
    pygame.display.update()
    pygame.draw.ellipse(screen,BROWN,(295,338,7,10))
    pygame.display.update()
    pygame.draw.ellipse(screen,BROWN,(282,352,15,8))
    pygame.display.update()
    pygame.draw.ellipse(screen,(60,40,40),(300,460,20,50))
    pygame.display.update()
    pygame.draw.ellipse(screen,(60,40,40),(265,460,20,50))
    pygame.display.update()
    pygame.draw.ellipse(screen,(60,40,40),(245,360,20,40))
    pygame.display.update()
    pygame.draw.ellipse(screen,(60,40,40),(320,360,20,40))
    pygame.display.update()
    time.sleep(10)
    background_image4=pygame.image.load("forest.png").convert()
    background_image4=pygame.transform.scale(background_image4,(600,600))
    screen.blit(background_image4,[0,0])
    pygame.display.update()




    YPOS4=400
    POS4=(XPOS,YPOS4)
    pygame.draw.circle(screen,FACE,POS4,RADIUS)
    pygame.display.update()
    pygame.draw.polygon(screen,BLUE,[[350,420],[400,470],[300,470]])
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(375,470,10,40))
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(325,470,10,40))
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[300,450],[290,450],[350,420],[350,419]])
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[400,450],[410,450],[350,420],[350,419]])
    pygame.display.update()
    time.sleep(1)
    background_image5=pygame.image.load("forest.png").convert()
    background_image5=pygame.transform.scale(background_image5,(600,600))
    screen.blit(background_image5,[0,0])
    pygame.display.update() 
    pygame.draw.circle(screen,FACE, POS, RADIUS)
    pygame.display.update()
    pygame.draw.polygon(screen,BLUE,[[350,370],[400,420],[300,420]])
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(375,420,10,40))
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(325,420,10,40))
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[300,400],[290,400],[350,370],[350,369]])
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[400,400],[410,400],[350,370],[350,369]])
    pygame.display.update()
    time.sleep(2)
 


    """background coming back"""
    background_image1=pygame.image.load("backgroundvillage.png").convert()
    background_image1=pygame.transform.scale(background_image1,(600,600))
    screen.blit(background_image1,[0,0])
    pygame.display.update()
  

    """XPOS1=350
    YPOS1=450
    POS1=(XPOS1,YPOS1)
    pygame.draw.circle(screen,FACE,POS1,RADIUS)
    pygame.display.update()
    pygame.draw.polygon(screen,BLUE,[[350,570],[400,620],[300,620]])
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(375,620,10,40))
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(325,620,10,40))
    pygame.display.update()
    time.sleep(1)"""



    background_image2=pygame.image.load("backgroundvillage.png").convert()
    background_image2=pygame.transform.scale(background_image2,(600,600))
    screen.blit(background_image2,[0,0])
    pygame.display.update()
    YPOS2=500
    POS2=(XPOS1,YPOS2)
    pygame.draw.circle(screen,FACE,POS2,RADIUS)
    pygame.display.update()
    pygame.draw.polygon(screen,BLUE,[[350,520],[400,570],[300,570]])
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(375,570,10,40))
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(325,570,10,40))
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[300,550],[290,550],[350,520],[350,519]])
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[400,550],[410,550],[350,520],[350,519]])
    pygame.display.update()
    time.sleep(1)
    background_image3=pygame.image.load("backgroundvillage.png").convert()
    background_image3=pygame.transform.scale(background_image3,(600,600))
    screen.blit(background_image3,[0,0])
    pygame.display.update()




    YPOS3=450
    POS3=(XPOS1,YPOS3)
    pygame.draw.circle(screen,FACE,POS3,RADIUS)
    pygame.display.update()
    pygame.draw.polygon(screen,BLUE,[[350,470],[400,520],[300,520]])
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(375,520,10,40))
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(325,520,10,40))
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[300,500],[290,500],[350,470],[350,469]])
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[400,500],[410,500],[350,470],[350,469]])
    pygame.display.update()
    time.sleep(1)
    background_image4=pygame.image.load("backgroundvillage.png").convert()
    background_image4=pygame.transform.scale(background_image4,(600,600))
    screen.blit(background_image4,[0,0])
    pygame.display.update()





    YPOS4=400
    POS4=(XPOS,YPOS4)
    pygame.draw.circle(screen,FACE,POS4,RADIUS)
    pygame.display.update()
    pygame.draw.polygon(screen,BLUE,[[350,420],[400,470],[300,470]])
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(375,470,10,40))
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(325,470,10,40))
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[300,450],[290,450],[350,420],[350,419]])
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[400,450],[410,450],[350,420],[350,419]])
    pygame.display.update()
    time.sleep(1)
    background_image5=pygame.image.load("backgroundvillage.png").convert()
    background_image5=pygame.transform.scale(background_image5,(600,600))
    screen.blit(background_image5,[0,0])
    pygame.display.update() 
    pygame.draw.circle(screen,FACE, POS, RADIUS)
    pygame.display.update()
    pygame.draw.polygon(screen,BLUE,[[350,370],[400,420],[300,420]])
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(375,420,10,40))
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(325,420,10,40))
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[300,400],[290,400],[350,370],[350,369]])
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[400,400],[410,400],[350,370],[350,369]])
    pygame.display.update()
    time.sleep(2)

    """home sceen"""



    background_image5=pygame.image.load("bedroom.png").convert()
    background_image5=pygame.transform.scale(background_image5,(600,600))
    screen.blit(background_image5,[0,0])
    pygame.display.update()
    
    XPOS_2=550
    YPOS_2=280
    POS_2=(XPOS_2,YPOS_2)
    pygame.draw.circle(screen,FACE,POS_2,RADIUS)
    pygame.display.update()
    pygame.draw.polygon(screen,BLUE,[[550,300],[600,350],[500,350]])
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(575,350,10,40))
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(525,350,10,40))
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[550,300],[500,330],[490,330],[550,299]])
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[550,300],[590,330],[600,330],[550,299]])
    pygame.display.update()
    time.sleep(1)
    background_image6=pygame.image.load("bedroom.png").convert()
    background_image6=pygame.transform.scale(background_image6,(600,600))
    screen.blit(background_image6,[0,0])
    pygame.display.update()



    XPOS_2=535
    YPOS_2=280
    POS_2=(XPOS_2,YPOS_2)
    pygame.draw.circle(screen,FACE,POS_2,RADIUS)
    pygame.display.update()
    pygame.draw.polygon(screen,BLUE,[[535,300],[575,350],[485,350]])
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(560,350,10,40))
    pygame.display.update()
    pygame.draw.rect(screen,BROWN,(510,350,10,40))
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[535,300],[485,330],[475,330],[535,299]])
    pygame.display.update()
    pygame.draw.polygon(screen,FACE,[[535,300],[575,330],[585,330],[535,299]])
    pygame.display.update()
    time.sleep(1)
    """next monster"""


    XPOS_1=285
    YPOS_1=345
    RADIUS_1=25
    pygame.draw.ellipse(screen,(100,20,20),(250,360,80,110))
    pygame.display.update()
    POS_1=(XPOS_1,YPOS_1)
    pygame.draw.circle(screen,FACE,POS_1,RADIUS_1)
    pygame.display.update()
    pygame.draw.ellipse(screen,BROWN,(276,338,7,10))
    pygame.display.update()
    pygame.draw.ellipse(screen,BROWN,(295,338,7,10))
    pygame.display.update()
    pygame.draw.ellipse(screen,BROWN,(282,352,15,8))
    pygame.display.update()
    pygame.draw.ellipse(screen,(60,40,40),(300,460,20,50))
    pygame.display.update()
    pygame.draw.ellipse(screen,(60,40,40),(265,460,20,50))
    pygame.display.update()
    pygame.draw.ellipse(screen,(60,40,40),(245,360,20,40))
    pygame.display.update()
    pygame.draw.ellipse(screen,(60,40,40),(320,360,20,40))
    pygame.display.update()
    time.sleep(2)
    pygame.draw.ellipse(screen,(0,0,0),(450,315,40,20))
    pygame.display.update()
    
    pygame.draw.ellipse(screen,(0,0,0,),(475,315,10,45))
    pygame.display.update()
    time.sleep(2)
    pygame.draw.ellipse(screen,(255,0,0),(440,315,20,20))
    pygame.display.update()
    time.sleep(2)
    """import pygame
import time
 
pygame.init()
width = 600
height = 600
 
#make the pygame window
pygame.display.set_mode((width, height ) )
pygame.display.set_caption("clevergirl")
running = True
 
while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False"""







    XPOS_1=285
    YPOS_1=345
    RADIUS_1=25
    pygame.draw.ellipse(screen,(100,20,20),(250,360,80,110))
    pygame.display.update()
    POS_1=(XPOS_1,YPOS_1)
    pygame.draw.circle(screen,FACE,POS_1,RADIUS_1)
    pygame.display.update()
    pygame.draw.ellipse(screen,BROWN,(276,338,7,10))
    pygame.display.update()
    pygame.draw.ellipse(screen,BROWN,(295,338,7,10))
    pygame.display.update()
    pygame.draw.ellipse(screen,BROWN,(282,352,15,8))
    pygame.display.update()
    pygame.draw.ellipse(screen,(60,40,40),(300,460,20,50))
    pygame.display.update()
    pygame.draw.ellipse(screen,(60,40,40),(265,460,20,50))
    pygame.display.update()
    pygame.draw.ellipse(screen,(60,40,40),(245,360,20,40))
    pygame.display.update()
    pygame.draw.ellipse(screen,(60,40,40),(320,360,20,40))
    pygame.display.update()
  
    pygame.draw.ellipse(screen,(0,0,0),(450,315,40,20))
    pygame.display.update()
    
    pygame.draw.ellipse(screen,(0,0,0,),(475,315,10,45))
    pygame.display.update()
   
    pygame.draw.ellipse(screen,(255,0,0),(270,380,20,20))
    pygame.display.update()
    
    time.sleep(10)
    
    
    
    
    
    

    pygame.display.flip()
    clock.tick(clock_tick_rate)







import pygame
pygame.font.init() #imports all fonts
# pip install [name of package]


width ,height= 800, 400 #Y
Screen_color = (0,0,200) #(R,G,B) 0<x<250
width_sp , height_sp = 60 , 60
step=5
WHITE=(250,250,250)
RED=(100,0,0)
red_bullet=[]
yellow_bullet=[]
bullet_step = 5
Red_color=(100,0,0)
Yellow_color=(0,100,0)
#--------------------------------------------
BackGround=pygame.image.load('background.jpg')
BackGround=pygame.transform.scale(BackGround,(width ,height))
#----------------------------------------------
RED_HIT=pygame.USEREVENT+1
YELLOW_HIT= pygame.USEREVENT+2
#------------------------------------
Yellow_sp = pygame.image.load('Yellow.png')
Yellow_sp=pygame.transform.scale(Yellow_sp,(width_sp , height_sp))
Yellow_sp=pygame.transform.rotate(Yellow_sp,-90)
#-----------------------------------------------------
Red_sp = pygame.image.load('red.png')
Red_sp=pygame.transform.scale(Red_sp,(width_sp , height_sp))
Red_sp=pygame.transform.rotate(Red_sp,90)
#----------------------------------------------------
Window = pygame . display .set_mode((width,height)) #یک پنجره برای بازی درست کردیم 
pygame.display.set_caption('جنگ ستارگان')

#---------------------------------------------------------

#--------------------------------------------------------

def draw_window(red,yellow,red_bullets,yellow_bullet,yellow_heart,red_heart): #Graphics
    #Window.fill(Screen_color)
    Window.blit(BackGround,(0,0))
    score_font=pygame.font.SysFont('comicsansms', 18)

    red_score= score_font.render("red score:" + str(red_heart),1,WHITE)
    Window.blit(red_score,(width//2+10,10))

    yellow_score= score_font.render("yellow score:" + str(yellow_heart),1,WHITE)
    Window.blit(yellow_score,(10,10))

    pygame.draw.line(Window,'white',(width/2,0),(width/2,height),10)
    Window.blit(Yellow_sp,(yellow.x,yellow.y))
    Window.blit(Red_sp,(red.x,red.y))
    for bullet in red_bullet:
        pygame.draw.rect(Window, Red_color, bullet)
    for bullet in yellow_bullet:
        pygame.draw.rect(Window,Yellow_color,bullet)
    pygame.display.update()

def draw_wintext(win_text):
    font_winner=pygame.font.SysFont('cambria',100)
    text=font_winner.render(win_text,1,RED)
    Window.blit(text,(width//4,height//4))
    pygame.display.update()
    pygame.time.delay(10000) # mili second



def Move_Yellow(key_pressed,yellow):
    if key_pressed[pygame.K_UP] and yellow.y>0:
        yellow.y = yellow.y - step
    if key_pressed[pygame.K_DOWN] and yellow.y < height - height_sp:
        yellow.y = yellow.y + step
    if key_pressed[pygame.K_RIGHT] and yellow.x < width/2 - width_sp :
        yellow.x = yellow.x + step
    if key_pressed[pygame.K_LEFT] and yellow.x>0:
         yellow.x = yellow.x - step
 
def Move_Red(key_pressed,red):
    if key_pressed[pygame.K_w] and red.y > 0:
        red.y = red.y - step
    if key_pressed[pygame.K_s] and red.y < height - height_sp:
        red.y = red.y + step
    if key_pressed[pygame.K_d] and red.x<width - width_sp:
        red.x = red.x + step
    if key_pressed[pygame.K_a] and red.x>width//2:
         red.x = red.x - step

def Bullets_movement(red , yellow, red_bullet , yellow_bullet):

    for bullet in red_bullet:
        bullet.x= bullet.x- bullet_step
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            # red_bullet.remove(bullet)
        if bullet.x <0:
            red_bullet.remove(bullet)
 #-----------------------------------------------       
    for bullet in yellow_bullet:
        bullet.x= bullet.x+ bullet_step
        if red.colliderect(bullet):
            #yellow_bullet.remove(bullet)
            pygame.event.post(pygame.event.Event(RED_HIT))
        if bullet.x>width:
            yellow_bullet.remove(bullet)

 
def main():
    yellow_heart = 10
    red_heart = 10
    clock=pygame.time.Clock()
    yellow = pygame.Rect(100,150,width_sp , height_sp)
    red =pygame.Rect(600,150,width_sp , height_sp)
    RUN=True
    while RUN:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type==pygame.KEYDOWN: 
                if event.key==pygame.K_LCTRL: #red
                    bullet= pygame.Rect(red.x,red.y,10,5)
                    red_bullet.append(bullet)

                if event.key==pygame.K_RCTRL: #yellow
                    bullet= pygame.Rect(yellow.x,yellow.y,10,5)
                    yellow_bullet.append(bullet)

            if event.type==RED_HIT:
                yellow_heart=  yellow_heart - 1 
            if event.type==YELLOW_HIT:
                red_heart=  red_heart - 1

        if yellow_heart<=0:
            win_text="yellow wins"
            draw_wintext(win_text)
            break
        if red_heart<=0:
            win_text="red wins"
            draw_wintext(win_text)
            break
             
            
                
                




        draw_window(red,yellow,red_bullet,yellow_bullet,yellow_heart,red_heart)
        key_pressed=pygame.key.get_pressed()
        Move_Yellow(key_pressed,yellow)
        Move_Red(key_pressed,red)
        Bullets_movement(red , yellow, red_bullet , yellow_bullet)


    
    pygame.quit()


if __name__ == '__main__':
    main()


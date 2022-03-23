from turtle import width
import pygame

pygame.display.set_caption("Spaceship Game!")
width, height = 900, 500
win = pygame.display.set_mode((width,height))
border = pygame.Rect((width/2)-5, 0, 10, height) # we find the middle of the window

def handle_bullets(yellow_bullet, red_bullet, yellow, red):
    for bullet in yellow_bullet:
        bullet.x += bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullet.remove(bullet)
        elif bullet.x > width:
            yellow_bullet.remove(bullet)

    for bullet in red_bullet:
        bullet.x -= bullet_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullet.remove(bullet)
        elif bullet.x < 0:
            red_bullet.remove(bullet)


def yellow_movement(keys, yellow):
    if keys[pygame.K_a] and yellow.x -vel > 0: # left
        yellow.x -= vel 
    elif keys[pygame.K_d] and yellow.x + vel + yellow.width < border.x: # right
        yellow.x += vel
    elif keys[pygame.K_w] and yellow.y-vel > 0: # up
        yellow.y -= vel
    elif keys[pygame.K_s] and yellow.y + vel + yellow.height < height - 15: # down
        yellow.y += vel

def red_movement(keys, red):
    if keys[pygame.K_LEFT] and red.x - vel > border.x + border.width: # left
        red.x -= vel 
    elif keys[pygame.K_RIGHT] and red.x + vel + red.width < width: # right
        red.x += vel
    elif keys[pygame.K_UP] and red.y - vel > 0: # up
        red.y -= vel
    elif keys[pygame.K_DOWN] and red.y + vel + red.height < height - 15 : # down
        red.y += vel
    

def draw_window(red, yellow, red_bullet, yellow_bullet): # the game window design
    win.fill((255,255,255))
    pygame.draw.rect(win, (0,0,0),border)

    for bullet in red_bullet:
        pygame.draw.rect(win, (255,0,0), bullet)

    for bullet in yellow_bullet:
        pygame.draw.rect(win,(255,255,0), bullet)

    win.blit(yellow_space,(yellow.x, yellow.y))
    win.blit(red_space,(red.x, red.y))
    pygame.display.update()

FPS  = 60

space_width, space_height = 55, 40
vel = 5
bullet_vel = 10
max_bullet = 5 # there can only be max 5 bullets on the screen

yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2


#Load yellow spaceships
yellow_space = pygame.image.load("C:/Users/bizga/Desktop/SCHOOL/Programming/Python Semester 2/Assets/spaceship_yellow.png")
yellow_space = pygame.transform.scale(yellow_space,(space_width,space_height))
yellow_space = pygame.transform.rotate(yellow_space, 90)

#Load red spaceships
red_space = pygame.image.load("C:/Users/bizga/Desktop/SCHOOL/Programming/Python Semester 2/Assets/spaceship_red.png")
red_space = pygame.transform.scale(red_space,(space_width,space_height))
red_space = pygame.transform.rotate(red_space, 270)



def main():
    red = pygame.Rect(100,300,space_width,space_width)
    yellow = pygame.Rect(100,300,space_width,space_height)

    yellow_bullet = []
    red_bullet = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): # list of diferrent events
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullet) < max_bullet:
                    bullet = pygame.Rect(yellow.x+yellow.width, yellow.y + yellow.height/2 -2, 10, 5)
                    yellow_bullet.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullet) < max_bullet:
                    bullet = pygame.Rect(red.x, red.y + red.height/2 - 2, 10, 5)
                    red_bullet.append(bullet)

        keys = pygame.key.get_pressed()
        yellow_movement(keys,yellow)
        red_movement(keys,red)
        handle_bullets(yellow_bullet, red_bullet, yellow, red)
        draw_window(red, yellow,yellow_bullet, red_bullet)
       
              

main()
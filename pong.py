import pygame, sys, random

#ball movement
def ball_animation():
    #it's necessary to define those variables as blobal
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    #<= or >= is used because when ball is moving each pixel it can cross 0 and break the game
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
         ball_restart()
        
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    #Setting limits for player
    #Top will always be 0, bottom can be infinite so you use screen_height property
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        player.bottom = screen_height
        
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

#General Setup
pygame.init()
clock = pygame.time.Clock()

#Setting up main window
screen_width = 960
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

#Define Game Rectangles params = x, y, width, height
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)  
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

#Colors
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

#Speeds
ball_speed_x = 7 *random.choice((1, -1))
ball_speed_y = 7 *random.choice((1, -1))
player_speed = 0
opponent_speed = 7

#Event listening
while True:
    #handling input, it checks user actions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN : 
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        #This setting not only stops movement it also balance player speed by counteract it counter
        if event.type== pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    ball_animation()    
    player_animation() 
    opponent_ai()          


            
# Visuals Draw rectangles from bottom to top
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))
            
# Updating window
    pygame.display.flip()
    #60 frames per second
    clock.tick(60) 
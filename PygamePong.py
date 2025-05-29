import pygame
import sys
import random

pygame.init()

def game_over_screen():
    screen.fill(black)
    game_over_text = font.render('Game Over', True, white)
    press_R_restart_text = smaller_font.render("Press \"R\" To Restart", True, white)
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2 , screen_height // 2.5))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == game_over_screen and pygame.K_r:
                waiting = False
                score_reset()
            
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
    
def ball_reset():
    global ball_speed_x, ball_speed_y
    if ball.left <= 0 or ball.right >= screen_width:
        ball.x = screen_width/2 - 17.5
        ball.y = screen_height/2 - 17.5
        ball_speed_x = random.choice([-7,7])
        ball_speed_y = random.choice([-7,7])
  
# window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Medieval Pygame Pong")

# clock
clock = pygame.time.Clock()

# colours
white = (255, 255, 255)
black = (0, 0, 0)
grey = (191, 191, 191)

# font
font = pygame.font.SysFont("arial", 40)
smaller_font = pygame.font.SysFont("ariel", 35)

# ball 
ball = pygame.Rect(screen_width/2 - 17.5, screen_height/2 - 17.5,35,35)
ball_speed_x = 6
ball_speed_y = 6

# paddle_A
paddle_A = pygame.Rect(screen_width - 100, screen_height/2 - 75,20,150)
paddle_A_speed = 0

# paddle_B
paddle_B = pygame.Rect(screen_width - 1180, screen_height/2 - 75,20,150)
paddle_B_speed = 0

# scoring
score_right = 5
score_left = 5
score_font = pygame.font.Font(None, 100)
 
clock = pygame.time.Clock()

# main-Game-Loop
KeepGameRunning = True
while KeepGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            KeepGameRunning = False
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle_A_speed=-5.5
            elif event.key == pygame.K_DOWN:
                paddle_A_speed =5.5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle_B_speed=-5.5
            elif event.key == pygame.K_s:
                paddle_B_speed =5.5
       
    # on-Screen-Objects
    screen.fill(black)
    score_left_surface = score_font.render(str(score_left), True, "white")
    score_right_surface = score_font.render(str(score_right), True, "white")
    screen.blit(score_left_surface,(3*screen_width/4,20))
    screen.blit(score_right_surface,(screen_width/4,20))
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.rect(screen, white, paddle_A)
    pygame.draw.rect(screen, white, paddle_B)
    
    # movements
    ball.x += ball_speed_x 
    ball.y += ball_speed_y
    paddle_A.y += paddle_A_speed
    paddle_B.y += paddle_B_speed
    
    # border-Checking
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    
    if paddle_A.top <= 0 or paddle_A.bottom >= screen_height:
        paddle_A_speed = 0
    if paddle_B.top <= 0 or paddle_B.bottom >= screen_height:
        paddle_B_speed = 0
    
    # paddle-ball-collision
    if ball.colliderect(paddle_A):
        ball_speed_x *= -1
        ball.right = paddle_A.left 
    
    if ball.colliderect(paddle_B):
        ball_speed_x *= -1
        ball.left = paddle_B.right
        
        # scoring
    if ball.left <= 0:
        score_left -= 1
        if score_left == 0:
            game_over_screen()
        
    if ball.right >= screen_width:
        score_right -= 1
        if score_right == 0:
            game_over_screen()
            
    # function
    ball_reset()
    
    pygame.display.update()
    clock.tick(60)

            
    
import pygame
import random
import json

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake game")

clock = pygame.time.Clock()

pygame.font.init()

with open('Scores.json') as f:
    data = json.load(f)

SCORE_FONT = pygame.font.SysFont('comicsans', 20)

GRID = []

for i in range(20, WIDTH - 20, 20):
    GRID.append(i)

snake = pygame.Rect(GRID[random.randrange(len(GRID))], GRID[random.randrange(len(GRID))], 20, 20)
snake_size = 1
snake_directions = [[]]
snake_positions = [[]]
old_snake_positions = []
snake_tail = []

xspeed = 0
yspeed = 0

left_wall = pygame.Rect((0, 0, snake.width, WIDTH))
upper_wall = pygame.Rect((0, 0, WIDTH, snake.width))
bottom_wall = pygame.Rect((WIDTH - snake.width, 0, snake.width, WIDTH))
right_wall = pygame.Rect((0, WIDTH - snake.width, WIDTH, snake.width))

walls = [left_wall, upper_wall, bottom_wall, right_wall]

food = pygame.Rect((GRID[random.randrange(len(GRID))], GRID[random.randrange(len(GRID))], 20, 20))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Snake:
    def __init__(self, x, y, xspeed, yspeed, width):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.width = width
    
    def update(self):
        self.x += self.xspeed
        self.y += self.yspeed
    
    def dir(self, x, y):
        self.xspeed = x * self.width
        self.yspeed = y * self.width

    def show(self, win):
        pygame.draw.rect(win, GREEN, (self.x, self.y, self.width, self.width))

 
def draw(win):
    WIN.fill(WHITE)
    for wall in walls:
        pygame.draw.rect(win, BLACK, wall)
    pygame.draw.rect(win, GREEN, snake)
    for tail in snake_tail:
        pygame.draw.rect(win, GREEN, tail)
    pygame.draw.rect(win, ORANGE, food)
    pygame.display.update()

def draw_score(text):
    draw_text = SCORE_FONT.render(text, 1, (0, 0, 0))
    WIN.blit(draw_text, (WIDTH - draw_text.get_width() - 20, 20))

def snake_move():
    old_snake_positions = snake_positions.copy()

    snake.x += xspeed
    snake.y += yspeed

    if snake.colliderect(food):
        while [food.x, food.y] in snake_positions or (food.x, food.y) == (snake.x, snake.y):
            food.x = GRID[random.randrange(len(GRID))]
            food.y = GRID[random.randrange(len(GRID))]
        global snake_size
        snake_size += 1
    
    if snake_size > len(snake_positions):
        snake_positions.append(old_snake_positions[-1])
        snake_tail.append(pygame.Rect(snake_positions[-1][0], snake_positions[-1][1], 20, 20))
    

    for i in range(len(snake_positions) - 2, -1, -1):
        snake_positions[i + 1] = snake_positions[i]
    
    for i in range(len(snake_tail)):
        snake_tail[i].x, snake_tail[i].y = snake_positions[i + 1]

    snake_positions[0] = [snake.x, snake.y]
    snake_directions[0] = [xspeed, yspeed]



while 1:
    clock.tick(10)
    print(snake_positions)
    draw(WIN)
    draw_score(f"Score: {snake_size}")
    pygame.display.update()
    count = 0
    print(snake_positions)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('Scores.json', 'w') as f:
                json.dump(data, f, indent=2)
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and yspeed == 0 and count == 0:
                yspeed = -snake.width
                xspeed = 0
                count += 1
            elif event.key == pygame.K_a and xspeed == 0 and count == 0:
                yspeed = 0
                xspeed = -snake.width
                count += 1
            elif event.key == pygame.K_s and yspeed == 0 and count == 0:
                yspeed = snake.width
                xspeed = 0
                count += 1
            elif event.key == pygame.K_d and xspeed == 0 and count == 0:
                yspeed = 0
                xspeed = snake.width
                count += 1
    snake_move()

    for wall in walls:
        if snake.colliderect(wall):
            snake = pygame.Rect(GRID[random.randrange(len(GRID))], GRID[random.randrange(len(GRID))], 20, 20)
            food = pygame.Rect((GRID[random.randrange(len(GRID))], GRID[random.randrange(len(GRID))], 20, 20))
            data['User Scores'].append(snake_size)
            snake_size = 1
            snake_directions = [[]]
            snake_positions = [[]]
            old_snake_positions = []
            snake_tail = []

            xspeed = 0
            yspeed = 0


    
    for tail in snake_tail:
        if snake.colliderect(tail):
            snake = pygame.Rect(GRID[random.randrange(len(GRID))], GRID[random.randrange(len(GRID))], 20, 20)
            food = pygame.Rect((GRID[random.randrange(len(GRID))], GRID[random.randrange(len(GRID))], 20, 20))
            data['User Scores'].append(snake_size)
            snake_size = 1
            snake_directions = [[]]
            snake_positions = [[]]
            old_snake_positions = []
            snake_tail = []

            xspeed = 0
            yspeed = 0

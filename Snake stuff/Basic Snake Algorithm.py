import pygame
import random
import json

with open('Scores.json') as f:
    data = json.load(f)

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake game")

clock = pygame.time.Clock()

pygame.font.init()

SCORE_FONT = pygame.font.SysFont('comicsans', 30)

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


def make_path(snake, food, xspeed, yspeed):
    if xspeed > 0:
        direction = 'right'
    elif xspeed < 0:
        direction = 'left'
    elif yspeed > 0:
        direction = 'down'
    else:
        direction = 'up'
    temp_path = []
    temp_x = int(food.x / 20 - snake.x / 20)
    temp_y = int(food.y / 20 - snake.y / 20)
    if direction == 'right':
        if temp_x > 0:
            for i in range(temp_x):
                temp_path.append('r')
        if temp_y > 0:
            for i in range(temp_y):
                temp_path.append('d')
        elif temp_y < 0:
            for i in range(temp_y * -1):
                temp_path.append('u')
        if temp_x < 0:
            for i in range(temp_x * -1):
                temp_path.append('l')
    if direction == 'left':
        if temp_x < 0:
            for i in range(temp_x * -1):
                temp_path.append('l')
        if temp_y > 0:
            for i in range(temp_y):
                temp_path.append('d')
        elif temp_y < 0:
            for i in range(temp_y * -1):
                temp_path.append('u')
        if temp_x > 0:
            for i in range(temp_x):
                temp_path.append('r')
    if direction == 'up':
        if temp_y < 0:
            for i in range(temp_y * -1):
                temp_path.append('u')
        if temp_x > 0:
            for i in range(temp_x):
                temp_path.append('r')
        elif temp_x < 0:
            for i in range(temp_x * -1):
                temp_path.append('l')
        if temp_y > 0:
            for i in range(temp_y):
                temp_path.append('d')
    if direction == 'down':
        if temp_y > 0:
            for i in range(temp_y):
                temp_path.append('d')
        if temp_x > 0:
            for i in range(temp_x):
                temp_path.append('r')
        elif temp_x < 0:
            for i in range(temp_x * -1):
                temp_path.append('l')
        if temp_y < 0:
            for i in range(temp_y * -1):
                temp_path.append('u')
    print(temp_path)
    print(snake)
    print(food)
    return temp_path

path = make_path(snake, food, 1, 0)
while 1:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('Scores.json', 'w') as f:
                json.dump(data, f, indent=2)
            quit()
            
    draw(WIN)
    draw_score(f"Score: {snake_size}")
    pygame.display.update()
    count = 0
    if path[0] == 'r':
        xspeed = snake.width
        yspeed = 0
    elif path[0] == 'l':
        xspeed = -snake.width
        yspeed = 0
    elif path[0] == 'u':
        xspeed = 0
        yspeed = -snake.width
    elif path[0] == 'd':
        xspeed = 0
        yspeed = snake.width
    path.remove(path[0])
    
    old_snake_positions = snake_positions.copy()

    snake.x += xspeed
    snake.y += yspeed

    if snake.colliderect(food):
        while [food.x, food.y] in snake_positions or (food.x, food.y) == (snake.x, snake.y):
            food.x = GRID[random.randrange(len(GRID))]
            food.y = GRID[random.randrange(len(GRID))]
        snake_size += 1
        path = make_path(snake, food, xspeed, yspeed)
    
    if snake_size > len(snake_positions) and len(snake_positions) > 0:
        snake_positions.append(old_snake_positions[-1])
        snake_tail.append(pygame.Rect(snake_positions[-1][0], snake_positions[-1][1], 20, 20))
    

    for i in range(len(snake_positions) - 2, -1, -1):
        snake_positions[i + 1] = snake_positions[i]
    
    for i in range(len(snake_tail)):
        snake_tail[i].x, snake_tail[i].y = snake_positions[i + 1]

    snake_positions[0] = [snake.x, snake.y]
    snake_directions[0] = [xspeed, yspeed]

    for wall in walls:
        if snake.colliderect(wall):
            snake = pygame.Rect(GRID[random.randrange(len(GRID))], GRID[random.randrange(len(GRID))], 20, 20)
            food = pygame.Rect((GRID[random.randrange(len(GRID))], GRID[random.randrange(len(GRID))], 20, 20))
            data['Version1 Scores'].append(snake_size)
            snake_size = 1
            snake_directions = [[]]
            snake_positions = [[]]
            old_snake_positions = []
            snake_tail = []

            xspeed = 0
            yspeed = 0

            path = make_path(snake, food, 1, 0)


    
    for tail in snake_tail:
        if snake.colliderect(tail):
            snake = pygame.Rect(GRID[random.randrange(len(GRID))], GRID[random.randrange(len(GRID))], 20, 20)
            food = pygame.Rect((GRID[random.randrange(len(GRID))], GRID[random.randrange(len(GRID))], 20, 20))
            data['Version1 Scores'].append(snake_size)
            snake_size = 1
            snake_directions = [[]]
            snake_positions = [[]]
            old_snake_positions = []
            snake_tail = []

            xspeed = 0
            yspeed = 0

            path = make_path(snake, food, 1, 0)

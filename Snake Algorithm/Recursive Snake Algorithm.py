import pygame
import random
import json
# the algorithm will look at the outcome of going in either direction when given a choice between two directions
# To be added: when the algorithm looks at the path and sees that there is a collision, store the point at which that collision initially happened. As the minimax function looks at the other possible direction it could have gone at that point, if it still runs into another collision at that point, go back to the point that was saved and choose the other direction

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
    for i in path_positions:
        pygame.draw.rect(WIN, RED, (i[0], i[1], 20, 20))
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
    return temp_path

def check_path(path, snake_positions, snake, depth):
    if depth > 100:
        return path
    temp_x = 0
    temp_y = 0
    temp_snake = snake.copy()
    temp_snake_positions = snake_positions.copy()
    for i in range(len(path)):
        if len(temp_snake_positions) > 0:
            temp_snake_positions.remove(temp_snake_positions[-1])
        if path[i] == 'r':
            temp_x = 1
            temp_y = 0
        elif path[i] == 'l':
            temp_x = -1
            temp_y = 0
        elif path[i] == 'u':
            temp_y = -1
            temp_x = 0
        else:
            temp_y = 1
            temp_x = 0
        temp_snake.x = temp_snake.x + temp_x * 20
        temp_snake.y = temp_snake.y + temp_y * 20
        if [temp_snake.x, temp_snake.y] in temp_snake_positions:
            if path[i] == 'r':
                temp = path[i]
                path[i] = 'u'
                path.insert(i + 1, temp)
                path.append('d')
                path = check_path(path, snake_positions, snake, depth + 1)
                return path
            elif path[i] == 'l':
                temp = path[i]
                path[i] = 'u'
                path.insert(i + 1, temp)
                path.append('d')
                path = check_path(path, snake_positions, snake, depth + 1)
                return path
            elif path[i] == 'u':
                temp = path[i]
                path[i] = 'l'
                path.insert(i + 1, temp)
                path.append('r')
                path = check_path(path, snake_positions, snake, depth + 1)
                return path
            elif path[i] == 'd':
                temp = path[i]
                path[i] = 'l'
                path.insert(i + 1, temp)
                path.append('r')
                path = check_path(path, snake_positions, snake, depth + 1)
                return path
            temp_snake.x = temp_snake.x - temp_x * 20
            temp_snake.y = temp_snake.y - temp_y * 20
            if path[i] == 'r':
                temp_x = 1
                temp_y = 0
            elif path[i] == 'l':
                temp_x = -1
                temp_y = 0
            elif path[i] == 'u':
                temp_y = -1
                temp_x = 0
            else:
                temp_y = 1
                temp_x = 0
            temp_snake.x = temp_snake.x + temp_x * 20
            temp_snake.y = temp_snake.y + temp_y * 20
    return path

def make_path_positions(path, snake):
    temp_x = 0
    temp_y = 0
    temp_path = []
    temp_snake = snake.copy()

    for direction in path:
        if direction == 'r':
            temp_x = 1
            temp_y = 0
        elif direction == 'l':
            temp_x = -1
            temp_y = 0
        elif direction == 'u':
            temp_y = -1
            temp_x = 0
        else:
            temp_y = 1
            temp_x = 0
        temp_snake.x = temp_snake.x + temp_x * 20
        temp_snake.y = temp_snake.y + temp_y * 20
        temp_path.append([temp_snake.x, temp_snake.y])
    return temp_path
        

path = make_path(snake, food, 0, 0)
path_positions = make_path_positions(path, snake)
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('Scores.json', 'w') as f:
                json.dump(data, f, indent=2)
            quit()
            
    draw(WIN)
    draw_score(f"Score: {snake_size}")
    pygame.display.update()

    
    if path[0] == 'r':
        xspeed = 20
        yspeed = 0
    elif path[0] == 'l':
        xspeed = -20
        yspeed = 0
    elif path[0] == 'u':
        xspeed = 0
        yspeed = -20
    else:
        xspeed = 0
        yspeed = 20
    snake.x += xspeed
    snake.y += yspeed
    path.remove(path[0])
    path_positions.remove(path_positions[0])
    
    old_snake_positions = snake_positions.copy()

    if snake.colliderect(food):
        while [food.x, food.y] in snake_positions or (food.x, food.y) == (snake.x, snake.y):
            food.x = GRID[random.randrange(len(GRID))]
            food.y = GRID[random.randrange(len(GRID))]
        snake_size += 1
        path = make_path(snake, food, xspeed, yspeed)
        path = check_path(path, snake_positions, snake, 0)
        path_positions = make_path_positions(path, snake)
    
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
            data['Version2 Scores'].append(snake_size)
            snake_size = 1
            snake_directions = [[]]
            snake_positions = [[]]
            old_snake_positions = []
            snake_tail = []

            xspeed = 0
            yspeed = 0

            path = make_path(snake, food, xspeed, yspeed)
            path_positions = make_path_positions(path, snake)


    
    for tail in snake_tail:
        if snake.colliderect(tail):
            print(path)
            snake = pygame.Rect(GRID[random.randrange(len(GRID))], GRID[random.randrange(len(GRID))], 20, 20)
            food = pygame.Rect((GRID[random.randrange(len(GRID))], GRID[random.randrange(len(GRID))], 20, 20))
            data['Version2 Scores'].append(snake_size)
            snake_size = 1
            snake_directions = [[]]
            snake_positions = [[]]
            old_snake_positions = []
            snake_tail = []

            xspeed = 0
            yspeed = 0

            path = make_path(snake, food, xspeed, yspeed)
            path_positions = make_path_positions(path, snake)

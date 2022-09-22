from ssl import Purpose
import pygame
import random
pygame.init()

WIDTH = 360
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Block:
    def __init__(self, x, y, block_size, color):
        self.color = color
        self.Rect = pygame.Rect(x, y, block_size, block_size)

BLOCK_NAMES = ["Orange Ricky", "Blue Ricky", "Cleveland Z", "Rhode Island Z", "Hero", "Teewee", "Smashboy"]

class Tetromino:
    def __init__(self, name, block_size):
        self.name = name
        self.orientations = []
        self.orientation = 0
        
        self.x = 0
        self.y = 0
        
        self.block_size = block_size
        
        if name == "Orange Ricky":
            self.blocks = [Block(block_size * 2, 0, block_size, ORANGE), Block(0, block_size, block_size, ORANGE), Block(block_size, block_size, block_size, ORANGE), Block(block_size * 2, block_size, block_size, ORANGE)]
            self.width = 3
            self.height = 2
        elif name == "Blue Ricky":
            self.blocks = [Block(0, 0, block_size, BLUE), Block(0, block_size, block_size, BLUE), Block(block_size, block_size, block_size, BLUE), Block(block_size * 2, block_size, block_size, BLUE)]
            self.width = 3
            self.height = 2
        elif name == "Cleveland Z":
            self.blocks = [Block(0, 0, block_size, RED), Block(block_size, 0, block_size, RED), Block(block_size, block_size, block_size, RED), Block(block_size * 2, block_size, block_size, RED)]
            self.width = 3
            self.height = 2
        elif name == "Rhode Island Z":
            self.blocks = [Block(block_size, 0, block_size, GREEN), Block(block_size * 2, 0, block_size, GREEN), Block(0, block_size, block_size, GREEN), Block(block_size, block_size, block_size, GREEN)]
            self.width = 2
            self.height = 3
        elif name == "Hero":
            self.blocks = [Block(0, 0, block_size, TURQUOISE), Block(0, block_size, block_size, TURQUOISE), Block(0, block_size * 2, block_size, TURQUOISE), Block(0, block_size * 3, block_size, TURQUOISE)]
            self.width = 1
            self.height = 4
        elif name == "Teewee":
            self.blocks = [Block(block_size, 0, block_size, PURPLE), Block(0, block_size, block_size, PURPLE), Block(block_size, block_size, block_size, PURPLE), Block(block_size * 2, block_size, block_size, PURPLE)]
            self.width = 3
            self.height = 2
        elif name == "Smashboy":
            self.blocks = [Block(0, 0, block_size, YELLOW), Block(block_size, 0, block_size, YELLOW), Block(0, block_size, block_size, YELLOW), Block(block_size, block_size, block_size, YELLOW)]
            self.width = 2
            self.height = 2
        
        for block in self.blocks:
            block.Rect.x += (WIDTH // 2 - block_size * 2)
        self.x += (WIDTH // 2 - block_size * 2)
    
    def rotate(self):
        self.orientation += 1
        
        if self.name == "Orange Ricky":
            self.orientations = [[Block(self.block_size * 2, 0, self.block_size, ORANGE), Block(0, self.block_size, self.block_size, ORANGE), Block(self.block_size, self.block_size, self.block_size, ORANGE), Block(self.block_size * 2, self.block_size, self.block_size, ORANGE)],
                                [Block(self.block_size, 0, self.block_size, ORANGE), Block(self.block_size, self.block_size, self.block_size, ORANGE), Block(self.block_size, self.block_size * 2, self.block_size, ORANGE), Block(self.block_size * 2, self.block_size * 2, self.block_size, ORANGE)],
                                [Block(0, self.block_size, self.block_size, ORANGE), Block(self.block_size, self.block_size, self.block_size, ORANGE), Block(self.block_size * 2, self.block_size, self.block_size, ORANGE), Block(0, self.block_size * 2, self.block_size, ORANGE)],
                                [Block(0, 0, self.block_size, ORANGE), Block(self.block_size, 0, self.block_size, ORANGE), Block(self.block_size, self.block_size, self.block_size, ORANGE), Block(self.block_size, self.block_size * 2, self.block_size, ORANGE)]]
        elif self.name == "Blue Ricky":
            self.orientations = [[Block(0, 0, self.block_size, BLUE), Block(0, self.block_size, self.block_size, BLUE), Block(self.block_size, self.block_size, self.block_size, BLUE), Block(self.block_size * 2, self.block_size, self.block_size, BLUE)],
                                 [Block(self.block_size, 0, self.block_size, BLUE), Block(self.block_size * 2, 0, self.block_size, BLUE), Block(self.block_size, self.block_size, self.block_size, BLUE), Block(self.block_size, self.block_size * 2, self.block_size, BLUE)],
                                 [Block(0, self.block_size, self.block_size, BLUE), Block(self.block_size, self.block_size, self.block_size, BLUE), Block(self.block_size * 2, self.block_size, self.block_size, BLUE), Block(self.block_size * 2, self.block_size * 2, self.block_size, BLUE)],
                                 [Block(self.block_size, 0, self.block_size, BLUE), Block(self.block_size, self.block_size, self.block_size, BLUE), Block(self.block_size, self.block_size * 2, self.block_size, BLUE), Block(0, self.block_size * 2, self.block_size, BLUE)]]
        elif self.name == "Cleveland Z":
            self.orientations = [[Block(0, 0, self.block_size, RED), Block(self.block_size, 0, self.block_size, RED), Block(self.block_size, self.block_size, self.block_size, RED), Block(self.block_size * 2, self.block_size, self.block_size, RED)],
                                 [Block(self.block_size, 0, self.block_size, RED), Block(0, self.block_size, self.block_size, RED), Block(self.block_size, self.block_size, self.block_size, RED), Block(0, self.block_size * 2, self.block_size, RED)]]
        elif self.name == "Rhode Island Z":
            self.orientations = [[Block(self.block_size, 0, self.block_size, GREEN), Block(self.block_size * 2, 0, self.block_size, GREEN), Block(0, self.block_size, self.block_size, GREEN), Block(self.block_size, self.block_size, self.block_size, GREEN)],
                                 [Block(0, 0, self.block_size, GREEN), Block(0, self.block_size, self.block_size, GREEN), Block(self.block_size, self.block_size, self.block_size, GREEN), Block(self.block_size, self.block_size * 2, self.block_size, GREEN)]]
        elif self.name == "Hero":
            self.orientations = [[Block(0, 0, self.block_size, TURQUOISE), Block(0, self.block_size, self.block_size, TURQUOISE), Block(0, self.block_size * 2, self.block_size, TURQUOISE), Block(0, self.block_size * 3, self.block_size, TURQUOISE)],
                                 [Block(0, 0, self.block_size, TURQUOISE), Block(self.block_size, 0, self.block_size, TURQUOISE), Block(self.block_size * 2, 0, self.block_size, TURQUOISE), Block(self.block_size * 3, 0, self.block_size, TURQUOISE)]]
        elif self.name == "Teewee":
            self.orientations = [[Block(self.block_size, 0, self.block_size, PURPLE), Block(0, self.block_size, self.block_size, PURPLE), Block(self.block_size, self.block_size, self.block_size, PURPLE), Block(self.block_size * 2, self.block_size, self.block_size, PURPLE)],
                                 [Block(0, 0, self.block_size, PURPLE), Block(0, self.block_size, self.block_size, PURPLE), Block(self.block_size, self.block_size, self.block_size, PURPLE), Block(0, self.block_size * 2, self.block_size, PURPLE)],
                                 [Block(0, 0, self.block_size, PURPLE), Block(self.block_size, 0, self.block_size, PURPLE), Block(self.block_size * 2, 0, self.block_size, PURPLE), Block(self.block_size, self.block_size, self.block_size, PURPLE)],
                                 [Block(self.block_size * 2, 0, self.block_size, PURPLE), Block(self.block_size, self.block_size, self.block_size, PURPLE), Block(self.block_size * 2, self.block_size, self.block_size, PURPLE), Block(self.block_size * 2, self.block_size * 2, self.block_size, PURPLE)]]
        elif self.name == "Smashboy":
            self.orientations = [[Block(0, 0, self.block_size, YELLOW), Block(self.block_size, 0, self.block_size, YELLOW), Block(0, self.block_size, self.block_size, YELLOW), Block(self.block_size, self.block_size, self.block_size, YELLOW)]]
        
        self.blocks = self.orientations[self.orientation % len(self.orientations)]
        
        for block in self.blocks:
            print(block.Rect.x)
            print(block.Rect.y)
            block.Rect.x += self.x
            block.Rect.y += self.y
        
       
def delete_items(nums, rem_nums):
    temp = []
    
    for i in nums:
        if not i.Rect.y in rem_nums:
            temp.append(i)
    
    return temp

def main():
    block_size = 30
    current_piece = [Tetromino(BLOCK_NAMES[random.randrange(0, len(BLOCK_NAMES))], block_size)]
    future_pieces = [Tetromino(BLOCK_NAMES[random.randrange(0, len(BLOCK_NAMES))], block_size), Tetromino(BLOCK_NAMES[random.randrange(0, len(BLOCK_NAMES))], block_size), Tetromino(BLOCK_NAMES[random.randrange(0, len(BLOCK_NAMES))], block_size)]
    static_blocks = []
    
    BLOCK_FALL = pygame.USEREVENT + 0
    pygame.time.set_timer(BLOCK_FALL, 300)
    
    border_walls = [pygame.Rect(0, 0, 1, HEIGHT), pygame.Rect(0, 0, WIDTH, 1), pygame.Rect(WIDTH - 1, 0, 1, HEIGHT), pygame.Rect(0, HEIGHT - 1, WIDTH, 1)]
    
    score = 0
    
    while True:
        WIN.fill(BLACK)
        
        for block in current_piece[0].blocks:
            pygame.draw.rect(WIN, block.color, block.Rect)
            
        for block in static_blocks:
            pygame.draw.rect(WIN, block.color, block.Rect)
            
        pygame.display.update()
        
        static_rects = []
        
        for i in static_blocks:
            static_rects.append(i.Rect)
            
        keys_pressed = pygame.key.get_pressed()
        
        current_rects = []
        for block in current_piece[0].blocks:
            current_rects.append(block.Rect)
        
        move_left = True
        move_right = True
        move_down = True
        
        for block in current_rects:
            if pygame.Rect(block.x - block_size, block.y, block.width, block.height).collidelist(static_rects) != -1 or border_walls[0].collidelist(current_rects) != -1:
                move_left = False
            if pygame.Rect(block.x + block_size, block.y, block.width, block.height).collidelist(static_rects) != -1 or border_walls[2].collidelist(current_rects) != -1:
                move_right = False
            if pygame.Rect(block.x, block.y + block_size, block.width, block.height).collidelist(static_rects) != -1 or border_walls[3].collidelist(current_rects) != -1:
                move_down = False
        
        if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]) and move_left and move_down:
            for block in current_piece[0].blocks:
                block.Rect.x -= block_size
            current_piece[0].x -= block_size
        if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]) and move_right and move_down:
            for block in current_piece[0].blocks:
                block.Rect.x += block_size
            current_piece[0].x += block_size
        if (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]) and move_down:
            for block in current_piece[0].blocks:
                block.Rect.y += block_size     
            current_piece[0].y += block_size
        
        current_rects = []
        for block in current_piece[0].blocks:
            current_rects.append(block.Rect)
        
        for block in current_rects:
            if pygame.Rect(block.x - block_size, block.y, block.width, block.height).collidelist(static_rects) != -1 or border_walls[0].collidelist(current_rects) != -1:
                move_left = False
            if pygame.Rect(block.x + block_size, block.y, block.width, block.height).collidelist(static_rects) != -1 or border_walls[2].collidelist(current_rects) != -1:
                move_right = False
            if pygame.Rect(block.x, block.y + block_size, block.width, block.height).collidelist(static_rects) != -1 or border_walls[3].collidelist(current_rects) != -1:
                move_down = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == BLOCK_FALL and move_down:
                for block in current_piece[0].blocks:
                    block.Rect.y += block_size
                current_piece[0].y += block_size
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    current_piece[0].rotate()
                    static_rects = []
                    for block in static_blocks:
                        static_rects.append(block.Rect)
                    for block in current_piece[0].blocks:
                        while pygame.Rect(block.Rect.x - 1, block.Rect.y, block.Rect.width, block.Rect.height).colliderect(border_walls[2]):
                            for block in current_piece[0].blocks:
                                block.Rect.x -= block_size
                        while pygame.Rect(block.Rect.x + 1, block.Rect.y, block.Rect.width, block.Rect.height).colliderect(border_walls[0]):
                            for block in current_piece[0].blocks:
                                block.Rect.x += block_size
                        while pygame.Rect(block.Rect.x, block.Rect.y - 1, block.Rect.width, block.Rect.height).colliderect(border_walls[3]):
                            for block in current_piece[0].blocks:
                                block.Rect.y -= block_size
                        
                        # left_counter = 0
                        # up_counter = 0
                        # while block.Rect.collidelist(static_rects) != -1:
                        #     for block in current_piece[0].blocks:
                        #         block.Rect.x -= block_size
                        #     left_counter += 1
                        #     for block in current_piece[0].blocks:
                        #         block.Rect.y -= block_size
                        #     up_counter += 1
                        
                        # if left_counter < up_counter:
                        #     if left_counter < current_piece[0].width:
                        #         block.Rect.y += block_size * up_counter
                        # else:
                        #     if up_counter < current_piece[0].height:
                        #         block.Rect.x += block_size * left_counter
                        #     else:
                        #         block.Rect.x += block_size * left_counter
                        #         block.Rect.y += block_size * up_counter
                        #         while block.Rect.collidelist(static_rects) != -1:
                        #             for block in current_piece[0].blocks:
                        #                 block.Rect.x += block_size
        
        if not move_down:
            for block in current_piece[0].blocks:
                static_blocks.append(block)
            current_piece.pop()
            current_piece.append(future_pieces.pop(0))
            static_rects = []
            for block in static_blocks:
                static_rects.append(block.Rect)
            for block in current_piece[0].blocks:
                if block.Rect.collidelist(static_rects) != -1:
                    print("You Lose")
                    print("Score: {}".format(score))
                    main()
            future_pieces.append(Tetromino(BLOCK_NAMES[random.randrange(0, len(BLOCK_NAMES))], block_size))
            for piece in current_piece:
                print("current piece: {}".format(piece.name))
            for piece in future_pieces:
                print("future piece: {}".format(piece.name))
            for piece in current_piece:
                print("current piece: {}".format(piece.name))
            for piece in future_pieces:
                print("future piece: {}".format(piece.name))
                
            if static_blocks != []:
                static_blocks.sort(key=lambda x: x.Rect.y)
                temp = static_blocks[0].Rect.y
                counter = 0
                full_rows = []
                
                for block in static_blocks:
                    if block.Rect.y == temp:
                        counter += 1
                    else:
                        temp = block.Rect.y
                        counter = 1
                    
                    if counter == WIDTH / block_size:
                        full_rows.append(temp)
                        counter = 0
                
                print("full rows: {}".format(full_rows))
                if full_rows != []:
                    static_blocks = delete_items(static_blocks, full_rows.copy())
                    print(full_rows, len(full_rows))
                    score += len(full_rows)
                    print("score: {}".format(score))
                    for block in static_blocks:
                        if block.Rect.y <= full_rows[0]:
                            block.Rect.y += (block_size * len(full_rows))
        
        clock.tick(20)

if __name__ == "__main__":
    main()
import pygame,sys
from random import randrange as rand

tetris_shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6, 6, 6]],

    [[7, 7],
     [7, 7]]
]

colors = [
(0,   0,   0  ),
(255, 85,  85),
(100, 200, 115),
(120, 108, 245),
(255, 140, 50 ),
(50,  120, 52 ),
(146, 202, 73 ),
(150, 161, 218 ),
(35,  35,  35) 
]

def draw_board():
    board = [ [ 0 for x in range(10) ]
            for y in range(22) ]
    board += [[ 1 for x in range(10)]]
    return board


def check_collision(board, shape):
    for cy, row in enumerate(shape):
        for cx, cell in enumerate(row):
            try:
                if cell and board[cy][cx]:
                    return true;
            except IndexError:
             
                return True

def join_matrixes(mat1, mat2):
    for cy, row in enumerate(mat2):
        for cx, val in enumerate(row):
            mat1[cy-1][cx] += val
    return mat1



class Tetris(object):

    def __init__(self):
        pygame.init()
        self.width = 595
        self.height = 900
        self.background_grid = [[ 8 if x%2==y%2 else 0 for x in range(33)] for y in range(50)]
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.init_game()

    def new_stone(self):
        self.stone = self.next_stone[:]
        self,next_sto
    def init_game(self):
        self.board = draw_board()


    def start_game(self):
        if self.gameover:
            self.init_game()
            self.gameover = False

    def drop(self,manual):
        if not self.gameover and not self.paused:
            self.stone_y += 1
            if check_collision(self.board, self.stone, (self.stone_x, self.stone_y)):
                self.board = join_matrixes(self.board, self.stone)
                self.new_stone()

    def draw_matrix(self, matrix):
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val:
                    pygame.draw.rect(self.screen,(200,0,0),pygame.Rect(x*18,y*18,18,18),0)

    def run(self):
        self.gameover = False
        self.paused = False

        while 1:
            self.screen.fill((0, 0, 0))
            if self.gameover:
                pass
            else:
                if self.paused:
                    pass
                else:
                    self.draw_matrix(self.background_grid)
                    # self.draw_matrix(self.board)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.update()
                    sys.exit()


if __name__ == '__main__':
    App = Tetris()
    App.run()

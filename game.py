from random import randrange as rand
import pygame, sys
import datetime
import random

# The configuration
cell_size = 20
cols =      20
full =       0
rows =      40
maxfps =    60

colors = [
(0,   0,   0  ),
(255, 85,  85),
(100, 200, 115),
(120, 108, 245),
(255, 140, 50 ),
(50,  120, 52 ),
(146, 202, 73 ),
(150, 161, 218 ),
(35,  35,  35) #
]

#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = ( 50,  50,  50)
BLACK       = (  0,   0,   0)
RED         = (255,   0,   0)
ORANGE      = (255, 153,   0)
YELLOW      = (255, 255,   0)
GREEN       = ( 51, 255,  51)
BLUE        = (  0,   0, 255)
LIGHTBLUE   = ( 51, 255, 255)
PUPPLE      = (153,   0, 204)
SHADOW      = (130, 130, 130)
DARKBLUE = (20,16,97)


BGCOLOR = BLACK

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
def rotate_clockwise(shape):
    return [ [ shape[y][x]
            for y in range(len(shape)) ]
        for x in range(len(shape[0]) - 1, -1, -1) ]

def check_collision(board, shape, offset):
    off_x, off_y = offset
    for cy, row in enumerate(shape):
        for cx, cell in enumerate(row):
            try:
                if cell and board[ cy + off_y ][ cx + off_x ]:
                    return True
            except IndexError:
                return True
    return False

def remove_row(board, row):
    del board[row]
    return [[0 for i in range(cols)]] + board

def join_matrixes(mat1, mat2, mat2_off):
    off_x, off_y = mat2_off
    for cy, row in enumerate(mat2):
        for cx, val in enumerate(row):
            mat1[cy+off_y-1 ][cx+off_x] += val
    return mat1

def new_board():
    board = [ [ 0 for x in range(cols) ]
            for y in range(rows) ]
    board += [[ 1 for x in range(cols)]]
    return board


def dumbmenu(screen, menu, x_pos = 100, y_pos = 100, font = None,
            size = 70, distance = 1.4, fgcolor = (255,255,255),
            cursorcolor = (255,0,0), exitAllowed = True):




	# Draw the Menupoints
	pygame.font.init()
	if font == None:
		myfont = pygame.font.Font('MKX Title.ttf', size)
	else:
		myfont = pygame.font.SysFont('MKX Title.ttf', size)
	cursorpos = 0
	renderWithChars = False
	for i in menu:
		if renderWithChars == False:
			text =  myfont.render(str(cursorpos + 1)+".  " + i,
				True, fgcolor)
		else:
			text =  myfont.render(chr(char)+".  " + i,
				True, fgcolor)
			char += 1
		textrect = text.get_rect()
		textrect = textrect.move(x_pos,
		           (size // distance * cursorpos) + y_pos)
		screen.blit(text, textrect)
		pygame.display.update(textrect)
		cursorpos += 1
		if cursorpos == 9:
			renderWithChars = True
			char = 65

	# Draw the ">", the Cursor
	cursorpos = 0
	cursor = myfont.render(">", True, cursorcolor)
	cursorrect = cursor.get_rect()
	cursorrect = cursorrect.move(x_pos - (size // distance),
	             (size // distance * cursorpos) + y_pos)

	# The whole While-loop takes care to show the Cursor, move the
	# Cursor and getting the Keys (1-9 and A-Z) to work...
	ArrowPressed = True
	exitMenu = False
	clock = pygame.time.Clock()
	filler = pygame.Surface.copy(screen)
	fillerrect = filler.get_rect()
	while True:
		clock.tick(30)
		if ArrowPressed == True:
			screen.blit(filler, fillerrect)
			pygame.display.update(cursorrect)
			cursorrect = cursor.get_rect()
			cursorrect = cursorrect.move(x_pos - (size // distance),
			             (size // distance * cursorpos) + y_pos)
			screen.blit(cursor, cursorrect)
			pygame.display.update(cursorrect)
			ArrowPressed = False
		if exitMenu == True:
			break
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return -1
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE and exitAllowed == True:
					if cursorpos == len(menu) - 1:
						exitMenu = True
					else:
						cursorpos = len(menu) - 1; ArrowPressed = True


				# This Section is huge and ugly, I know... But I don't
				# know a better method for this^^
				if event.key == pygame.K_1:
					cursorpos = 0; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_2 and len(menu) >= 2:
					cursorpos = 1; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_3 and len(menu) >= 3:
					cursorpos = 2; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_4 and len(menu) >= 4:
					cursorpos = 3; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_5 and len(menu) >= 5:
					cursorpos = 4; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_6 and len(menu) >= 6:
					cursorpos = 5; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_7 and len(menu) >= 7:
					cursorpos = 6; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_8 and len(menu) >= 8:
					cursorpos = 7; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_9 and len(menu) >= 9:
					cursorpos = 8; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_a and len(menu) >= 10:
					cursorpos = 9; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_b and len(menu) >= 11:
					cursorpos = 10; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_c and len(menu) >= 12:
					cursorpos = 11; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_d and len(menu) >= 13:
					cursorpos = 12; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_e and len(menu) >= 14:
					cursorpos = 13; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_f and len(menu) >= 15:
					cursorpos = 14; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_g and len(menu) >= 16:
					cursorpos = 15; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_h and len(menu) >= 17:
					cursorpos = 16; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_i and len(menu) >= 18:
					cursorpos = 17; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_j and len(menu) >= 19:
					cursorpos = 18; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_k and len(menu) >= 20:
					cursorpos = 19; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_l and len(menu) >= 21:
					cursorpos = 20; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_m and len(menu) >= 22:
					cursorpos = 21; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_n and len(menu) >= 23:
					cursorpos = 22; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_o and len(menu) >= 24:
					cursorpos = 23; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_p and len(menu) >= 25:
					cursorpos = 24; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_q and len(menu) >= 26:
					cursorpos = 25; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_r and len(menu) >= 27:
					cursorpos = 26; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_s and len(menu) >= 28:
					cursorpos = 27; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_t and len(menu) >= 29:
					cursorpos = 28; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_u and len(menu) >= 30:
					cursorpos = 29; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_v and len(menu) >= 31:
					cursorpos = 30; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_w and len(menu) >= 32:
					cursorpos = 31; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_x and len(menu) >= 33:
					cursorpos = 32; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_y and len(menu) >= 34:
					cursorpos = 33; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_z and len(menu) >= 35:
					cursorpos = 34; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_UP:
					ArrowPressed = True
					if cursorpos == 0:
						cursorpos = len(menu) - 1
					else:
						cursorpos -= 1
				elif event.key == pygame.K_DOWN:
					ArrowPressed = True
					if cursorpos == len(menu) - 1:
						cursorpos = 0
					else:
						cursorpos += 1
				elif event.key == pygame.K_KP_ENTER or \
				     event.key == pygame.K_RETURN:
							exitMenu = True

	return cursorpos


class TetrisApp(object):
    def __init__(self,width,height,rlim,screen,default_font):

        self.width = width
        self.height = height
        self.rlim = rlim
        self.default_font = default_font
        self.screen = screen

        # self.rlim = 0
        self.bground_grid = [[ 8 if x%2==y%2 else 0 for x in range(cols)] for y in range(rows)]

        self.next_stone = tetris_shapes[rand(len(tetris_shapes))]
        self.init_game()

    def new_stone(self):
        self.stone = self.next_stone[:]
        self.next_stone = tetris_shapes[rand(len(tetris_shapes))]
        self.stone_x = int(cols / 2 - len(self.stone[0])/2)
        self.stone_y = 0
        self.stone_y_shadow = 0

        if check_collision(self.board,self.stone,(self.stone_x, self.stone_y)):
            self.gameover = True

    def init_game(self):
        self.board = new_board()
        self.new_stone()
        self.level = 1
        self.score = 0
        self.lines = 0
        pygame.time.set_timer(pygame.USEREVENT+1, 1000)

    def disp_msg(self, msg, topleft):
        x,y = topleft
        for line in msg.splitlines():
            self.screen.blit(self.default_font.render(line,True,(255,255,255),BGCOLOR),(x,y))
            y+=10

    def center_msg(self, msg):
        for i, line in enumerate(msg.splitlines()):
            msg_image =  self.default_font.render(line, False,
                (255,255,255), BGCOLOR)

            msgim_center_x, msgim_center_y = msg_image.get_size()
            msgim_center_x //= 2
            msgim_center_y //= 2

            self.screen.blit(msg_image, (self.width // 2-msgim_center_x,self.height // 2-msgim_center_y+i*22))

    def draw_matrix(self, matrix, offset):
        off_x, off_y  = offset
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val:
                    pygame.draw.rect(self.screen, colors[val], pygame.Rect( (off_x+x) * cell_size + 1, (off_y+y) * cell_size +1, cell_size -1 ,cell_size -1 ),0)

    def draw_shadow(self, matrix, offset):
        off_x, off_y  = offset
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val:
                    pygame.draw.rect(self.screen, SHADOW, pygame.Rect( (off_x+x) * cell_size , (off_y+y) * cell_size, cell_size  ,cell_size  ),0)

    def draw_background(self,matrix,offset):
        global BGCOLOR
        if BGCOLOR == BLACK:
            c = GRAY
        else:
            c = BLACK
        off_x, off_y  = offset
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val:
                    pygame.draw.rect(self.screen,c,pygame.Rect( (off_x+x) * cell_size, (off_y+y) * cell_size, cell_size,cell_size),0)

    def add_cl_lines(self, n):
        linescores = [0, 40, 100, 300, 1200]
        self.lines += n
        if n > 4:
            n = 4
        self.score += linescores[n] * self.level
        # if self.lines >= self.level*6:
        #     newdelay = 1000-50*(self.level-1)
        #     newdelay = 100 if newdelay < 100 else newdelay
        #     pygame.time.set_timer(pygame.USEREVENT+1, newdelay)

    def move(self, delta_x):
        if not self.gameover and not self.paused:
            new_x = self.stone_x + delta_x
            if new_x < 0:
                new_x = 0
            if new_x > cols - len(self.stone[0]):
                new_x = cols - len(self.stone[0])
            if not check_collision(self.board, self.stone, (new_x, self.stone_y)):
                self.stone_x = new_x




    def quit(self):
        pygame.display.update()
        sys.exit()

    def drop(self, manual):
        if not self.gameover and not self.paused:
            self.score += 1 if manual else 0
            self.stone_y += 1
            if self.score  > self.level * 1000:
                self.level+=1
            newdelay = 1000 - (self.level * 50)
            if newdelay <50:
                newdelay = 20

            pygame.time.set_timer(pygame.USEREVENT+1,newdelay)
            if check_collision(self.board, self.stone,(self.stone_x, self.stone_y)):
                self.board = join_matrixes(self.board, self.stone, (self.stone_x, self.stone_y))
                self.new_stone()
                cleared_rows = 0
                while True:
                    for i, row in enumerate(self.board[:-1]):
                        if 0 not in row:
                            self.board = remove_row(self.board, i)
                            cleared_rows += 1
                            break
                    else:
                        break
                self.add_cl_lines(cleared_rows)
                return True
        return False


    def shadow(self, manual):
        if not self.gameover and not self.paused:
            self.stone_y_shadow += 1
            if check_collision(self.board, self.stone,(self.stone_x, self.stone_y_shadow)):

                return True
        return False

    def shadow_drop(self):
        if not self.gameover and not self.paused:
            self.stone_y_shadow = 0
            while(not self.shadow(True)):
                pass
        self.stone_y_shadow -= 1

        if(self.stone_y_shadow < self.stone_y):
            self.stone_y_shadow = self.stone_y


    def insta_drop(self):
        if not self.gameover and not self.paused:
            while(not self.drop(True)):
                pass

    def rotate_stone(self):
        if not self.gameover and not self.paused:
            new_stone = rotate_clockwise(self.stone)
            if not check_collision(self.board,
                                   new_stone,
                                   (self.stone_x, self.stone_y)):
                self.stone = new_stone

    def toggle_pause(self):
        self.paused = not self.paused

    def start_game(self):
        if self.gameover:
            self.init_game()
            self.gameover = False

    def return_menu(self):
        pygame.display.update()

        new_game = Menu()




    def run(self):
        key_actions = {
            'BACKSPACE':   self.return_menu,
            'LEFT':     lambda:self.move(-1),
            'RIGHT':    lambda:self.move(+1),
            'DOWN':     lambda:self.drop(True),
            'UP':       self.rotate_stone,
            'p':        self.toggle_pause,
            'RETURN':    self.start_game,
            'SPACE':   self.insta_drop
        }

        self.gameover = False
        self.paused = False

        dont_burn_my_cpu = pygame.time.Clock()
        while 1:
            self.screen.fill(BGCOLOR)
            if self.gameover:
                self.center_msg("""Game Over!\nYour score: %d # Press ENTER to continue""" % self.score)
            else:
                if self.paused:
                    self.center_msg("Paused")
                else:
                    self.draw_background(self.bground_grid, (0,0))
                    now = datetime.datetime.now()
                    nowTime = now.strftime('%H:%M:%S')
                    pygame.draw.line(self.screen,
                        (255,255,255),
                        (self.rlim+1, 0),
                        (self.rlim+1, self.height-1))
                    self.disp_msg("Next:", (self.rlim+cell_size,2))

                    self.disp_msg("Score: %d\n\nLevel: %d\n\nLines: %d" % (self.score, self.level, self.lines),(self.rlim+cell_size, cell_size*5))
                    self.disp_msg("backspace:quit \n\n\np : pause \n\n\nspace : quick", (self.rlim+cell_size,200))
                    self.disp_msg(nowTime, (self.rlim+cell_size,650))

                    # print(self.stone_y_shadow)
                    self.draw_matrix(self.board, (0,0))
                    self.draw_shadow(self.stone,(self.stone_x,self.stone_y_shadow))
                    self.draw_matrix(self.stone,(self.stone_x, self.stone_y))
                    self.draw_matrix(self.next_stone,(cols+1,2))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.USEREVENT+1:
                    self.drop(False)
                    self.shadow_drop()
                elif event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    for key in key_actions:
                        if event.key == eval("pygame.K_"+key):
                            key_actions[key]()
                    self.shadow_drop()
            dont_burn_my_cpu.tick(maxfps)


class Menu(object):
    def __init__(self):
        pygame.init()
        icon = pygame.image.load('image.png')
        pygame.display.set_icon(icon)

        self.width = cell_size*(cols+6)
        self.height = cell_size*rows
        self.rlim = cell_size*cols

        pygame.key.set_repeat(250,25)
        self.default_font =  pygame.font.Font('MKX Title.ttf', 16)

        global full
        if full == 0:
            self.screen = pygame.display.set_mode((self.width, self.height))
        else:
            self.screen = pygame.display.set_mode((self.width, self.height),pygame.FULLSCREEN)
        # self.screen = pygame.display.set_mode((self.width, self.height),pygame.FULLSCREEN)

        pygame.event.set_blocked(pygame.MOUSEMOTION)


        self.main()


    def main(self):
        global full
        global BGCOLOR
        self.screen.fill(BGCOLOR)
        pygame.display.update()

        if BGCOLOR == BLACK:
            color_text ='Black'
        else:
            color_text ='Dark Blue'

        if full == 1:
            screen_state = 'Full Screen'
        else:
            screen_state = 'Windowed'
        choose = dumbmenu(self.screen, [
                            'Start Game',
                            str(screen_state),
                            'COLOR : ' + str(color_text),
                            'Quit'], 170,250,None,30,0.5)

        if choose == 0:
            self.tetris_start()

        elif choose == 1:

            if full==1:
                self.screen = pygame.display.set_mode((self.width, self.height))
                full = 0

            else:
                self.screen = pygame.display.set_mode((self.width, self.height),pygame.FULLSCREEN)
                full = 1
            self.main()

        elif choose == 2:
            if BGCOLOR == BLACK:
                BGCOLOR = DARKBLUE
            else:
                BGCOLOR = BLACK
            self.main()

        else :
            pygame.quit()
            sys.exit()


    def tetris_start(self):
        App = TetrisApp(self.width,self.height,self.rlim,self.screen,self.default_font)
        App.run()





if __name__ == '__main__':
    game = Menu()

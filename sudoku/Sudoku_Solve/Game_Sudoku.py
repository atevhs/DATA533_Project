import os
import sys
import time
import pygame
import numpy as np
 
from Sudoku_Show.paint import Paint
from Sudoku_Show.Generate import Generate
 
# inherit from Paint class
class Game_Sudoku(Paint):
    # initiate
    def __init__(self, screen_width, screen_height, selected_width, selected_height,
                 block_gap, block_size, level):
        """ window """
        self.screen_width = screen_width  # width
        self.screen_height = screen_height  # height
        self.block_gap = block_gap  # block gap 10
        self.block_size = block_size  # block size 86
        self.form = ''  # main window of game
 
        self.martix = []  # sudoku game
 
        self.x, self.y = 0, 0  # start position
        self.row, self.col = 0, 0  # relative position
 
        """ others """
        self.tmp = 0  # time interval
        self.time = ""  # 0:00:00
        self.start_time = ""  # start time
        self.end="" #end time
        self.nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # the number in sudoku
        self.empty = []  # blank position
        self.is_same = []  # When the same number appears in the same row, column or square, the position of the same number in Sudoku
        self.issuccess = False  # if game success
        self.start = False  # if game start
 
        """ font """
        self.title_font = ''  
        self.time_font = ''  
        self.tips_font = '' 
        self.font = ''  
 
        """ select window """
        self.selected_form = ""  
        self.selected_width = selected_width  
        self.selected_height = selected_height  
 
        self.selected_font = ""  # easy/medium/hard font and size
 
        self.move_x, self.move_y = 0, 0  # mouse moving position
        self.press_x, self.press_y = 0, 0  # mouse clicking position
 
        self.level = level  # the level of game
        self.counts = [30, 40, 50]  # blank number
 
    # windows setting
    def Form(self):
        """
        :return:
        """
        pygame.init()  # import pygame module
        pygame.display.set_caption("Game Sudoku")  # window title
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # center
        self.form = pygame.display.set_mode([self.screen_width, self.screen_height], 0, 0)  # size of the window
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # center
 
        self.start_time = time.time()
 
        """ initiate """
        self.init()
 
        while True:
            self.Action()  # user action: keyboard/mouse input
            self.IsSuccess()  # determine whether the game success
 
    # select form setting
    def SelectedForm(self):
        """
        :return:
        """
        pygame.init()  
        pygame.display.set_caption("Game Sudoku")  
        os.environ['SDL_VIDEO_CENTERED'] = '1'  
        self.selected_form = pygame.display.set_mode([self.selected_width, self.selected_height], 0, 0)  # window size
 
        while True:
            self.SelectedAction() 
            pygame.display.update()
 
    # user action(main window): keyboard/mouse input
    def Action(self):
        #pygame.display.update()
        for event in pygame.event.get(): 
             # pygame.event.get(): Get all messages and remove them from the queue
            if event.type == pygame.QUIT:  # pygame.QUIT
                # sys.exit()  
                self.SelectedForm()
            elif event.type == pygame.MOUSEMOTION:  # mouse moving
                pos = pygame.mouse.get_pos()
                self.move_x, self.move_y = pos[0], pos[1]
            elif event.type == pygame.MOUSEBUTTONDOWN:  # mouse clicking
                pos = pygame.mouse.get_pos()
                self.press_x, self.press_y = pos[0], pos[1]
                self.row, self.col = (self.press_y - 140 - 1) // 61, (self.press_x - 5 - 1) // 61
            elif event.type == pygame.KEYDOWN:  # keyboard input
                """
                pygame.KEYDOWN when press down the keyboard
                pygame.KEYUP when press up the keyboard
                """
                """ 
                K_ESCAPE: ESC
                """
                if event.key == pygame.K_SPACE:
                    self.start = True
                    self.start_time = time.time()
                elif event.key == pygame.K_ESCAPE:
                    """ game initiate """
                    self.init()
                elif chr(event.key) in self.nums and 0 <= self.row <= 8 and 0 <= self.col <= 8 \
                        and [self.row, self.col] in self.empty:
                    self.IsRight(chr(event.key))
                    self.martix[self.row][self.col] = chr(event.key)
                elif event.key == pygame.K_BACKSPACE:
                    if [self.row, self.col] in self.empty:
                        self.martix[self.row][self.col] = 0
        if self.issuccess==False:
            paint = Paint()
            paint.PaintForm(self.form, self.start_time, self.block_size, self.block_gap,
                                self.move_x, self.move_y, self.press_x, self.press_y, self.martix,
                                self.empty, self.is_same, self.issuccess, self.start,self.end)  # draw grid
            pygame.display.update()
        else:
            paint = Paint()
            paint.PaintForm(self.form, self.start_time, self.block_size, self.block_gap,
                                self.move_x, self.move_y, self.press_x, self.press_y, self.martix,
                                self.empty, self.is_same, self.issuccess, self.start,self.end)  # draw grid
            paint.Paint_success(self.form)
            #pygame.display.update()

    # user action(select window): keyboard/mouse input
    def SelectedAction(self):
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  # pygame.QUIT
                sys.exit()  # The sys.exit() function is used to terminate the process by throwing an exception
            elif event.type == pygame.MOUSEMOTION:  # mouse moving
                pos = pygame.mouse.get_pos()
                self.move_x, self.move_y = pos[0], pos[1]
            elif event.type == pygame.MOUSEBUTTONDOWN:  # mouse clicking
                pos = pygame.mouse.get_pos()
                self.press_x, self.press_y = pos[0], pos[1]
                if 0 < self.press_x < 260 and 0 < self.press_y < 100:
                    self.level = 0
                elif 0 < self.press_x < 260 and 100 < self.press_y < 200:
                    self.level = 1
                elif 0 < self.press_x < 260 and 200 < self.press_y < 300:
                    self.level = 2
            elif event.type == pygame.MOUSEBUTTONUP:  # mouse button up
                self.Form()
        paint = Paint()
        paint.PaintSelected(self.selected_form, self.move_x, self.move_y)  # draw grid
 
    # game initiate
    def init(self):
        self.empty = []
        # sudoku question and answer
        g = Generate(self.counts[self.level])
        self.martix = g.build_martix()
 
        # get the position of blank
        for i in range(9):
            for j in range(9):
                if self.martix[i][j] == 0:
                    self.empty.append([i, j])
 
    # determine whether the input number is right
    def IsRight(self, num):
        """
        :param num: input number
        :return: Whether the row, column, or large table has the same number as num
        """
        """
        self.martix[self.row, :]: row
        self.martix[:, self.col]: column
        self.martix[self.row // 3 * 3: self.row // 3 * 3 + 3, self.col // 3 * 3: self.col // 3 * 3 + 3]: the grid
        """
        rowset = self.martix[self.row, :]  # row
        colset = self.martix[:, self.col]  # column
        blockset = self.martix[self.row // 3 * 3: self.row // 3 * 3 + 3, self.col // 3 * 3: self.col // 3 * 3 + 3].reshape(9)  # grid
 
        num = int(num)
        self.is_same = []
        if num in rowset or num in colset or num in blockset:
            pos = np.where(self.martix == num)
            pos_x, pos_y = pos[0], pos[1]
            for i in range(len(pos_x)):
                self.is_same.append([pos_x[i], pos_y[i]])
 
    # determine whether the game is success
    def IsSuccess(self):
        if self.martix.min() > 0 and not self.is_same:
            self.empty = []
            self.issuccess = True
            self.end = time.time()
        else:
            self.issuccess = False
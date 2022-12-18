import time
import pygame
import datetime
 
 
class Paint(object):
    # initiate
    def __init__(self):
        self.martix = []  # the number in 9 by 9 grid
        self.timing = ""
 
    # draw seleced form
    def PaintSelected(self, selected_form, move_x, move_y):
        """ game background """
        # fill(color)
        selected_form.fill((193,205,193))
 
        """ font setting """
        # initiate font
        pygame.font.init()
 
        # part_1: easy
        # pygame.draw.rect(self.selected_form, (128, 128, 128), (0, 0, 260, 100))
        selected_font = pygame.font.SysFont('comicsansms', 30, True)
        easy_text = selected_font.render('EASY', True, (0, 128, 128))
        selected_form.blit(easy_text, (90, 30))
 
        # part_2: medium
        # pygame.draw.rect(self.selected_form, (128, 128, 128), (0, 100, 260, 100))
        medium_text = selected_font.render('MEDIUM', True, (128, 0, 128))
        selected_form.blit(medium_text, (68, 130))
 
        # part_3: hard
        # pygame.draw.rect(self.selected_form, (128, 128, 128), (0, 200, 260, 100))
        hard_text = selected_font.render('DIFFICULT', True, (0, 128, 0))
        selected_form.blit(hard_text, (55, 230))
 
        """ mouse moving """
        if 0 < move_x < 260 and 0 < move_y < 100:
            pygame.draw.rect(selected_form, (128, 128, 128), (0, 0, 260, 100))
            easy_text = selected_font.render('EASY', True, (255, 255, 255))
            selected_form.blit(easy_text, (90, 30))
        elif 0 < move_x < 260 and 100 < move_y < 200:
            pygame.draw.rect(selected_form, (128, 128, 128), (0, 100, 260, 100))
            medium_text = selected_font.render('MEDIUM', True, (255, 255, 255))
            selected_form.blit(medium_text, (68, 130))
        elif 0 < move_x < 260 and 200 < move_y < 300:
            pygame.draw.rect(selected_form, (128, 128, 128), (0, 200, 260, 100))
            hard_text = selected_font.render('DIFFICULT', True, (255, 255, 255))
            selected_form.blit(hard_text, (55, 230))
 
    # draw main form
    def PaintForm(self, form, start_time, block_size, block_gap,
                  move_x, move_y, press_x, press_y, martix, empty, is_same, issuccess, start,end_time):
        """ game background """
        # fill(color)
        form.fill((220, 220, 220))
 
        """ main form---upper """
        # initiate font
        pygame.font.init()
        # add title
        # f = pygame.font.get_fonts() 
        # pygame.font.Font.render()
        title_font = pygame.font.SysFont('arial', 50, True)
        title_text = title_font.render('Sudoku Game', True, (128, 0, 128))
        form.blit(title_text, (70, 3))

        pygame.draw.rect(form, (128, 128, 128), (410, 3, 130, 67))
        time_font = pygame.font.SysFont('arial', 28, True)
        time_text = time_font.render('Time', True, (0, 255, 255))
        form.blit(time_text, (440, 5))

        if issuccess==False:
        # add time: 0:00:00
            tmp = round(time.time() - int(start_time), 0)
            self.time = str(datetime.timedelta(seconds=tmp))
            digtial_time = time_font.render(self.time, True, (255, 250, 250))
            form.blit(digtial_time, (420, 35))
        else:
            tmp = round(int(end_time) - int(start_time), 0)
            self.time = str(datetime.timedelta(seconds=tmp))
            digtial_time = time_font.render(self.time, True, (255, 250, 250))
            form.blit(digtial_time, (420, 35))
            #pygame.display.update()

 
        #time.sleep(1)

        # game description
        tips_font = pygame.font.SysFont('comicsansms', 15)
        tips_text = tips_font.render('Fill 9x9 grid to make each row,column and 3x3 section contain 1 to 9', True, (0, 0, 0))
        form.blit(tips_text, (25, 70))
 
        tips_text = tips_font.render('Each number used once and only once in each section', True, (0, 0, 0))
        form.blit(tips_text, (25, 90))
 
        tips_text = tips_font.render('Press Esc To Restart', True, (0, 0, 0))
        form.blit(tips_text, (25, 110))
 
        """ main window————middle """

        pygame.draw.rect(form, (0, 0, 0), (5, 140, 550, 550))  

        for i in range(9):
            for j in range(9):
                # (x, y) initiate position of block
                x = j * block_size + (j + 1) * block_gap
                y = i * block_size + (i + 1) * block_gap
 
                """ mouse moving """
                # when mouse moving to the block,it will change color
                if x + 5 < move_x < x + 5 + block_size and y + 140 < move_y < y + 140 + block_size:
                    pygame.draw.rect(form, (220, 220, 220), (x + 5, y + 140, block_size, block_size))
                else:
                    pygame.draw.rect(form, (255, 255, 255), (x + 5, y + 140, block_size, block_size))
 
                """ mouse click """
                # when the mouse press the block, the row and column will change color
                # column
                if x + 5 < press_x < x + 5 + block_size and 140 < press_y < 690:
                    pygame.draw.rect(form, (220, 220, 220), (x + 5, y + 140, block_size, block_size))
                # row
                if y + 140 < press_y < y + 140 + block_size and 5 < press_x < 555:
                    pygame.draw.rect(form, (220, 220, 220), (x + 5, y + 140, block_size, block_size))
 
                # draw number
                num_font = pygame.font.SysFont('comicsansms', 45, True)  # font and size
                if martix[i][j] != 0:
                    if [i, j] not in empty and [i, j] not in is_same:
                        num_text = num_font.render(str(martix[i][j]), True, (0, 0, 0))
                    elif [i, j] not in empty and [i, j] in is_same:
                        num_text = num_font.render(str(martix[i][j]), True, (255, 0, 0))
                    else:
                        num_text = num_font.render(str(martix[i][j]), True, (65, 105, 225))
                # if martix[i][j] == 0:
                #     num_text = num_font.render(str(martix[i][j]), True, (255, 255, 255))
                # else:
                #     num_text = num_font.render(str(martix[i][j]), True, (0, 0, 0))
                    form.blit(num_text, (x + 22, y + 140))

        # draw border
        pygame.draw.rect(form, (65, 105, 225), (5, 140, 185, 185),2) 
        pygame.draw.rect(form, (65, 105, 225), (5, 323, 185, 185),2)  
        pygame.draw.rect(form, (65, 105, 225), (5, 506, 185, 185),2)  

        pygame.draw.rect(form, (65, 105, 225), (188, 140, 185, 185),2)  
        pygame.draw.rect(form, (65, 105, 225), (188, 323, 185, 185),2)  
        pygame.draw.rect(form, (65, 105, 225), (188, 506, 185, 185),2)  

        pygame.draw.rect(form, (65, 105, 225), (371, 140, 185, 185),2)  
        pygame.draw.rect(form, (65, 105, 225), (371, 323, 185, 185),2)  
        pygame.draw.rect(form, (65, 105, 225), (371, 506, 185, 185),2)  

        """ game not start """
        if not start:
            pygame.draw.rect(form, (192, 192, 192), (100, 250, 360, 300))
            font = pygame.font.SysFont("comicsansms", 30, True)
            str_text = font.render('Press Blank To Start', True, (128, 0, 128))
            form.blit(str_text, (130, 375))

    def Paint_success(self,form): 
        success_font = pygame.font.SysFont("comicsansms", 30, True)
        #str_text = success_font.render('*********************', True, (178, 34, 34))
        Img = pygame.image.load('game-over.png')
        form.blit(Img, (30,150))
        #form.blit(str_text, (115, 367))
        pygame.display.update((50,50,150,200))
        return True

class Paintchild(Paint):
    def __init__(self,msg):
        super().__init__()
        self.msg = msg
    def Paint_success(self,form,msg):
        Paint.Paint_success(self,form)
        success_font1 = pygame.font.SysFont("arial", 60, True)
        str_text1 = success_font1.render(msg, True, (0, 128, 0))
        form.blit(str_text1, (50, 367))
        pygame.display.update((5,140,555,560))
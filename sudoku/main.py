from Sudoku_Solve import configs
from Sudoku_Solve.Game_Sudoku import Game_Sudoku
import pygame
 
 
def main(args_form,args_selectedform,args_block):
    """
    screen_width: Width of the form
    screen_height: Height of the form
    """
    screen_width = args_form.screen_width
    screen_height = args_form.screen_height
    selected_width = args_selectedform.selected_width
    selected_height = args_selectedform.selected_height
    block_gap = args_block.block_gap
    block_size = args_block.block_size
    level = args_block.level
 
    game = Game_Sudoku(screen_width, screen_height, selected_width, selected_height,
                       block_gap, block_size, level)
    game.SelectedForm()
    # game.Form()

if __name__ == '__main__':
    args_form = configs.parse_args1()
    args_selectedform = configs.parse_args2()
    args_block = configs.parse_args3()
    main(args_form,args_selectedform,args_block)
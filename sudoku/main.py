from Sudoku_Solve import configs
from Sudoku_Solve.Game_Sudoku import Game_Sudoku
 
 
 
def main(args):
    """
    screen_width: Width of the form
    screen_height: Height of the form
    """
    screen_width = args.screen_width
    screen_height = args.screen_height
    selected_width = args.selected_width
    selected_height = args.selected_height
    block_gap = args.block_gap
    block_size = args.block_size
    level = args.level
 
    game = Game_Sudoku(screen_width, screen_height, selected_width, selected_height,
                       block_gap, block_size, level)
    game.SelectedForm()
    # game.Form()

if __name__ == '__main__':
    args = configs.parse_args()
    main(args)

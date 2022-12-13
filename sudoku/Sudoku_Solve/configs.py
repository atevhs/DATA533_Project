import argparse
 
def parse_args1():
 
    parser1 = argparse.ArgumentParser(description='Sudoku Game')
 
    # Form
    """
    screen_width: Width of the form
    screen_height: Height of the form
    """
    parser1.add_argument('--screen_width', default=560, type=int)
    parser1.add_argument('--screen_height',default=700, type=int)

    return parser1.parse_args()

def parse_args2(): 

    parser2 = argparse.ArgumentParser(description='Sudoku Game')

    # Selected form
    """
    selected_width: Width of the selected form
    selected_height: Height of the selected form
    """

    parser2.add_argument('--selected_width', default=260, type=int)
    parser2.add_argument('--selected_height', default=300, type=int)

    return parser2.parse_args()

def parse_args3(): 

    parser3 = argparse.ArgumentParser(description='Sudoku Game')

    # Difficulty level
    """
    level: The difficulty level of game, default value is 0
    0 means simple; 1 means medium; 2 means hard
    """

    parser3.add_argument('--level', default=0, type=int)

    # Block
    """
    block_gap: Gap between two blocks
    block_size: Size of a block
    """
    parser3.add_argument('--block_gap', default=1,type=int)
    parser3.add_argument('--block_size', default=60,type=int)
 
    return parser3.parse_args()

import argparse
 
def parse_args():
 
    parser = argparse.ArgumentParser(description='Sudoku Game')
 
    # Form
    """
    screen_width: Width of the form
    screen_height: Height of the form
    """
    parser.add_argument('--screen_width', default=560, type=int)
    parser.add_argument('--screen_height',default=700, type=int)
 
    # Selected form
    """
    selected_width: Width of the selected form
    selected_height: Height of the selected form
    """
    parser.add_argument('--selected_width', default=260, type=int)
    parser.add_argument('--selected_height', default=300, type=int)
 
    """
    block_gap: Gap between two blocks
    block_size: Size of a block
    """
    parser.add_argument('--block_gap', default=1,type=int)
    parser.add_argument('--block_size', default=60,type=int)
 
    return parser.parse_args()

# Sudoku Game Technical Specification Doc

### 1) Sub-Package : Sudoku_Show
- ##### Module : Paint.py : 
It uses brush functions to paint the interface of the window. It uses python inbuild libraries like time/datetime and pygame.

 - **Class Paint** 
 attributes of paint are matrix and timing.
1) **Function : PaintSelected**:
*input parameters* :  self, 
                    selected_form, 
                    move_x, 
                    move_y
        It constructs the game background and font setting for selected EASY, MEDIUM and HARD levels. It also captures mouse_movement.
2) **Function : PaintForm**:
*input parameters* :  self, 
                    form, 
                    start_time, 
                    block_size, 
                    block_gap,
                    move_x, 
                    move_y, 
                    press_x, 
                    press_y, 
                    martix, 
                    empty, 
                    is_same, 
                    issuccess, 
                    start,
                    end_time)
It constructs the selected game background. It captures mouse_movement for selected block like when mouse moving to the block,it will change color,
when the mouse press the block, the row and column will change color.
It also constructs and operates the time block.
If the game doesn't start, it gives option of pressing blank to start.
3) **Function : Paint_success**:
*input parameters* :  self, 
                    form
It constructs the success window after the game is successfully completed.                    
- ##### Module : Generate.py : 
It generates random Sudoku puzzles that conform to the rules of the game, and guarantees unique solutions. Python inbuilt libraries used are random and numpy.
1) **Function : LasVegas**:
It uses Lasvegas algorithm to generate sudoku using python library random.
*input parameters* :  self, 
                    counts
it returns the random numbers as per the difficulty: 30,40 and 50.
2) **Function : Solve**:
*input parameters* : self
It uses DFS algorithm to solve sudoku.
3) **Function : Get_possible**:
it prepares the matrix as arranged as per row grid and column grid.
*input parameters* :row: x-coordinate
        :col: y-coordinate
        :return: return possible number set
4) **Function : Generate**:
This is to Generate Sudoku puzzles from Sudoku disks.
*input parameters* :n i.e. number of blanks for sudoku based on level.
5) **Function : IsUnique**:
determine whether we have unique solution
*input parameters* :row: x-coordinate
        :col: y-coordinate
        :return : True/False

###  2) Sub-Package : Sudoku Solve
- ##### Module : Config.py : 
 A configuration file where some parameters can be changed via reading command-line positional arguments using argparse library from python

This is for parsing the arguments for configuration input from command-line.
###### Function : parsing arguments for main screen
  - **screen_width**: Width of the form. argument from command-line = --screen_width and default value=560 type=int
 - **screen_height**: Height of the form.argument from command-line = --screen_height and default value=700 type=int
 
###### Function : parsing arguments for selected screen
 - **selected_width**: Width of the selected form.argument from command-line = --selected_width and default value=260 type=int
 - **selected_height**: Height of the selected form.argument from command-line = --selected_height and default value=300 type=int

###### Function : parsing arguments for block gap, bloack size and game level.
 - **level**: The difficulty level of game, default value is 0. argument from command-line = --level type=int
(*0 :simple; 1 :medium; 2 :hard*)
 - **block_gap**: Gap between two blocks.argument from command-line =--block_gap and default=1 type=int
 - **block_size**: Size of a block.argument from command-line =--block_size and default=60 type=int

| Parameter | command-line argument | default value | type |
|--|--|--|--|
|screen_width|--screen_width|560|int|
|screen_height|--screen_height|700|int|
|selected_width|--selected_width|260|int|
|selected_height|--selected_height|300|int|
|level|--level|0|int|
|block_gap|--block_gap|1|int|
|block_size|--block_size|60|int|

- ##### Module : Game_Sudoku.py : 
It evaluates User input settings and determining whether user input matches the rules.

1) **Function : __init__** : for initialization and initiation.
input parameters : (self, screen_width, screen_height, selected_width, selected_height,block_gap, block_size, level)
2) **Function : Form** : for window settings
3) **Function : SelectedForm** : for selected window setting
4) **Function : Action** : user action(main window): keyboard/mouse input
    pygame.KEYDOWN when press down the keyboard
    pygame.KEYUP when press up the keyboard
    K_ESCAPE: ESC
5) **Function : SelectedAction** : captures the selected action
6) **Function : IsRight** : determine whether the input number is right
        :param num: input number
        :return: Whether the row, column, or large table has the same number as num
        self.martix[self.row, :]: row
        self.martix[:, self.col]: column
        self.martix[self.row // 3 * 3: self.row // 3 * 3 + 3, self.col // 3 * 3: self.col // 3 * 3 + 3]: the grid
7) **Function : IsSuccess** : determine whether the game is success.
    






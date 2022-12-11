# Sudoku Game Project

**Contributors : Tia Wang & Shveta Sharma**

**Course : DATA-533**

###### Introduction
**Sudoku** is a mathematical game that originated in Switzerland in the 18th century. It is a logic game that uses paper and pencil to perform calculations. Players need to reason out the numbers of all the remaining spaces based on the known numbers on a 9×9 board, and satisfy that the numbers in each row, column, and thick-line palace (3*3) contain 1-9 and are not repeated.

- **Choose Level** [Easy/Medium/Difficult]
- **Generate Sudoku Layout**
- **Game process** (i.e. identify same number user input)
- **Input Success Tracking**
- **Finish Game**

### Real World Application of Sudoku Game :

1)**Artificial Intelligence** : Sudoku algorithms are actively used in Artificial Intelligence to train bots for various tasks. These grids and the logic behind them helps developers train bots to understand human behavior and adapt to it.

2)**Mathematics** : Sudoku grids are sometimes translated to coloring grids and this links them to solve crucial mathematical complications.

3)**Spyware** : Sudoku grids are sometimes used to hide secret messages in hiding techniques such as Steganography, a key is hidden behind the puzzle to find the answer.


##### Packages
- *Main.py* (Main module, start game)
 - **Sub-package1**-sudoku_solve
 
 - **Module1**-config 

(A configuration file where some parameters can be changed.)
    
    - Function1 - Main window parameters
    - Function2 - Selected window parameters
    - Function3 - level and block parameters
    
 - **Module2**-Game_sudoku

(User input settings and determining whether user input matches the rules)

    - Function1 - main and select window setting (user input)
    - Function2 - user actions (main and select window)
    - Function3 - Determine if the numbers filled in match the game requirements
    - Function4 - Determine if the game is successful
    
  - **Sub-package2**-sudoku_show
  - **Module1**-paint 
 
(Mainly brush functions to paint the interface of the window)
 
    - Function1 - The selected window
    - Function2 - The main window

  - **Module2**-generate 

(Mainly generates random Sudoku puzzles that conform to the rules of the game, and guarantees unique solutions)
    
    - Function1 - build matrix
    - Function2 - LasVegas algorithm to build sudoku
    - Function3 - solve sudoku
    - Function4 - Determine if there is only one answer

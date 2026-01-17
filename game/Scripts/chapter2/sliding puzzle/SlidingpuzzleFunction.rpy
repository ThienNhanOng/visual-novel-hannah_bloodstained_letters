# Default puzzle state
default puzzleState = []
init python:
    import random

    
    #Swap two tiles
    def swap_tiles(index1, index2):
        puzzleState[index1], puzzleState[index2] = puzzleState[index2], puzzleState[index1]

    #Find the blank tile
    def find_blank():
        return puzzleState.index(None)

    #Check if puzzle is solved
    def is_puzzle_solved():
        return puzzleState == puzzleImages
    
    #Shuffle the puzzle tiles using fisher yates algorithm
    def shufflePuzzle():
        #make a copy of the original puzzle that is sorted
        store.puzzleState = store.puzzleImages[:]
        store.puzzle_completed = False #flag puzzle as unsolved
        
        #Call fisher yates from card shuffle file. renpy.random keep desyncing.
        fisherYates(store.puzzleState)

    #Instantly solve puzzle
    def solve_puzzle_instantly():
        store.puzzleState = store.puzzleImages[:]
        store.puzzle_completed = True

# importing the pygame
import pygame
# importing request library
import requests

# setting up the width and the background color of the window
WIDTH = 550
background_color = (38, 38, 38)
original_grid_element_color = (255, 255, 255) 
buffer = 5
#adding API in our sudoku game
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
grid_original = [[grid[x][y]] for y in range[len[grid[0]]]] for x in range[len[grid]]
#adding the functionality that can add the number on user bases
def insert(win, position):
    i,j = position[1], position[0]
    #adding the font and its size
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                   
                if(grid_original[i-1][j-1] != 0):
                    return
                if(event.key == 48): #checking with 0
                  grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
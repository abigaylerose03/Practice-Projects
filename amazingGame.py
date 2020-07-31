
import pygame
from pygame.locals import *
from tkinter import *
from random import *
from PIL import Image, ImageTk

pygame.init()
root = Tk()

""" What is Do You Know De Wae? It's a desktop application that
    generates completely randomized mazes to solve """

def main():
    
    """ sets general width and height for usage in the game """
    width = 640
    height = 490

    """ frames-per-second """
    fps = 60

    screen = pygame.display.set_mode((width+32, height-32))
    title = "Find Your Wae"
    pygame.display.set_caption(title)

    timer = pygame.time.Clock()

    """ inits the built-in pygame colors for usage within the game """
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    
    score = 0
    fontSize = 30
    time = 15
    oneSecond = fps

    defeatMessage = "Game Over!"
    limit = 0 # when the time reaches 0, game over!!!

    status = "game"


    """ Draws the Score """
    class ScoreBoard() :
        def __init__(self):

            self.status = "game"

            self.score = 0

            self.milis = 15
            self.time = 15
            
            self.font1 = pygame.font.SysFont(None, int(fontSize))
            self.font2 = pygame.font.SysFont(None, round(int(width/ len(defeatMessage))))
            self.font3 = pygame.font.SysFont(None, int(fontSize))
            
            self.render1 = self.font1.render("Score: " + str(self.score), 1, blue)
            self.render2 = self.font2.render(defeatMessage, 1, red)
            self.render3 = self.font1.render("Time: " + str(self.time), 1, blue)
        def paint(self):
            self.milis -= 1
            if self.milis % oneSecond == 0:
                self.time -= 1
            if self.time == limit:

                self.status = "loss"
            self.render3 = self.font1.render("Time: " + str(self.time), 1, blue)
            self.render1 = self.font1.render("Score: " + str(self.score), 1, blue)

            if self.status == "loss":
                screen.blit(self.render2, (0, 0))
            else:
                screen.blit(self.render1, (0,0))
                screen.blit(self.render3, (0, 25))
            

    """ This class generates each individual pixel block
        as the walls of the maze """
    class Block():
        
        def __init__(self, size, x, y):
            self.size = size
            self.x = x
            self.y = y

        def paint(self):
            pygame.draw.rect(screen, white, [self.x, self.y, self.size, self.size])


    """ Seperate method that adds in-game collision functionality """
    def collide(x1, y1, w1, h1, x2, y2, w2, h2):
        rect1 = pygame.Rect(x1, y1, w1, h1)
        rect2 = pygame.Rect(x2, y2, w2, h2)
        return rect1.colliderect(rect2)


    
    """ Player class that controls green player movement ->
        size, speed, and direction """
    class Player():

        def __init__(self):
            self.size = 32
            self.x = self.size
            self.y = self.size
            self.speed = 4
            self.dir = 0

        def paint(self):
            pygame.draw.rect(screen, green, [self.x, self.y, self.size, self.size])
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_LEFT]:
                self.x -= self.speed
                self.dir = 1
            elif self.keys[pygame.K_RIGHT]:
                self.x += self.speed
                self.dir = 2
            elif self.keys[pygame.K_UP]:
                self.y -= self.speed
                self.dir = 3
            elif self.keys[pygame.K_DOWN]:
                self.y += self.speed
                self.dir = 4

    """ The class that 'paints' the end block
        the player moves to this block in order to complete the game """
    class EndObject():

        def __init__(self):
            self.size = 32
            self.x = width-self.size
            self.y = height-self.size

        def paint(self):
            pygame.draw.rect(screen, red, [self.x, self.y, self.size, -self.size])

    """ Generates the actual maze using the Block class """
    class MazeGenerator():

        def __init__(self, tiles, block_size):
            self.tiles = tiles
            self.size = block_size
            self.blocks = list()

        def generate(self):
            for i in range(self.tiles):
                x = randint(0, width // self.size) * self.size 
                y = randint(0, height // self.size) * self.size
                if x != width-self.size and y != height-self.size and x != self.size and y != self.size:
                    self.blocks.append(Block(self.size, x, y)) 
          
                
        def paint(self):
            for block in self.blocks:
                block.paint()


    """ Initializes the menu """
    class Menu(Frame):

        def __init__(self, master = None):
            
            Frame.__init__(self, master)
            self.master = master
            self.init_window()

        def init_window(self):
            self.master.title("Do You Know De Wae?")
            # inits the title
            self.pack(fill = BOTH, expand = 1)  
            self.pack(fill = BOTH, expand = 1)
            self.pack(fill = BOTH, expand = 1)
                                
            playButton = Button(self, bg = "yellow", width = 50, text = "Play Now!", command = self.display_all)
            playButton.place(x = 80, y = 180)

            exitButton = Button(self, bg = "red", width = 50, text = "Exit", command = self.exit_game)
            exitButton.place(x = 80, y = 215)

        """ within the menu class, this display_all() method creates instances of the EndObject and Player class
            drawing them on the screen """
        def display_all(self):

            screen = pygame.display.set_mode((width+32, height-32))
            title = "Find Your Wae"
            pygame.display.set_caption(title)
            
            self.tiles = 100
            
            self.generator = MazeGenerator(self.tiles, 32)
            self.generator.generate()
            
            self.end = EndObject()
            self.player = Player()
            self.scoreBoard = ScoreBoard()
            

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                        exit()
                    
                pygame.display.update()

                screen.fill(black) # fills the screen with black, so the player doesn't overwrite itself
                if self.scoreBoard.status != "loss":
                    
                    self.end.paint()
                    self.player.paint()
                    self.generator.paint()
                    
                    for i in self.generator.blocks:
                        if collide(i.x, i.y, i.size, i.size, self.player.x, self.player.y, self.player.size, self.player.size): 
                            if self.player.dir == 1:
                                self.player.x += self.player.speed # left key
                            if self.player.dir == 2:
                                self.player.x -= self.player.speed # right key
                            if self.player.dir == 3:
                                self.player.y += self.player.speed # up key
                            if self.player.dir == 4:
                                self.player.y -= self.player.speed # down key
                if collide(self.player.x, self.player.y, self.player.size, self.player.size, self.end.x, self.end.y, self.end.size, self.end.size):
                    self.player.x = 32
                    self.player.y = 32
                    del self.generator.blocks[0:len(self.generator.blocks)]
                    self.generator.generate()
                    self.scoreBoard.time = 15 # resets time to default
                    self.scoreBoard.milis = 15
                    self.scoreBoard.score += 10
                    
                self.scoreBoard.paint()
                timer.tick(fps)

        def exit_game(self):
            exit()
        

    
    root.geometry("500x500")

    game = Menu(root) # init the menu
       
    game.configure(bg = 'grey')
    label = Label(root, text = "A Simple Game Created By ~ARP", bg = "pink")
    label.pack()
    
    
    root.mainloop() # kick off the main menu loop

    

if __name__ == "__main__":
    main()
    

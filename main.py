# import the pygame module so we can use it
import pygame

# set up colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)

# set up screen
W = 640
H = 480
screen = pygame.display.set_mode( (W, H) )
screen.fill(BLACK)

class Ship:
    def __init__(self, size=15, Color=WHITE):
        self.x = W / 2
        self.y = H / 2
        self.color = Color
        self.base = size
        self.height = 1.5 * size
        
    def vertices(self):
        # There is probably some built-in type that would make this easier.
        # This isn't any of the definitions of the center of triangle, close enough for today
        vself = [[(-self.base * 0.5)+self.x, (self.height * 0.5)+self.y],
                 [(self.base * 0.5)+self.x, (self.height * 0.5)+self.y],
                 [self.x, (-self.height * 0.5)+self.y]]
        return vself

# define a main function
def runGame():
    # initialize the pygame module
    pygame.init()
    
    # define a variable to control the main loop
    running = True
    
    # get ship
    ship = Ship()
    pygame.draw.polygon(screen, ship.color, ship.vertices())
    pygame.display.flip()
    
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False to ext the main loop
                running = False
                
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__"                :
    # call the main function
    runGame()
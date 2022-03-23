import pygame
import sys
import random

# This class represents the moving snake
class Snake():
    def __init__(self):
        # We set the snakes's length to 1
        self.length = 1
        # We set the snake's position to the center of the screen
        self.positions = [((screen_width/2), (screen_height/2))]
        # The snake is pointing to a random direction
        self.direction = random.choice([up, down, left, right])
        # Limegreen color
        self.color = (50,205,50)
    
    # Initialize the game score to 0
        self.score = 0
    # This function returns the position of the head of the snake which is stored in the "positions" list properties already created
    def get_head_position(self):
        return self.positions[0]

    # If the snake measures only one block it can move to any direction
    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        # But if the snake is longer then one block it has only 3 possible (valid) movement patterns because it cant reverse
        else:
            self.direction = point

# This is how the snake moves
    def move(self):
        # First we get the position of the head of the snake
        cur = self.get_head_position()
        # We get the current direction
        x,y = self.direction
        new = (((cur[0]+(x*gridsize))%screen_width), (cur[1]+(y*gridsize))%screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self,surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)

# This class represents the stationary blocks that the snake must eat to grow
class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

# Here we randomize the position of the food
    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

# Here we draw the representation of the food
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

def drawGrid(surface):
    # Double FOR loop to iterate over each x, y coordinate in our grid
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            # If the x + y sum is divisible by 2 then   
            if (x+y)%2 == 0:
                # we draw a sqaure at that position
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(93,216,228), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (84,194,205), rr)

# Global variables for the game features
screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

# possible movements of the snake
up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

# Main game loop which runs untill the game is exited
def main():
    # Initialize pygame
    pygame.init()
    # Intialize the clock
    clock = pygame.time.Clock()
    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
    # Draw the screen and surface that gets updated whenever an action is performed
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("monospace",16)

    while (True):
        # we set the clock at 5 frames per second
        clock.tick(5)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        # We update and refresh the screen and the surface
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()

main()
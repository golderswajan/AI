import pygame

# Define some colors
BLACK = (41, 161, 151)
WHITE = (255, 255, 240)
GREEN = (219, 68, 55)
RED = (255, 0, 0)


def draw_the_queen(queen_matrix,comment, no):
    WIDTH = 61
    HEIGHT = 61
    MARGIN = 1

    grid = []
    for row in range(8):
        grid.append([])
        for column in range(8):
            grid[row].append((row + column) % 2)  # Append a cell
    # print(queen_matrix)
    for column in range(len(queen_matrix)):
        current_row = list(queen_matrix[:, column]).index(1)
        grid[current_row][column] = 2


    pygame.init()
    WINDOW_SIZE = [500, 500]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("No->" + str(no+1)+" Attack->" + comment)

    done = False

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
        # Set the screen background
        screen.fill(BLACK)

        # Draw the grid
        for row in range(8):
            for column in range(8):
                color = WHITE
                if grid[row][column] == 1:
                    color = BLACK
                elif grid[row][column] == 2:
                    color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    pygame.quit()
    return

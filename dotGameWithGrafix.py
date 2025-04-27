import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
N = 5  # Grid size (N x N)
WIDTH, HEIGHT = 500, 500  # Window size
BLOCK_SIZE = WIDTH // N  # Size of each block

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots and Boxes Game")

# Enum for players
RED_PLAYER = 0
BLUE_PLAYER = 1
score = [0, 0]
turn = RED_PLAYER

# Grid state
grid = [[' ' for _ in range(N-1)] for _ in range(N-1)]
h = [[False for _ in range(N-1)] for _ in range(N)]
v = [[False for _ in range(N)] for _ in range(N-1)]

# Font
font = pygame.font.SysFont("Arial", 24)

# Clear screen function
def clear_screen():
    screen.fill(WHITE)

# Draw the grid
def draw_grid():
    # Draw horizontal lines (dots)
    for i in range(N):
        for j in range(N):
            pygame.draw.circle(screen, BLACK, (j * BLOCK_SIZE, i * BLOCK_SIZE), 5)

    # Draw the grid lines
    for i in range(1, N):
        pygame.draw.line(screen, BLACK, (0, i * BLOCK_SIZE), (WIDTH, i * BLOCK_SIZE), 2)  # horizontal lines
        pygame.draw.line(screen, BLACK, (i * BLOCK_SIZE, 0), (i * BLOCK_SIZE, HEIGHT), 2)  # vertical lines

# Draw the lines (horizontal and vertical)
def draw_lines():
    for i in range(N - 1):
        for j in range(N - 1):
            if h[i][j]:
                pygame.draw.line(screen, RED if grid[i][j] == 'R' else BLUE,
                                 (j * BLOCK_SIZE, i * BLOCK_SIZE),
                                 ((j + 1) * BLOCK_SIZE, i * BLOCK_SIZE), 5)
            if v[i][j]:
                pygame.draw.line(screen, RED if grid[i][j] == 'R' else BLUE,
                                 (i * BLOCK_SIZE, j * BLOCK_SIZE),
                                 (i * BLOCK_SIZE, (j + 1) * BLOCK_SIZE), 5)

# Draw the boxes
def draw_boxes():
    for i in range(N - 1):
        for j in range(N - 1):
            if grid[i][j] != ' ':
                text = font.render(grid[i][j], True, RED if grid[i][j] == 'R' else BLUE)
                screen.blit(text, (j * BLOCK_SIZE + BLOCK_SIZE // 4, i * BLOCK_SIZE + BLOCK_SIZE // 4))

# Add score for the player
def add_score(player):
    if player == RED_PLAYER:
        score[RED_PLAYER] += 1
    else:
        score[BLUE_PLAYER] += 1

# Check if the move is within bounds
def is_inside_grid(is_horizontal, x, y):
    if is_horizontal:  # Horizontal
        return x >= 0 and x < N - 1 and y >= 0 and y < N - 1
    else:  # Vertical
        return x >= 0 and x < N - 1 and y >= 0 and y < N - 1

# Check if the game is finished
def game_finished():
    return (score[RED_PLAYER] + score[BLUE_PLAYER]) == (N - 1) * (N - 1)

# Update grid and score when a valid line is drawn
def update_grid(is_horizontal, x, y, player):
    box_completed = False
    if is_horizontal:
        if h[x][y]:
            return False
        h[x][y] = True

        if x > 0 and h[x - 1][y] and v[x - 1][y] and v[x - 1][y + 1]:
            grid[x - 1][y] = 'R' if player == RED_PLAYER else 'B'
            add_score(player)
            box_completed = True
        if x < N - 1 and h[x + 1][y] and v[x][y] and v[x][y + 1]:
            grid[x][y] = 'R' if player == RED_PLAYER else 'B'
            add_score(player)
            box_completed = True
    else:
        if v[x][y]:
            return False
        v[x][y] = True

        if y > 0 and v[x][y - 1] and h[x][y - 1] and h[x + 1][y - 1]:
            grid[x][y - 1] = 'R' if player == RED_PLAYER else 'B'
            add_score(player)
            box_completed = True
        if y < N - 1 and v[x][y + 1] and h[x][y] and h[x + 1][y]:
            grid[x][y] = 'R' if player == RED_PLAYER else 'B'
            add_score(player)
            box_completed = True
    return box_completed

# Get user input
def get_input():
    global turn
    block_size = BLOCK_SIZE
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Determine if the click is close to a horizontal or vertical line
    if mouse_x % block_size < 10:  # Close to the left edge (vertical line)
        is_horizontal = False
        x = (mouse_y // block_size)
        y = (mouse_x // block_size) - 1
    elif mouse_y % block_size < 10:  # Close to the top edge (horizontal line)
        is_horizontal = True
        x = (mouse_y // block_size) - 1
        y = (mouse_x // block_size)
    else:
        return None, None, None

    return is_horizontal, x, y

# Main function to run the game
def main():
    global turn
    running = True
    
    while running:
        clear_screen()
        draw_grid()
        draw_lines()
        draw_boxes()

        # Display score
        score_text = font.render(f"Player R: {score[RED_PLAYER]} | Player B: {score[BLUE_PLAYER]}", True, BLACK)
        screen.blit(score_text, (10, HEIGHT - 40))

        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_horizontal, x, y = get_input()
                if is_horizontal is None or x is None or y is None:
                    continue
                
                if not is_inside_grid(is_horizontal, x, y):
                    continue

                # Update grid and check if a box is completed
                box_scored = update_grid(is_horizontal, x, y, turn)
                if not box_scored:
                    turn = BLUE_PLAYER if turn == RED_PLAYER else RED_PLAYER

        pygame.display.flip()

        # Check if the game is finished
        if game_finished():
            running = False

    print(f"Final Score: Player R: {score[RED_PLAYER]}, Player B: {score[BLUE_PLAYER]}")
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

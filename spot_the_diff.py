import pygame
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('spot the diff.mp3')
pygame.mixer.music.play(-1)

# Screen dimensions and setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spot the Difference")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Load images
image1 = pygame.image.load("royal fam.webp")  # Left image
image2 = pygame.image.load("royal fam diff.jpg")  # Right image

# Resize images if needed
image1 = pygame.transform.scale(image1, (400, 400))
image2 = pygame.transform.scale(image2, (400, 400))

# Difference locations (coordinates relative to image position)
DIFFERENCES = [(-15, 310, 15),(18, 185, 10), (120, 240, 15), (200, 240, 15)]  # (x, y, radius)
found_differences = []

# Font for text
font = pygame.font.Font('Hello Avocado.ttf', 36)

# Game variables
score = 0
max_score = len(DIFFERENCES)

def draw_text(text, x, y, color=WHITE):
    """Utility function to draw text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def check_click(pos, differences, found):
    """Check if the player clicked on a difference."""
    global score
    for diff in differences:
        x, y, radius = diff
        if ((pos[0] - x)**2 + (pos[1] - y)**2)**0.5 <= radius:
            if diff not in found:
                found.append(diff)
                score += 1
                return True
    return False

game_over = False
current_state_game2 = 'boat'

# Main game loop
running_game = True
while running_game:
    screen.fill(BLACK)

    # Display images
    screen.blit(image1, (0, 100))
    screen.blit(image2, (400, 100))

    # for diff in DIFFERENCES:
    #     pygame.draw.circle(screen, RED, (50 + diff[0], 50 + diff[1]), diff[2])  # Left image
    #     pygame.draw.circle(screen, RED, (450 + diff[0], 50 + diff[1]), diff[2])

    # Draw circles around found differences
    for diff in found_differences:
        pygame.draw.circle(screen, RED, (50 + diff[0], 50 + diff[1]), diff[2], 2)  # Left image
        pygame.draw.circle(screen, RED, (450 + diff[0], 50 + diff[1]), diff[2], 2)  # Right image

    # Draw the score
    draw_text(f"Score: {score}/{max_score}", 10, 10)

    # Check for win
    if score == max_score:
        draw_text("You might have solved this puzzle, but it is not enough!", 5, 510, WHITE)
        draw_text("Press ENTER to continue", 250, 550, WHITE)
        game_over = True

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and game_over:
                
                current_state_game2 = "room3"

            elif event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # Check clicks on both images
            if 0 <= mouse_pos[0] <= 400 and 0 <= mouse_pos[1] <= 550:  # Left image
                adjusted_pos = (mouse_pos[0] - 50, mouse_pos[1] - 50)
                check_click(adjusted_pos, DIFFERENCES, found_differences)
            elif 400 <= mouse_pos[0] <= 750 and 50 <= mouse_pos[1] <= 550:  # Right image
                adjusted_pos = (mouse_pos[0] - 400, mouse_pos[1] - 50)
                check_click(adjusted_pos, DIFFERENCES, found_differences)

    # if current_state_game2 == "room3":
    #     screen.blit(image1, (0,0))

    pygame.display.flip()

pygame.quit()
sys.exit()

import pygame
import sys

# Initialize pygame
pygame.init()

# Load the map image
map_image = pygame.image.load("imagination_map_2.jpg")

# Set screen dimensions based on image size
SCREEN_WIDTH, SCREEN_HEIGHT = map_image.get_size()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fantasy Map Adventure")

# Define locations with clickable areas (x, y, width, height)
locations = {
    "Golden Harbor": (100, 500, 80, 80),
    "Shadowmere Forest": (300, 400, 100, 100),
    "Dragonspire Peak": (600, 100, 90, 90),
    "Eldoria Castle": (500, 300, 100, 100),
    "Whispering Ruins": (700, 600, 90, 90),
    "Frozen Tundra": (900, 50, 110, 110),
    "Mystic Swamp": (400, 700, 100, 100)
}

# Define event messages for locations
events = {
    "Golden Harbor": "You found a hidden treasure chest!",
    "Shadowmere Forest": "A band of goblins ambushed you!",
    "Dragonspire Peak": "A dragon is spotted in the distance!",
    "Eldoria Castle": "The king requests your assistance!",
    "Whispering Ruins": "Ancient runes glow under the moonlight!",
    "Frozen Tundra": "You struggle against the icy winds!",
    "Mystic Swamp": "A mysterious figure offers you a potion!"
}

# Function to check if a point is inside a rectangle
def is_inside(x, y, rect):
    rx, ry, rw, rh = rect
    return rx <= x <= rx + rw and ry <= y <= ry + rh

# Game loop
running = True
while running:
    screen.blit(map_image, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for location, rect in locations.items():
                if is_inside(mx, my, rect):
                    print(events[location])  # Display event message in console

    pygame.display.flip()

pygame.quit()
sys.exit()

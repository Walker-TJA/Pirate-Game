import pygame # Cancer
import random
pygame.init()

#The ultimate resolution
sw = 1920
sh = 1080

screen = pygame.display.set_mode((sw, sh)) # Initialize Screen
clock = pygame.time.Clock() # Initialize time/ticks

# Player stuff
p1_x = 100
p1_y = 100
vel_x = 0
vel_y = 0
friction = 0.95  # closer to 1 = less friction
speed = 0.5       # how fast it accelerates

# Waves are BS
waves = []
WAVE_PATTERN = [
    [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0]
]

class Wave:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        for row_idx, row in enumerate(WAVE_PATTERN):
            for col_idx, pixel in enumerate(row):
                if pixel:
                    surface.set_at((self.x + col_idx, self.y + row_idx), (255, 255, 255))

Menu = True
while Menu == True: # MENU LOOP

    StartMenu = True
    while StartMenu: # MAIN LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        mx, my = pygame.mouse.get_pos() 
        screen.blit(pygame.image.load('Assets/MenuBackground/MenuBackground.png'), (0, 0)) # Load the background image

        if mx > sw/2 - 225/2 and mx < sw/2 + 225/2 and my > sh/2 - 75/2 and my < sh/2 + 75/2:  # Check if mouse is over the button
            if pygame.mouse.get_pressed()[0]: # Check if left mouse button is pressed
                StartMenu = False

        screen.blit(pygame.image.load('Assets/StartButton/StartButton.png'), (sw/2 - 225/2, sh/2 - 75/2))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: 
            pygame.quit()

        pygame.display.flip()

    # Generate wave objects on a grid with randomness
    spacing_x = 40
    spacing_y = 40
    offset_range = 10  # randomness amount      
    # Wave spacing and adding to be drawn
    for x in range(0, sw, spacing_x):
        for y in range(0, sh, spacing_y):
            offset_x = random.randint(-offset_range, offset_range)
            offset_y = random.randint(-offset_range, offset_range)
            waves.append(Wave(x + offset_x, y + offset_y))

    GameMenu = True
    while GameMenu: # GAME LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((0, 150, 255))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: 
            pygame.quit()
        if keys[pygame.K_TAB]: 
            StartMenu = True
            GameMenu = False
        if keys[pygame.K_UP]:
            vel_y -= speed
        if keys[pygame.K_DOWN]:
            vel_y += speed
        if keys[pygame.K_LEFT]:
            vel_x -= speed
        if keys[pygame.K_RIGHT]:
            vel_x += speed
        
        # Apply Velocity
        p1_x += vel_x
        p1_y += vel_y

        # Apply Friction
        vel_x *= friction
        vel_y *= friction

        # Draw all waves
        for wave in waves:
            wave.draw(screen)
        
        pygame.draw.rect(screen, (255, 0, 0), (p1_x, p1_y, 50, 50))
        pygame.display.flip()  
        clock.tick(60)
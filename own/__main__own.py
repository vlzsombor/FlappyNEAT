import pygame, sys
from game.globals import *



pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Segoe", 26)
window = pygame.display.set_mode((win_width, win_height))

# while True:
#     clock.tick(1)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print(clock.tick())
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.KEYDOWN:
#             key=pygame.key.name(event.key)
#             print (key, "Key is pressed")
#         if event.type == pygame.KEYUP:
#             key=pygame.key.name(event.key)
#             print (key, "Key is released")

def quit_game():
    # Exit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset()
            if event.key == pygame.K_q:
                pygame.quit()
                exit()

def menu():
    # Start Screen
    while GAME_STOPPED:
        quit_game()

        # Draw Menu
        window.fill((0, 0, 0))
        window.blit(skyline_image, (0, -400))
        # window.blit(ground_image, Ground(0, 520, ground_image))
        window.blit(bird_images[0], (100, 250))
        # window.blit(
        #     start_image,
        #     (
        #         win_width // 2 - start_image.get_width() // 2,
        #         win_height // 2 - start_image.get_height() // 2,
        #     ),
        # )
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        # create a text surface object,
        # on which text is drawn on it.
        font = pygame.font.Font('freesansbold.ttf', 32)
        
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render('zs o m b o r', True, green, blue)
        
        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        
        # set the center of the rectangular object.
        textRect.center = (win_width // 2, win_height // 8 * 7)
 
        window.blit(text, textRect)
        # User Input
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            # Start Game when space pressed
            main()

        pygame.display.update()


# Run only if this file is executed
if __name__ == "__main__":
    menu()

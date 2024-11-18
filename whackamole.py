import pygame
import random



def main():
    try:

        pygame.init()
        molecoords = (0, 0)
        # You can draw the mole with this snippet:

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    event.pos = pygame.mouse.get_pos()
                    if event.pos[0] in range(molecoords[0]+32) and event.pos[1] in range(molecoords[1]+32):
                        molecoords = (random.randint(0,20)*32, random.randint(0,16)*32)
                        screen.blit(mole_image, mole_image.get_rect(topleft=(molecoords)))

            screen.fill("light green")
            for i in range(20):
                pygame.draw.line(screen, "black", ((32*i), 0), ((32*i), 512))
            for i in range(16):
                pygame.draw.line(screen, "black", (0, (32*i)), (640, (32*i)))

            screen.blit(mole_image, mole_image.get_rect(topleft=(molecoords)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

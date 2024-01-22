import pygame
from pykinect import nui

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Kinect Pygame")

    with nui.Runtime() as kinect:
        kinect.skeleton_engine.enabled = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            # Captura de fotograma de Kinect
            frame = kinect.depth_frame()

            # Dibuja el fotograma en la pantalla
            screen.fill((0, 0, 0))
            screen.blit(pygame.surfarray.make_surface(frame), (0, 0))
            pygame.display.update()

if __name__ == "__main__":
    main()

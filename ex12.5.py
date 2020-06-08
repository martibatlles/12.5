import pygame

class ImprimirEvents:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Imprimir events")

    def _mirar_events(self):
        for event in pygame.event.get():
            print(event)

    def _actualitza_pantalla(self):
        self.screen.fill((255, 255, 255))
        pygame.display.flip()

    def run(self):
        while True:
            self._mirar_events()
            self._actualitza_pantalla()

def main():
    imprimir_events = ImprimirEvents()
    imprimir_events.run()

if __name__ == "__main__":
    main()

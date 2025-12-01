import pygame

class Game:
    def __init__(self, title, fps=60, size=(640, 400)):
        self.title = title
        self.fps = fps
        self.size = size
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.screen = None

    def init_game(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode(self.size)

    def game_loop(self):
        while True:
            self.dt = self.clock.tick(self.fps) / 1000  # Delta-Zeit in Sekunden
            if not self.event_handling():
                break
            if not self.update_game():
                break
            self.draw_game()

    def exit_game(self):
        pygame.quit()

    def event_handling(self):
        for event in pygame.event.get():
            if not self.handle_event(event):
                return False
        return True

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return False
        return True

    def update_game(self):
        return True

    def draw_game(self):
        pygame.display.flip()

    def run(self):
        self.init_game()
        self.game_loop()
        self.exit_game()



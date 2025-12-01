import pygame
from game import *
from compute import *


class CubeGame(Game):
    def __init__(self):
        # Initialisiert Pygame-Fenster mit 700x700
        super().__init__('3D Cube', 60, (700, 700))

        # 8 3D-Eckpunkte des Würfels
        self.cube_positions = [[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
                               [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]]

        # Rotationswinkel
        self.angle_x = 0.0
        self.angle_y = 0.0

        # NEU: Steuerungsvariablen
        self.is_rotating = False  # Status, ob der Würfel gerade rotieren soll
        self.rotation_speed = 0.01  # Winkel, um den sich der Würfel pro Frame dreht

        # Definition der 12 Kanten als Indexpaare
        self.edges = [
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 1), (1, 2), (2, 3), (3, 0),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]

        self.projected_points = []

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return False

        # Wenn Maustaste gedrückt wird: Rotation EIN
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.is_rotating = True

        # Wenn Maustaste losgelassen wird: Rotation AUS
        elif event.type == pygame.MOUSEBUTTONUP:
            self.is_rotating = False

        return True

    def update_game(self):
        # Aktualisiert die Winkel nur, wenn die Maustaste gedrückt gehalten wird
        if self.is_rotating:
            self.angle_x += self.rotation_speed
            self.angle_y += self.rotation_speed

        self.projected_points = []

        # 1. Erstellung der Rotationsmatrizen
        R_x = rot_3D(self.angle_x, 'x')
        R_y = rot_3D(self.angle_y, 'y')

        # 2. Gesamt-Rotationsmatrix mit matmul berechnen
        R_complete = matmul(R_x, R_y)

        # 3. Alle 8 Punkte transformieren und projizieren
        for cube_position in self.cube_positions:
            # Punkt in 3x1 Matrix umwandeln
            point_matrix = [[cube_position[0]], [cube_position[1]], [cube_position[2]]]

            # Matrix-Vektor Multiplikation: R_complete * Punkt
            new_position_matrix = matmul(R_complete, point_matrix)

            # Ergebnis zurück in ein Tupel umwandeln
            new_cube_position = (
                new_position_matrix[0][0],
                new_position_matrix[1][0],
                new_position_matrix[2][0]
            )

            # Projektion und Skalierung (100)
            projected_to_2D = project_ortho(new_cube_position, 100)

            # 4. Verschiebung zur Fenstermitte (700 / 2 = 350)
            center_x = self.size[0] / 2
            center_y = self.size[1] / 2

            final_x = projected_to_2D[0] + center_x
            final_y = projected_to_2D[1] + center_y

            # 5. Finalen, verschobenen Punkt speichern
            self.projected_points.append((final_x, final_y))

        return True

        # Überschreibt draw_game aus der Basisklasse

    def draw_game(self):
        self.screen.fill(pygame.Color('black'))

        if self.projected_points:
            for start_index, end_index in self.edges:
                start_pos = self.projected_points[start_index]
                end_pos = self.projected_points[end_index]

                pygame.draw.line(self.screen, pygame.Color('red'), start_pos, end_pos, 1)

        pygame.display.flip()


if __name__ == '__main__':
    game = CubeGame()
    game.run()
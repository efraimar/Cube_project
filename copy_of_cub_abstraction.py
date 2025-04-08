
from copy import deepcopy
import numpy as np
import copy
import random

# change somthing 2
class Cube:
    def __init__(self):
        self.opposite_faces = {"w": "y", "y": "w", "g": "b", "b": "g", "o": "r", "r": "o"}

        self.front = None
        self.back = None
        self.left = None
        self.right = None
        self.up = None
        self.down = None

        self.cube = {color: np.full((3, 3), color, dtype=object) for color in "wgobry"}

        self.history_move = []

    def Position(self, color_front, color_up, color_right):
        self.front = color_front
        self.up = color_up
        self.right = color_right
        self.down = self.opposite_faces[self.up]
        self.back = self.opposite_faces[self.front]
        self.left = self.opposite_faces[self.right]

        return

    def R_rotation(self, clockwise=True):
        self.cube[self.right] = np.rot90(self.cube[self.right], k=-1 if clockwise else 1)
        temp = copy.deepcopy(self.cube[self.front][:, 2])

        if clockwise:
            self.cube[self.front][:, 2] = self.cube[self.down][:, 2]
            self.cube[self.down][:, 2] = np.flip(self.cube[self.back][:, 0])  # תיקון הפוך
            self.cube[self.back][:, 0] = np.flip(self.cube[self.up][:, 2])    # תיקון הפוך
            self.cube[self.up][:, 2] = temp
            self.history_move.append("R")
        else:
            self.cube[self.front][:, 2] = self.cube[self.up][:, 2]
            self.cube[self.up][:, 2] = np.flip(self.cube[self.back][:, 0])
            self.cube[self.back][:, 0] = np.flip(self.cube[self.down][:, 2])
            self.cube[self.down][:, 2] = temp
            self.history_move.append("R'")


    def L_rotation(self, clockwise=True):
        self.cube[self.left] = np.rot90(self.cube[self.left], k=-1 if clockwise else 1)
        temp = copy.deepcopy(self.cube[self.front][:, 0])

        if clockwise:
            self.cube[self.front][:, 0] = self.cube[self.down][:, 0]
            self.cube[self.down][:, 0] = np.flip(self.cube[self.back][:, 0])
            self.cube[self.back][:, 0] = np.flip(self.cube[self.up][:, 0])
            self.cube[self.up][:, 0] = temp
            self.history_move.append("L")
        else:
            self.cube[self.front][:, 0] = self.cube[self.up][:, 0]
            self.cube[self.up][:, 0] = np.flip(self.cube[self.back][:, 0])
            self.cube[self.back][:, 0] = np.flip(self.cube[self.down][:, 0])
            self.cube[self.down][:, 0] = temp
            self.history_move.append("L'")

    def U_rotation(self, clockwise=True):
        self.Position("o", "w", "g")
        self.cube[self.up] = np.rot90(self.cube[self.up], k=-1 if clockwise else 1)
        temp = copy.deepcopy(self.cube[self.front][0])
        if clockwise:
            self.cube[self.front][0] = self.cube[self.right][0]
            self.cube[self.right][0] = self.cube[self.back][0]
            self.cube[self.back][0] = self.cube[self.left][0]
            self.cube[self.left][0] = temp
            self.history_move.append("U")
        else:
            self.cube[self.front][0] = self.cube[self.left][0]
            self.cube[self.left][0] = self.cube[self.back][0]
            self.cube[self.back][0] = self.cube[self.right][0]
            self.cube[self.right][0] = temp
            self.history_move.append("U'")

    def D_rotation(self, clockwise=True):
        self.cube[self.down] = np.rot90(self.cube[self.down], k=-1 if clockwise else 1)
        temp = copy.deepcopy(self.cube[self.front][2])
        if clockwise:
            self.cube[self.front][2] = self.cube[self.right][2]
            self.cube[self.right][2] = self.cube[self.back][2]
            self.cube[self.back][2] = self.cube[self.left][2]
            self.cube[self.left][2] = temp
            self.history_move.append("D")
        else:
            self.cube[self.front][2] = self.cube[self.left][2]
            self.cube[self.left][2] = self.cube[self.back][2]
            self.cube[self.back][2] = self.cube[self.right][2]
            self.cube[self.right][2] = temp
            self.history_move.append("D'")

    def F_rotation(self, clockwise=True):
        self.cube[self.front] = np.rot90(self.cube[self.front], k=-1 if clockwise else 1)
        temp = copy.deepcopy(self.cube[self.right][:, 0])

        if clockwise:
            self.cube[self.right][:, 0] = np.flip(self.cube[self.up][2])
            self.cube[self.up][2] = self.cube[self.left][:, 2]
            self.cube[self.left][:, 2] = np.flip(self.cube[self.down][0])
            self.cube[self.down][0] = temp
            self.history_move.append("F")
        else:
            self.cube[self.right][:, 0] = self.cube[self.down][0]
            self.cube[self.down][0] = np.flip(self.cube[self.left][:, 2])
            self.cube[self.left][:, 2] = self.cube[self.up][2]
            self.cube[self.up][2] = np.flip(temp)
            self.history_move.append("F'")


    def B_rotation(self, clockwise=True):
        self.cube[self.back] = np.rot90(self.cube[self.back], k=-1 if clockwise else 1)  # סיבוב הפאה האחורית
        temp = copy.deepcopy(self.cube[self.right][:, 2])
        if clockwise:
            self.cube[self.right][:, 2] = self.cube[self.down][2]
            self.cube[self.down][2] = self.cube[self.left][:, 0]
            self.cube[self.left][:, 0] = self.cube[self.up][0]
            self.cube[self.up][0] = temp
            self.history_move.append("B")
        else:
            self.cube[self.right][:, 2] = self.cube[self.up][0]
            self.cube[self.up][0] = self.cube[self.left][:, 0]
            self.cube[self.left][:, 0] = self.cube[self.down][2]
            self.cube[self.down][2] = temp
            self.history_move.append("B'")


    def scramble_cube(self, num_moves):
      moves = ["U", "D", "L", "R", "F", "B"]
      directions = ["", "'"]  # רגיל או נגד כיוון השעון
      scramble_moves = []

      for _ in range(num_moves):
          move = random.choice(moves) + random.choice(directions)
          scramble_moves.append(move)
          self.perform_move(move)

    def perform_move(self, move):

        if move == "U":
            self.U_rotation()
        elif move == "U'":
            self.U_rotation(False)
        elif move == "D":
            self.D_rotation()
        elif move == "D'":
            self.D_rotation(False)
        elif move == "L":
            self.L_rotation()
        elif move == "L'":
            self.L_rotation(False)
        elif move == "R":
            self.R_rotation()
        elif move == "R'":
            self.R_rotation(False)
        elif move == "F":
            self.F_rotation()
        elif move == "F'":
            self.F_rotation(False)
        elif move == "B":
            self.B_rotation()
        elif move == "B'":
            self.B_rotation(False)

# פתרון קוביה

    def solve_scramble(self):
        """ פותר את הקובייה על ידי היפוך המהלכים האחרונים """
        if not self.history_move:
            return

        # הפוך את רשימת המהלכים
        reverse_moves = self.history_move[::-1]

        for move in reverse_moves:
            inverse_move = move[:-1] if "'" in move else move + "'"  # משנה כיוון
            print(f"🔄 Before execution{inverse_move}:\n")
            for s in "wgobry":
                print(f"{s}:\n{x.cube[s]}\n")  # מדפיס מצב קודם
            self.perform_move(inverse_move)
            print(f"✔️ Done :{inverse_move}")

        # ניקוי היסטוריית המהלכים לאחר הפתרון
        self.history_move = []

        print("\n✅ The cube returned to its initial position.!")


    def print_cube(self):
        for face in "wgobry":
            print(f"{face.upper()} face:")
            print(self.cube[face])
            print()

x = Cube()
x.front = "o"
x.back = "r"
x.left = "b"
x.right = "g"
x.up = "w"
x.down = "y"
x.scramble_cube(20)
print(x.history_move)
x.print_cube()
x.solve_scramble()
x.print_cube()


import tkinter as tk
from tkinter import scrolledtext, ttk
from combat_sys import *
from character import Character


class ColorfulMatrixGame:
    def __init__(self, root, matrix, piece_size, obstacle_numbers):
        self.root = root
        self.root.title("Map")
        self.root.configure(bg='black')
        self.root.attributes('-fullscreen', True)

        self.matrix = matrix
        self.matrix_size = len(matrix)
        self.piece_size = piece_size
        self.person_position = (self.matrix_size // 2, self.matrix_size // 2)  # Start in the middle of the matrix

        self.obstacle_numbers = obstacle_numbers
        self.colors = {}  # Dictionary to store the colors of each number
        self.revealed = set()  # Set to keep track of revealed numbers

        # Calculate the dimensions for the canvas and the position for the matrix
        canvas_width = self.piece_size * (self.matrix_size)
        canvas_height = self.piece_size * (self.matrix_size)




        self.canvas = tk.Canvas(root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.border_x1 = 0
        self.border_y1 = 0
        self.border_x2 = canvas_width + 1
        self.border_y2 = canvas_height + 1



        self.init_color_map()
        self.draw_matrix()

        # Arrow key bindings
        root.bind("<Left>", lambda event: self.move_player("left"))
        root.bind("<Right>", lambda event: self.move_player("right"))
        root.bind("<Up>", lambda event: self.move_player("up"))
        root.bind("<Down>", lambda event: self.move_player("down"))


    def colors_mapping(self):
        return {
            0: "lawngreen",
            1: "coral",
            2: "olive",
            3: "royalblue",
            4: "grey",
            5: "lime",
            6: "teal",
            7: "aqua",
            8: "sienna",
            9: "firebrick",
            10: "blue",
            11: "forestgreen",
            12: "darkgrey",
            13: "bisque",
            14: "chocolate",
        }




    def init_color_map(self):
        color_mapping = self.colors_mapping()
        for number, color in color_mapping.items():
            self.colors[number] = color


    def draw_matrix(self):
        self.canvas.delete("all")
        temp = 150
        current_piece_x, current_piece_y = self.person_position[0] // temp, self.person_position[1] // temp

        for i in range(current_piece_x * temp, min((current_piece_x + 1) * temp, self.matrix_size)):
            for j in range(current_piece_y * temp, min((current_piece_y + 1) * temp, self.matrix_size)):
                x1 = (i - current_piece_x * temp) * self.piece_size
                y1 = (j - current_piece_y * temp) * self.piece_size
                x2 = x1 + self.piece_size
                y2 = y1 + self.piece_size

                number = self.matrix[i][j]

                if (i, j) == self.person_position:
                    color = "white"
                elif (i, j) in self.revealed:
                    color = self.colors.get(number, "")
                else:
                    color = ""

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")




    def move_player(self, direction, steps=1):
        dx, dy = 0, 0
        if direction == "up":
            dy = -5
        elif direction == "down":
            dy = 5
        elif direction == "left":
            dx = -5
        elif direction == "right":
            dx = 5

        for _ in range(steps):
            new_x, new_y = self.person_position[0] + dx, self.person_position[1] + dy
            if (
                    0 <= new_x < self.matrix_size
                    and 0 <= new_y < self.matrix_size
                    and self.matrix[new_x][new_y] not in self.obstacle_numbers
            ):
                # Check if the next cell has a different color
                if (
                        self.matrix[new_x][new_y]
                        != self.matrix[self.person_position[0]][self.person_position[1]]
                ):
                    self.person_position = (new_x, new_y)
                    self.reveal_nearby_numbers()
                    break  # Stop moving if encountering a new color
                self.person_position = (new_x, new_y)
                self.reveal_nearby_numbers()
            else:
                break  # Stop moving if an obstacle is encountered
        self.draw_matrix()



    def reveal_nearby_numbers(self):
        x, y = self.person_position

        for i in range(x - 100, x + 101):
            for j in range(y - 100, y + 101):
                if 0 <= i < self.matrix_size and 0 <= j < self.matrix_size:
                    self.revealed.add((i, j))




from map_creator import map1

def main():
    my_map = map1(150)
    ####
    root = tk.Tk()

    # Example: Create a 5x5 matrix filled with random numbers from 0 to 10
    #matrix = [[random.randint(0, 10) for _ in range(10)] for _ in range(10)]
    matrix = my_map.map
    # Example: Specify obstacle numbers
    obstacle_numbers = list(my_map.unmov)

    game = ColorfulMatrixGame(root, matrix, 5, obstacle_numbers)



    root.mainloop()



if __name__ == "__main__":
    main()
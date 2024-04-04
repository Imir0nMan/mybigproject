import tkinter as tk

class GameFeatures:
    def __init__(self, canvas, player, map_objects):
        self.canvas = canvas
        self.player = player
        self.map_objects = map_objects

    def draw_player_position(self):
        self.canvas.delete("player")
        cell_size = 20
        x, y = self.player["x"], self.player["y"]
        x0, y0 = x * cell_size, y * cell_size
        x1, y1 = x0 + cell_size, y0 + cell_size
        self.canvas.create_rectangle(x0, y0, x1, y1, fill='white', outline='black', tags="player")

    def get_current_cell_color(self):
        x, y = self.player["x"], self.player["y"]
        if [x, y] in self.map_objects.values():
            for key, value in self.map_objects.items():
                if value == [x, y]:
                    return 'red' if key == 'K' else 'yellow'
        else:
            return '#808080'  # Default color for ground

    def display_current_cell_color(self):
        self.canvas.delete("color_indicator")
        cell_size = 20
        x, y = self.player["x"], self.player["y"]
        color = self.get_current_cell_color()
        x0, y0 = x * cell_size, y * cell_size
        x1, y1 = x0 + cell_size, y0 + cell_size
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='', tags="color_indicator")

    def move_player(self, direction):
        if direction == "up":
            if self.player["y"] > 0:
                self.player["y"] -= 1
        elif direction == "down":
            if self.player["y"] < len(self.map_objects) - 1:
                self.player["y"] += 1
        elif direction == "left":
            if self.player["x"] > 0:
                self.player["x"] -= 1
        elif direction == "right":
            if self.player["x"] < len(self.map_objects[0]) - 1:
                self.player["x"] += 1

        self.draw_player_position()
        self.display_current_cell_color()

    def process_command(self, event):
        command = self.input.get().lower()
        self.input.delete(0, tk.END)

        if command == "quit":
            self.print_message("Game over. Thanks for playing!")
            self.after(2000, self.destroy)
        elif command in ["up", "down", "left", "right"]:
            self.move_player(command)
        else:
            self.print_message("Unknown command: {}".format(command))

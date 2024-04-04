import tkinter as tk
from tkinter import messagebox
import random

def format_color(color_code):
    return "#{:06x}".format(color_code)

class Map(tk.Canvas):
    def __init__(self, master, width, height, cell_size, unmovable_colors, *args, **kwargs):
        super().__init__(master, width=width*cell_size, height=height*cell_size, *args, **kwargs)
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.unmovable_colors = unmovable_colors
        self.map_data = self.generate_map_data()
        self.player_position = (self.width // 2, self.height // 2)  # Starting position for the player
        self.configure(bg='black')
        self.history = []
        self.comment_text = tk.StringVar()
        self.command_text = tk.StringVar()
        self.map_enabled = True
        self.game_over = False
        self.command_bar = tk.Entry(master, textvariable=self.command_text, bg='black', fg='green', insertbackground='green', font=('Courier', 12))
        self.command_bar.pack(side="bottom", fill="x", padx=10, pady=10)
        self.comment_bar = tk.Label(master, textvariable=self.comment_text, bg="black", fg="green", font=("Arial", 14), height=2)
        self.comment_bar.pack(side="bottom", fill="x", padx=10, pady=(10, 0))
        self.draw_map()
        self.bind_controls()

    def generate_map_data(self):
        map_data = [[random.choice(range(256)) for _ in range(self.width)] for _ in range(self.height)]
        for color in self.unmovable_colors:
            for _ in range(10):  # Choose ten positions for each unmovable color
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                map_data[y][x] = color
        return map_data

    def draw_map(self):
        self.delete("all")
        if self.map_enabled:
            start_x = (self.master.winfo_width() - self.width * self.cell_size) // 2
            start_y = (self.master.winfo_height() - self.height * self.cell_size) // 2
            for y in range(self.height):
                for x in range(self.width):
                    color = format_color(self.map_data[y][x])
                    self.create_rectangle(start_x + x*self.cell_size, start_y + y*self.cell_size,
                                           start_x + (x+1)*self.cell_size, start_y + (y+1)*self.cell_size, fill=color, outline="")

            # Draw player
            px, py = self.player_position
            self.create_oval(start_x + px * self.cell_size, start_y + py * self.cell_size,
                              start_x + (px + 1) * self.cell_size, start_y + (py + 1) * self.cell_size, fill="gray")

    def move_player(self, dx, dy):
        if self.game_over:
            return

        new_x = self.player_position[0] + dx
        new_y = self.player_position[1] + dy
        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            if self.map_data[new_y][new_x] in self.unmovable_colors:
                if self.map_data[new_y][new_x] == self.unmovable_colors[0]:  # Red
                    messagebox.showinfo("Game Over", "You touched a red object! Game Over!")
                    self.game_over = True
                else:
                    self.comment_text.set("You touched an unmovable object!")
            else:
                self.player_position = (new_x, new_y)
                self.history.append(f"Moved {'Up' if dy == -1 else 'Down' if dy == 1 else 'Left' if dx == -1 else 'Right'} 1 step")
                self.comment_text.set(self.history[-1])
        self.draw_map()

    def execute_command(self, command):
        if command == "up":
            self.move_player(0, -1)
        elif command == "down":
            self.move_player(0, 1)
        elif command == "left":
            self.move_player(-1, 0)
        elif command == "right":
            self.move_player(1, 0)
        elif command == "enable":
            self.map_enabled = True
            self.draw_map()
        elif command == "disable":
            self.map_enabled = False
            self.delete("all")  # Clear canvas
        elif command == "exit":
            self.master.destroy()
        else:
            self.comment_text.set("Invalid command!")
            return
        self.command_text.set("")
        if len(self.history) > 5:
            self.history = self.history[-5:]
        self.comment_text.set("\n".join(self.history))

    def bind_controls(self):
        self.master.bind("<Return>", lambda event: self.execute_command(self.command_text.get()))
        self.master.bind("<Up>", lambda event: self.move_player(0, -1))
        self.master.bind("<Down>", lambda event: self.move_player(0, 1))
        self.master.bind("<Left>", lambda event: self.move_player(-1, 0))
        self.master.bind("<Right>", lambda event: self.move_player(1, 0))

def main():
    root = tk.Tk()
    root.title("Map with Unmovable Colors and Player")
    root.configure(bg="black")
    root.attributes('-fullscreen', True)

    width = 50
    height = 50
    cell_size = 10
    unmovable_colors = [0xFF0000, 0x00FF00, 0x0000FF]  # Red, Green, Blue as unmovable colors

    map_canvas = Map(root, width, height, cell_size, unmovable_colors)
    map_canvas.pack(expand=True, fill=tk.BOTH)

    root.mainloop()

if __name__ == "__main__":
    main()


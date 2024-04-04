class InteractionHandler:
    def __init__(self, game):
        self.game = game

    def check_interaction(self):
        current_color = self.get_current_color()
        next_color = self.get_next_color()

        if current_color != next_color:
            interaction_message = f"You stepped from {current_color} to {next_color}."
            self.game.print_message(interaction_message)

    def get_current_color(self):
        current_x, current_y = self.game.person_position
        return self.game.colors.get(self.game.matrix[current_x][current_y], "Unknown")

    def get_next_color(self):
        next_x, next_y = self.calculate_next_position()
        return self.game.colors.get(self.game.matrix[next_x][next_y], "Unknown")

    def calculate_next_position(self):
        dx, dy = self.get_movement_vector()
        next_x, next_y = self.game.person_position[0] + dx, self.game.person_position[1] + dy
        return next_x, next_y

    def get_movement_vector(self):
        # You can modify this method based on how the player's movement is handled in your game
        # For example, if the player moves left, dx = -1 and dy = 0
        # Implement logic to calculate the movement vector based on the current direction of the player
        return 0, 0  # Placeholder values


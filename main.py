from visual_map import *
from map_creator import map1
from cutscenes import *

def main():
    my_map = map1(150)
    ####
    root = tk.Tk()

    # Example: Create a 5x5 matrix filled with random numbers from 0 to 10
    #matrix = [[random.randint(0, 10) for _ in range(10)] for _ in range(10)]
    matrix = my_map.map
    # Example: Specify obstacle numbers
    obstacle_numbers = list(my_map.unmov)

    game = ColorfulMatrixGame(root, matrix, 10, obstacle_numbers)
    interaction_handler = InteractionHandler(game)

    interaction_handler.check_interaction()


    root.mainloop()

main()
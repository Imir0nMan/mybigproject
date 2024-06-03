import numpy as np
import random
def filler(arr, param, *argv):
    if len(argv) == 4:
        row_a, row_z, col_a, col_z = argv
        arr[row_a:row_z, col_a:col_z] = param
    else:
        raise Exception("Too much or less arguments")

class Map:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = np.zeros((self.row, self.col))
        self.w_len = len(self.map)
        self.movable = {0,}
        self.unmov = set(())


    def canyon(self, param, *argv):
        self.unmov.add(param)
        filler(self.map, param, *argv)

    def river(self, param, drct, *argv):
        self.unmov.add(param)
        if len(argv) != 4:
            raise Exception("Too much or less arguments")

        if drct == 0:
            row, row_e, col, col_e = argv
            if 0 <= row < self.w_len and 0 <= col < self.w_len:
                filler(self.map, param, row, row_e, col, col_e)
            else:
                raise Exception("Range error in map")
        elif drct == 1:
                row_a, row_z, col_a, col_z = argv
                np.fill_diagonal(self.map[row_a:row_z, col_a:col_z], param)
                np.fill_diagonal(self.map[row_a:row_z, col_a+1:col_z+1], param)
        elif drct == 2:
                row_a, row_z, col_a, col_z = argv
                np.fill_diagonal(np.fliplr(self.map[row_a:row_z, col_a:col_z]), param)
                np.fill_diagonal(np.fliplr(self.map[row_a:row_z, col_a+1:col_z+1]), param)
        else:
            raise Exception("Wrong argument for direction")

    def quicksand(self, param, *argv):
        self.movable.add(param)
        filler(self.map, param, *argv)

    def secta(self, param, *argv):
        self.movable.add(param)
        filler(self.map, param, *argv)

    def ocean(self, param, *argv):
        self.unmov.add(param)
        filler(self.map, param, *argv)

    def trees(self, param):
        self.unmov.add(param)
        rows = self.row
        cols = self.col
        min_distance = 1

        def distance_to_nearest_tree(row, col):
            tree_positions = np.argwhere(self.map == param)
            if not tree_positions.any():
                return float('inf')  # No trees placed yet
            distances = np.abs(tree_positions - np.array([row, col]))
            min_distances = np.min(distances, axis=1)
            return np.min(min_distances)

        for _ in range(rows * cols // 2):
            while True:
                row, col = np.random.randint(0, rows), np.random.randint(0, cols)
                if self.map[row, col] == 0 and distance_to_nearest_tree(row, col) >= min_distance:
                    self.map[row, col] = param
                break

    def highway(self, param, *argv):
        self.movable.add(param)
        filler(self.map, param, *argv)

    def village(self, param, *argv):
        self.movable.add(param)
        filler(self.map, param, *argv)

    def passport(self, param, *argv):
        self.movable.add(param)
        filler(self.map, param, *argv)

    def aliens_invasion(self, param, *argv):
        self.movable.add(param)
        filler(self.map, param, *argv)


    def sword(self, param, *argv):
        self.movable.add(param)
        filler(self.map, param, *argv)


    def hunters_house(self, param, *argv):
        self.movable.add(param)
        filler(self.map, param, *argv)


    def mountains(self, param, *argv):
        self.unmov.add(param)
        filler(self.map, param, *argv)


    def simulation(self, param, *argv):
        self.movable.add(param)
        filler(self.map, param, *argv)


    def checker(self, *argv):
        tempx = 0
        tempy = 0
        x1, y1, x2, y2 = argv
        if x2 - x1:
            tempx = x2 - x1
            if self.map(x1 + tempx, y1) in self.movable:
                return True
        elif y2 - y1:
            tempy = y2 - y1
            if self.map(x1, y1 + tempy) in self.movable:
                return True
        else:
            return False


    def enemy(self, param):
        self.unmov.add(param)
        for _ in range(5):
            x = random.randint(0, self.row - 1)
            y = random.randint(0, self.col - 1)
            filler(self.map, param, x - 1, x + 1, y - 1, y + 1)
            print(x - 1, x + 1, y - 1, y + 1)
        x = 55
        y = 55
        filler(self.map, param, x - 1, x + 1, y - 1, y + 1)

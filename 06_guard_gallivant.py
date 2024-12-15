import numpy as np

from utils.input_data import InputData

TEST_INPUT = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


class GuardGallivant:
    def __init__(self, testing):
        self.guard_icon_list = ["^", ">", "v", "<"]
        self.guard_icon = self.guard_icon_list[0]
        self.testing = testing
        self.load_input()
        self.get_guard_path()

    def load_input(self):
        if self.testing:
            self.input = TEST_INPUT.split("\n")
        else:
            self.input = InputData(6).input_data
        self.map = np.matrix([[j for j in i] for i in self.input])

    def _get_guard_location(self):
        if sum(np.isin(self.guard_icon_list, self.map)) == 1:
            self.guard_loc = np.where(self.map == self.guard_icon)
            # print(f"The guard is still here, at pos: {self.guard_loc}")
            return True
        else:
            self.guard_in_map = False
            return False

    def _get_guard_adjustment(self):
        match self.guard_icon:
            case "^":
                self.adjustment = (-1, 0)
            case ">":
                self.adjustment = (0, 1)
            case "v":
                self.adjustment = (1, 0)
            case "<":
                self.adjustment = (0, -1)
        # print(f"New guard adjustment: {self.adjustment}")

    def _update_map(self):
        self.map[self.guard_loc] = "X"
        if self.new_pos:
            self.map[self.new_pos] = self.guard_icon

    def _get_new_position(self):
        new_x, new_y = [
            int(p[0] + adj) for p, adj in zip(self.guard_loc, self.adjustment)
        ]
        if (
            (new_x < 0)
            | (new_y < 0)
            | (new_x > (self.map.shape[1] - 1))
            | (new_y > (self.map.shape[0] - 1))
        ):
            self.new_pos = None

        else:
            new_pos = self.map[new_x, new_y]
            if new_pos == "#":
                return self._turn_guard()
            else:
                self.new_pos = [new_x], [new_y]

    def _move_guard_forward(self):
        self._get_guard_adjustment()
        self._get_new_position()
        self._update_map()

    def _turn_guard(self):
        curr_idx = self.guard_icon_list.index(self.guard_icon)
        self.guard_icon = self.guard_icon_list[curr_idx - 3]
        # print(f"Guard turned, now heading: {self.guard_icon}")
        self._get_guard_adjustment()
        self._get_new_position()

    def get_guard_path(self):
        self.new_pos = None
        self.guard_in_map = True
        print(self.map)

        while self.guard_in_map:
            self._get_guard_location()
            self._move_guard_forward()
            print(self.map)

        num_locs = len(np.where(self.map == "X")[0])
        print(f"Part 1: Total number of locations guard visits: {num_locs}")

    def place_obstruction(self):
        self.map_copy = self.map.copy()
        self.map_copy[self.obs_loc] = "#"

    def test_obstructions(self):
        self.place_obstruction()

        pass

    def look_for_cyclical_obstructions(self):
        for idx, val in np.ndenumerate(self.map):
            if val not in ["#", "^"]:
                self.obs_loc = idx
                self.test_obstructions()


if __name__ == "__main__":
    guard = GuardGallivant(testing=True)

import math
from simpleai.search import SearchProblem, astar


class MazeSolver(SearchProblem):
    def __init__(self, board):
        self.board = board
        self.goal = (0, 0)

        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x].lower() == "o":
                    self.initial = (x, y)
                elif self.board[y][x].lower() == "x":
                    self.goal = (x, y)

        super(MazeSolver, self).__init__(initial_state=self.initial)

    # Define the method that takes actions to arrive at the solution
    def actions(self, state):
        actions = []
        for action in COSTS.keys():
            newx, newy = self.result(state, action)
            if self.board[newy][newx] != "#":
                actions.append(action)

        return actions

    # Based on the action, updating state
    def result(self, state, action):
        x, y = state

        if action.count("up"):
            y -= 1
        if action.count("down"):
            y += 1
        if action.count("left"):
            x -= 1
        if action.count("right"):
            x += 1

        new_state = (x, y)

        return new_state

    # Check if goal is reached
    def is_goal(self, state):
        return state == self.goal

    # Cost Calculation
    def cost(self, state, action, state2):
        return COSTS[action]

    # Heuristic to arrive at the solution
    def heuristic(self, state):
        x, y = state
        gx, gy = self.goal

        return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)


def mazeprint(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if (x, y) == problem.initial:
                print('o', end='')
            elif (x, y) == problem.goal:
                print('x', end='')
            elif (x, y) in path:
                print('-', end='')
            else:
                print(maze[y][x], end='')
        print()


if __name__ == "__main__":
    # maze input
    MAP = """
    ##############################
    #         #              #   #
    # ####    ########       #   #
    #  o #    #              #   #
    #    ###     #####  ######   #
    #      #   ###   #           #
    #      #     #   #  #  #   ###
    #     #####    #    #  # x   #
    #              #       #     #
    ##############################
    """

    # Convert map to a list
    print(MAP)
    maze_conversion = []
    lines = MAP.splitlines()
    for line in lines:
        maze_conversion.append(list(line))
    maze = maze_conversion
    # Define initial cost
    cost_regular = 1.0
    cost_diagonal = 1.7

    # Cost dictionary
    COSTS = {
        "up": cost_regular,
        "down": cost_regular,
        "left": cost_regular,
        "right": cost_regular,
        "up left": cost_diagonal,
        "up right": cost_diagonal,
        "down left": cost_diagonal,
        "down right": cost_diagonal,
    }

    # Create maze solver object and getting problem
    problem = MazeSolver(maze)

    # For solving problem, running astar to get optimal path
    result = astar(problem, graph_search=True)

    # Getting path
    path = []
    y = []
    for x in result.path():
        y.append(x[1])
    path = y
    # Printing maze
    mazeprint(maze)


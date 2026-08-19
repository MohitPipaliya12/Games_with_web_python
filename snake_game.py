import random


class SnakeGame:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        center_x = self.width // 2
        center_y = self.height // 2

        self.snake = [
            [center_x, center_y],
            [center_x - 1, center_y],
            [center_x - 2, center_y]
        ]

        self.direction = "RIGHT"
        self.score = 0
        self.game_over = False

        self.food = self.create_food()

    def create_food(self):
        while True:
            food = [
                random.randint(0, self.width - 1),
                random.randint(0, self.height - 1)
            ]

            if food not in self.snake:
                return food

    def change_direction(self, new_direction):
        opposite = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }

        if new_direction in opposite:
            if new_direction != opposite[self.direction]:
                self.direction = new_direction

    def move(self):
        if self.game_over:
            return

        head_x, head_y = self.snake[0]

        if self.direction == "UP":
            head_y -= 1
        elif self.direction == "DOWN":
            head_y += 1
        elif self.direction == "LEFT":
            head_x -= 1
        elif self.direction == "RIGHT":
            head_x += 1

        new_head = [head_x, head_y]

        # Wall collision
        if (
            head_x < 0
            or head_x >= self.width
            or head_y < 0
            or head_y >= self.height
        ):
            self.game_over = True
            return

        # Snake collision
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # Food
        if new_head == self.food:
            self.score += 10
            self.food = self.create_food()
        else:
            self.snake.pop()

    def get_state(self):
        return {
            "snake": self.snake,
            "food": self.food,
            "score": self.score,
            "game_over": self.game_over,
            "width": self.width,
            "height": self.height
        }
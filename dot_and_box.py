class DotAndBoxesGame:

    def __init__(self, size=4, players=2):
        self.size = size
        self.players = players

        self.current_player = 0

        self.horizontal_lines = set()
        self.vertical_lines = set()

        self.scores = [0] * players

        self.boxes = {}

        self.game_over = False

        self.total_lines = (
            size * (size + 1) +
            size * (size + 1)
        )

    # -------------------------
    # Make a move
    # -------------------------

    def make_move(self, line_type, row, col):

        if self.game_over:
            return {
                "success": False,
                "message": "Game is over"
            }

        if line_type == "h":

            line = (row, col)

            if line in self.horizontal_lines:
                return {
                    "success": False,
                    "message": "Line already selected"
                }

            self.horizontal_lines.add(line)

        elif line_type == "v":

            line = (row, col)

            if line in self.vertical_lines:
                return {
                    "success": False,
                    "message": "Line already selected"
                }

            self.vertical_lines.add(line)

        else:

            return {
                "success": False,
                "message": "Invalid line"
            }

        completed = self.check_boxes()

        if completed > 0:

            self.scores[
                self.current_player
            ] += completed

            # Player gets another turn

        else:

            self.next_player()

        if self.is_finished():
            self.game_over = True

        return {
            "success": True,
            "completed": completed,
            "current_player": self.current_player,
            "scores": self.scores,
            "game_over": self.game_over
        }

    # -------------------------
    # Change player
    # -------------------------

    def next_player(self):

        self.current_player = (
            self.current_player + 1
        ) % self.players

    # -------------------------
    # Check completed boxes
    # -------------------------

    def check_boxes(self):

        completed = 0

        for row in range(self.size):

            for col in range(self.size):

                key = (row, col)

                if key in self.boxes:
                    continue

                top = (row, col)

                bottom = (
                    row + 1,
                    col
                )

                left = (row, col)

                right = (
                    row,
                    col + 1
                )

                if (
                    top in self.horizontal_lines
                    and bottom in self.horizontal_lines
                    and left in self.vertical_lines
                    and right in self.vertical_lines
                ):

                    self.boxes[key] = (
                        self.current_player
                    )

                    completed += 1

        return completed

    # -------------------------
    # Check game finished
    # -------------------------

    def is_finished(self):

        used_lines = (
            len(self.horizontal_lines) +
            len(self.vertical_lines)
        )

        return used_lines >= self.total_lines

    # -------------------------
    # Get winner
    # -------------------------

    def get_winner(self):

        highest = max(self.scores)

        winners = [
            i
            for i, score in enumerate(self.scores)
            if score == highest
        ]

        if len(winners) > 1:
            return {
                "tie": True,
                "players": winners
            }

        return {
            "tie": False,
            "player": winners[0]
        }

    # -------------------------
    # Game state
    # -------------------------

    def get_state(self):

        return {
            "size": self.size,
            "players": self.players,
            "current_player": self.current_player,
            "scores": self.scores,
            "horizontal_lines": [
                list(x)
                for x in self.horizontal_lines
            ],
            "vertical_lines": [
                list(x)
                for x in self.vertical_lines
            ],
            "boxes": {
                f"{r},{c}": player
                for (r, c), player
                in self.boxes.items()
            },
            "game_over": self.game_over,
            "winner": (
                self.get_winner()
                if self.game_over
                else None
            )
        }
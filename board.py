class Board(object):

    def __init__(self, m, n, k):
        self.m = m
        self.n = n
        self.k = k
        self.board = [
            [
                None
                for x in range(self.n)
            ]
            for y in range(self.m)
        ]

    def __getitem__(self, position):
        return self.board[position.x][position.y]

    def __setitem__(self, position, player):
        self.board[position.x][position.y] = player.marker

    def get_empty_positions(self):
        return [
            Position(x, y)
            for (x, column) in enumerate(self.board)
            for (y, marker) in enumerate(column)
            if marker is None
        ]

    def is_empty_position(self, position):
        if self[position] is None:
            return True
        return False

    def is_k_in_row(self, position, player):
        if self._k_in_row(position, (0, 1), player):
            return True
        elif self._k_in_row(position, (1, 0), player):
            return True
        elif self._k_in_row(position, (1, 1), player):
            return True
        elif self._k_in_row(position, (1, -1), player):
            return True
        return False

    def _k_in_row(self, position, vector, player):
        n = 1
        x_delta, y_delta = vector
        offset = Position(position.x + x_delta, position.y + y_delta)
        if self[position] == player.mark:
            while n < self.k:
                try:
                    if self[offset] == player.mark:
                        n += 1
                        offset.x += x_delta
                        offset.y += y_delta
                    else:
                        break
                except IndexError:
                    break
            offset = Position(position.x - x_delta, position.y - y_delta)
            while n < self.k:
                try:
                    if self[offset] == player.mark:
                        n += 1
                        offset.x -= x_delta
                        offset.y -= y_delta
                    else:
                        break
                except IndexError:
                    break
        return n == self.k

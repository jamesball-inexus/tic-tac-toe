m = 3
n = 3
k = 3

messages = {
    "select_player": "SELECT PLAYER ({}): ",
    "enter_position": "{} TURN: ",
    "not_empty_position": "POSITION NOT AVAILABLE!",
    "invalid_selection": "INVALID SELECTION!",
    "win": "{} WINNER!",
    "draw": "DRAW!",
    "restart": "PLAY AGAIN (Y/N)? "
}

players = [
    'X',
    'O'
]

vectors = [
    (0, 1),
    (1, 0),
    (1, 1),
    (1, -1)
]

def draw_board(board):
    for (x, row) in enumerate(board):
        squares = [" " if square is None else square for square in row]
        if x == 0:
            print("   ", "   ".join(str(i) for i in range(len(row))))
            print("  +", len(row) * "---+", sep="", end="\n")
            print(
                "{} |".format(str(x)),
                " | ".join(squares), sep=" ", end=" |\n"
            )
            print("  +", len(row) * "---+", sep="", end="\n")
        else:
            print(
                "{} |".format(str(x)),
                " | ".join(squares), sep=" ", end=" |\n"
            )
            print("  +", len(row) * "---+", sep="", end="\n")

def set_board(m, n):
    return [
        [None for i in range(n)]
        for i in range(m)
    ]

def get_positions(board):
    return [
        (x, y)
        for (x, row) in enumerate(board)
        for (y, square) in enumerate(row)
    ]

def get_empty_positions(board):
    return [
        position
        for position in get_positions(board)
        if is_empty_postion(board, position) is True
    ]

def is_empty_postion(board, position):
    if get_position(board, position) is None:
        return True
    return False

def get_position(board, position):
    x, y = position
    return board[x][y]

def set_position(board, position, player):
    x, y = position
    board[x][y] = player

def input_position(board, player, messages):
    while True:
        try:
            x, y = [
                int(i)
                for i in input(
                    messages["enter_position"].format(player)
                ).split(",")
            ]
            if (x, y) in get_empty_positions(board):
                return (x, y)
            else:
                print(messages["not_empty_position"])
        except Exception:
            print(messages["invalid_selection"])

def is_winner(board, k, position, vectors, player):
    return any(
        is_k_in_row(board, k, position, vector, player)
        for vector in vectors
    )

def is_k_in_row(board, k, position, vector, player):
    x, y = position
    x_delta, y_delta = vector
    n = 1
    x_offset = x + x_delta
    y_offset = y + y_delta
    offset = (x_offset, y_offset)
    while n < k:
        if offset in get_positions(board):
            if get_position(board, offset) == player:
                n += 1
                x_offset += x_delta
                y_offset += y_delta
                offset = (x_offset, y_offset)
            else:
                break
        else:
            break
    x_offset = x - x_delta
    y_offset = y - y_delta
    offset = (x_offset, y_offset)
    while n < k:
        if offset in get_positions(board):
            if get_position(board, offset) == player:
                n += 1
                x_offset -= x_delta
                y_offset -= y_delta
                offset = (x_offset, y_offset)
            else:
                break
        else:
            break
    return n == k

def input_player(players, messages):
    while True:
        player = input(
            messages["select_player"].format(', '.join(players))
        ).upper()
        if player in players:
            return player
        else:
            print(messages["invalid_selection"])

def set_player_cycle(players):
    while players:
        for player in players:
            yield player

def restart():
    while True:
        result = input(messages["restart"]).upper()
        if result in ['Y', 'N']:
            if result == 'Y':
                return True
            return False
        else:
            print(messages["invalid_selection"])

while True:
    player = input_player(players, messages)
    player_cycle = set_player_cycle(players)
    board = set_board(m, n)
    draw_board(board)
    while True:
        player = next(player_cycle)
        position = input_position(board, player, messages)
        set_position(board, position, player)
        draw_board(board)
        if is_winner(board, k, position, vectors, player):
            print(messages["win"].format(player))
            break
        else:
            if len(get_empty_positions(board)) == 0:
                print(messages["draw"])
                break
    if restart() is True:
        pass
    else:
        break

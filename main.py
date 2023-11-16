import turtle as t
import math as m

SQUARE_LEN = 150
START_X = -250
START_Y = -250

X_OFFSET = 10


# =================================================
# Draw functions

def draw_board():
    t.penup()

    t.goto(START_X, START_Y + SQUARE_LEN)
    t.pendown()
    t.forward(3 * SQUARE_LEN)
    t.penup()

    t.goto(START_X, START_Y + 2*SQUARE_LEN)
    t.pendown()
    t.forward(3 * SQUARE_LEN)
    t.penup()

    t.left(90)

    t.goto(START_X + SQUARE_LEN, START_Y)
    t.pendown()
    t.forward(3 * SQUARE_LEN)
    t.penup()

    t.goto(START_X + 2*SQUARE_LEN, START_Y)
    t.pendown()
    t.forward(3 * SQUARE_LEN)
    t.penup()


def draw_x():
    t.color("red")
    t.forward(X_OFFSET)
    t.right(90)
    t.forward(X_OFFSET)
    t.left(45)
    t.pendown()
    inner_len = SQUARE_LEN - 2*X_OFFSET
    line_len = m.sqrt(2 * inner_len**2)
    t.forward(line_len)
    t.right(45)
    t.penup()
    t.back(inner_len)
    t.right(45)
    t.pendown()
    t.forward(line_len)
    t.penup()
    t.left(135)


def draw_circle():
    t.color("blue")
    t.forward(X_OFFSET + 5)
    t.right(90)
    t.forward(X_OFFSET + 60)
    t.pendown()
    t.circle(60)
    t.penup()
    t.left(90)


def draw_square(x, y, shape):
    t.goto(START_X + x * SQUARE_LEN, START_Y + y * SQUARE_LEN)
    if shape == "X":
        draw_x()
    else:
        draw_circle()


def draw_line(x1, y1, x2, y2):
    t.width(t.width() * 5)
    t.color("light green")
    t.goto(START_X + (x1 + 0.5) * SQUARE_LEN, START_Y + (y1 + 0.5) * SQUARE_LEN)
    t.pendown()
    t.goto(START_X + (x2 + 0.5) * SQUARE_LEN, START_Y + (y2 + 0.5) * SQUARE_LEN)
    t.penup()
    t.width(int(t.width() / 5))


def draw_all_squares(board):
    for x in range(3):
        for y in range(3):
            shape = board[x][y]
            if shape is not None:
                draw_square(x, y, shape)


# =================================================
# Board functions

def make_board(x, y):
    board = []
    for i in range(x):
        board += [[None] * y]
    return board


def make_board_from_strings(strs):
    board = make_board(3, 3)
    for y in range(3):
        for x in range(3):
            shape = strs[2-y][x]
            if shape != " ":
                update_board(board, x, y, shape)
            # print("x={} y={} shape={} board={}".format(x, y, shape, board))
    return board


def update_board(board, x, y, shape):
    if board[x][y]:
        return False
    board[x][y] = shape
    return True


def check_win_line(board, x1, y1, x2, y2):
    if (board[x1][y1] == board[x2][y2]) and (board[x1][y1] == board[int((x1 + x2) / 2)][int((y1 + y2) / 2)]):
        return board[x1][y1]
    return None


def check_win_board(board):
    for line in [(0, 0, 2, 0), (0, 1, 2, 1), (0, 2, 2, 2), (0, 2, 0, 0), (1, 2, 1, 0), (2, 2, 2, 0), (0, 0, 2, 2), (0, 2, 2, 0)]:
        if check_win_line(board, line[0], line[1], line[2], line[3]):
            return line
    return None


# =================================================
# Game functions

def run_game():
    # Make and draw the board
    board = make_board(3, 3)
    draw_board()
    num_pieces = 0

    # main game loop
    while True:

        # Ask current player for a move
        if num_pieces % 2 == 0:
            current_shape = "X"
        else:
            current_shape = "O"

        print("\n\nPlayer {}".format(current_shape))
        x = input("What x to put your piece in: ")
        if x not in ["0", "1", "2"]:
            print("That is not a valid x")
            continue
        x = int(x)
        y = input("What y to put your piece in: ")
        if y not in ["0", "1", "2"]:
            print("That is not a valid y")
            continue
        y = int(y)

        # Try to add piece to the board
        if not update_board(board, x, y, current_shape):
            print("That is not a valid move, please try again")
            continue

        # Draw the  piece
        draw_square(x, y, current_shape)

        # Check for win
        winning_line = check_win_board(board)
        if winning_line:
            print("Game over. Player {} has won!".format(current_shape))

            # Draw win line
            draw_line(winning_line[0], winning_line[1], winning_line[2], winning_line[3])
            break

        # Switch to the next player
        num_pieces += 1

        # Check for draw
        if num_pieces == 9:
            print("There are no more spaces left on the board. It's a draw.")
            break


    input("Press enter to exit this game")

# ------------------------

t.speed(10)




run_game()
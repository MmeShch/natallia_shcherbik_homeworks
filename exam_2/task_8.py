
def is_king_can_move(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2

    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
        return "YES"
    else:
        return "NO"

def is_knight_can_move(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2

    if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
        return "YES"
    else:
        return "NO"

def is_rook_can_move(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2

    if x1 == x2 or y1 == y2:
        return "YES"
    else:
        return "NO"


def is_queen_can_move(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2

    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return "YES"
    else:
        return "NO"


def is_bishop_can_move(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2

    if abs(x1 - x2) == abs(y1 - y2):
        return "YES"
    else:
        return "NO"

print("=========king==========")
print(is_king_can_move([2, 2], [4, 4]))
print(is_king_can_move([2, 2], [2, 3]))
print(is_king_can_move([2, 2], [3, 2]))
print(is_king_can_move([2, 2], [1, 1]))
print(is_king_can_move([2, 2], [2, 4]))
print("==========knight==============")
print(is_knight_can_move([1, 2], [3, 3]))
print(is_knight_can_move([4, 4], [2, 3]))
print(is_knight_can_move([3, 1], [1, 2]))
print(is_knight_can_move([4, 4], [2, 1]))
print(is_knight_can_move([3, 1], [1, 5]))
print("================rook==============")
print(is_rook_can_move([2, 2], [2, 5]))
print(is_rook_can_move([2, 2], [4, 2]))
print(is_rook_can_move([2, 2], [3, 3]))
print(is_rook_can_move([2, 2], [1, 4]))
print("===================queen===============")
print(is_queen_can_move([2, 3], [4, 5]))
print(is_queen_can_move([1, 3], [1, 1]))
print(is_queen_can_move([4, 4], [1, 4]))
print(is_queen_can_move([2, 2], [4, 3]))
print("==============bishop===============")
print(is_bishop_can_move([2, 2], [4, 4]))
print(is_bishop_can_move([2, 4], [3, 3]))
print(is_bishop_can_move([2, 3], [4, 1]))
print(is_bishop_can_move([2, 4], [4, 4]))
print(is_bishop_can_move([2, 2], [2, 5]))



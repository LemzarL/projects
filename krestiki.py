def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("   с компьютером   ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if not 0 <= x <= 2 or not 0<= y <= 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл Компьютер!!!")
            return True
    return False

#функция разворота игрового поля
def rotate_matrix( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

# ходы компьютора, если игрок начал  с угла
def player_in_corner():
    if count == 2:
        x, y = 0, 0
    elif count == 4:
        if field[2][2] == " ":
            x, y = 2, 2
        else:
            x, y = 1, 2
    elif count == 6:
        if field[1][0] == " ":
            x, y = 1, 0
        else:
            x, y = 2, 1
    elif count == 8:
        if field[0][1] == " ":
            x, y = 0, 1
        else:
            x, y = 2, 0
    return x, y

# ходы компьютора, если игрок начал не с угла
def player_not_corner():
    if count == 2:
        x, y = 0, 0
    elif count == 4:
        if field[2][2] == " ":
            x, y = 2, 2
        else:
            x, y = 2, 0
    elif count == 6:
        if field[1][0] == " ":
            x, y = 1, 0
        elif field[0][2] == " ":
            x, y = 0, 2
    return x, y


def computer_move():
# Определяем начал игрок с угла или нет
    if field[0][2] == "X":
        x, y = player_in_corner()
    else:
        x, y = player_not_corner()
    return x, y





greet()
field = [[" "] * 3 for i in range(3)]
count = 0
print( "\n Компьютор ходит первым")
field[1][1] = "0"
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
        x, y = ask()
        field[x][y] = "X"
        # Повернем поле на 90, 180 или 270 градусов, чтобы "X" был на первой строке
        while not (field[0][1] == "X" or field[0][2] == "X"):
            field = rotate_matrix(field)
            print("\n Повернем поле")

    else:
        print(" Ходит компьютор!")
        x, y = computer_move()
        field[x][y] = "0"


    if check_win():
        break

    if count == 8:
        print(" Ничья!")
        break
show()

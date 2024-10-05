
field = [' ' for _ in range(9)]
#функция для печати поля
def print_field():
    print(f" {field[0]} | {field[1]} | {field[2]} ")
    print("---+---+---")
    print(f" {field[3]} | {field[4]} | {field[5]} ")
    print("---+---+---")
    print(f" {field[6]} | {field[7]} | {field[8]} ")

#функция для проверки победы
def check_win():
    win_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for i in win_combinations:
        if field[i[0]] == field[i[1]] == field[i[2]] != ' ':
            return True
    return False
#главный блок игры
player = 'X'
while True:
    print_field()
    move = int(input(f"Игрок {player} введите номер ячейки от 1 до 9: "))
    if move < 1 or move > 9:
        print("Неправильный ввод")
    else:
        if field[move - 1] != ' ':
            print("Ячейка занята")
            continue
        field[move - 1] = player
        if check_win():
            print_field()
            print(f"Победа игрока {player}. Поздравляю!")
            break

        player = 'O' if player == 'X' else 'X'
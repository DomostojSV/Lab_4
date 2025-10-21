def draw_rectangle(rows, columns, ch="#"):

    for i in range(rows):
        for j in range(columns):
            print(ch, end="")
        print()


def draw_right_triangle(rows, ch="#"):

    for i in range(1, rows + 1):
        for j in range(i):
            print(ch, end="")
        print()


def draw_frame(rows, columns, ch="#"):

    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(ch, end="")
            else:
                print(" ", end="")
        print()


def main():

    try:
        n = int(input("Введите количество строк: "))
        m = int(input("Введите количество столбцов: "))
    except ValueError:
        print("Введите ЦЕЛЫЕ числа!")
        return

    print("\nПРЯМОУГОЛЬНИК:")
    draw_rectangle(n, m)

    print("\nПРАВЫЙ ТРЕУГОЛЬНИК:")
    draw_right_triangle(n)

    print("\nРАМКА:")
    draw_frame(n, m)



main()
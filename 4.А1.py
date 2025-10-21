import random
import time


def multiplication_trainer():
    try:
        N = int(input("Введите количество примеров: "))
    except ValueError:
        print("Введите ЦЕЛОЕ число! ")
        return

    correct_answers = 0
    total_time = 0
    times = []

    for i in range(N):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        correct_result = a * b

        print(f"Вопрос {i + 1}/{N}")

        while True:
            start_time = time.time()
            try:
                user_answer = input(f"{a} × {b} = ")
                time_spent = time.time() - start_time
                user_answer = int(user_answer)
                break
            except ValueError:
                print("Введите ЦЕЛОЕ число! ")

        if user_answer == correct_result:
            print(f"Верно! (Время: {time_spent:.1f} сек)")
            correct_answers += 1
        else:
            print(f"Неверно! Правильно: {correct_result} (Время: {time_spent:.1f} сек)")

        total_time += time_spent
        times.append(time_spent)


    print("=" * 60)
    print("СТАТИСТИКА:")
    print("=" * 60)
    print(f"Общее время: {total_time:.1f} секунд")
    print(f"Среднее время на вопрос: {total_time / N:.1f} сек")
    print(f"Правильных ответов: {correct_answers}/{N}")
    print(f"Процент правильных: {correct_answers / N * 100:.1f}%")



multiplication_trainer()
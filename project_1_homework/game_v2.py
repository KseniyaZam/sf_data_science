"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        if len(str(number))==1:
            predict_number = np.random.randint(1, 10)  # предполагаемое число
            if int(number) == predict_number:
                break
        if len(str(number))==3:
            predict_number=100
            break
        if len(str(number))==2:
            if str(number)[0]==1:
                predict_number = np.random.randint(10, 20)
                if int(number) == predict_number:
                    break
            if str(number)[0]==2:
                predict_number = np.random.randint(20, 30)
                if int(number) == predict_number:
                    break
            if str(number)[0]==3:
                predict_number = np.random.randint(30, 40)
                if int(number) == predict_number:
                    break
            if str(number)[0]==4:
                predict_number = np.random.randint(40, 50)
                if int(number) == predict_number:
                    break 
            if str(number)[0]==5:
                predict_number = np.random.randint(50, 60)
                if int(number) == predict_number:
                    break
            if str(number)[0]==6:
                predict_number = np.random.randint(60, 70)       
                if int(number) == predict_number:
                    break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

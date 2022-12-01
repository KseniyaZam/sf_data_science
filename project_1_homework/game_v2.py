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
    n=str(number)

    while True:
        count += 1
        if len(n)==1:
            predict_number = np.random.randint(1, 10)  # предполагаемое число
            if int(number) == predict_number:
                break
        if len(n)==3:
            predict_number=100
            break
        if len(n)==2:
            for i in n:
                if int(i)==1:
                    predict_number = np.random.randint(10, 20)   
                    if number == predict_number:
                        break
                    else:
                        continue
                if int(i)==2:
                    predict_number = np.random.randint(20, 30)   
                    if number == predict_number:
                        break
                    else:
                        continue
                if int(i)==3:
                    predict_number = np.random.randint(30, 40)   
                    if number == predict_number:
                        break
                    else:
                        continue
                if int(i)==4:
                    predict_number = np.random.randint(40, 50)   
                    if number == predict_number:
                        break
                    else:
                        continue
                if int(i)==5:
                    predict_number = np.random.randint(50, 60)   
                    if number == predict_number:
                        break
                    else:
                        continue
                if int(i)==6:
                    predict_number = np.random.randint(60, 70)   
                    if number == predict_number:
                        break
                    else:
                        continue
                if int(i)==7:
                    predict_number = np.random.randint(70, 80)   
                    if number == predict_number:
                        break
                    else:
                        continue
                if int(i)==8:
                    predict_number = np.random.randint(80, 90)   
                    if number == predict_number:
                        break
                    else:
                        continue
                if int(i)==9:
                    predict_number = np.random.randint(90, 100)   
                    if number == predict_number:
                        break
                    else:
                        continue
                # выход из цикла если угадали
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

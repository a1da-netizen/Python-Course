import numpy as np


def game_core_v1(number):
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)

        if number == predict:
            return count


def game_core_v2(number):
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1

        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count


def game_core_v3(number):
    left = 1
    right = 100
    count = 1
    predict = (left + right) // 2

    while number != predict:
        count += 1

        if number > predict:
            left = predict + 1
        elif number < predict:
            right = predict - 1

        predict = (left + right) // 2

    return count


def score_game(game_score):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        count_ls.append(game_score(number))

    score = int(np.mean(count_ls))

    return score

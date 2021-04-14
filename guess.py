import numpy as np

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v3(number):
    '''Сначала проверяем число 50, а потом уменьшаем или увеличиваем его в зависимости от того,
     больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = 50
    step = predict
    while True:
        count+=1
        step = int(step/2) if int(step/2) else 1 #уменьшаем шаг в 2 раза до 1
        if number > predict:
            predict += step
        elif number < predict:
            predict -= step
        else: return count
    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v3)
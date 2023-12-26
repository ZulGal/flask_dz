# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# 🐀 Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# 🐀 Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# 🐀 При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# 🐀 В каждом решении нужно вывести время выполнения
# вычислений.
import threading
import time
import numpy as np


N = 1000000
arr = np.random.randint(0,10,N)

sum=0
def sequential(arr,calc,thead):
    global sum
    print(f"Запускаем поток № {thead}")
    start = thead * calc
    stop = (thead + 1) * calc
    for i in range(start,stop):
        sum += arr[i]
    print(f"{stop} циклов вычислений закончены, sum = {sum} Поток № {thead}")
    return sum

def threaded(theads, calc):
    # theads - количество потоков
    # calc - количество операций на поток

    threads = []

    # делим вычисления на `theads` потоков
    for thead in range(theads):
        t = threading.Thread(target=sequential, args=(arr, calc, thead))
        threads.append(t)
        t.start()
    # Подождем, пока все потоки завершат свою работу.
    for thread in threads:
        thread.join()

if __name__=='__main__':
    start_time = time.time()
    # разделим вычисления на 4 потока
    # в каждом из которых по 250000 операций
    threaded(4,250000)

    # print(sequential(arr, 5, 2000))
    print(f'Общее время {time.time() - start_time} секунд')



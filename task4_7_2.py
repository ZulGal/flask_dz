# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# 🐀 Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# 🐀 Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# 🐀 При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# 🐀 В каждом решении нужно вывести время выполнения
# вычислений.
import multiprocessing
import time
import numpy as np


N = 1000000
arr = np.random.randint(0,10,N)

sum=0
def sequential(arr,calc,proc):
    global sum
    print(f"Запускаем поток № {proc}")
    start = proc * calc
    stop = (proc + 1) * calc
    for i in range(start,stop):
        sum += arr[i]
    print(f"{stop} циклов вычислений закончены, sum = {sum} Поток № {proc}")
    return sum

def processesed(procs, calc):
    # procs - количество потоков
    # calc - количество операций на поток

    processes = []

    # делим вычисления на `theads` потоков
    for proc in range(procs):
        p = multiprocessing.Process(target=sequential, args=(arr, calc, proc))
        processes.append(p)
        p.start()
    # Подождем, пока все потоки завершат свою работу.
    for p in processes:
        p.join()

if __name__=='__main__':
    start_time = time.time()
    # узнаем количество ядер у процессора
    n_proc = multiprocessing.cpu_count()
    # вычисляем сколько циклов вычислений будет приходится
    # на 1 ядро, что бы в сумме получилось 80 или чуть больше
    calc = 250000 // n_proc + 1
    processesed(n_proc, calc)

    print(f"Всего {n_proc} ядер в процессоре")
    print(f"На каждом ядре произведено {calc} циклов вычислений")
    print(f"Итого {n_proc * calc} циклов за: ", time.time() - start_time)
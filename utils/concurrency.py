import threading


def split_into_threads(tasks: list, threads_num: int) -> list:
    threads = []
    temp = []
    for i in range(len(tasks)):
        temp.append(tasks[i])
        if i % threads_num == 0:
            threads.append(temp)
            temp = []
    return threads


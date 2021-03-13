import threading


def split_into_threads(tasks: list, threads_num: int) -> list:
    """
    Splits a 1D list of tasks into a 2D array of iterable threads
    :param tasks:
    :param threads_num:
    :return:
    """

    threads = []
    temp = []
    for i in range(len(tasks)):
        temp.append(tasks[i])
        if i % threads_num == 0:
            threads.append(temp)
            temp = []
    return threads


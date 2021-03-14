import threading
from colorama import Fore

import requests


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


def mycroft_stuff(url: str, fails: bool) -> None:
    """
    Gets the status code of a target social media account
    :param url:
    :param fails:
    :return:
    """
    try:
        # print("sending " + url)
        page = requests.get(url)
        content = str(page.content)
        code = int(page.status_code)
        if code == 404 or code == 403 or "404" in content:
            if fails:
                print(Fore.MAGENTA + "[!] Failed " + url + Fore.RESET)
                return
        else:
            print(Fore.GREEN + "[+] Got user at <:" + url + Fore.LIGHTYELLOW_EX + " with status code <: " + page.status_code + Fore.RESET)

    except:
        pass


def thread_all(urls_list: list, fails: bool) -> None:
    for url_list in urls_list:
        threads = []
        for url in url_list:
            # print(url)
            t = threading.Thread(target=mycroft_stuff, args=[url, fails])
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()

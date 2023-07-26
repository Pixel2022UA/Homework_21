import concurrent.futures
import math
import multiprocessing
import time
import threading
import requests

    ################# Task №1 #################


def num1():
    for num in range(2, 21, 2):
        print(f"Парное число: {num}")


def num2():
    for num in range(1, 20, 2):
        print(f"Непарное число: {num}")


if __name__ == "__main__":
    t1 = threading.Thread(target=num1)
    t2 = threading.Thread(target=num2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    ################ Task №2 #################


def calculate_factorial(number):
    result = math.factorial(number)
    print(f"Факториал числа {number}: {result}")


if __name__ == "__main__":
    start_time = time.time()

    threads = []
    for i in range(1, 11):
        t = threading.Thread(target=calculate_factorial, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    multi_thread_time = time.time() - start_time
    print(f"Время выполнения многопоточного метода: {multi_thread_time:.5f} секунд")

    processes = []
    for i in range(1, 11):
        p = multiprocessing.Process(target=calculate_factorial, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    multi_process_time = time.time() - start_time
    print(
        f"Время выполнения многопроцессорного метода: {multi_process_time:.5f} секунд"
    )

    ################# Task №3 #################


def test_url(url, my_file):
    response = requests.get(url)
    if response.status_code == 200:
        with open(my_file, "a") as file:
            file.write(f"URL: {url}\n")
            file.write(f"Response:\n{response.text}\n")
            file.write("=" * 50 + "\n")


if __name__ == "__main__":
    urls = [
        "https://mylibrary-e460551407b2.herokuapp.com/api/authors/1/",
        "https://mylibrary-e460551407b2.herokuapp.com/api/authors/2/",
        "https://mylibrary-e460551407b2.herokuapp.com/api/authors/3/",
    ]
    my_file = "response_data.txt"
    start_time = time.time()
    threads = []
    for elem in urls:
        t = threading.Thread(target=test_url, args=(elem, my_file))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Время выполнения многопоточного метода: {elapsed_time:.5f} секунд")

    ################# Task №4 #################


def fetch_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"URL: {url}")


if __name__ == "__main__":
    urls = [
        "https://hub.dummyapis.com/delay?seconds=1",
        "https://mylibrary-e460551407b2.herokuapp.com/api/authors/2/",
        "https://jsonplaceholder.typicode.com/users/1",
    ]

    start_time = time.time()

    processes = []
    for url in urls:
        p = multiprocessing.Process(target=fetch_url, args=(url,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Время выполнения многопроцессорного метода: {elapsed_time:.5f} секунд")

    ################# Task №5 #################


def my_urls(url):
    response = requests.get(url)
    if response.status_code == 200:
        return f"URL: {url}\nResponse:\n{response.text[:200]}...\n"


if __name__ == "__main__":
    urls = [
        "https://mylibrary-e460551407b2.herokuapp.com/api/authors/1/",
        "https://mylibrary-e460551407b2.herokuapp.com/api/authors/2/",
        "https://mylibrary-e460551407b2.herokuapp.com/api/authors/3/",
    ]

    start_time = time.time()
    for url in urls:
        result_1 = [my_urls(url) for url in urls]
    end_time = time.time()
    time_result_1 = end_time - start_time

    print(f"Время последовательных запросов: {time_result_1:.5f} секунд\n")

    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(urls)) as executor:
        futures = [executor.submit(my_urls, url) for url in urls]

        result_2 = []
        for future in concurrent.futures.as_completed(futures):
            result_2.append(future)

    end_time = time.time()
    concurrent_elapsed_time = end_time - start_time

    print(
        f"Время с использованием concurrent.futures: {concurrent_elapsed_time:.5f} секунд"
    )
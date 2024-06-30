import requests

# i=0

# def save_ts(i):
#     with open(f'aaa/{i}.ts', 'wb') as file:
#         r=requests.get(url.format(i))
#         file.write(r.content)
#     i+=1


url='https://dgeft87wbj63p.cloudfront.net/a3e6f89ba0ff62839039_silvername_42509957928_1719140149/720p60/{}.ts'
# while True:
#     with open(f'aaa/{i}.ts', 'wb') as file:
#         r=requests.get(url.format(i))
#         file.write(r.content)
#     i+=1
#     # if i>5: break
#     print(i)
#     print (i*10/60/60)



import concurrent.futures
import time

# Пример функции, которую нужно выполнить в потоках
def save_ts(i):
    with open(f'aaa/{i}.ts', 'wb') as file:
        r=requests.get(url.format(i))
        file.write(r.content)
    print(i)

# Количество потоков
n_threads = 15
identifiers = range(3000)  # Пример списка идентификаторов для выполнения

# Используем ThreadPoolExecutor для запуска функций в нескольких потоках
with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
    # Запускаем функцию save_ts в n потоков
    futures = [executor.submit(save_ts, id) for id in identifiers]

    # Опционально: ждем завершения всех потоков и обрабатываем результаты
    # for future in concurrent.futures.as_completed(futures):
    #     try:
    #         result = future.result()  # Получаем результат выполнения
    #     except Exception as exc:
    #         print(f'Generated an exception: {exc}')
    #     else:
    #         print(f'Result: {result}')
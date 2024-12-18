import time

def log_message(message, log_file):
    """Записывает сообщение в лог-файл."""
    with open(log_file, 'a') as f:
        f.write(message + '\n')

def binary_search_recursive(func, interval, tol=1e-5, log_file='log.txt'):
    """Рекурсивный бинарный поиск корня функции."""
    start_time = time.time()
    a, b = interval
    fa, fb = func(a), func(b)

    # Логирование значений на границах
    log_message(f"Interval: [{a}, {b}], f(a): {fa}, f(b): {fb}", log_file)

    if fa * fb > 0:
        log_message("No root found in the interval.", log_file)
        return None

    mid = (a + b) / 2
    fmid = func(mid)

    log_message(f"Midpoint: {mid}, f(mid): {fmid}, Time elapsed: {time.time() - start_time:.6f} seconds", log_file)

    if abs(fmid) < tol:
        return mid

    if fa * fmid < 0:
        return binary_search_recursive(func, (a, mid), tol, log_file)
    else:
        return binary_search_recursive(func, (mid, b), tol, log_file)

def binary_search_iterative(func, interval, tol=1e-5, log_file='log.txt'):
    """Итеративный бинарный поиск корня функции."""
    start_time = time.time()
    a, b = interval
    fa, fb = func(a), func(b)

    # Логирование значений на границах
    log_message(f"Interval: [{a}, {b}], f(a): {fa}, f(b): {fb}", log_file)

    if fa * fb > 0:
        log_message("No root found in the interval.", log_file)
        return None

    while True:
        mid = (a + b) / 2
        fmid = func(mid)

        log_message(f"Midpoint: {mid}, f(mid): {fmid}, Time elapsed: {time.time() - start_time:.6f} seconds", log_file)

        if abs(fmid) < tol:
            return mid

        if fa * fmid < 0:
            b = mid
            fb = fmid
        else:
            a = mid
            fa = fmid

# Пример функции для поиска корня
def example_function(x):
    return x**2 - 2  # Корень: √2

# Задание интервала
interval = [0, 2]

# Запись логов в файл
log_file = 'binary_search_log.txt'

# Очистка файла перед записью
with open(log_file, 'w') as f:
    f.write("Binary Search Log\n")

# Запуск рекурсивного бинарного поиска
recursive_result = binary_search_recursive(example_function, interval, log_file=log_file)
print("Recursive Binary Search Result:", recursive_result)

# Запуск итеративного бинарного поиска
iterative_result = binary_search_iterative(example_function, interval, log_file=log_file)
print("Iterative Binary Search Result:", iterative_result)

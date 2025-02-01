import timeit

def find_coins_greedy(amount):
    # Жадібний алгоритм
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= count * coin
    return result

def find_min_coins(amount):
    # Динамічне програмування
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [0] * (amount + 1)
    used_coins = [{} for _ in range(amount + 1)]

    for i in range(1, amount + 1):
        min_coins[i] = float('inf')
        for coin in coins:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                used_coins[i] = used_coins[i - coin].copy()
                if coin in used_coins[i]:
                    used_coins[i][coin] += 1
                else:
                    used_coins[i][coin] = 1

    return used_coins[amount]

amount = 1000
# Вимірюємо час виконання жадібного алгоритму
greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=10000)

# Вимірюємо час виконання алгоритму динамічного програмування
dynamic_time = timeit.timeit(lambda: find_min_coins(amount), number=10000)

print(f"Жадібний алгоритм (середній час за 10000 виконань): {greedy_time:.6f} сек")
print(f"Динамічне програмування (середній час за 10000 виконань): {dynamic_time:.6f} сек")
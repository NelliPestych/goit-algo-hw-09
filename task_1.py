import time

# Реалізація Жадібного Алгоритму
# Жадібний алгоритм буде вибирати монети з найбільшим номіналом спочатку і так далі, поки не буде видана вся сума.
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count

    return result

# Реалізація Алгоритму Динамічного Програмування
# Алгоритм динамічного програмування буде будувати рішення поступово, використовуючи раніше знайдені оптимальні рішення
# для менших сум.
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_count = [None] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_count[i] = coin

    result = {}
    while amount > 0:
        coin = coin_count[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Порівняння Ефективності
amount = 113

start = time.time()
greedy_result = find_coins_greedy(amount)
greedy_time = time.time() - start

start = time.time()
dp_result = find_min_coins(amount)
dp_time = time.time() - start

print(f"Greedy Result: {greedy_result}, Time: {greedy_time:.6f} seconds")
print(f"DP Result: {dp_result}, Time: {dp_time:.6f} seconds")


def best(prices, window_size):
    n = len(prices)

    current_total = sum(prices[0:window_size])
    best_total = current_total
    print(f"Window: {prices[0:window_size]} = {current_total}")
    for i in range(window_size, n):
        left = prices[i - window_size]
        right = prices[i]
        # Update current window sum
        current_total = current_total - left + right
        # Update maximum sum
        best_total = max(best_total, current_total)
        
        window = prices[i - window_size + 1 : i + 1]
        print(f"Window: {window} = {current_total}")
    return best_total

prices = [2, 4, 6, 1, 7, 3, 5]

answer = best(prices, 4)
print("Best total:", answer)




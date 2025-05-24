""" Buy and Sell Stock problem (improved)"""

def best_profit(stock_values: list):
    """Calculates best moment to buy and sell stocks

    Args:
        stock_values (list): List of stock prices

    Returns:
        _type_: List containing maximum profit, best buy price and best sell price
    """
    buy_price = stock_values[0] # Starting price
    max_profit = best_buy_price = best_sell_price = 0 # Initializing indicators to 0
    for _, value in enumerate(stock_values):
        if buy_price <= value: # If profit is positive or zero (buying option)
            profit = value - buy_price
            max_profit = max(max_profit, profit)
            if profit == max_profit: # Sets best buy and sell prices if the profit is maximum
                best_buy_price = buy_price
                best_sell_price = value
        else: # If profit is negative the buy price is set to the value itself (no buying option)
            buy_price = value
    return max_profit, best_buy_price, best_sell_price # Returns 3 values at once in a list format

stock = [7, 10, 1, 3, 6, 4]
result = best_profit(stock)
print(f"Best profit: {result[0]} (Buy price: {result[1]} - Sell price: {result[2]})")

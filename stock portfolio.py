# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_investment = 0

# File me result save karne ke liye
file = open("portfolio.txt", "w")

n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock_name = input("\nEnter stock name (AAPL, TSLA, GOOGL, MSFT): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Investment in {stock_name}: ${investment}")

        file.write(
            f"Stock: {stock_name}, Quantity: {quantity}, Investment: ${investment}\n"
        )

    else:
        print("Stock not available!")

print("\nTotal Investment Value: $", total_investment)

file.write(f"\nTotal Investment Value: ${total_investment}")
file.close()

print("Portfolio saved in portfolio.txt")
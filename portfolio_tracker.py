# This Dictionary stores stock symbols and their prices
stock_prices = {
    "apple": 250.00,
    "google": 150.00,
    "amazon": 350.00,
    "microsoft": 200.00
}

print("Welcome to your stock tracker!")

while True:
    symbol = input("Enter stock symbol (or 'done' to finish): ").lower()
    if symbol == "done":
        break
    
    quantity = int(input("How many shares do you own?: "))
    
    if symbol in stock_prices:
        price = stock_prices[symbol]
        total_value = price * quantity
        print(f"The total value of {symbol}: ${total_value}")

        # optional: save the portfolio to a .txt file
        with open("portfolio.txt", "a") as file:
            file.write(f"Total portfolio value for {symbol}: ${total_value}\n")
    else:
        print("Stock not found!")
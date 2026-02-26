# This Dictionary stores stock symbols and their prices
stock_prices = {
    "apple": 250.00,
    "google": 150.00,
    "amazon": 350.00,
    "microsoft": 200.00}

print("welcome to your stock tracker!")
symbol = input(
    "Enter stock symbol (apple, google, amazon, microsoft) : ").upper()
quantity = int(input("how many shares do you own?:"))
if symbol in stock_prices:
    price = stock_prices[symbol]
    total_value = price * quantity
    print(f"The total value of {symbol}: ${total_value}")

    # optional: save the portfolio to a .txt file
    with open("portfolio.txt", "a") as file:
        file.write(f"Total portfolio value for {symbol}: ${total_value}\n")
else:
    print("Stock not found!")

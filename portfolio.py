portfolios = {
    "P101": {
        "cash_balance": 500000,
        "restricted_securities": ["Airtel", "Coco Cola"],
        "max_position_pct": 30,
        "current_holdings": [
            {
                "security_id": "EPAM",
                "quantity": 50,
                "market_price": 1000
            },
            {
                "security_id": "Google",
                "quantity": 100,
                "market_price": 1500
            },
            {
                "security_id": "TCS",
                "quantity": 20,
                "market_price": 4000
            }
        ]
    }
}

def check_trade(portfolio, security_id, action, quantity, price):

    # STEP 1
    if quantity <= 0 or price <= 0:
        return "Rejected", "Invalid trade data."

    if action not in ["Buy", "Sell"]:
        return "Rejected", "Invalid trade data."

    # STEP 2
    if security_id in portfolio["restricted_securities"]:
        return "Rejected", "Security is restricted for this portfolio."

    existing_quantity = 0
    for holding in portfolio["current_holdings"]:
        if holding["security_id"] == security_id:
            existing_quantity += holding["quantity"]

    # STEP 3
    if action == "Sell":
        if existing_quantity < quantity:
            return "Rejected", "Insufficient holdings to sell."


    # STEP 4
    if action == "Buy":
        purchase_cost = quantity * price
        if purchase_cost > portfolio["cash_balance"]:
            return "Rejected", "Insufficient cash for this buy order."

    #STEP 5
    if action == "Buy":
        post_trade_cash = portfolio["cash_balance"] - purchase_cost
        post_trade_quantity = existing_quantity + quantity
        post_trade_security_value = post_trade_quantity * price
        value_of_other_holdings = 0

        for holding in portfolio["current_holdings"]:
            if holding["security_id"] != security_id:
                value_of_other_holdings += holding["quantity"] * holding["market_price"]

        total_portfolio_value_after = post_trade_cash + post_trade_security_value + value_of_other_holdings
        position_pct = (post_trade_security_value / total_portfolio_value_after) * 100

        if position_pct > portfolio["max_position_pct"]:
            return ("Needs Manual Sign-off","Exceeds maximum position concentration — requires approval.")

    # STEP 6
    return "Approved", "All compliance checks passed."

def display_result(portfolio_id, security_id, action, quantity, price, decision, reason):
    print("Portfolio ID:", portfolio_id)
    print("Security ID:", security_id)
    print("Action:", action)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Decision:", decision)
    print("Reason:", reason)

def enter_trade():
    portfolio_id = input("Enter Portfolio ID: ")
    if portfolio_id not in portfolios:
        print("Portfolio not found!")
        return
    security_id = input("Enter Security ID: ")
    action = input("Enter Buy or Sell: ")
    quantity = float(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    portfolio = portfolios[portfolio_id]
    decision, reason = check_trade(portfolio, security_id, action,quantity, price)
    display_result(portfolio_id, security_id, action,quantity, price, decision, reason)

def main():
    while True:
        print("\n1. Enter New Trade")
        print("2. View Portfolio")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            enter_trade()
        elif choice == "2":
            print(portfolios)
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

main()
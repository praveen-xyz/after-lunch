# Currency Converter: INR to USD, AED, SGD

def currency_converter(amount_in_inr):

    rates = {
        "USD": 0.012,   # 1 INR = 0.012 USD
        "AED": 0.044,   # 1 INR = 0.044 AED
        "SGD": 0.016    # 1 INR = 0.016 SGD
    }

    usd = amount_in_inr * rates["USD"]
    aed = amount_in_inr * rates["AED"]
    sgd = amount_in_inr * rates["SGD"]

    print(f"\n₹{amount_in_inr} INR = ${usd:.2f} USD")
    print(f"₹{amount_in_inr} INR = {aed:.2f} AED (Dubai Dirham)")
    print(f"₹{amount_in_inr} INR = ${sgd:.2f} SGD (Singapore Dollar)")
print(" Currency Converter (INR → USD / AED / SGD)")
amount = float(input("Enter amount in Indian Rupees (INR): "))
currency_converter(amount)

file = open("Act 4B\currency.csv", "r")
lines = file.readlines()
file.close()

lines.pop(0)

currency_rates = {}
index = 0
while index < len(lines):
    parts = lines[index].strip().split(",")
    currency_rates[parts[0]] = float(parts[2])
    index += 1

usd_amount = float(input("How much dollar do you have? "))
currency = input("What currency you want to have? ").upper()

if currency in currency_rates:
    converted_amount = usd_amount * currency_rates[currency]
    print(f"\nDollar: {usd_amount} USD")
    print(f"{currency}: {converted_amount}")
else:
    print("Currency not found.")


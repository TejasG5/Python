"""Currency Converter
   Indian Rupees to any currency
   In Currency Data.txt 1st column is name of currency
                        2nd column is 1 INR to that currency
                        3rd column is 1 in that currency to INR"""

with open("Currency Data.txt") as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = float(input("Enter the amount: "))
print("Enter the name of currency you want convert this amount to\nChoose among the following:-\n")
[print(item) for item in currencyDict.keys()]

currency = input("Enter one of these currencies: ")
print(f"{amount} INR = {amount* float(currencyDict[currency])} {currency}")
import urllib.request

url = "http://www.cbr.ru/scripts/XML_daily.asp"
crb = urllib.request.urlopen(url)
string = str(crb.read())
usd = ""
string.index("USD")
exchange = string.index("USD")+91
rawusd = string[exchange:exchange+10]

for i in rawusd:
    if i.isnumeric() == True:
        usd += str(i)
    elif i == ",":
        usd += "."

print("Текущий курс: 1 USD =",usd,"RUB")
while True:
    inputkeyboard = input("Введите сумму в долларах: ")
    if inputkeyboard.isnumeric() == True:
        break
    else:
        print("Введено неверное значение")

result = float(inputkeyboard)*float(usd)
print(inputkeyboard, "USD =" , round(result), "RUB")
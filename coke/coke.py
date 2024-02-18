def coins():
    coin = input("Insert Coin!: ")
    coin = int(coin)
    valid_currency = [5, 10, 25]
    if coin in valid_currency:
        return coin
    else:
        return 0

def main():
    price = 50
    while price != 0:
        price = price - coins()
        if price <= 0:
            print("Change owed: ", abs(price))
            return
        else:
            print("Amount due: ", price)


main()
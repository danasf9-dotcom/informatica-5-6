def main():
    pesos = float(input("What did you have left in pesos? "))
    soles = float(input("What did you have left in soles? "))
    reais = float(input("What did you have left in reais? "))

    usd = (pesos * 0.00032) + (soles * 0.30) + (reais * 0.19)
    mxn = round(usd * 17.07,2)

    print(f"USD: {round(usd, 2)}")
    print(f"MXN: {mxn}")

if __name__ == "__main__":
    main()


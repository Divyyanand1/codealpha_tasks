Stocks={
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 400
}

total_investment=0

while True:

    Enter_stock=input("Enter The Stock Name:").upper()
    if Enter_stock=="DONE":
        break
    if Enter_stock in Stocks:
        Quantity=int(input("Enter The Quantity:"))
        price=Stocks[Enter_stock]*Quantity
        print("price:",price)

        investement=price

        total_investment=total_investment+investement
    else:
        print("NO STOCK FOUND!!")    

print(total_investment)


with open("Portfolio.txt","a") as f:
    f.write("Stock_Portfolio\n",)
    f.write("Total_Investment:"+str(total_investment)+"\n\n")
    print("Portfolio Done!!")


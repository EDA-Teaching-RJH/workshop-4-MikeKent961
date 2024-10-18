machineOn = False
drinksPrice = [75, 50, 100]
coinsAccepted = [50, 20, 10, 5]
drinks = ["Coffee", "Tea", "Hot Chocolate"]
isCoinAccepted = False

def main():
    print("Coffee Machine :D")
    machineOn = True
    while machineOn == True:
        payment(chooseDrink())
        userCont = input("Do you want another one? ")
        if userCont == "no" or userCont == "No":
            machineOn = False
    print("aight bye")      
        
    

def chooseDrink():
    print("Please select number of drink you would like.")
    for i in drinks:
        print(str(drinks.index(i)+1) + "." , i)
    
    return int(input("Enter here: "))
    

def payment(choice):
    userPayed = 0
    while userPayed < drinksPrice[choice-1]:
        print("Amount left to pay:" , drinksPrice[choice-1] - userPayed)
        coinInsert = int(input("Insert coin: "))
        for i in coinsAccepted:
            if coinInsert == i:
                isCoinAccepted = True
                
            
        if isCoinAccepted == False:
            print("Invalid coin.")
            print("")
            continue
        else:
            userPayed += coinInsert
            isCoinAccepted=False

        print("")

    if userPayed > choice-1:
        print("Your change is:" , userPayed-drinksPrice[choice-1])


main()
# We will make a currency converter in this vedio...


# at first we will make a text file which will used as a data base...

with open("currencydb.txt") as db:
    lines = db.readlines()

cd ={}
for line in lines :
    parsed= line.split("\t")
    cd[parsed[0]] = parsed[1]

ammount = int(input("Enter the ammount :"))

print("Choose the currency to convert...........")
[print(item) for item in cd.keys()]
money = input("Enter the name :")

print(f"{ammount} Dollar = {ammount * float(cd[money])}{money}")
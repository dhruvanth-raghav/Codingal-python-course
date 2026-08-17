currency={
    "IND":"Rupee",
    "USA":"Dollar",
    "UAE":"Dirham",
    "Singapore":"Singoporean dollar"
}
print(currency['IND'])
print(type(currency))
print(len(currency))

country=input("Enter a country to see its currency:")
# print(currency[country])

#SAFELY ACCESSING DICITIONARY KEYS
print(currency.get(country,"Country not found!"))

currency.pop("Singapore")
print(currency)


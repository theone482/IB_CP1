# IB 2nd order up
menu = {
    "Island favorites":{
        "three meat mix": 16.79,
        "two meat mix": 13.99,
        "hawaiian BBQ mix": 19.79,
        "seafood mix": 18.29,
        "BBQ & Katsu Mix": 18.29,
        'grilled Spam & eggs': 12.99,
        "Loco Moco": 13.99
    },
    "Chicken Plates": {
        "hawaiian BBQ chicken": 13.99,
        "katsu chicken": 13.99,
        "teriyaki chicken": 13.99,
        "island Fire chicken": 14.99
    },
    "beef plates": {
        "kalbi Short Ribs": 21.29,
        "teryaki beef": 16.99,
        "Hawwaiian BBQ Beef": 16.99
    },
    "pork":{
        "kalua Pork": 13.99
    },
    "seafood Plates":{
        "Island white fish": 14.99,
        "Tempure shrimp": 14.99,
        "crispy shrimp":14.99
    },
    "mini meal": {
        "mini Hawaiian BBQ chicken": 10.25,
        "mini teriyaki Chicken": 10.25,
        "mini katsu chicken": 10.25,
        "mini hawaiian BBQ Beef": 11.00,
        "mini teriyaki beef": 11.00,
        "mini kalua Pork": 10.25,
        "mini grilled spam & eggs": 10.25,
        "mini crispy shrmp": 10.50,
        "mini island fire chcicken": 10.50,
        "mini loco moco": 10.25
    },
    "appetizers & sides": {
        "spam musubi": 6.49,
        "BBQ chicken musubi": 6.49,
        "BBQ beef musubi": 6.49,
        "crispy shrimp 5 pieces": 7.69,
        "tempure shrimp 1 pieces": 2.00,
        "tempure shrimp 2 pieces": 3.29,
        "gyoza 3 pieces": 3.99,
        "gyoza 6 pieces":7.25,
        "steam white rice": 2.99,
        "steam brown rice": 2.99,
    },
    "salads":{
        "Side House salad": 5.95,
        "full House salad": 8.25,
        "House salad w/protein": 9.99,
        "1 scoop macaroni salad": 2.59,
        "2 scoop macaroni salad": 4.59,
        "4 scoop macaroni salad":8.09
    },
    "drinks":{
        "Hawaiian sun: Lilikoi Passion": 5.99,
        "Hawaiian sun: guava": 5.99,
        "Hawaiian sun: Passion Orange": 5.99,
        "Hawaiian sun: Pineapple": 5.99,
        "Hawaiian sun: Mango Orange": 5.99,
        "Hawaiian sun: Luau punch": 5.99,
        "Hawaiian sun: strawberry Guava": 5.99,
        "Hawaiian sun: Strawberrt lilikoi": 5.99,
        "Hawaiian sun: lilikoi lychee": 5.99
    }
}
def show_menu():
    for cat, items in menu.items():
        print(f"\n{cat}")
        for item, price in items.items():
            print(f"  {item} - ${price:.2f}")

def get_choice(cat, msg):
    while True:
        choice = input(msg).lower()
        if choice in [i.lower() for i in menu[cat]]:
            for item, price in menu[cat].items():
                if item.lower() == choice:
                    return item, price
        print("Not on the menu, try again.")

def get_main():
    mains = {}
    for cat in ["Island favorites","Chicken Plates","beef plates","pork","seafood Plates","mini meal"]:
        for item, price in menu[cat].items():
            mains[item.lower()] = (item, price)
    while True:
        choice = input("Pick a main: ").lower()
        if choice in mains:
            return mains[choice]
        print("Not on the menu, try again.")

# get choice from any category
def get_choice(category, msg):
    while True:
        choice = input(msg).strip().lower()
        options = {k.lower(): v for k, v in menu[category].items()}
        if choice in options:
            return choice, options[choice]
        else:
            print("Not on the menu, try again.")

# main order
def main():
    show_menu()
    drink, d_price = get_choice("drinks","Pick a drink: ")
    main_item, m_price = get_main()
    side1, s1_price = get_choice("appetizers & sides","Pick side 1: ")
    side2, s2_price = get_choice("appetizers & sides","Pick side 2: ")
    total = d_price + m_price + s1_price + s2_price
    print("\n--- Your Order ---")
    print(f"{drink} - ${drink_price:.2f}")
    print(f"{main_item} - ${main_price:.2f}")
    print(f"{side1} - ${side1_price:.2f}")
    print(f"{side2} - ${side2_price:.2f}")
    print(f"Total: ${total:.2f}")
#get the progarm running
if __name__ = "__main__":
    main()


show_menu()
get_main()
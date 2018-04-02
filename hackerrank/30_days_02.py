
if __name__ == "__main__":
    meal_cost = float(raw_input().strip())
    tip_percent = int(raw_input().strip())
    tax_percent = int(raw_input().strip())

    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    total = meal_cost + tip + tax

    print("The total meal cost is {:.0f} dollars.".format(total))

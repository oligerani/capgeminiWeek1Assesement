def split_bill():
    

    total_bill = float(input("Enter the total bill amount: "))
    num_people = int(input("Enter the number of people: "))
    tip_percentage = float(input("Enter the tip percentage  "))

    total_with_tip = total_bill * (1 + tip_percentage / 100)
    amount_per_person = total_with_tip / num_people

    print(f"\nTotal bill (with tip): ₹{total_with_tip:.2f}")
    print(f"Each person needs to pay: ₹{amount_per_person:.2f}")


split_bill()

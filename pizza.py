def main():
    size = str(input("What size are you thinking about ordering: enter medium or large? ---> "))
    size_inches = int(input("What size is the pizza in inches? --> "))
    menu_price = float(input("What is the menu price? --> $ "))
    pizza_discount = int(input("How many pizzas do you have to order, at a minimum, to get a discount? --> "))

    if pizza_discount == 3:
        pizza_quantity = int(input("How many {size medium or large} pizza(s) are you ordering? --> "))
        new_price = float(input("What is the new discounted price per pizza? --> $  "))
        radius = size_inches / 2
        area_pizza = 3.14 * radius * radius
        price_perinch = menu_price / area_pizza
        price = menu_price * pizza_quantity
        if size == "medium":
            price_perinch = new_price / area_pizza
            price_per_square = menu_price / area_pizza
            subtotal = new_price * pizza_quantity
            savings = price - subtotal 
            print(f"You want to order {pizza_quantity} {size} {size_inches} inch pizzas. This a ${price_perinch:.2f} per square inch value at the discounted price vs ${price_per_square:.2f} per square inch at the menu price.")
            print(f"The subtotal is ${subtotal:.2f} to order {pizza_quantity} {size} {size_inches} inch pizzas. This a ${price_per_square:.2f} per square inch at the menu price.")
            print(f"The subtotal is $ {subtotal:.2f} and you save ${savings:.2f}")


    if pizza_discount == 1:
        pizza_quantity = int(input("How many {size medium or large} pizza(s) are you ordering? --> "))
        new_price = float(input("What is the new discounted price per pizza? --> $  "))
        radius = size_inches / 2
        area_pizza = 3.14 * radius * radius
        price_perinch = menu_price / area_pizza
        price = menu_price * pizza_quantity
        if size == "large":
            price_perinch = new_price / area_pizza
            price_per_square = menu_price / area_pizza
            subtotal = new_price * pizza_quantity
            savings = price - subtotal 
            print(f"You want to order {pizza_quantity} {size} {size_inches} inch pizzas. This a ${price_perinch:.2f} per square inch value at the discounted price vs ${price_per_square:.2f} per square inch at the menu price.")
            print(f"The subtotal is ${subtotal:.2f} and you saved ${savings:.2f}")
    if pizza_discount == 1 and pizza_quantity <= 1:
        price_per_square = menu_price / area_pizza
        subtotal = menu_price * pizza_quantity
        print(f"You want to order {pizza_quantity} {size} {size_inches} inch pizzas. This a $ {price_per_square:.2f},per square inch at the menu price.")
        print(f"The subtotal is ${subtotal:.2f}")



    delivery_option = str(input("Delivery or Pickup? Enter X for delivery, Y for pickup --> "))
    if delivery_option == "X":
        delivery_fee = 5.49
        new_subtotal = subtotal + delivery_fee
        print(f"You want the pizza delivered and the $5.49 delivery fee has been added. Your new subtotal is ${new_subtotal:.2f}")
    elif delivery_option == "Y":
        pickup_discount = -2.00
        new_subtotal = subtotal + pickup_discount
        print(f"You choose the pick up option and the $2.00 discount has been added. Your new subtotal is ${new_subtotal:.2f}")
    student = str(input("Are you a student? enter X for yes, Y for no ---> "))
    if student == "X":
        student_discount = 10
        discount = new_subtotal / student_discount
        print(f"Because you are a student, a 10.00% discount of ${discount:.2f} has been deducted from the subtotal")
        student_subtotal = new_subtotal - discount
        print(f"Your new subtotal is now ${student_subtotal:.2f}")
        tax = 0.1025
        tax_after = student_subtotal * tax
        subtotal_tax = student_subtotal + tax_after
        print(f"The local tax rate of 10.25% has been added to your subtotal.  You were charged ${tax_after:.2f} in taxes.  Your new after tax subtotal is now ${subtotal_tax:.2f}")
        tip_amount = float(input("How much do you want to tip? --> $"))
        grand_total = tip_amount + subtotal_tax
        print(f"Your tip of ${tip_amount} was added to your subtotal of ${subtotal_tax:.2f}. The grand total due is now ${grand_total:.2f}")
    if student == "Y":
        student_discount = 0
        tax = 0.1025
        tax_after = new_subtotal * tax
        subtotal_tax = student_subtotal + tax_after
        print(f"The local tax rate of 10.25% has been added to your subtotal.  You were charged ${tax_after:.2f} in taxes.  Your new after tax subtotal is now ${subtotal_tax:.2f}")
        tip_amount = float(input("How much do you want to tip? --> $"))
        grand_total = tip_amount + subtotal_tax
        print(f"Your tip of ${tip_amount} was added to your subtotal of $. The grand total due is now ${grand_total:.2f}")
    repeat = input("Would you like to repeat the process? Enter Yes or No: ")
    if repeat == "Yes":
        main()
    else:
        print("Thank you")
        exit()
main()
size = str(input("What size are you thinking about ordering: enter medium or large? ---> "))
size_inches = int(input("What size is the pizza in inches? --> "))
menu_price = float(input("What is the menu price? --> $ "))
pizza_discount = int(input("How many pizzas do you have to order, at a minimum, to get a discount? --> "))
again = True
if pizza_discount == 3:
    pizza_quantity = int(input("How many {size medium or large} pizza(s) are you ordering? --> "))
    radius = size_inches / 2
    area_pizza = 3.14 * radius * radius
    price_perinch = menu_price / area_pizza
    price = menu_price * pizza_quantity
    if size == "medium":
        new_price = menu_price -10
        price_perinch = new_price / area_pizza
        price_per_square = menu_price / area_pizza
        subtotal = new_price * pizza_quantity
        savings = price - subtotal 
    print("You want to order ",pizza_quantity, size, size_inches, "inch pizzas. This a $", price_perinch, " per square inch value at the discounted price vs $", price_per_square,"per square inch at the menu price.")
    print("The subtotal is $",subtotal, "and you saved $",savings)

if pizza_discount == 1:
    pizza_quantity = int(input("How many {size medium or large} pizza(s) are you ordering? --> "))
    radius = size_inches / 2
    area_pizza = 3.14 * radius * radius
    price_perinch = menu_price / area_pizza
    price = menu_price * pizza_quantity
    if size == "large":
        new_price = menu_price - 9
        price_perinch = new_price / area_pizza
        price_per_square = menu_price / area_pizza
        subtotal = new_price * pizza_quantity
        savings = price - subtotal 
    print("You want to order ",pizza_quantity, size, size_inches, "inch pizzas. This a $", price_perinch, " per square inch value at the discounted price vs $", price_per_square,"per square inch at the menu price.")
    print("The subtotal is $",subtotal, "and you saved $",savings)

delivery_option = str(input("Delivery or Pickup? Enter X for delivery, Y for pickup --> "))
if delivery_option == "X":
    delivery_fee = 5.49
    new_subtotal = subtotal + delivery_fee
    print("You want the pizza delivered and the $5.49 delivery fee has been added. Your new subtotal is $",new_subtotal)
elif delivery_option == "Y":
    pickup_discount = -2.00
    new_subtotal = subtotal + pickup_discount
    print("You choose the pick up option and the $2.00 discount has been added. Your new subtotal is $",new_subtotal)
student = str(input("Are you a student? enter X for yes, Y for no ---> "))
if student == "X":
    student_discount = 10
    discount = new_subtotal / student_discount
    print("Because you are a student, a 10.00% discount of $",discount, "has been deducted from the subtotal")
    student_subtotal = new_subtotal - discount
    print("Your new subtotal is now $",student_subtotal)
    tax = 10.25
    tax_after = student_subtotal / tax
    print("The local tax rate of 10.25% has been added to your subtotal.  You were charged $",tax_after, " in taxes.  Your new after tax subtotal is now $",(student_subtotal + tax_after))
    tip_amount = float(input("How much do you want to tip? --> $"))
    print("Your tip of $5.00 was added to your subtotal of $26.25. The grand total due is now $",(student_subtotal + tax_after + tip_amount))
if student == "Y":
    student_discount = 0
    tax = 10.25
    tax_after = new_subtotal / tax
    print("The local tax rate of 10.25% has been added to your subtotal.  You were charged $",tax_after, " in taxes.  Your new after tax subtotal is now $",(new_subtotal + tax_after))
    tip_amount = float(input("How much do you want to tip? --> $"))
    print("Your tip of $5.00 was added to your subtotal of $26.25. The grand total due is now $",(new_subtotal + tax_after + tip_amount))

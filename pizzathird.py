# Luis Sequera 
# CIS 101 fall 2022
# Assigment: Pizza calculator

# pseudocode
# name a variable that store the size of the pizza, in -> size of the pizza, medium, large
# name a variable that store the size of the pizza in inches, in-> size of the pizza in inches
# name a variable that store the menu price of the pizza, in-> menu price
# name a variable that store the minimum of pizzas to get a discount, in -> minumum of pizzas
# name a variable that store the quantity of pizzas are ordering, in-> quantity of pizza
# make a conditional branch if the quantity of pizzas is greater than the minumum of pizzas to get of discount
# then, the pizzas have a new price.
# inside the conditional branch calculate the pizza price per square inch using the area formula
# calculate the first subtotal which is the menu price * quantity
# inside the conditional branch if quantity is greater than the minimum, open another conditional branch
# if size is medium or the size is large we calculate the new price per square inch using the discount price
# inside we calculate the NEW subtotal wich is the price with discount plus the quantity
# we calculate the saving = the new subtotal with discount price - the first subtotal with the menu price
# print the results
# outside, make a new conditional branch elif the quantity is less than the minimun, we dont input the new price, but still calculate the price per inch using the menu price
# inside the elif, open a new if size is == medium or == large
# calculate the subtotal wich in this conditional is just the menu price times the quantity
# print the results
# out of that if, we open a new elif, elif the minimum of pizzas to get a discount is equal to the quantity of pizzas and the size is large, assuming in every store is one large pizza minimum to get discount
# then calculate the price per square inch using the menu price, because it is not more than one
# calculate the subtotal wich in this conditional is just the menu price times the quantity
# print the results
# create a new elif with the conditions that minimum pizzas to order is equal than quantity
# we input the new price
# calculate the area
# calculate the cost per square inch
# inside, another if size == large or medium
# calculate the subtotal using the new price and the savings
# print the results
# create a variable that holds a input of the delivery option, pick up or delivery. in -> delivery option
# if the delivery option is delivery
# charge a fee of 5.49
# print the new subtotal with the delivery fee
# if the delivery option is pick up
# give a discount of 2$
# print the new subtoltal with the discount
# create a variable that holds the input of the student option. in -> student? yes or no
# if student is yes
# discount of 10%
# student subtotal = subtotal / 10
# also, inside calculate the taxes wich is 10.25%
# tax = student subtotal * 0.1025
# cost = student subtotal + tax
# print the new subtotal
# inside the if create another variable that hold the tip of the customer, in -> how much do you want to tip
# add the tip to the subtotal below 
# print the overall pay
# if student is no
# do not receive any discount
# discount = 0
# still calculate the taxes wich is 10.25%
# tax = student subtotal * 0.1025
# cost = student subtotal + tax
# print the new subtotal
# inside the if create another variable that hold the tip of the customer, in -> how much do you want to tip
# add the tip to the subtotal below 
# print the overall pay



def main():             # i put a loop to repeat the process whatever i want
    size = str(input("What size are you thinking about ordering: enter small, medium, large or extralarge? ---> ")) #this is the variable for the size and his input. medium large
    size_inches = int(input("What size is the pizza in inches? --> ")) # variable for the pizza size in inches and his input
    menu_price = float(input("What is the menu price? --> $ ")) # variable for the menu price and his input that is a float 
    pizza_discount = int(input("How many pizzas do you have to order, at a minimum, to get a discount? --> "))  #variable for the minimum of pizzas to get a discount and his input 
    pizza_quantity = int(input("How many {size medium or large} pizza(s) are you ordering? --> ")) # the number of pizzas you want to order

    if pizza_quantity>pizza_discount: # conditional branch for the condition if the quantity of pizzas is greather than the minimum of pizzas to order
        new_price = float(input("What is the new discounted price per pizza? --> $  ")) # then inside create a new variable that holds the new discounted price
        radius = size_inches / 2 # radius formula 
        area_pizza = 3.14 * radius * radius # area of the circle formula
        price_perinch = menu_price / area_pizza # calculating the price per square inch using the menu price
        price = menu_price * pizza_quantity  # calculating the whole price using the menu price * the quantity
        if size == "medium" or size=="large" or size == "small" or size == "extralarge": # another conditional branch using the size
            price_perinch = new_price / area_pizza # calculate the price per inch using the new discounted price
            price_per_square = menu_price / area_pizza # calculate the price per inch using the menu price
            subtotal = new_price * pizza_quantity # calculate the subtotal with the discounted price
            savings = price - subtotal #calculate the saving menu price - discounted price
            #print the results
            print(f"You want to order {pizza_quantity} {size} {size_inches} inch pizzas. This a ${price_perinch:.2f} per square inch value at the discounted price vs ${price_per_square:.2f}  per square inch at the menu price.")
            print(f"The subtotal is ${subtotal:.2f} to order {pizza_quantity} {size} {size_inches} inch pizzas. This a ${price_per_square:.2f}  per square inch at the menu price.")
            print(f"The subtotal is $ {subtotal:.2f} and you save ${savings:.2f}")

        

    elif pizza_quantity < pizza_discount: # conditional branch if the pizza quantity is less than the minimum of pizzas to get a discount
        radius = size_inches / 2 # radius formula
        area_pizza = 3.14 * radius * radius # area of the cirle formula
        price_perinch = menu_price / area_pizza # calculating the price per square inch using the mnu price
        price = menu_price * pizza_quantity # calculating the whole price using the menu price * the quantity
        if size =="medium" or size =="large" or size == "small" or size == "extralarge": # another conditional branch using the size
            price_per_square = menu_price / area_pizza # calculate the price per inch using the menu price
            subtotal = menu_price * pizza_quantity # calculating the subtotal using the menu price because the quantity of pizzas is not greater than the minimun to get a discount
            #print the results
            print(f"You want to order {pizza_quantity} {size} {size_inches} inch pizzas. This a $ {price_per_square:.2f} per square inch at the menu price.")
            print(f"The subtotal is ${subtotal:.2f}")


    elif pizza_discount == pizza_quantity and size =="large" or size =="extralarge": # out of that if, we open a new elif, elif the minimum of pizzas to get a discount is equal to the quantity of pizzas and the size is large, assuming in every store is one large pizza minimum to get discount
        radius = size_inches / 2 # radius formula
        area_pizza = 3.14 * radius * radius # area of the circle formula
        price_perinch = menu_price / area_pizza # calculating the price per inch using the menu price
        price = menu_price * pizza_quantity # calculating the whole price using the menu price * the quantity
        price_per_square = menu_price / area_pizza # calculating  the price per inch using the menu price
        subtotal = menu_price * pizza_quantity # calculating the subtotal using the menu price because the quantity of pizzas is not greater than the minimum to get a discount
        #print the results
        print(f"You want to order {pizza_quantity} {size} {size_inches} inch pizzas. This a $ {price_per_square:.2f} per square inch at the menu price.")
        print(f"The subtotal is ${subtotal:.2f}")


    elif pizza_quantity == pizza_discount: # conditional branch elif that the quantity of pizzas is equal as the minimum of pizzas to get a discount
        new_price = float(input("What is the new discounted price per pizza? --> $  ")) # then inside create a new variable that holds the new discounted price
        radius = size_inches / 2 # radius formula
        area_pizza = 3.14 * radius * radius # area of the circle formula
        price_perinch = menu_price / area_pizza # calculating the price per inch using the menu price
        price = menu_price * pizza_quantity # calculating the whole price with the menu price
        if size =="medium" or size == "large" or size == "small" or size == "extralarge": # another conditional branch with the size medium or large
            price_perinch = new_price / area_pizza # calculating the price per inch using the new discounted price
            price_per_square = menu_price / area_pizza # calculating the price per inch using the menu price
            subtotal = new_price * pizza_quantity # calculating the subtotal using the discounted price
            savings = price - subtotal  # calculate the saving menu price - discounted price
            # print the results
            print(f"You want to order {pizza_quantity} {size} {size_inches} inch pizzas. This a ${price_perinch:.2f} per square inch value at the discounted price vs ${price_per_square:.2f}  per square inch at the menu price.")
            print(f"The subtotal is $ {subtotal:.2f} and you save ${savings:.2f}")

        
    delivery_option = str(input("Delivery or Pickup? Enter X for delivery, Y for pickup --> ")) # create a variable that holds a input of the delivery option, pick up or delivery. in -> delivery option
    if delivery_option == "X": # if the delivery option is delivery
        delivery_fee = 5.49 # variable that holds the delivery fee
        new_subtotal = subtotal + delivery_fee # calculating the new subtotal adding the delivery fee
        #print the results
        print(f"You want the pizza delivered and the $5.49 delivery fee has been added. Your new subtotal is ${new_subtotal:.2f}")
    elif delivery_option == "Y": # if the delivery option is Pick up
        pickup_discount = -2.00 # variable that holds the 2 dollars discount
        new_subtotal = subtotal + pickup_discount # calculating the new subtotal adding the discount
        # print the results
        print(f"You choose the pick up option and the $2.00 discount has been added. Your new subtotal is ${new_subtotal:.2f}") 
    student = str(input("Are you a student? enter X for yes, Y for no ---> ")) #create a variable that holds the input of the student option. in -> student? yes or no
    if student == "X" or student =="x": # if the customer is a student then he get a discount
        student_discount = 10 # variable that holds the student discount
        discount = new_subtotal / student_discount # calculating the discount
        # print the results
        print(f"Because you are a student, a 10.00% discount of ${discount:.2f} has been deducted from the subtotal")
        student_subtotal = new_subtotal - discount # calculating the new subtotal
        # print the results
        print(f"Your new subtotal is now ${student_subtotal:.2f}")
        tax = 0.1025 # variable that holds the percent of tax
        tax_after = student_subtotal * tax # calculate the tax of the subtotal
        subtotal_tax = student_subtotal + tax_after # calculating the new subtotal with the tax
        # print the results
        print(f"The local tax rate of 10.25% has been added to your subtotal.  You were charged ${tax_after:.2f} in taxes.  Your new after tax subtotal is now ${subtotal_tax:.2f}")
        tip_amount = float(input("How much do you want to tip? --> $")) # new variable that holds how much tip the client wants to tip
        grand_total = tip_amount + subtotal_tax # calculating the final price of the order
        # print the results
        print(f"Your tip of ${tip_amount} was added to your subtotal of ${subtotal_tax:.2f}. The grand total due is now ${grand_total:.2f}")
    if student == "Y" or student =="y": # if student is NO
        student_discount = 0 # do not receive any discount
        tax = 0.1025 # variable that holds the percent of tax
        tax_after = new_subtotal * tax # calculating the tax of the subtotal
        subtotal_tax = student_subtotal + tax_after # calculating the new subtotal with the tax
        # print the results
        print(f"The local tax rate of 10.25% has been added to your subtotal.  You were charged ${tax_after:.2f} in taxes.  Your new after tax subtotal is now ${subtotal_tax:.2f}")
        tip_amount = float(input("How much do you want to tip? --> $")) # variable that holds how much tip the client wants to tip
        grand_total = tip_amount + subtotal_tax #  calculating the final price of the order
        # print the results
        print(f"Your tip of ${tip_amount} was added to your subtotal of $. The grand total due is now ${grand_total:.2f}")

    
    
    repeat = input("Would you like to repeat the process? Enter Yes or No: ") # variable that holds the option to repeat the whole process
    if repeat == "Yes" or repeat =="yes": # if the users wants to repeat
        main() # go to the beginning
    else: # if the user do not want to repeat 
        print("Thank you") # print the words that let the user know that the program is close
        exit() # close the program
main()
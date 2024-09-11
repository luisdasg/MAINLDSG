"""Pseudocode: 
tax = 0.0
total = 0.0                                                                   
income = total

input= employee name
input= number of hours worked
input= pay rate per hour

if less than 40 hrs
    normalhrs = 40
    overtime = 0
else 
    normal = 40
    overtime = overtimehrs - 40

if more than 40 hrs
    otpay = pay * 1.5
    overtime = (normalhrs -40) * otpay

else
    overtime = 0

print(all the results)


"""
tax= 0.0         #Set the tax variable as 0.0 because is a odd number#
total = 0.0      #Set the total variable as 0.0 #
income = total   # Income, is the total pay after the taxes#
name=input("Enter the name of the employee: ")       #Requesting the name of the employee#
hrs=float(input("Enter the hours worked: "))         #Requesting the hours worked#
pay= float(input("Enter the pay rate per hour: "))   #Requesting the pay rate per hour for the employee#

if hrs<40:                                         #Setting a conditional branch to make a condition if the hours worked are less than
    normalhrs= hrs                                 #40hrs so the employee do not received overtime pay
    overtimehrs= 0
else:
    normalhrs= 40                                  #If are more than 40 hours setting the variable for the othours
    overtimehrs= hrs - 40
if hrs >40:
    overtimepay= 1.5 * pay                         #setting the own conditional for the overtime hours, calculating the pay rate per hour
    overtime = overtimehrs * overtimepay           # plus the overtime hours
else:
    overtime = 0  
    overtimepay = 0                                #if that not happen the overtime is juts 0
normalpay = normalhrs * pay                      #setting the variable to calculate the normal hrs( NO overtime) and the normal pay rate      
total= overtime + normalpay                      # setting the variable for the gross pay wich adds together the value of the overtime money and the normal money
income = total / 10                             #setting the variable to calculate the taxes
incometotal = total - income                     #calculate the  net pay of the total pay with taxes
print("Employee Name: " ,name)
print("Hours Worked: " ,hrs)
print("Gross pay: ", total)
print("Taxes paid: " ,income)
print("Net pay: " ,incometotal)
print(name,"you worked", hrs, "this week. You earned $",pay," per hour for the first 40 hours. You work overtime for",overtimehrs," hours and you earned",overtimepay,"per hour for your overtime hours. You earned a gross pay of $",total,".  You paid $",income,"in taxes. Your net pay is $",incometotal)
print("Calculator made by Luis, B)")
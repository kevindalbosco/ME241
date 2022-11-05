#Name: Kevin Raphael Dalbosco Dal Forno
#ME241

#Homework #2

#Problem #1:

import math
import os

#defining variables for equation and operation.
s=0
i=0
term=1

#operation to solve the summation part of equation.
while term>1e-15:
    term=(math.factorial(4*i)*(1103+26390*i))/((math.factorial(i))**4*396**(4*i)) #portion of equation inside sigma.
    s=s+term
    i=i+1


c=9801/(2*2**.5*s)  #inverse of the remaining equation (outside sigma) multiplied by the inverse of the value obtained from the summation
print('\nProblem #1:\n')
print('Value of pi: {:.15f}'.format(math.pi))   #printing actual pi value up to 15 digits.
print('Calculated value of pi: {:.15f}\n'.format(c),'\n')  #printing calculated value of pi.


#Problem #2:

print('Problem #2:\n')

#Defining input commands for user to input # amount of coins for each separate coin.
q_cents = int(input("Enter the amount of cents: "))
q_nickels = int(input("Enter the amount of nickels: "))
q_dimes = int(input("Enter the amount of dimes: "))
q_quarter = int(input("Enter the amount of quarters: "))

#Equation to sum up the values of each individual input.
ValueDollar = (q_cents*0.01) + (q_nickels*0.05) + (q_dimes*0.10) + (q_quarter*0.25)

#Print function for the total amount in dollars.
print("\nYour coins add up to : ${:.2f}".format(ValueDollar),"\n")

#Problem #3:

print('Problem #3:\n') 

#Input commands of type float for user to insert what is required.
kwCost = float(input("Enter the kW/h cost in cents: "))
watts = float(input("Enter the wattage of your appliance in Watts: "))
time = float(input("Enter the amount of hours the applience is used daily: "))

#Calculation to determine total cost over a period of 10 years from user inputs.
totalCost = (((watts/1000)*time)*kwCost)*30

#Formatted print function of the cost in dollars with a precision of 2 decimal places.
print("The appliance in 10 years will have a total energy cost of: ${:.2f}".format(totalCost),"\n")

#Problem #4:

import time

print('Problem #4:\n') 

#Time function that recalls time in seconds since epoch
currentTime = time.time()

#Determining the amount of seconds for each time period 
yearSec = 31557600
weekSec = 604800
daySec = 60*60*24
hourSec = 60*60
minSec = 60

#Divmod functions that are used to determine the highest integer value followed by the remainder, which is then used in the next divmod function for the nex time period and so on.
year = (divmod(currentTime,yearSec))
week = divmod(year[1],weekSec)
day = divmod(week[1], daySec)
hour = divmod(day[1],hourSec)
min = divmod(hour[1],minSec)
sec = int(min[1])

#Print function to output each time period separately 
print("Time since midnight 1st January 1970 is: {:.0f} years, {:.0f} weeks, {:.0f} days, {:.0f} hours, {:.0f} minutes, and {} seconds.".format(year[0], week[0], day[0], hour[0], min[0], sec),"\n")

os.system("pause")
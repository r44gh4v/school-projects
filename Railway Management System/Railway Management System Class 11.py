"""
11 Sci A Computer Group Project on
RAILWAY MANAGEMENT SYSTEM
Group members:
Raaghav Rathi (contributor)
Savyasachi Sonar (contributor)
Dia Garg
Anish Kumar
Sara Agarwal
Anubhav Agarwal
"""

route_name = [None, "SILIGURI - DALGAON", "SILIGURI - KISHANGANJ", "SILIGURI - MALDA", "SILIGURI - ALIPUR DWAR", "SILIGURI - HOWRAH"]
route_price_list = [None, 70, 80, 90, 100, 110]
#route_price var in code

num_ppl=0
age_price = 0
age_price_ppl_list=[None, ]

coach_name = [None, "General", "Sleeper", "AC 3-Tier", "AC 2-Tier", "AC 1-Tier"]
coach_price_list = [None, 30, 40, 60, 70, 80]
#total coach_price var in code

food_name = [None, "Veg", "Non-Veg"]
food_price_list = [None, 70, 90]



print("----------------------------------------")
print("Welcome to Railway Ticket Booking System")
print("----------------------------------------")
print ("\n")



print("CHOOSE A ROUTE")
print("1)", route_name[1], "- Rs", route_price_list[1])
print("2)", route_name[2], "- Rs", route_price_list[2])
print("3)", route_name[3], "- Rs", route_price_list[3])
print("4)", route_name[4], "- Rs", route_price_list[4])
print("5)", route_name[5], "- Rs", route_price_list[5])
print ("\n")
route = int(input("Enter Route Number(1-5): "))
route_price = route_price_list[route] #route total price



ppl_dict = {}
while True:
    print ("\n")
    person = str(input("Enter Name: "))
    age = int(input("Enter Age: "))
    ppl_dict[person] = age
    num_ppl += 1
    if input("Add another person?(y/n): ") == "n":
        break

for keys, value in ppl_dict.items():
    if(value <= 5):
        age_price_ppl_list.append(20) #half price for people below 5 years
    else:
        age_price_ppl_list.append(40) #price for people above 5 years
for k in range(1, num_ppl + 1):
    age_price += age_price_ppl_list[k]
print ("\n")



print("CHOOSE CLASS")
print("1)", coach_name[1], "- Rs",coach_price_list[1], "/person")
print("2)", coach_name[2], "- Rs",coach_price_list[2], "/person")
print("3)", coach_name[3], "- Rs",coach_price_list[3], "/person")
print("4)", coach_name[4], "- Rs",coach_price_list[4], "/person")
print("5)", coach_name[5], "- Rs",coach_price_list[5], "/person")
print ("\n")
coach = int(input("Enter Class Number(1-5): "))
coach_price = coach_price_list[coach] * num_ppl #coach total price
print ("\n")



food=input("Would you like to add Food?(y/n): ")
print ("\n")
if food == "y":
    print("CHOOSE")
    print("1)", food_name[1], "- Rs",food_price_list[1], "/person")
    print("2)", food_name[2], "- Rs",food_price_list[2], "/person")
    print ("\n")
    food = int(input("Enter Food Type Number(1-2): "))
    food_price = food_price_list[food] * num_ppl
    print ("\n")



print("Generating Bill...")
print ("\n")

#BILLING
print("---------BILL---------")
print ("\n")
print("PASSENGERS")

i=1
for keys, value in ppl_dict.items():
    print(keys, "-", str(value), "years - Rs", age_price_ppl_list[i])
    i += 1
print ("\n")

print("Route: ", route_name[route], "-", "Rs", route_price)
print("Coach: ", coach_name[coach], "-", coach_price_list[coach], "X", num_ppl, "= Rs", coach_price)
print("Food: ", food_name[food], "-", food_price_list[food], "X", num_ppl, "= Rs", food_price)

total_bill = age_price + route_price + coach_price + food_price
print("TOTAL: Rs",total_bill)
print ("\n")

print("Thank You for using our system!")
print ("\n")

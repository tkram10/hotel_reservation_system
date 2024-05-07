# importing necessary classes
import customer
import hotel
import reservation
import customer_interface
import admin

# creating objects of all the classes
cust = customer.Customer()
hotel = hotel.Hotel()
res = reservation.Reservation()
ci = customer_interface.CustomerInterface()
ai = admin.AdminInterface()


# greeting message
print("Hi, Welcome to tripadvisor.com!")

# asking user if they are an admin or not
inp = input("Are you an Admin(Y/N): ")

# condition to check if user is an admin
if inp.lower() == "y":
    ai.admin_interface()   # calls the admin method of the AdminInterface class
# condition to check if user is a customer
elif inp.lower() == "n":
    ci.customer_interface()  # calls the customer_interface method of the CustomerInterface class
# condition for invalid input
else:
    print("Invalid input.")
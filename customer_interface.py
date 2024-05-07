import customer
import hotel
import reservation

# creating objects of all the classes
cust = customer.Customer()
hotel = hotel.Hotel()
res = reservation.Reservation()

class CustomerInterface:
    def customer_interface(self):
        print("Hello, Customer!")
        print("To Make a reservation,Please enter 1 \n To Cancel a reservation,please enter 2")
        inp = input("Enter your choice: ")
        if inp == "1":
            print("(ID, Hotel_Name, Room_Type, Price )")
            hotel.fetchById()
            select_hotel = input("Select your desired hotel(Enter the hotel ID): ")
            start_date = input("Enter the start date(yyyy-MM-dd): ")
            end_date = input("Enter the end date(yyyy-MM-dd): ")
            print("Enter your details:")
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            phone = input("Enter your phone number: ")
            email = input("Enter your email: ")
            res.make_reservation(email, select_hotel, start_date, end_date)
            cust.add(first_name, last_name, phone, email)
            res.fetch_reservation(email)
        elif inp == "2":
            reservation_id = input("Enter the reservation id: ")
            res.cancel_reservation(reservation_id)
        else:
            print("Invalid input.")
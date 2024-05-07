import customer
import hotel
import reservation

# creating objects of all the classes
cust = customer.Customer()
hotel = hotel.Hotel()
res = reservation.Reservation()

class AdminInterface:

    def admin_interface(self):
        id = input("Enter your ID: ")
        if id == "ATA12" or id == "ATA13" or id == "ATA14":
            print("what operation do you want to perform:")
            print("1. Add a Hotel\n2. Update a Hotel\n3. Delete a Hotel\n4. View Hotels\n5. View customers\n6. Delete customer")
            op = input("Enter the operation: ")
            if op == "1":
                hotel_name = input("Enter hotel name: ")
                room_id = input("Enter room id: ")
                room_type = input("Enter room type: ")
                no_of_rooms = input("Enter no of rooms: ")
                is_booked = input("Is the room available to book(Enter 1 - Yes / 0 - No): ")
                price = input("Enter price of the room: ")
                hotel.add(hotel_name, room_id, room_type, no_of_rooms, is_booked, price)
            elif op == "2":
                hotel_id = input("Enter the hotel id:")
                hotel_name = input("Enter hotel name: ")
                room_id = input("Enter room id: ")
                room_type = input("Enter room type: ")
                no_of_rooms = input("Enter no of rooms: ")
                is_booked = input("Is the room available to book(Enter 1 - Yes / 0 - No): ")
                price = input("Enter price of the room: ")
                hotel.update(hotel_id, hotel_name, room_id, room_type, no_of_rooms, is_booked, price)
            elif op == "3":
                hotel_id_delete = input("Enter the hotel id to be deleted: ")
                hotel.delete(hotel_id_delete)
            elif op == "4":
                view_hotels = input("press enter to view all hotel details: ")
                print("(id, hotel_name, room_type, price)")
                hotel.fetchById(view_hotels)
            elif op == "5":
                view_customer = input("press enter to view all customer details: ")
                print("(customer_id, first_name, last_name, phone_number, email)")
                cust.fetch(view_customer)
            elif op == "6":
                customer_id = input("Enter the id of the customer which needs to be deleted: ")
                cust.delete(customer_id)
            else:
                print("Invalid input.")
        else:
            print("Invalid ID, Please enter valid ID.")
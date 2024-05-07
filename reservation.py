import sqlite3
from datetime import datetime
from db_base import DBbase
import csv

class Reservation(DBbase):
    def __init__(self):
        super().__init__("Hotel_Reservation.sqlite")

    def make_reservation(self, email, hotel_id, start_date, end_date):
        try:
            # Fetch hotel details for given hotel_id
            sql = f"select hotel_name, room_type, price, no_of_rooms from hotels where id = {hotel_id}"
            self.get_cursor.execute(sql)  # Execute SQL query
            result = self.get_cursor.fetchone()  # Fetch one row
            hotel_name, room_type, price, numberRooms = result[0], result[1], result[2], result[3]  # Unpack result into variables

            start_date = datetime.strptime(start_date, '%Y-%m-%d')  # Convert start_date string to datetime object
            end_date = datetime.strptime(end_date, '%Y-%m-%d')  # Convert end_date string to datetime object
            duration = (end_date - start_date).days  # Calculate duration in days
            amount = price * duration  # Calculate total amount

            numberRooms -= 1  # Decrease number of available rooms
            if numberRooms == 0:
                is_booked = 0  # Set is_booked to 0 if no rooms are available
            else:
                is_booked = 1  # Set is_booked to 1 if rooms are available


            sql = f"Update hotels set no_of_rooms = {numberRooms}, is_booked = {is_booked} where id = '{hotel_id}'"
            self.get_cursor.execute(sql)
            self.get_connection.commit()


            sql = f"INSERT INTO reservation (email, hotel_id, hotel_name, room_type, start_date, end_date, amount) VALUES ('{email}', {hotel_id}, '{hotel_name}', '{room_type}', '{start_date}', '{end_date}', {amount})"
            self.get_cursor.execute(sql)
            self.get_connection.commit()

            print("Your reservation has been made succesfully.")
            return 1

        except sqlite3.Error as e:
            print(f"Error: {e}")

    # Function to cancel a reservation based on reservation ID
    def cancel_reservation(self, reservation_id):
        try:

            sql = f"SELECT hotel_id FROM reservation WHERE id = {reservation_id}"
            self.get_cursor.execute(sql)

            result = self.get_cursor.fetchone()
            if result is not None and len(result) > 0:
                hotel_id = result[0]

            else:
                print("Error: No reservation found with the specified ID.")
                return
            sql = f"Update hotels set no_of_rooms = no_of_rooms + 1, is_booked = 1 where id = {hotel_id}"
            self.get_cursor.execute(sql)
            self.get_connection.commit()

            sql = f"DELETE FROM reservation WHERE id = {reservation_id}"
            self.get_cursor.execute(sql)
            self.get_connection.commit()

            print("Reservation successfully cancelled.")

        except sqlite3.Error as e:
            print(f"Error: {e}")

    # Function to fetch reservation details based on customer email
    def fetch_reservation(self, email):
        try:
            sql = f"select * from reservation where email = '{email}'"
            self.get_cursor.execute(sql)
            rows = self.get_cursor.fetchall()
            if rows:
                print("Your reservation details are:")
                for row in rows:
                    id, email, hotel_id, hotel_name, room_type, start_date, end_date, amount = row  # Get the values from the result
                    print(f"Reservation ID: {id}")
                    print(f"Email: {email}")
                    print(f"Hotel ID: {hotel_id}")
                    print(f"Hotel Name : {hotel_name}")
                    print(f"Room type: {room_type}")
                    print(f"Start Date: {start_date}")
                    print(f"End Date: {end_date}")
                    print(f"Amount: {amount}")
                    print()
            else:
                print(f"No reservation found for {email}.")

        except sqlite3.Error as e:
            print(f"Error: {e}")

    def reset_database(self):
        try:
            sql = "DROP TABLE IF EXISTS reservation"
            self.get_cursor.execute(sql)
            # Recreate the reservation table with the initial schema
            sql = "CREATE TABLE reservation (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, email TEXT NOT NULL, hotel_id INTEGER NOT NULL, hotel_name TEXT NOT NULL, room_type TEXT NOT NULL, start_date TEXT NOT NULL, end_date TEXT NOT NULL, amount REAL NOT NULL, FOREIGN KEY (email) REFERENCES customers(email), FOREIGN KEY (hotel_id) REFERENCES hotel(id))"
            self.get_cursor.execute(sql)
            self.get_connection.commit()

            # Read data from the reservation.csv file and insert it into the newly created reservation table
            with open('reservation.csv') as csvfile:
                csvreader = csv.reader(csvfile)
                next(csvreader)  # skip header row
                for row in csvreader:
                    email = row[0]
                    hotel_id = int(row[1])
                    hotel_name = row[2]
                    room_type = row[3]
                    start_date = row[4]
                    end_date = row[5]
                    amount = float(row[6])
                    sql = f"INSERT INTO reservation (email, hotel_id, hotel_name, room_type, start_date, end_date, amount) VALUES ('{email}', {hotel_id}, '{hotel_name}', '{room_type}', '{start_date}', '{end_date}', {amount})"
                    self.get_cursor.execute(sql)
                    self.get_connection.commit()

        except sqlite3.Error as e:
            print(f"Error: {e}")

# reservation = Reservation()
# reservation.reset_database()
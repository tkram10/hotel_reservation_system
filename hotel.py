# Importing the modules
import db_base as db
import sqlite3
import csv

# Defining class
class Hotel(db.DBbase):
    def __init__(self):
        super().__init__("Hotel_Reservation.sqlite")

    # Method to add details to the hotels table
    def add(self, hotel_name, room_id, room_type, no_of_rooms, is_booked, price):
        try:
            sql = f"INSERT INTO hotels (hotel_name, room_id, room_type, no_of_rooms, is_booked, price) VALUES ('{hotel_name}', '{room_id}', '{room_type}', {no_of_rooms}, {is_booked}, {price})"
            self.get_cursor.execute(sql)
            self.get_connection.commit()
            print("Details added successfully.")
        except sqlite3.IntegrityError:
            print(f"Error: Hotel with this id '{room_id}' and '{hotel_name}' already exists.")

    # Method to update details in the hotels table
    def update(self, hotel_id, hotel_name=None, room_id=None, room_type=None, no_of_rooms=None, is_booked=None,
               price=None):
        try:
            sql = "UPDATE hotels SET"
            if hotel_name is not None and hotel_name != '':
                sql += f" hotel_name = '{hotel_name}',"
            if room_id is not None and room_id != '':
                sql += f" room_id = '{room_id}',"
            if room_type is not None and room_type != '':
                sql += f" room_type = '{room_type}',"
            if no_of_rooms is not None and no_of_rooms != '':
                sql += f" no_of_rooms = {no_of_rooms},"
            if is_booked is not None and is_booked != '':
                sql += f" is_booked = {is_booked},"
            if price is not None and price != '':
                sql += f" price = {price},"
            # Remove the last comma
            sql = sql[:-1]
            sql += f" WHERE id = {hotel_id}"
            self.get_cursor.execute(sql)
            self.get_connection.commit()
        except sqlite3.IntegrityError:
            print(f"Error: Hotel with this id '{room_id}' and '{hotel_name}' already exists.")

    # Method to delete details from the hotels table
    def delete(self, hotel_id):
        try:
            sql = f"DELETE FROM hotels WHERE id = {hotel_id}"
            self.get_cursor.execute(sql)
            self.get_connection.commit()
        except sqlite3.IntegrityError:
            print(f"Error: Could not delete hotel with id '{hotel_id}'.")

    def fetch(self, hotel_id=None):
        try:
            if hotel_id is None:
                sql = "SELECT * FROM hotels"
            else:
                sql = f"SELECT * FROM hotels WHERE id = {hotel_id}"
            self.get_cursor.execute(sql)
            rows = self.get_cursor.fetchall()
            for row in rows:
                print(row)
            return rows
        except sqlite3.Error as e:
            print(f"Error: {e}")

    def fetchById(self, hotel_id=None):
        try:
            if ValueError:
                sql = f"SELECT id, hotel_name, room_type, price FROM hotels where is_booked = 1"
            else:
                sql = f"SELECT id, hotel_name, room_type, price FROM hotels WHERE id = {hotel_id} and is_booked = 1"
            self.get_cursor.execute(sql)
            rows = self.get_cursor.fetchall()
            for row in rows:
                print(row)
            return rows
        except sqlite3.Error as e:
            print(f"Error: {e}")

    def reset_database(self):
        try:
            sql = "DROP TABLE IF EXISTS hotels"  # drop table if it already exists
            self.get_cursor.execute(sql)
            sql = "CREATE TABLE hotels (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, hotel_name TEXT NOT NULL, room_id TEXT NOT NULL, room_type TEXT NOT NULL, no_of_rooms INTEGER NOT NULL, is_booked INTEGER NOT NULL, price INTEGER NOT NULL)"  # create new hotels table with columns
            self.get_cursor.execute(sql)

            with open('hotel.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)  # skip header row
                for row in reader:
                    hotel_name, room_id, room_type, no_of_rooms, is_booked, price = row
                    sql = f"INSERT INTO hotels (hotel_name, room_id, room_type, no_of_rooms, is_booked, price) VALUES ('{hotel_name}', '{room_id}', '{room_type}', {no_of_rooms}, {is_booked}, {price})"  # insert row data into hotels table
                    self.get_cursor.execute(sql)

            self.get_connection.commit()

        except sqlite3.Error as e:
            print(f"Error: {e}")
# hotel = Hotel()
# hotel.reset_database()
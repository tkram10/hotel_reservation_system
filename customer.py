import db_base as db  # importing the db_base module as db
import sqlite3  # importing the sqlite3 module for database operations
import csv  # importing the csv module for reading csv files

class Customer(db.DBbase):

    def __init__(self):
        super().__init__("Hotel_Reservation.sqlite")

    def add(self, first_name, last_name, phone_number, email):
        try:
            sql = f"INSERT INTO customers (first_name, last_name, phone_number, email) VALUES ('{first_name}', '{last_name}', '{phone_number}', '{email}')"
            self.get_cursor.execute(sql)
            self.get_connection.commit()
        except sqlite3.IntegrityError:  # handling the IntegrityError exception
            print(f"Error: Customer with email '{email}' already exists.")

    def update(self, customer_id, first_name=None, last_name=None, phone_number=None, email=None):
        try:
            sql = "UPDATE customers SET"
            if first_name is not None:
                sql += f" first_name = '{first_name}',"
            if last_name is not None:
                sql += f" last_name = '{last_name}',"
            if phone_number is not None:
                sql += f" phone_number = '{phone_number}',"
            if email is not None:
                sql += f" email = '{email}',"
            # remove the last comma
            sql = sql[:-1]
            sql += f" WHERE id = {customer_id}"
            self.get_cursor.execute(sql)
            self.get_connection.commit()
        except sqlite3.IntegrityError:  # handling the IntegrityError exception
            print(f"Error: Customer with email '{email}' already exists.")

    def delete(self, customer_id):
        try:
            # Construct the SQL query to delete a customer record using customer_id
            sql = f"DELETE FROM customers WHERE id = {customer_id}"
            self.get_cursor.execute(sql)
            self.get_connection.commit()
            print("Successfully deleted")
        except sqlite3.IntegrityError:  # handling the IntegrityError exception
            print(f"Error: Could not delete customer with id '{customer_id}'.")

    def fetch(self, customer_id=None):
        try:
            # Construct the SQL query to display the details of the customer using customer_id
            if ValueError:
                sql = "SELECT * FROM customers"
            else:
                sql = f"SELECT * FROM customers WHERE id = {customer_id}"
            self.get_cursor.execute(sql)
            rows = self.get_cursor.fetchall()
            for row in rows:
                print(row)
            return rows
        except sqlite3.Error as e:  # handling the SQLite exception
            print(f"Error: {e}")


    def reset_database(self):
        try:
            # Drop and recreate the customers table
            sql = "DROP TABLE IF EXISTS customers"
            self.get_cursor.execute(sql)
            sql = "CREATE TABLE customers (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, first_name TEXT NOT NULL, last_name TEXT NOT NULL, phone_number TEXT, email TEXT NOT NULL UNIQUE)"
            self.get_cursor.execute(sql)

            # Read data from customer.csv and insert into the customers table
            with open('customer.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    sql = f"INSERT INTO customers (first_name, last_name, phone_number, email) VALUES ('{row['first_name']}', '{row['last_name']}', '{row['phone_number']}', '{row['email']}')"
                    self.get_cursor.execute(sql)

            self.get_connection.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")

# customer = Customer()
# customer.reset_database()

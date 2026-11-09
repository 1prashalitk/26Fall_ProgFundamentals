
# sensor_app_template.py - runs ON THE PC (regular Python 3, e.g. VS Code or IDLE)
# Template: talks to the board over USB serial and prints the readings.
# Rename a copy of this file (e.g. sensor_app.py) and extend it for the assignment.
#
# Setup: pip install pyserial
# IMPORTANT: close Thonny before running this, only one program can use the port.
import time
import serial # from the pyserial package
from datetime import datetime
PORT = "/dev/ttyACM0" # <-- CHANGE to your board's port (see Device Manager)
BAUD = 115200
def ask_board(ser, command):
    """Send a one-letter command to the board and return the number it replies with."""
    ser.reset_input_buffer() # discard any stale data
    ser.write((command + "\n").encode()) # send command + newline
    # Read lines until one starts with DATA (ignores any boot messages)
    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if line == "":
            raise TimeoutError("No reply from board")
        if line.startswith("DATA,"):
            return float(line.split(",")[2])

    
# TODO 1: write the DatabaseManager class here (sqlite3).
import sqlite3 # importing the sqlite3 to make a database.

class DatabaseManager: #created a class called Databasemanager
    def __init__(self): 
        self.conn = sqlite3.connect("sensor_data.db")
        self.cur = self.conn.cursor()

    def create_table(self): #creating table named sensroe_data
        self.cur.execute(""" 
            CREATE TABLE IF NOT EXISTS  sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT ,
            sensor_type TEXT,
            sensor_reading_value REAL
            )
        """)
        self.conn.commit()

    def insert_new_data(self, sensor_type, sensor_reading_value):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # i researched how to put in accurate timestamp

        self.cur.execute(
            "INSERT INTO sensor_data (timestamp,sensor_type,sensor_reading_value) VALUES (?,?,?)",
            (timestamp,sensor_type, sensor_reading_value,),
        ) # inserting the new data into the database

        self.conn.commit()

    def show_all_data(self):
        self.cur.execute("SELECT * FROM sensor_data")
        return self.cur.fetchall() #returns all the data in the database with .fetchall() method

    def close_database(self):
        """
        Close the database connection.
        """
        self.conn.close()


# TODO 2: write the temperature function here (ask the board with "T",
# display the value, and log it to the database).
    def request_display_log_temperature(self, ser):


        temperature = ask_board(ser, "T") #asking the board for temperature
        print(f"Temperature: {temperature:.1f} C") #rounding the temperature to 1 decimal place and printing it
        self.insert_new_data("Temperature", temperature) #Adding the new temperature value to the database

# TODO 3: write the humidity function here (ask the board with "H",
# display the value, and log it to the database).

    def request_display_log_humidity(self, ser):
        humidity = ask_board(ser, "H") #asking the board for humidity
        print(f"Humidity: {humidity:.1f} %") #rounding the humidity to 1 decimal place and printing it
        self.insert_new_data("Humidity", humidity) #Adding the new humidity value to the database


    
def main():
    # Open the serial port; opening it may reset the board, so wait a moment
    ser = serial.Serial(PORT, BAUD, timeout=3)
    time.sleep(2)
    ser.reset_input_buffer()
    # Demo only: read both sensors once and print them.
    # TODO 4: replace this with the menu and the user-choice loop.
    
    db = DatabaseManager()
    db.create_table()

    while True:

            print("Please choose from the following options:")
            print("T - Temperature")
            print("H - Humidity")
            print("0 - Both")
            print("V - View Log History")

            User_input = input("Enter choice: ").strip().upper()

            if User_input == "T":
                db.request_display_log_temperature(ser)

            elif User_input == "H":
                db.request_display_log_humidity(ser)

            elif User_input == "0":
                db.request_display_log_temperature(ser)
                db.request_display_log_humidity(ser)

            elif User_input == "V":
                records = db.show_all_data()
                for record in records:
                    print(record)

            else:
                print("Invalid Please enter T, H, 0, or V.")
    db.close_database()
    ser.close()
if __name__ == "__main__":
    main()


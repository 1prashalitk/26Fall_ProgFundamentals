import sqlite3
conn = sqlite3.connect("StudentRecords.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS StudentRecords")


cur.execute("""
CREATE TABLE StudentRecords (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  major TEXT
);

""")

StudentRecords= [ 
  (1, "Prashali", 18, "Computer Science Cyber Security"),
  (2, "Kayla", 22, "Data Science"),
  (3, "Sam", 20, "Computer Science"),
  (4, "Jose", 20, "Computer Science Cyber Security"),
  (5, "Sana", 18, "Data Science")

]

cur.executemany("INSERT INTO StudentRecords VALUES (?, ?, ?, ?)", StudentRecords)

print("StudentRecords without ID")
for row in cur.execute("SELECT name, age, major FROM StudentRecords"):
    print(row)

while True:
    user_input= input("Do you want to add a New Student? (yes/no): ").lower()
    if user_input in ("yes","no"):
      break
    print("Please Enter yes or no: ")

while True:

    add_name= input("Enter New student Name: ")
    if add_name:
        break
    print("Name cannot be empty")
    add_name= input("Enter New Student Name: ")

while True:
    add_age= int(input("Enter New Student Age: "))
    break
    
while True:
    add_major= input("Enter New Student major: ")
    if add_major:
        break
    print("Major cannot be empty")
    add_major= input("Enter New Student major: ")

    break


    print("Please Enter yes or no: ")


new_id= "6"

cur.execute("INSERT INTO StudentRecords VALUES (?, ?, ?, ?)",new_id, add_name, add_age, add_major)

conn.close()



import sqlite3
conn = sqlite3.connect("library.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS books")

cur.execute("""
CREATE TABLE books(
 id INTEGER PRIMARY KEY,
 title TEXT,
 author TEXT ,
 year INTEGER,                 
 genre TEXT, 
 copies INTEGER,
 ratings REAL
);

""")

cur.execute("""
INSERT INTO books
VALUES (1,  "Lorax",  "Dr. Seuss",  1971,  "picture book", 1000000, 4.35);
""")
books= [
    (2,  "Horton Hears a Who!" ,  "Dr. Seuss" ,  1954,  "fiction" , 600000000, 4.22),
    (3,  "The Treasure of Easter Island" ,  "Geronimo Stilton" ,  2015,  "Adventure Fiction", 180000000, 4.35),
    (4,  "Karate Mouse", "Geronimo Stilton" ,  2005, " Adventure Fiction" , 180000000, 4.2),
    (5,  "The Secret Of Cackelfur Castle", "Geronimo Stilton",  2005, "Mystery" , 190000000, 4.09),
    (6,  "Sideways Stories from Wayside School" , "Louis Sachar" , 1978, "fiction", 15000000, 5),
    (7, "Harry Potter and the Goblet of Fire" , "JK Rowling" , 2000, "fantasy" , 65000000, 4.57),
    (8, "The Hunger Games" , "Suzanne Collins" , 2008, "Young Adult fiction", 100000000, 4.36),
    (9,  "Dog Man" , "Dave Pilkey", 2016, "Graphic Novel", 70000000, 4.8),
    (10, "The Dancing Witch", "Ellen Shire", 1995, "fiction", 35000, None)
]

cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?)", books)

print(" Books and Author  published after 1990") 
for row in cur.execute("SELECT title, author FROM books WHERE year>1990"):
    print(row)

# Print the title of fiction books with more than 2 copies (AND).


print("AND: Fiction books with more than 2 copies")
for row in cur.execute("SELECT title FROM books WHERE genre = 'fiction' AND year >1990"):
    print(row)

#Print the title of books published before 1900 or rated 5 (OR).

print("\nOR: Title of books published before 1900, or rated 5")
for row in cur.execute("SELECT title FROM books WHERE year <= 1900 OR ratings = 5"):
    print(row)

#Print the title of books that are not in the Mystery genre (NOT)

print("\nNOT: books not in Mystery genre")
for row in cur.execute("SELECT title FROM books WHERE NOT genre = 'Mystery'"):
    print(row)


#Print the title of books in either the Science or History genre (IN).

print("\nIN: Books in Science or History genre")
for row in cur.execute("SELECT title FROM books WHERE genre IN ('Science','History')"):
    print(row)

#Ask the user for a letter, then print the authors whose names start with that letter (LIKE). Pass the letter with a ? placeholder.

Letter= input ("ENTER A LETTER: ")

print("\nLIKE: Author’s name starting with the letter " + Letter)
Letter = Letter +"%"
for row in cur.execute("SELECT title FROM books WHERE author LIKE ?", (Letter,)):
    print(row)

#Print the title of books that have no rating (IS NULL).

print("\nIS NULL: Books with no ratings")
for row in cur.execute("SELECT title FROM books WHERE ratings IS NULL"):
    print(row)

conn.close()

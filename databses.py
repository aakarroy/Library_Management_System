import mysql.connector as c
import random

#SQL CONNECTION 
con = c.connect(host='localhost',password="password",user="root",database="user") #USE PASSWORD OF YOUR OWN
cur = con.cursor()

#USER DATABASE
cur.execute("create database if not exists user")
cur.execute("use user")

#LIBRARY TABLE
book = [
    "To Kill a Mockingbird by Harper Lee",
    "1984 by George Orwell",
    "Pride and Prejudice by Jane Austen",
    "The Great Gatsby by F. Scott Fitzgerald",
    "Moby-Dick by Herman Melville",
    "War and Peace by Leo Tolstoy",
    "Jane Eyre by Charlotte Brontë",
    "Wuthering Heights by Emily Brontë",
    "Dune by Frank Herbert",
    "Neuromancer by William Gibson",
    "A Game of Thrones by George R.R. Martin",
    "The Left Hand of Darkness by Ursula K. Le Guin",
    "Snow Crash by Neal Stephenson",
    "The Hitchhiker's Guide to the Galaxy by Douglas Adams",
    "Ender's Game by Orson Scott Card",
    "Good Omens by Neil Gaiman and Terry Pratchett",
    "The Girl with the Dragon Tattoo by Stieg Larsson",
    "Gone Girl by Gillian Flynn",
    "The Da Vinci Code by Dan Brown",
    "And Then There Were None by Agatha Christie",
    "The Silence of the Lambs by Thomas Harris",
    "All the Light We Cannot See by Anthony Doerr",
    "The Book Thief by Markus Zusak",
    "Wolf Hall by Hilary Mantel",
    "The Nightingale by Kristin Hannah",
    "Sapiens: A Brief History of Humankind by Yuval Noah Harari",
    "The Immortal Life of Henrietta Lacks by Rebecca Skloot",
    "Educated by Tara Westover",
    "Born a Crime by Trevor Noah",
    "Quiet: The Power of Introverts in a World That Can't Stop Talking by Susan Cain",
    "The Glass Castle by Jeannette Walls",
    "Bossypants by Tina Fey",
    "I Know Why the Caged Bird Sings by Maya Angelou",
    "Steve Jobs by Walter Isaacson",
    "Man's Search for Meaning by Viktor E. Frankl",
    "The Art of War by Sun Tzu",
    "The Alchemist by Paulo Coelho",
    "The Road Less Traveled by M. Scott Peck",
    "The Waste Land by T.S. Eliot",
    "Milk and Honey by Rupi Kaur",
    "Leaves of Grass by Walt Whitman",
    "Selected Poems by Langston Hughes"]
cur.execute("""create table if not exists LIBRARY
(book_id int,                                                  
book_name varchar(100))""")
for i in book:
    code = random.randint(100,999)                                 
    cur.execute("""INSERT INTO LIBRARY(book_id,book_name) VALUES (%s,%s)""",(code,i))
con.commit()

#CUSTOMER_DETAILS TABLE
cur.execute("""create table if not exists CUSTOMER_DETAILS
(name varchar(30),                                                  
phone_number int,
age int,
address varchar(50),
has_card varchar(5))""")

#BOOK_TYPES TABLE
cur.execute("""create table if not exists book_types
(classic_literature varchar(100) DEFAULT NULL,
science_fiction_and_fantasy varchar(100) DEFAULT NULL,
mystery_and_thriller varchar(100) DEFAULT NULL,
historical_fiction varchar(100) DEFAULT NULL,
non_fiction varchar(100) DEFAULT NULL,
philosophy_and_self_help varchar(100) DEFAULT NULL,
poetry varchar(100) DEFAULT NULL)""")
classic_literature = [
    "To Kill a Mockingbird by Harper Lee",
    "1984 by George Orwell",
    "Pride and Prejudice by Jane Austen",
    "The Great Gatsby by F. Scott Fitzgerald",
    "Moby-Dick by Herman Melville",
    "War and Peace by Leo Tolstoy",
    "Jane Eyre by Charlotte Brontë",
    "Wuthering Heights by Emily Brontë"]
science_fiction_and_fantasy = [
    "Dune by Frank Herbert",
    "Neuromancer by William Gibson",
    "A Game of Thrones by George R.R. Martin",
    "The Left Hand of Darkness by Ursula K. Le Guin",
    "Snow Crash by Neal Stephenson",
    "The Hitchhiker's Guide to the Galaxy by Douglas Adams",
    "Ender's Game by Orson Scott Card",
    "Good Omens by Neil Gaiman and Terry Pratchett"]
mystery_and_thriller = [
    "The Girl with the Dragon Tattoo by Stieg Larsson",
    "Gone Girl by Gillian Flynn",
    "The Da Vinci Code by Dan Brown",
    "And Then There Were None by Agatha Christie",
    "The Silence of the Lambs by Thomas Harris"]
historical_fiction = [
    "All the Light We Cannot See by Anthony Doerr",
    "The Book Thief by Markus Zusak",
    "Wolf Hall by Hilary Mantel",
    "The Nightingale by Kristin Hannah"]
non_fiction = [
    "Sapiens: A Brief History of Humankind by Yuval Noah Harari",
    "The Immortal Life of Henrietta Lacks by Rebecca Skloot",
    "Educated by Tara Westover",
    "Born a Crime by Trevor Noah",
    "Quiet: The Power of Introverts in a World That Can't Stop Talking by Susan Cain",
    "The Glass Castle by Jeannette Walls",
    "Bossypants by Tina Fey",
    "I Know Why the Caged Bird Sings by Maya Angelou",
    "Steve Jobs by Walter Isaacson",
    "Man's Search for Meaning by Viktor E. Frankl"]
philosophy_and_self_help = [
    "The Art of War by Sun Tzu",
    "The Alchemist by Paulo Coelho",
    "The Road Less Traveled by M. Scott Peck"]
poetry = [
    "The Waste Land by T.S. Eliot",
    "Milk and Honey by Rupi Kaur",
    "Leaves of Grass by Walt Whitman",
    "Selected Poems by Langston Hughes"]

max_len = 10
# MAKING EVERY LIST OF SAME LENGTH
classic_literature += [None] * (max_len-len(classic_literature))
science_fiction_and_fantasy += [None] * (max_len-len(science_fiction_and_fantasy))
mystery_and_thriller += [None] * (max_len-len(mystery_and_thriller))
historical_fiction += [None] * (max_len-len(historical_fiction))
non_fiction += [None] * (max_len-len(non_fiction))
philosophy_and_self_help += [None] * (max_len-len(philosophy_and_self_help))
poetry += [None] * (max_len-len(poetry))
for i in range(0,10):
    cur.execute("""INSERT INTO book_types VALUES (%s,%s,%s,%s,%s,%s,%s)""",(classic_literature[i],science_fiction_and_fantasy[i],mystery_and_thriller[i],historical_fiction[i],non_fiction[i],philosophy_and_self_help[i],poetry[i]))
con.commit()

#TABLE NUMBER TABLE
cur.execute("""
create table if not exists TABLE_NUMBER
(Table_num int,
status varchar(30))""")
for i in range(10):
    table_num = random.randint(100,999)
    occ = random.choice(["Occupied","Un-Occupied"])
    cur.execute("insert into TABLE_NUMBER values(%s,%s)",(table_num,occ))
    con.commit()

#ISSUED BOOKS TABLE
cur.execute("""
create table if not exists issued_books(
book_id int,
book_name varchar(100),
date_issued date)""")
con.commit()

#DONATE BOOKS TABLE
cur.execute("""create table if not exists donated_books
(book_id int,
book_name varchar(100),
person_donated varchar(40))""")
con.commit()
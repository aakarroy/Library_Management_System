import mysql.connector as c
import re
import random
import datetime

# SQL CONNECTION
con = c.connect(host='localhost',password="aakar@7906",user="root",database="aakar")
cur = con.cursor()

# POSITIVE APPRECIATION ON BOOKS 
positive_appreciations_past= [
    "What a captivating selection you made, it must had been a treat!",
    "You unearthed a literary gem with that choice!",
    "That book must had took you on an unforgettable journey!",
    "You picked a story that will lingered in your mind!",
    "You must have been enchanted by every chapter!",
    "Your reading adventure must have been thrilling with that choice!",
    "That book was a treasure trove of wisdom and delight!",
    "You chose a masterpiece that might have ignited your imagination!",
    "You embarked on a tale might stirred your soul!"]

positive_appreciations_present = [
    "What a captivating selection you made, it must be a treat!",
    "You unearth a literary gem with that choice!",
    "That book is taking you on an unforgettable journey!",
    "You pick a story that will linger in your mind!",
    "You are enchanted by every chapter!",
    "Your reading adventure is thrilling with that choice!",
    "That book is a treasure trove of wisdom and delight!",
    "You choose a masterpiece that ignites your imagination!",
    "You embark on a tale that stirs your soul!"]

poss_app_past = random.choice(positive_appreciations_past)
poss_app_pre = random.choice(positive_appreciations_present)

#GREET DECORATOR
def greet(fx):
    def mdfx(*args):
        fx(*args)
        print("Thank You For Coming....")
    return mdfx

#WELCOME FUNCTION
def welcome():
    print('''
                                Welcome to the Nexus of Knowledge, a cutting-edge sanctuary for the curious mind. 
                                Our futuristic library is designed to inspire and elevate your intellectual pursuits. 
                As you enter, you'll discover a world where advanced technology seamlessly integrates with a serene and inviting atmosphere. 
                Explore our extensive collection of books spanning all genres, from timeless classics to the latest scientific breakthroughs. 
        Our shelves are stocked with everything from gripping novels and historical accounts to comprehensive encyclopedias and innovative research. 
                    Here, your curiosity is our priority, and every corner is crafted to ignite your passion for learning. 
                                    Welcome to the future of libraries. Welcome to the Nexus of Knowledge.

''')

#TO GET TABLE NO. 
def  table_get():
    cur.execute("select Table_num from TABLE_NUMBER where occupied = 'Un-Occupied'")
    a = cur.fetchall()
    if a != []:
        b = str(random.choice(a))
        w = (re.findall(r"\d+",b)) 
        return(w[0])
    else:
        return None

#CUSTOMER DETAILS  
def customer_details():
    global has_card,phone,name,age,address
    name = input("Enter Your Name: ").title()
    phone = int(input("Enter Your Phone No.: "))
    age = int(input("Enter Your Age: "))
    address = input("Enter Your Address: ").title()
    has_card = input("Do you have already have a card? ").title()
    cur.execute("insert into CUSTOMER_DETAILS values(%s,%s,%s,%s,%s)",(name,phone,age,address,has_card))
    
    cur.execute("select name from CUSTOMER_DETAILS")
    names = cur.fetchall()
    if name in names:
        print(f"Oh,Welcome Back {name}")
    else:
        print("Hey, Welcome New Member")

#READING BOOKS   
@greet
def read(): 
    t = table_get()
    if t != None:
        a = '''
            we have various variety of books available here all most about all niches, please select a particular niche
                                                    you want to read: '''
        input(a.title())
        ch = '''
        1. Classic Literature
        2. Science Fiction & Fantasy
        3. Mystery & Thriller
        4. Historical Fiction
        5. Non-Fiction
        6. Philosophy & Self Help
        7. Poetry\n'''
        categories  = {
        1: "classic_literature",
        2: "science_fiction_and_fantasy",
        3: "mystery_and_thriller",
        4: "historical_fiction",
        5: "non_fiction",
        6: "philosophy_and_self_help",
        7: "poetry"}
        categories_name  = {
        1: "classic literature",
        2: "science fiction_and fantasy",
        3: "mystery and thriller",
        4: "historical fiction",
        5: "non fiction",
        6: "philosophy and self help",
        7: "poetry"} 
        l = []
        choice = int(input(ch.center(100)))
        if choice in [1,2,3,4,5,6,7]:
            cur.execute(f"select {categories[choice]} from book_types")
        fetched_books = list(cur.fetchall())
        print(f"YOU CHOSE: {categories_name[choice].title()}\n")
        v = 1
        for i in range(len(fetched_books)):
            a = str(fetched_books[i])
            words = re.findall("[^,^(^)]+",a)           
            for i in range(len(words)):                      
                b = words[i]
                words_final = re.findall(r"""[^'^"]+'s [^'^"]+|[^'^"]+'t [^'^"]+|[^'^"]+""",b)
                for i in range(len(words_final)):
                    
                    if words_final[i] == "None":
                        pass
                    else:
                        print(f"{v}. {words_final[i]}")
                        l.append(words_final[i]) 
            v = v+1
        
        t = input("Do you want to continue in this section: ").upper()
        if t == "YES":
            book_select = int(input("\nNow Select the no of the book you would like to read today: ").title())
            table = table_get()
    
            if book_select<=len(l):
                cur.execute("select book_id from library where book_name = %s",(l[book_select-1],))
                a = str(cur.fetchone())
                code_1 = (re.findall(r"\d+",a))
                code = int(code_1[0]) 
                print(f"\n({code}) {l[book_select-1]}, will to delivered to you an your table")
                print(f"Table No. {table} has been alloted to you. Now you can go and enjoy your reading. ")
            else:
                print("Invalid Book")
            cur.execute("update TABLE_NUMBER set occupied = 'Occupied' where Table_num = %s",(table,))
            con.commit()
        elif t == "NO":
            read()
        else:
            print("Invalid input")
    else:
        print("All the seats are currentely occupied. Please wait.")

#RETURN BOOK AFTER BORROWING
def return_book():
    q = int(input("Enter the Book Id: "))
    table = int(input("Enter the Table No. you honoured: "))
    print("OH, Okay Proceed Further..")
    cur.execute("select book_name from library where book_id = %s",(q,))
    v = str(cur.fetchone())
    v1 = re.findall(r"[^(^)^,^']+",v)
    if v1[0] != "None":
        print(f"{v1[0]}, {poss_app_past} ")
        cur.execute("update TABLE_NUMBER set occupied = 'Un-Occupied' where Table_num = %s",(table,))
        con.commit()
        
    else:
        print("Inalid Input")

#ISSUEING BOOK
@greet
def issue_book():
    date = datetime.datetime.today().date()
    a = '''
        we have various variety of books available here all most about all niches, please select a particular niche
                                                you want to read: '''
    input(a.title())
    ch = '''
    1. Classic Literature
    2. Science Fiction & Fantasy
    3. Mystery & Thriller
    4. Historical Fiction
    5. Non-Fiction
    6. Philosophy & Self Help
    7. Poetry\n'''
    categories  = {
    1: "classic_literature",
    2: "science_fiction_and_fantasy",
    3: "mystery_and_thriller",
    4: "historical_fiction",
    5: "non_fiction",
    6: "philosophy_and_self_help",
    7: "poetry"}
    categories_name  = {
    1: "classic literature",
    2: "science fiction_and fantasy",
    3: "mystery and thriller",
    4: "historical fiction",
    5: "non fiction",
    6: "philosophy and self help",
    7: "poetry"}
    l = []
    choice = int(input(ch.center(100)))
    if choice in [1,2,3,4,5,6,7]:
        cur.execute(f"select {categories[choice]} from book_types")
    fetched_books = list(cur.fetchall())
    print(f"YOU CHOSE: {categories_name[choice].title()}\n")
    v = 1
    for i in range(len(fetched_books)):
        a = str(fetched_books[i])
        words = re.findall("[^,^(^)]+",a)
        for i in range(len(words)):
            b = words[i]
            words_final = re.findall(r"""[^'^"]+'s [^'^"]+|[^'^"]+'t [^'^"]+|[^'^"]+""",b)
            for i in range(len(words_final)):
                if words_final[i] == "None":
                    pass
                else:
                    print(f"{v}. {words_final[i]}")
                    l.append(words_final[i])
                    v = v + 1
    book_select = int(input("Now Select the no of the book you would like to read today: ").title())
    cur.execute("select book_id from library where book_name = %s",(l[book_select-1],))
    a = str(cur.fetchone())
    code_1 = (re.findall(r"\d+",a))
    code = int(code_1[0]) 
    if book_select<=len(l):
        
        print(f"\n({code}) {l[book_select-1]}, {poss_app_pre}")
        print(f"According to our policy we issue books for maximum 10 days, so today is {date} thus last day of return is {date + datetime.timedelta(days=10) }")
        print("""
Your, Issueing Price is ₹299/-(inclusive of taxes) and security deposit of ₹500 which would be refunded after the successfull return of the book in desired condition.
Any damages to the book will cause you to pay extra charge of ₹199.
Late fee would be ₹50 per day.""")
        print("\n")
        customer_details()
        print(f'''\n
Your Receipt is:
Name: {name}
Phone: {phone}
Address: {address}
Amount to be paid: ₹799/- (₹500/- is refundable on return)\n
              ''')
    else:
        print("Invalid Book")
    cur.execute("insert into issued_books values(%s,%s,%s,%s)",(code,l[book_select-1],date,name))
    con.commit()

#RETURN ISSUED BOOK
@greet
def return_issued_book():
    book_issued = int(input("Enter The Book Id You want return: "))
    cur.execute("select book_name from issued_books where book_id = %s",(book_issued,))
    v = str(cur.fetchone())
    if v != "None":
        v1 = re.findall("[^,^(^)^']+",v)
        print(f"{v1[0]},{poss_app_past}")
        print("Here, you can have your ₹500/- ")
        cur.execute("delete from issued_books where book_id = %s",(book_issued,))
        con.commit()
    else:
        print("Inalid Input")

#DONATE BOOKS
@greet
def donate():
    old_books = []
    new_books = []
    customer_details()
    print("Here, we will begin by filling the names of the books along with there authors : ")
    a = (input("Enter Names Here (separated by comma): "))
    word1 = list(re.findall(r"[^,^]+| [^,^]+",a))
    cur.execute("select book_name from library")
    book = cur.fetchall()
    for i in word1:
        if i not in book: 
            new_books.append(i)
        elif i in book: 
            print(i)
            old_books.append(i)
    if old_books !=[]:
        print(f"{old_books}\nThese Books were already in the Collection thus we are obliged to Return to you")
    if new_books !=[]: 
        l = []
        cur.execute("select book_name from donated_books")
        fetched_books = cur.fetchall()
        v = 1
        for i in range(len(fetched_books)):
            a = str(fetched_books[i])
            words = re.findall("[^,^(^)]+",a)
            for i in range(len(words)):
                b = words[i]
                words_final = re.findall(r"""[^'^"]+'s [^'^"]+|[^'^"]+'t [^'^"]+|[^'^"]+""",b)
                for i in range(len(words_final)):
                    if words_final[i] == "None":
                        pass
                    else:
                        l.append(words_final[i])
                        v = v + 1
        old_donated_books = []
        for i in range(len(new_books)):
            if new_books[i] not in l:
                code = random.randint(100,999)
                cur.execute("insert into donated_books values (%s,%s,%s)",(code,new_books[i],name))
            elif new_books[i] in l:
                old_donated_books.append(new_books[i])
                
        if old_donated_books != []:
            print(f"\n{old_donated_books}\nThese Books were already in the Collection thus we are obliged to Return to you\n")
    con.commit()

#EXIT AN BREAK LOOP
@greet   
def exit():
    print("Alas, Leaving too soon...")
    a = input("Do you own a Library card: ").upper()
    if a == "NO":
        print('''            
                             _________________________________________________________________________________________________________
                            |    Our library card offers numerous features that significantly enhance the experience of our users.    |
                            |     Customers can enjoy a 10-15% discount on the entry fee every time they use their library card,      |
                            |providing excellent savings. The card also allows for effortless entry into the library, streamlining the| 
                            |  process and saving time. Additionally, it simplifies the procedure of issuing books, making borrowing  |
                            |   quick and convenient. To further add to its convenience, the card can be easily recharged online by   |  
                            |    visiting our website, ensuring uninterrupted access to all library services. This combination of     |
                            |      benefits makes our library card an invaluable tool for avid readers and library enthusiasts.       |
                            |                                                                                                         |
                            |          FOR FIRST 1000 CUSTOMERS A RECHARGE OF ₹1000 IS COMPLETELY FREE ON ISSUING THEIR FIRST         |
                            |                                           LIBRARY CARD                                                  |
                             _________________________________________________________________________________________________________
              ''')
        ch = input("Do you want to have a Library Card?: ").upper()
        if ch == "YES":
            b = int(input("Enter you Phone No.: "))
            print(f"An SMS has been Sent to {b} click on the link and buy the card for ₹399")
        else:
            print("See you soon...")
    else:
            print("See you soon...")
    

#PROGRAM'S MAIN FUNCTION
def main():     
    while True:
        welcome()
        ch = int(input("""
                                                    Welcome to The Reception of Nexus of Knowledge: A Public Library
    Please Select What You will like to do
        1. READ
        2. RETURN BOOK
        3. ISSUE BOOK 
        4. RETURN ISSUED BOOKS
        5. DONATE BOOKS
        6. EXIT\n""").title())

        if ch == 1:
            read()
        elif ch == 2:
            return_book()
        elif ch == 3:
            issue_book()
        elif ch == 4:
            return_issued_book()
        elif ch == 5:
            donate()
        elif ch == 6:
            exit()
            break
        
main()
# Task 1: Create a New SQLite Database
import sqlite3 

with sqlite3.connect("../db/magazines.db") as conn:
    print("Database created and connected successfully.")
    
     # Task 3: Populate Tables with Data
    conn.execute("PRAGMA foreign_keys = 1")

    # Task 2: Define Database Structure
    cursor = conn.cursor()
    
    # Create publishers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        );
        """)
    
    # Create magazines table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Magazines(
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
        );
        """)
    
    # Create subscribers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        );
        """)
    
    # Create subscriptions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscriptions(
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id)
        );
        """)
    
    print("Tables created successfully.")
    
    # Functions to insert data to the tables.
    def add_publisher(cursor, name):
        try:
            cursor.execute("INSERT INTO Publishers (name) VALUES (?)", (name,))
        except sqlite3.IntegrityError:
            print(f"Publisher '{name}' already exists.")
    
    def add_magazine(cursor, name, publisher_name):
        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
        row = cursor.fetchone()
        if not row:
            print(f"Cannot add magazine '{name}': publisher '{publisher_name}' not found.")
            return
        
        publisher_id = row[0]
            
        try:
            cursor.execute("INSERT INTO Magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        except sqlite3.IntegrityError:
            print(f"Magazine '{name}' already exists.")
        
    def add_subscribers(cursor, name, address):
        try:
            cursor.execute("INSERT INTO Subscribers (name, address) VALUES (?, ?)", (name, address))
        except sqlite3.IntegrityError:
            print(f"Subscriber '{name}' and address at '{address}' already exists.")
            
    def add_subscriptions(cursor, subscriber_name, subscriber_address, magazine_name, expiration_date):
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", 
                       (subscriber_name, subscriber_address))
        subscribe = cursor.fetchone()
        if not subscribe:
            print(f"Cannot found subscriber '{subscriber_name}' at the address '{subscriber_address}'. ")
            return
        subscriber_id = subscribe[0]
        
        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
        magazine = cursor.fetchone()
        if not magazine:
            print(f"Cannot found magazine '{magazine_name}'.")
            return
        magazine_id = magazine[0]
        
        try:
            cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
            (subscriber_id, magazine_id, expiration_date)
            )
        except sqlite3.IntegrityError:
            print(f"Subscription of '{subscriber_name}' for magazine '{magazine_name}' already exists.")
            
    add_publisher(cursor, "Time")
    add_publisher(cursor, "National Geographic")
    add_publisher(cursor, "Bloomberg Press")
    
    add_magazine(cursor, "Time", "Time")
    add_magazine(cursor, "National Geographic Traveler", "National Geographic")
    add_magazine(cursor, "Bloomberg Businessweek", "Bloomberg Press")
    
    add_subscribers(cursor, "Alice Smith", "123 Maple St, Springfield")
    add_subscribers(cursor, "Bob Jones",  "456 Oak Ave, Metropolis")
    add_subscribers(cursor, "Carol Lee",  "789 Pine Rd, Smallville")
    
    add_subscriptions(cursor, "Alice Smith", "123 Maple St, Springfield", "Time", "2025-12-31")
    add_subscriptions(cursor, "Bob Jones", "456 Oak Ave, Metropolis", "National Geographic Traveler", "2025-06-30")
    add_subscriptions(cursor, "Carol Lee", "789 Pine Rd, Smallville",  "Bloomberg Businessweek", "2026-01-15")
    
    conn.commit()
    print("Data inserted successfully.")
    
    # Task 4: Write SQL Queries
    
    # Write a query to retrieve all information from the subscribers table.
    print("\nAll subscribers: \n")
    cursor.execute("SELECT * FROM Subscribers")
    result = cursor.fetchall()
    for row in result:
        print(row)
        
    # Write a query to retrieve all magazines sorted by name.
    print("\nAll magazines: \n")
    cursor.execute("SELECT * FROM Magazines")
    result = cursor.fetchall()
    for row in result:
        print(row)
        
    # Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN.
    publisher = "Time"
    sql = """
        SELECT m.magazine_id, m.name, p.name FROM Magazines m
            JOIN Publishers p ON m.publisher_id = p.publisher_id
            WHERE p.name = ?;
    """
    cursor.execute(sql, (publisher,))
    result = cursor.fetchall()
    for row in result:
        print("Magazines for Time: \n", row)
        
   
    
        
    
import sqlite3

def create_database():
    # Connect to SQLite database (it will create the database if it doesn't exist)
    conn = sqlite3.connect('countries.db')
    
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    
    # SQL query to create the 'Countries' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            country_name TEXT NOT NULL, 
            area INTEGER NOT NULL, 
            population INTEGER NOT NULL
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    print("Database and table created successfully.")
    
    conn.close()

if __name__ == '__main__':
    create_database()

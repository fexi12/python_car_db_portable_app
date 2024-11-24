import sqlite3

def create_connection():
    # Create and return a database connection
    conn = sqlite3.connect('database.db')
    return conn

def create_table():
    # Create a connection to the database
    conn = create_connection()
    cursor = conn.cursor()

    # Create the 'vehicles' table if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vehicles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT,
        modelo TEXT,
        CC TEXT,
        cor TEXT,
        matricula TEXT,
        ano INTEGER,
        num_lugares TEXT,
        local_garagem TEXT,
        estado_geral TEXT,
        photo TEXT  -- No need for NULL here; it's the default behavior
    );
    ''')

    # Create the 'vehicle_photos' table if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vehicle_photos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vehicle_id INTEGER,
        photo TEXT,
        FOREIGN KEY(vehicle_id) REFERENCES vehicles(id) ON DELETE CASCADE
    );
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Database, vehicles table, and vehicle_photos table successfully!")

# Call create_table to create the tables if they don't exist
create_table()

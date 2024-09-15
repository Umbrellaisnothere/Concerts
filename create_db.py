import sqlite3

# Connect to the SQLite database *(or create it if it doesn't exist)*
conn = sqlite3.connect('concerts.db')
cursor = conn.cursor()

# Creates bands table
cursor.execute('''
CREATE TABLE IF NOT EXISTS bands (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    hometown TEXT NOT NULL
);
''')

# Creates venues table
cursor.execute('''
CREATE TABLE IF NOT EXISTS venues (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    city TEXT NOT NULL
);
''')

# Creates concerts table
cursor.execute('''
CREATE TABLE IF NOT EXISTS concerts (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    band_id INTEGER NOT NULL,
    venue_id INTEGER NOT NULL,
    FOREIGN KEY (band_id) REFERENCES bands(id),
    FOREIGN KEY (venue_id) REFERENCES venues(id)
);
''')

conn.commit()
conn.close()

print("The database and tables is created successfully!")

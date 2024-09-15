# Concerts System

- This is a simple concert management system using Python and SQLite. 

- It allows you to manage bands, venues, and concerts, and includes functionalities like retrieving data, performing queries on concerts, and more.

## Features

- Creates bands, venues, and concerts.

- Query concerts by venue or band.

- Checks if a concert is a band's hometown show.

- Introduces a band at a concert.

- Find the band with the most performances or the most frequent band at a venue.

- Add concerts to the database.

## Requirements

- Python 3.12 or above
- SQLite3

## Setup

1. **Clone the repository**:

git clone
   ```bash
    git@github.com:Umbrellaisnothere/Concerts.git
   ```

2. **Set up the virtual environment (this is optional but I recommend it)**:

```bash
pipenv install
```

3. **Navigate to the project directory**:


```bash
cd concert.py
```

4. **Install dependencies**: 

- There are no external dependencies, but ensure you have SQLite3 installed and configured.

5. **Create the database and tables**: 

- The project uses SQLite3 to store information about bands, venues, and concerts. To set up the database, simply run the script that creates the necessary tables.

```bash
python create_tables.py
```

or

```bash
python3 create_tables.py
```

Create the `concerts.db` database file with the following tables:

- bands
- venues
- concerts

## Usage

**Database Queries**

- You can run SQL queries using the `SQLite cursor` object, for example:

```python
cursor.execute("SELECT * FROM bands")
print(cursor.fetchall())
```

**An example**

1. **Adding Data to the Database**:

```python
# Example data

CURSOR.execute("INSERT INTO bands (name, hometown) VALUES (?, ?)", ('The Rolling Stones', 'London'))
CURSOR.execute("INSERT INTO venues (title, city) VALUES (?, ?)", ('Madison Square Garden', 'New York'))
CONN.commit()

# Add a concert
band_play_in_venue(1, 1, '2023-10-15')
```

2. **Querying the Data**:

```python
# Gets concerts at a specific venue
print(get_concerts_for_venue(1))

# Gets the most frequent band perfoming at a venue
print(most_frequent_band_at_venue(1))
```

**File Structure**

```
Concerts/
│
├── create_tables.py            # Script to create the tables in SQLite
├── concert.py       # Main Python script containing all the functions
├── __init__.py                 # An initialization file
├── README.md                   # Documentation
└── concerts.db                 # SQLite database (created after running the script)
```

**Contributing**

- All contributions are welcome! 
Please fork the repository and create a pull request for any enhancements or bug fixes.
_________

- This system was compiled to you by [Keith Murimi](https://github.com/Umbrellaisnothere). :)!!
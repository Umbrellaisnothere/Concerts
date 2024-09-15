from __init__ import CURSOR, CONN
 

    # returns the band linked with the concert
def get_band_for_concert(concert_id):
    query = "SELECT bands.* FROM bands JOIN concerts ON bands.id = concerts.band_id WHERE concerts.id = ?"
    CURSOR.execute(query, (concert_id,))
    return CURSOR.fetchone()

    # returns the venue linked to a specific concert
def get_venue_for_concert(concert_id):
    query = "SELECT venues.* FROM venues JOIN concerts ON venues.id = concerts.venue_id WHERE concerts.id = ?"
    CURSOR.execute(query, (concert_id,))
    return CURSOR.fetchone()

    # retrieves all the concerts a a specific venue
def get_concerts_for_venue(venue_id):
    query = "SELECT * FROM concerts WHERE venue_id = ?"
    CURSOR.execute(query, (venue_id,))
    return CURSOR.fetchall()

    # returns all the bands at a venue using DISTINCT(avoids duplicates)
def get_bands_for_venue(venue_id):
    query = """
    SELECT DISTINCT bands.* FROM bands
    JOIN concerts ON bands.id = concerts.band_id
    WHERE concerts.venue_id = ?
    """
    CURSOR.execute(query, (venue_id,))
    return CURSOR.fetchall()

    # returns all concerts a band has performed in
def get_concerts_for_band(band_id):
    query = "SELECT * FROM concerts WHERE band_id = ?"
    CURSOR.execute(query, (band_id,))
    return CURSOR.fetchall()

    # returns all the venues a band hs played in
def get_venues_for_band(band_id):
    query = """
    SELECT DISTINCT venues.* FROM venues
    JOIN concerts ON venues.id = concerts.venue_id
    WHERE concerts.band_id = ?
    """
    CURSOR.execute(query, (band_id,))
    return CURSOR.fetchall()

    # checks if the concert is in the band's hometown
def concert_hometown_show(concert_id):
    query = """
    SELECT CASE WHEN bands.hometown = venues.city THEN 1 ELSE 0 END
    FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    JOIN venues ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    """
    CURSOR.execute(query, (concert_id,))
    result = CURSOR.fetchone()
    return result and result[0] == 1 # returns the result if venue matches with band's hometown with a safety check


    # introduces the band for the concert
def concert_introduction(concert_id):
    query = """
    SELECT venues.city, bands.name, bands.hometown
    FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    JOIN venues ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    """
    CURSOR.execute(query, (concert_id,))
    result = CURSOR.fetchone()
    return f"Hello {result[0]}!!!!! We are {result[1]} and we're from {result[2]}"


def band_play_in_venue(band_id, venue_id, date):
    query = "INSERT INTO concerts (date, band_id, venue_id) VALUES (?, ?, ?)"
    CURSOR.execute(query, (date, band_id, venue_id))
    CONN.commit()

    # returns if the band has performed the most concerts
def band_with_most_performances():
    query = """
    SELECT bands.name FROM bands
    JOIN concerts ON bands.id = concerts.band_id
    GROUP BY bands.id
    ORDER BY COUNT(concerts.id) DESC
    LIMIT 1
    """
    CURSOR.execute(query)
    return CURSOR.fetchone()

    # returns the first concert at a venue on a specific date
    # LIMIT 1 is used to return only the first result
    # if no concert is found, it returns None
    # if multiple concerts are found, it returns the first one
def concert_on_date(venue_id, date):
    query = "SELECT * FROM concerts WHERE venue_id = ? AND date = ? LIMIT 1"
    CURSOR.execute(query, (venue_id, date))
    return CURSOR.fetchone()

    # returns the most played band at a venue
def most_frequent_band_at_venue(venue_id):
    query = """
    SELECT bands.name FROM bands
    JOIN concerts ON bands.id = concerts.band_id
    WHERE concerts.venue_id = ?
    GROUP BY bands.id
    ORDER BY COUNT(concerts.id) DESC
    LIMIT 1
    """
    CURSOR.execute(query, (venue_id,))
    return CURSOR.fetchone()
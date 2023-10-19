from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server.models import Artists, Albums, Customers, Employees, Genres, InvoiceItems, Invoices, MediaTypes, Playlists, PlaylistTrack, Tracks

# Define the database URL
DATABASE_URL = "sqlite:///../chinook.db"

# Create the engine for the database
engine = create_engine(DATABASE_URL)

# Define a session local using sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to get artists by name from the database
async def get_artists_by_name(db, artist_name):
    return db.query(Artists).filter(Artists.Name == artist_name).all()

# Function to get artists by ID from the database
async def get_artists_by_id(db, artist_id):
    return db.query(Artists).filter(Artists.ArtistId == artist_id).first()

# Function to get albums by artist ID from the database
async def get_album_by_artist_id(db, artist_id):
    return db.query(Albums).filter(Albums.ArtistId == artist_id).all()

# Function to get track names by album ID from the database
async def get_track_names_by_album_id(db, album_id):
    return db.query(Tracks).filter(Tracks.AlbumId == album_id).all()

# Function to get tracks by playlist ID from the database
async def get_track_by_playlist_id(db, playlist_id):
    return db.query(Tracks).join(PlaylistTrack).join(Playlists).filter(Playlists.PlaylistId == playlist_id).all()

# Function to get playlist by playlist ID from the database
async def get_playlist_by_playlist_id(db, playlist_id):
    return db.query(Playlists).filter(Playlists.PlaylistId == playlist_id).first()

# Function to get tracks by artist ID from the database
async def get_track_by_artist_id(db, artist_id):
    return db.query(Tracks).join(Albums).filter(Albums.ArtistId == artist_id).all()

# Function to get tracks by genre ID from the database
async def get_track_by_genre_id(db, genre_id):
    return db.query(Tracks).join(Genres).filter(Genres.GenreId == genre_id).all()

# Function to get genre by ID from the database
async def get_genre_by_id(db, genre_id):
    return db.query(Genres).filter(Genres.GenreId == genre_id).first()

# Function to get tracks by customer ID from the database
async def get_track_by_customer_id(db, customer_id):
    return db.query(Tracks).join(InvoiceItems).join(Invoices).join(Customers).filter(Customers.CustomerId == customer_id).all()

# Function to get customer by ID from the database
async def get_customer_by_id(db, customer_id):
    return db.query(Customers).filter(Customers.CustomerId == customer_id).first()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Artists, Albums, Customers, Employees, Genres, InvoiceItems, Invoices, MediaTypes, Playlists, PlaylistTrack, Tracks


DATABASE_URL = "sqlite:///../chinook.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def get_artists_by_name(db, artist_name):
    return db.query(Artists).filter(Artists.Name == artist_name).all()

async def get_artists_by_id(db, artist_id):
    return db.query(Artists).filter(Artists.ArtistId == artist_id).first()

async def get_album_by_artist_id(db, artist_id):
    return db.query(Albums).filter(Albums.ArtistId == artist_id).all()

async def get_track_names_by_album_id(db, album_id):
    return db.query(Tracks).filter(Tracks.AlbumId == album_id).all()

async def get_track_by_playlist_id(db, playlist_id):
    return db.query(Tracks).join(PlaylistTrack).join(Playlists).filter(Playlists.PlaylistId == playlist_id).all()

async def get_playlist_by_playlist_id(db, playlist_id):
    return db.query(Playlists).filter(Playlists.PlaylistId == playlist_id).first()

async def get_track_by_artist_id(db, artist_id):
    return db.query(Tracks).join(Albums).filter(Albums.ArtistId == artist_id).all()

async def get_track_by_genre_id(db, genre_id):
    return db.query(Tracks).join(Genres).filter(Genres.GenreId == genre_id).all()

async def get_genre_by_id(db, genre_id):
    return db.query(Genres).filter(Genres.GenreId == genre_id).first()

async def get_track_by_customer_id(db, customer_id):
    return db.query(Tracks).join(InvoiceItems).join(Invoices).join(Customers).filter(Customers.CustomerId == customer_id).all()

async def get_customer_by_id(db, customer_id):
    return db.query(Customers).filter(Customers.CustomerId == customer_id).first()

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Artists(Base):
    __tablename__ = 'artists'
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

class Albums(Base):
    __tablename__ = 'albums'
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('artists.ArtistId'))

class Customers(Base):
    __tablename__ = 'customers'
    CustomerId = Column(Integer, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    Company = Column(String)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)
    SupportRepId = Column(Integer, ForeignKey('employees.EmployeeId'))

class Employees(Base):
    __tablename__ = 'employees'
    EmployeeId = Column(Integer, primary_key=True)
    LastName = Column(String)
    FirstName = Column(String)
    Title = Column(String)
    ReportsTo = Column(Integer, ForeignKey('employees.EmployeeId'))
    BirthDate = Column(DateTime)
    HireDate = Column(DateTime)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)

class Genres(Base):
    __tablename__ = 'genres'
    GenreId = Column(Integer, primary_key=True)
    Name = Column(String)

class InvoiceItems(Base):
    __tablename__ = 'invoice_items'
    InvoiceLineId = Column(Integer, primary_key=True)
    InvoiceId = Column(Integer, ForeignKey('invoices.InvoiceId'))
    TrackId = Column(Integer, ForeignKey('tracks.TrackId'))
    UnitPrice = Column(Numeric)
    Quantity = Column(Integer)

class Invoices(Base):
    __tablename__ = 'invoices'
    InvoiceId = Column(Integer, primary_key=True)
    CustomerId = Column(Integer, ForeignKey('customers.CustomerId'))
    InvoiceDate = Column(DateTime)
    BillingAddress = Column(String)
    BillingCity = Column(String)
    BillingState = Column(String)
    BillingCountry = Column(String)
    BillingPostalCode = Column(String)
    Total = Column(Numeric)

class MediaTypes(Base):
    __tablename__ = 'media_types'
    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(String)

class PlaylistTrack(Base):
    __tablename__ = 'playlist_track'
    PlaylistId = Column(Integer, ForeignKey('playlists.PlaylistId'), primary_key=True)
    TrackId = Column(Integer, ForeignKey('tracks.TrackId'), primary_key=True)

class Playlists(Base):
    __tablename__ = 'playlists'
    PlaylistId = Column(Integer, primary_key=True)
    Name = Column(String)

class Tracks(Base):
    __tablename__ = 'tracks'
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('albums.AlbumId'))
    MediaTypeId = Column(Integer, ForeignKey('media_types.MediaTypeId'))
    GenreId = Column(Integer, ForeignKey('genres.GenreId'))
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Numeric)

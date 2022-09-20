from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine('postgresql://localhost:5432/chinook')
base = declarative_base()

# create a class-based model for the "Artist" table
class ArtistTable(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create a class-based model for the "Album" table
class AlbumTable(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

# create a class-based model for the "Track" table
class TrackTable(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(String)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)

# create a class-basde model for the "Album" table

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the session() subclass defined above
session = Session()

# creating the database using declarative_base_subclass
base.metadata.create_all(db)

# Query 1 - select all records from the "Artist" table
# artists = session.query(ArtistTable)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select only the "name" from the "Artist" table
# artists = session.query(ArtistTable)
# for artist in artists:
#     print(artist.Name, sep=" | ")

# Query 3 - select only the "name" from the "Artist" table
# artist = session.query(ArtistTable).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only the "name" from the "Artist" table
# artist = session.query(ArtistTable).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the "ArtistId" #51 from the "Artist" table
# artist = session.query(ArtistTable).filter_by(ArtistId="51").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the albums with "ArtistId" #51 from the "Album" table
artist = session.query(Album).filter_by(ArtistId="51")
for album in albums:
    print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")


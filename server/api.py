# Import the necessary modules
import random
from fastapi import FastAPI, Path, Depends, HTTPException
from server.database import *

# Initialize the FastAPI app
app = FastAPI()

# Define a function to get the database
def get_db():
    """
    Function to get the database connection.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint for searching artists by name
@app.get("/artist/{artist_name:path}/name")
async def search_artists_by_name(artist_name: str = Path(..., description="Artist Name"), db=Depends(get_db)):
    """
    Endpoint to search for artists by name.
    """
    # Fetch artists from the database based on the provided artist name
    artists = await get_artists_by_name(db, artist_name)
    if artists == []:
        raise HTTPException(status_code=404, detail="Artist Not Found")
    # Format the retrieved artist data and return it
    artist_data = [{"Name": artist.Name, "ArtistId": artist.ArtistId} for artist in artists]
    return artist_data

# Endpoint for retrieving albums by artist ID
@app.get("/artist/{artist_id}/albums")
async def albums_by_artist_id(artist_id: int = Path(..., description="artist ID"), db=Depends(get_db)):
    """
    Endpoint to retrieve albums by artist ID.
    """
    # Fetch albums from the database based on the provided artist ID
    albums = await get_album_by_artist_id(db, artist_id)
    if albums == []:
        raise HTTPException(status_code=404, detail="Artist Not Found")
    # Format the retrieved album data and return it
    album_data = [{"Title": album.Title} for album in albums]
    return album_data

# Endpoint for retrieving tracks by album ID
@app.get("/albums/{album_id}/tracks")
async def tracks_by_album_id(album_id: int = Path(..., description="album ID"), db=Depends(get_db)):
    """
    Endpoint to retrieve tracks by album ID.
    """
    # Fetch tracks from the database based on the provided album ID
    tracks = await get_track_names_by_album_id(db, album_id)
    if tracks == []:
        raise HTTPException(status_code=404, detail="Album Not Found")
    # Format the retrieved track data and return it
    track_data = [{"Name": (f"{track.TrackId}: {track.Name}", f"  {str(round(track.UnitPrice, 2))} £")} for track in tracks]
    return track_data

# Endpoint for shuffling tracks by album ID
@app.get("/albums/{album_id}/tracks/shuffle")
async def tracks_by_album_id_shuffle(album_id: int = Path(..., description="album ID"), db=Depends(get_db)):
    """
    Endpoint to shuffle tracks by album ID.
    """
    # Fetch tracks from the database based on the provided album ID
    tracks = await get_track_names_by_album_id(db, album_id)
    if tracks == []:
        raise HTTPException(status_code=404, detail="Album Not Found")
    # Shuffle the retrieved tracks and format the data before returning it
    random.shuffle(tracks)
    track_data = [{"Name": (f"{track.TrackId}: {track.Name}", f"  {str(round(track.UnitPrice, 2))} £")} for track in tracks]
    return track_data
# Endpoint for retrieving an artist with their albums and tracks
@app.get("/artist/{artist_id}")
async def artist_with_albums_and_tracks(artist_id: int = Path(..., description="artist ID"), db=Depends(get_db)):
    """
    Endpoint to retrieve an artist along with their albums and tracks.
    """
    # Retrieve the artist based on the provided artist ID
    artist = await get_artists_by_id(db, artist_id)
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist Not Found")
    # Prepare the data structure for the artist and their albums
    result = {}
    result["Artist"] = artist.Name
    albums = await get_album_by_artist_id(db, artist.ArtistId)
    albums_data = []
    # Retrieve tracks for each album and format the data
    for album in albums:
        album_data = {"Album": album.Title}
        tracks = await get_track_names_by_album_id(db, album.AlbumId)
        track_names = [(f"{track.TrackId}: {track.Name}", f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]
        album_data["Songs"] = track_names
        albums_data.append(album_data)
    result["Albums"] = albums_data
    return result

# Endpoint for retrieving tracks by playlist ID
@app.get("/playlist/{playlist_id}")
async def tracks_by_playlist_id(playlist_id: int = Path(..., description="playlist ID"), db=Depends(get_db)):
    """
    Endpoint to retrieve tracks by playlist ID.
    """
    # Retrieve tracks based on the provided playlist ID
    tracks = await get_track_by_playlist_id(db, playlist_id)
    playlist = await get_playlist_by_playlist_id(db, playlist_id)
    if playlist is None:
        raise HTTPException(status_code=404, detail="Playlist Not Found")
    # Format and return the playlist and its associated tracks
    return {"Playlist": f"{playlist.PlaylistId}: {playlist.Name}", "Tracks": [(f"{track.TrackId}: {track.Name}", f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]}

# Endpoint for shuffling tracks by playlist ID
@app.get("/playlist/{playlist_id}/shuffle")
async def tracks_by_playlist_id_shuffle(playlist_id: int = Path(..., description="playlist ID"), db=Depends(get_db)):
    """
    Endpoint to shuffle tracks by playlist ID.
    """
    # Retrieve tracks based on the provided playlist ID
    tracks = await get_track_by_playlist_id(db, playlist_id)
    random.shuffle(tracks)
    num_tracks_to_return = min(20, len(tracks))
    random_tracks = tracks[:num_tracks_to_return]
    playlist = await get_playlist_by_playlist_id(db, playlist_id)
    if playlist is None:
        raise HTTPException(status_code=404, detail="Playlist Not Found")
    # Format and return the shuffled playlist tracks
    return {"Playlist": f"{playlist.PlaylistId}: {playlist.Name}", "Tracks": [(f"{track.TrackId}: {track.Name}", f"  {str(round(track.UnitPrice, 2))} £") for track in random_tracks]}

# Endpoint for retrieving tracks by artist ID
@app.get("/artist/{artist_id}/tracks")
async def tracks_by_artist_id(artist_id: int = Path(..., description="artist ID"), db=Depends(get_db)):
    """
    Endpoint to retrieve tracks by artist ID.
    """
    # Retrieve tracks based on the provided artist ID
    tracks = await get_track_by_artist_id(db, artist_id)
    artist = await get_artists_by_id(db, artist_id)
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist Not Found")
    # Format and return the artist ID along with their tracks
    return {"Artist": f"{artist.ArtistId}: {artist.Name}", "Tracks": [(f"{track.TrackId}: {track.Name}", f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]}

# Endpoint for shuffling tracks by atrist ID
@app.get("/artist/{artist_id}/tracks/shuffle")
async def tracks_by_artist_id_shuffle(artist_id: int = Path(..., description="artist ID"), db=Depends(get_db)):
    """
    Endpoint to shuffle tracks by artist ID.
    """
    # Retrieve tracks based on the provided artist ID
    tracks = await get_track_by_artist_id(db, artist_id)
    random.shuffle(tracks)
    artist = await get_artists_by_id(db, artist_id)
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist Not Found")
    # Format and return the shuffled tracks associated with the artist
    return {"Artist": f"{artist.ArtistId}: {artist.Name}", "Tracks": [(f"{track.TrackId}: {track.Name}", f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]}

# Endpoint for retrieving genre by album ID
@app.get("/genre/{genre_id}/tracks")
async def tracks_by_genre_id(genre_id: int = Path(..., description="genre ID"), db=Depends(get_db)):
    """
    Endpoint to retrieve tracks by genre ID.
    """
    # Retrieve tracks based on the provided genre ID
    tracks = await get_track_by_genre_id(db, genre_id)
    genre = await get_genre_by_id(db, genre_id)
    if genre is None:
        raise HTTPException(status_code=404, detail="Genre Not Found")
    # Format and return the genre along with its associated tracks
    return {"Genre": f"{genre.GenreId}: {genre.Name}", "Tracks": [(f"{track.TrackId}: {track.Name}", f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]}

# Endpoint for shuffling tracks by genre ID
@app.get("/genre/{genre_id}/tracks/shuffle")
async def tracks_by_genre_id_shuffle(genre_id: int = Path(..., description="genre ID"), db=Depends(get_db)):
    """
    Endpoint to shuffle tracks by genre ID.
    """
    # Retrieve tracks based on the provided genre ID
    tracks = await get_track_by_genre_id(db, genre_id)
    random.shuffle(tracks)
    genre = await get_genre_by_id(db, genre_id)
    if genre is None:
        raise HTTPException(status_code=404, detail="Genre Not Found")
    # Format and return the shuffled tracks associated with the genre
    return {"Genre": f"{genre.GenreId}: {genre.Name}", "Tracks": [(f"{track.TrackId}: {track.Name}", f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]}

# Endpoint for retrieving tracks by customer ID
@app.get("/customer/{customer_id}/tracks")
async def tracks_by_customer_id(customer_id: int = Path(..., description="customer ID"), db=Depends(get_db)):
    """
    Endpoint to retrieve tracks by customer ID.
    """
    # Retrieve tracks based on the provided customer ID
    tracks = await get_track_by_customer_id(db, customer_id)
    customer = await get_customer_by_id(db, customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer Not Found")
    # Format and return the customer along with their associated tracks
    return {"Customer": [(f"{customer.CustomerId}: {customer.FirstName} {customer.LastName}")], "Tracks": [(f"{track.TrackId}: {track.Name}", f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]}

# Endpoint for shuffling tracks by customer ID
@app.get("/customer/{customer_id}/tracks/shuffle")
async def tracks_by_customer_id(customer_id: int = Path(..., description="customer ID"), db=Depends(get_db)):
    """
    Endpoint to shuffle tracks by customer ID.
    """
    # Retrieve tracks based on the provided customer ID
    tracks = await get_track_by_customer_id(db, customer_id)
    random.shuffle(tracks)
    customer = await get_customer_by_id(db, customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer Not Found")
    # Format and return the shuffled tracks associated with the customer
    return {"Customer": [(f"{customer.CustomerId}: {customer.FirstName} {customer.LastName}")], "Tracks": [(f"{track.TrackId}: {track.Name}", f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]}

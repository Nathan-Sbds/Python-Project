import random
from fastapi import FastAPI, Path,Depends
from database import *

app = FastAPI()

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/artist/{artist_name:path}/name")
async def search_artists_by_name(artist_name: str = Path(..., description="Artist Name"), db = Depends(get_db)):
    artists = await get_artists_by_name(db, artist_name)
    if artists == []:
        return "Artist Not Found"
    artist_data = [{"Name": artist.Name, "ArtistId": artist.ArtistId} for artist in artists]
    return artist_data
    
@app.get("/artist/{artist_id}/albums")
async def albums_by_artist_id(artist_id: int = Path(..., description="artist ID"),db = Depends(get_db)):
    albums = await get_album_by_artist_id(db, artist_id)
    print(albums)
    if albums == []:
        return "Artist Not Found"
    album_data = [{"Title": album.Title} for album in albums]
    return album_data

@app.get("/albums/{album_id}/tracks")
async def tracks_by_album_id(album_id: int = Path(..., description="album ID"),db = Depends(get_db)):
    tracks = await get_track_names_by_album_id(db, album_id)
    if tracks == []:
        return "Album Not Found"
    track_data = [{"Name": (f"{track.TrackId}: {track.Name}",f"  {str(round(track.UnitPrice, 2))} £")} for track in tracks]
    return track_data


@app.get("/albums/{album_id}/tracks/shuffle")
async def tracks_by_album_id(album_id: int = Path(..., description="album ID"),db = Depends(get_db)):
    tracks = await get_track_names_by_album_id(db, album_id)
    if tracks == []:
        return "Album Not Found"
    random.shuffle(tracks)
    track_data = [{"Name": (f"{track.TrackId}: {track.Name}",f"  {str(round(track.UnitPrice, 2))} £")} for track in tracks]
    return track_data


@app.get("/artist/{artist_id}")
async def artist_with_albums_and_tracks(artist_id: int = Path(..., description="artist ID"),db = Depends(get_db)):
    artist = await get_artists_by_id(db, artist_id)
    if artist == None:
        return "Artist Not Found"
    result = {}

    result["Artist"] = artist.Name
    albums = await get_album_by_artist_id(db, artist.ArtistId)
    albums_data = []

    for album in albums:
        album_data = {"Album": album.Title}
        tracks = await get_track_names_by_album_id(db, album.AlbumId)
        track_names = [(f"{track.TrackId}: {track.Name}",f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]
        album_data["Songs"] = track_names
        albums_data.append(album_data)

    result["Albums"] = albums_data
    return result

@app.get("/playlist/{playlist_id}")
async def tracks_by_playlist_id(playlist_id: int = Path(..., description="playlist ID"),db = Depends(get_db)):
    tracks = await get_track_by_playlist_id(db, playlist_id)
    playlist = await get_playlist_by_playlist_id(db, playlist_id)
    if playlist == None:
        return "Playlist Not Found"
    return {"Playlist": f"{playlist.PlaylistId}: {playlist.Name}", "Tracks": [(f"{track.TrackId}: {track.Name}",f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]}

@app.get("/playlist/{playlist_id}/shuffle")
async def tracks_by_playlist_id_shuffle(playlist_id: int = Path(..., description="playlist ID"),db = Depends(get_db)):
    tracks = await get_track_by_playlist_id(db, playlist_id)
    random.shuffle(tracks)
    num_tracks_to_return = min(20, len(tracks))
    random_tracks = tracks[:num_tracks_to_return]
    playlist = await get_playlist_by_playlist_id(db, playlist_id)
    if playlist == None:
        return "Playlist Not Found"
    return {"Playlist": f"{playlist.PlaylistId}: {playlist.Name}", "Tracks": [(f"{track.TrackId}: {track.Name}",f"  {str(round(track.UnitPrice, 2))} £") for track in random_tracks]}


@app.get("/artist/{artist_id}/tracks")
async def tracks_by_artist_id(artist_id: int = Path(..., description="artist ID"),db = Depends(get_db)):
    tracks = await get_track_by_artist_id(db, artist_id)
    artist = await get_artists_by_id(db, artist_id)
    if artist == None:
        return "Artist Not Found"
    return {"Artist": f"{artist.ArtistId}: {artist.Name}", "Tracks": [(f"{track.TrackId}: {track.Name}",f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]}


@app.get("/artist/{artist_id}/tracks/shuffle")
async def tracks_by_artist_id_shuffle(artist_id: int = Path(..., description="artist ID"),db = Depends(get_db)):
    tracks = await get_track_by_artist_id(db, artist_id)
    random.shuffle(tracks)
    artist = await get_artists_by_id(db, artist_id)
    if artist == None:
        return "Artist Not Found"
    return {"Artist": f"{artist.ArtistId}: {artist.Name}", "Tracks": [(f"{track.TrackId}: {track.Name}",f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]}


@app.get("/genre/{genre_id}/tracks")
async def tracks_by_genre_id(genre_id: int = Path(..., description="genre ID"),db = Depends(get_db)):
    tracks = await get_track_by_genre_id(db, genre_id)
    genre = await get_genre_by_id(db, genre_id)
    if genre == None:
        return "Genre Not Found"
    return {"Genre": f"{genre.GenreId}: {genre.Name}", "Tracks": [(f"{track.TrackId}: {track.Name}",f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]}


@app.get("/genre/{genre_id}/tracks/shuffle")
async def tracks_by_genre_id_shuffle(genre_id: int = Path(..., description="genre ID"),db = Depends(get_db)):
    tracks = await get_track_by_genre_id(db, genre_id)
    random.shuffle(tracks)
    genre = await get_genre_by_id(db, genre_id)
    if genre == None:
        return "Genre Not Found"
    return {"Genre": f"{genre.GenreId}: {genre.Name}", "Tracks": [(f"{track.TrackId}: {track.Name}",f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]}


@app.get("/customer/{customer_id}/tracks")
async def tracks_by_customer_id(customer_id: int = Path(..., description="customer ID"),db = Depends(get_db)):
    tracks = await get_track_by_customer_id(db, customer_id)
    customer = await get_customer_by_id(db, customer_id)
    if customer == None:
        return "Customer Not Found"
    return {"Customer": [(f"{customer.CustomerId}: {customer.FirstName} {customer.LastName}")], "Tracks": [(f"{track.TrackId}: {track.Name}",f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]}


@app.get("/customer/{customer_id}/tracks/shuffle")
async def tracks_by_customer_id(customer_id: int = Path(..., description="customer ID"),db = Depends(get_db)):
    tracks = await get_track_by_customer_id(db, customer_id)
    random.shuffle(tracks)
    customer = await get_customer_by_id(db, customer_id)
    if customer == None:
        return "Customer Not Found"
    return {"Customer": [(f"{customer.CustomerId}: {customer.FirstName} {customer.LastName}")], "Tracks": [(f"{track.TrackId}: {track.Name}",f"  {str(round(track.UnitPrice, 2))} £") for track in tracks]}
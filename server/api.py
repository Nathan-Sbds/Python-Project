import random
from fastapi import FastAPI, Path, Query
from database import SessionLocal, get_artists_by_name, get_album_by_artist_id, get_track_names_by_album_id,get_artists_by_id,get_track_by_playlist_id,get_playlist_by_playlist_id,get_track_by_artist_id

app = FastAPI()

@app.get("/artist/{artist_name:path}/name")
async def search_artists_by_name(artist_name: str = Path(..., description="Artist Name")):
    db = SessionLocal()
    artists = await get_artists_by_name(db, artist_name)
    db.close()
    artist_data = [{"Name": artist.Name, "ArtistId": artist.ArtistId} for artist in artists]
    return artist_data

@app.get("/artist/{artist_id}/albums")
async def get_albums_by_artist_id(artist_id: int = Path(..., description="artist ID")):
    db = SessionLocal()
    album = await get_album_by_artist_id(db, artist_id)
    db.close()
    album_data = [{"Title": album.Title} for album in album.Name]
    return album_data

@app.get("/albums/{album_id}/tracks")
async def get_tracks_by_album_id(album_id: int = Path(..., description="album ID")):
    db = SessionLocal()
    track_names = await get_track_names_by_album_id(db, album_id)
    db.close()
    track_data = [{"Name": (track.Name, track.TrackId)      } for track in track_names]
    return track_data


@app.get("/albums/{album_id}/tracks/shuffle")
async def get_tracks_by_album_id(album_id: int = Path(..., description="album ID")):
    db = SessionLocal()
    track_names = await get_track_names_by_album_id(db, album_id)
    db.close()
    random.shuffle(track_names)
    track_data = [{"Name": (track.Name, track.TrackId)} for track in track_names]
    return track_data


@app.get("/artist/{artist_id}")
async def get_artist_with_albums_and_tracks(artist_id: int = Path(..., description="artist ID")):
    db = SessionLocal()
    artists = await get_artists_by_id(db, artist_id)
    result = {}

    for artist in artists:
        result["Artist"] = artist.Name
        albums = await get_album_by_artist_id(db, artist.ArtistId)
        albums_data = []

        for album in albums:
            album_data = {"Album": album.Title}
            tracks = await get_track_names_by_album_id(db, album.AlbumId)
            track_names = [(track.Name, track.TrackId) for track in tracks]
            album_data["Songs"] = track_names
            albums_data.append(album_data)

        result["Albums"] = albums_data
    db.close()
    return result

@app.get("/playlist/{playlist_id}")
async def get_tracks_by_playlist_name(playlist_id: int = Path(..., description="playlist ID")):
    db = SessionLocal()
    tracks = await get_track_by_playlist_id(db, playlist_id)
    db.close()
    return {"Playlist": await get_playlist_by_playlist_id(db, playlist_id), "Tracks": [(track.Name, track.TrackId) for track in tracks]}

@app.get("/playlist/{playlist_id}/shuffle")
async def get_tracks_by_playlist_name_shuffle(playlist_id: int = Path(..., description="playlist ID")):
    db = SessionLocal()
    tracks = await get_track_by_playlist_id(db, playlist_id)
    db.close()
    random.shuffle(tracks)
    num_tracks_to_return = min(20, len(tracks))
    random_tracks = tracks[:num_tracks_to_return]
    return {"Playlist": await get_playlist_by_playlist_id(db, playlist_id), "Tracks": [(track.Name, track.TrackId) for track in random_tracks]}


@app.get("/artist/{artist_id}/tracks")
async def get_tracks_by_playlist_name(artist_id: int = Path(..., description="artist ID")):
    db = SessionLocal()
    tracks = await get_track_by_artist_id(db, artist_id)
    db.close()
    return {"Artist": await get_artists_by_id(db, artist_id), "Tracks": [(track.Name, track.TrackId) for track in tracks]}


@app.get("/artist/{artist_id}/tracks/shuffle")
async def get_tracks_by_playlist_name(artist_id: int = Path(..., description="artist ID")):
    db = SessionLocal()
    tracks = await get_track_by_artist_id(db, artist_id)
    db.close()
    random.shuffle(tracks)
    return {"Artist": await get_artists_by_id(db, artist_id), "Tracks": [(track.Name, track.TrackId) for track in tracks]}
import pytest
from fastapi.testclient import TestClient
from server.api import app

# Create a TestClient instance
client = TestClient(app)

# Test cases for searching artists by name
def test_search_artists_by_name():
    response = client.get("/artist/AC/DC/name")
    assert response.status_code == 200

# Test case for searching artists by invalid name
def test_search_artists_by_name_invalid():
    response = client.get("/artist/invalid_name/name")
    assert response.status_code == 404

# Test cases for retrieving albums by artist ID
def test_albums_by_artist_id():
    response = client.get("/artist/1/albums")
    assert response.status_code == 200

# Test case for retrieving albums by invalid artist ID
def test_albums_by_artist_id_invalid():
    response = client.get("/artist/1000/albums")
    assert response.status_code == 404

# Test cases for retrieving tracks by album ID
def test_tracks_by_album_id():
    response = client.get("/albums/1/tracks")
    assert response.status_code == 200

# Test case for retrieving tracks by invalid album ID
def test_tracks_by_album_id_invalid():
    response = client.get("/albums/1000/tracks")
    assert response.status_code == 404

# Test cases for shuffling tracks by album ID
def test_tracks_by_album_id_shuffle():
    response = client.get("/albums/1/tracks/shuffle")
    assert response.status_code == 200

# Test case for retrieving an artist with their albums and tracks
def test_artist_with_albums_and_tracks():
    response = client.get("/artist/1")
    assert response.status_code == 200

# Test case for retrieving an artist with invalid artist ID
def test_artist_with_albums_and_tracks_invalid():
    response = client.get("/artist/1000")
    assert response.status_code == 404

# Test case for retrieving tracks by playlist ID
def test_tracks_by_playlist_id():
    response = client.get("/playlist/1")
    assert response.status_code == 200

# Test case for retrieving tracks by invalid playlist ID
def test_tracks_by_playlist_id_invalid():
    response = client.get("/playlist/1000")
    assert response.status_code == 404

# Test case for shuffling tracks by playlist ID
def test_tracks_by_playlist_id_shuffle():
    response = client.get("/playlist/1/shuffle")
    assert response.status_code == 200

# Test case for retrieving tracks by artist ID
def test_tracks_by_artist_id():
    response = client.get("/artist/1/tracks")
    assert response.status_code == 200

# Test case for retrieving tracks by invalid artist ID
def test_tracks_by_artist_id_invalid():
    response = client.get("/artist/1000/tracks")
    assert response.status_code == 404

# Test case for shuffling tracks by artist ID
def test_tracks_by_artist_id_shuffle():
    response = client.get("/artist/1/tracks/shuffle")
    assert response.status_code == 200

# Test case for retrieving tracks by genre ID
def test_tracks_by_genre_id():
    response = client.get("/genre/1/tracks")
    assert response.status_code == 200

# Test case for retrieving tracks by invalid genre ID
def test_tracks_by_genre_id_invalid():
    response = client.get("/genre/1000/tracks")
    assert response.status_code == 404

# Test case for shuffling tracks by genre ID
def test_tracks_by_genre_id_shuffle():
    response = client.get("/genre/1/tracks/shuffle")
    assert response.status_code == 200

# Test case for retrieving tracks by customer ID
def test_tracks_by_customer_id():
    response = client.get("/customer/1/tracks")
    assert response.status_code == 200

# Test case for retrieving tracks by invalid customer ID
def test_tracks_by_customer_id_invalid():
    response = client.get("/customer/1000/tracks")
    assert response.status_code == 404

# Test case for shuffling tracks by customer ID
def test_tracks_by_customer_id_shuffle():
    response = client.get("/customer/1/tracks/shuffle")
    assert response.status_code == 200

# Music Database API

This API provides endpoints to retrieve information from a music database. It allows users to search for artists, albums, tracks, genres, playlists, and customers. The API interacts with the database using FastAPI and provides various endpoints for different types of queries.

## Endpoints

- **Search Artists by Name:** 
  - Endpoint: `/artist/{artist_name}/name`
  - Description: Search for artists by name.

- **Retrieve Albums by Artist ID:**
  - Endpoint: `/artist/{artist_id}/albums`
  - Description: Retrieve albums by artist ID.

- **Retrieve Tracks by Album ID:**
  - Endpoint: `/albums/{album_id}/tracks`
  - Description: Retrieve tracks by album ID.

- **Shuffle Tracks by Album ID:**
  - Endpoint: `/albums/{album_id}/tracks/shuffle`
  - Description: Shuffle tracks by album ID.

- **Retrieve an Artist with Their Albums and Tracks:**
  - Endpoint: `/artist/{artist_id}`
  - Description: Retrieve an artist along with their albums and tracks.

- **Retrieve Tracks by Playlist ID:**
  - Endpoint: `/playlist/{playlist_id}`
  - Description: Retrieve tracks by playlist ID.

- **Shuffle Tracks by Playlist ID:**
  - Endpoint: `/playlist/{playlist_id}/shuffle`
  - Description: Shuffle tracks by playlist ID.

- **Retrieve Tracks by Artist ID:**
  - Endpoint: `/artist/{artist_id}/tracks`
  - Description: Retrieve tracks by artist ID.

- **Shuffle Tracks by Artist ID:**
  - Endpoint: `/artist/{artist_id}/tracks/shuffle`
  - Description: Shuffle tracks by artist ID.

- **Retrieve Tracks by Genre ID:**
  - Endpoint: `/genre/{genre_id}/tracks`
  - Description: Retrieve tracks by genre ID.

- **Shuffle Tracks by Genre ID:**
  - Endpoint: `/genre/{genre_id}/tracks/shuffle`
  - Description: Shuffle tracks by genre ID.

- **Retrieve Tracks by Customer ID:**
  - Endpoint: `/customer/{customer_id}/tracks`
  - Description: Retrieve tracks by customer ID.

- **Shuffle Tracks by Customer ID:**
  - Endpoint: `/customer/{customer_id}/tracks/shuffle`
  - Description: Shuffle tracks by customer ID.

## Usage

To use the API, you can send requests to the specified endpoints to retrieve the desired information. Make sure to provide the required parameters as indicated in the documentation.

## Installation

To use this API, you need to have FastAPI and the required dependencies installed. Ensure that the database is properly set up and the necessary modules are imported. 

## Note

This API is designed for a music database and allows users to retrieve various information related to artists, albums, tracks, genres, playlists, and customers.

## License

This API is open-source and free to use.


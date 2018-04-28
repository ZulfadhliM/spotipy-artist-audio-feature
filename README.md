# Audio Features of Artists using Spotipy

Getting audio features from each song in each album of your favourite artist(s) using the Spotipy library.

## Getting Started

1. Install dependencies (Spotipy, pandas and matlplotlib)
2. Make an app on [https://developer.spotify.com](https://developer.spotify.com) and get your client ID and client secret.
3. Create a python script called `app_credentials.py` and copy and paste your client ID and client secret like so:
```
client_id = 'COPY_PASTE_YOUR_CLIENT_ID_HERE'
client_secret = 'COPY_PASTE_YOUR_CLIENT_SECRET'
```
4. Run `artist_audio_features.py` on the command line with the audio feature and artists you would like to analyse:
```
python artist_audio_features.py "energy" "The Strokes" "Radiohead" "Tame Impala"
```
Output:

![energy.png](https://github.com/ZulfadhliM/spotipy-artist-audio-feature/blob/master/images/energy.png)

## Dependencies
* [Spotipy](https://github.com/plamere/spotipy)
* pandas
* matplotlib

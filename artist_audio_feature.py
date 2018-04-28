import sys
import pandas as pd
import matplotlib.pyplot as plt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import app_credentials

def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

def get_artist_album_ids(name):
	artist = get_artist(name)
	results = sp.artist_albums(artist['id'], album_type='album', country='US')
	albums = results['items']
	album_ids = []
	for album in albums:
		album_ids.append(album['id'])

	return album_ids

def get_artist_features(name, feature='valence'):
	# features: valence (default), acousticness, danceability,
	#           energy, instrumentalness, speechiness, & tempo
	album_ids = get_artist_album_ids(name)
	features = []
	for album_id in album_ids:
		results = sp.album_tracks(album_id)
		tracks = results['items']

		for track in tracks:
			audioFeatures = sp.audio_features(track['id'])
			features.append(audioFeatures[0][feature])

	return features

def show_artists_features(artistNames, feature='valence'):
	plt.figure(figsize=(6, 4))

	if feature in ['tempo']:
		histRange = (24, 240)
	else:
		histRange = (0, 1)

	for artist in artistNames:
		features = get_artist_features(artist, feature)
		series = pd.Series(features)
		series.hist(density=True, alpha=0.7, bins = 20, range=histRange, label=artist)
	plt.ylabel('probability density')
	plt.xlabel(feature)
	plt.xlim(histRange)
	plt.legend(loc = 'upper right')
	plt.show()

if len(sys.argv) > 1:
	artists = []
	feature = sys.argv[1]
	for i in range(2, len(sys.argv)):
		artists.append(sys.argv[i])
else:
	feature = 'valence'
	artists = ['Weezer']

client_credentials_manager = SpotifyClientCredentials(client_id=app_credentials.client_id, client_secret=app_credentials.client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

show_artists_features(artists, feature=feature)

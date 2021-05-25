# from PyLyrics.functions import PyLyrics
from PyLyrics import *;
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import requests
from bs4 import BeautifulSoup
import re
import lyricsgenius as lg

# Set environment variables
os.environ['SPOTIPY_CLIENT_ID'] = 'a613312a002b4e5baa4c2efaf91d20d6'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'abd026c24af64fb294849383b2dc6ce3'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://example.com'
corpus = open("corpus.txt", "w")
genius = lg.Genius('D8JvvAIQsEfFTrpaKFQepQx2egIOJDTqtIXovRNmIerS-tPgE3A84vB717kbScDT', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)


def get_songs(n):
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope),)
    results = sp.playlist_items('37i9dQZF1DXaqCgtv7ZR3L?si=69d763c84af24554', limit=5)
    tracks = results['tracks']
    track_data = results['tracks']['items']
    song_dict = {}
    for i in range(10):
        song_dict[track_data[i]['track']['artists'][0]['name']] = track_data[i]['track']['name']
    return song_dict

def generate_links(songs):
    limit = len(songs);
    links = {}
    for artist, song in songs.items():
        # print(artist + song)
        name_split = artist.split()
        for i in range(1, len(name_split)):
            name_split[i] = name_split[i].lower()
        artist_name = '-'.join(name_split)
        song_split = song.split()
        for i in range(0, len(song_split)):
            # print(song_split[i])
            if '(' in song_split[i]:
                song_split = song_split[:i]
                break
            song_split[i] = song_split[i].lower()
        song_name = '-'.join(song_split)

        url ='https://genius.com/' + artist_name +'-'+ song_name + '-lyrics'
        # print(url)
        links[song] = url
        limit -=1
        if limit == 0:
            break
    return links

songs = get_songs(10)
links = generate_links(songs)
# for song, link in links.items():
#     print(song + ":\n" + link + '\n')

# Scrape lyrics from a Genius.com song URL
def scrape_song_lyrics(songs):
    lyrics = []
    for artist, song in songs.items():
        lyrics.append(genius.search_song(song, artist).lyrics)
    

print(genius.search_song("The Box", "Roddy Ricch").lyrics)
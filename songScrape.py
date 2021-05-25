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
corpus = open("corpus.txt", "w", encoding='utf-8')
genius = lg.Genius('D8JvvAIQsEfFTrpaKFQepQx2egIOJDTqtIXovRNmIerS-tPgE3A84vB717kbScDT', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)


def get_songs(n):
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope),)
    results = sp.playlist_items('37i9dQZF1DXaqCgtv7ZR3L?si=69d763c84af24554')
    tracks = results['tracks']
    track_data = results['tracks']['items']
    song_dict = {}
    for i in range(n):
        song_dict[track_data[i]['track']['artists'][0]['name']] = track_data[i]['track']['name']
    return song_dict



# Scrape lyrics from a Genius.com song URL
def folder_corpus(songs):
    # lyrics = []
    for artist, song in songs.items():
        for k in range(0,len(song.split())):
            if '(' in song.split()[k] or '-' in song.split()[k]:
                song = ' '.join(song.split()[:k])
                break
        with open('corpus/'+'_'.join(song.split())+".txt", "w", encoding='utf-8') as f:
            print(genius.search_song(song, artist).lyrics, file=f)
def compiled_corpus(songs):
    lyrics = []
    for artist, song in songs.items():
        for k in range(0,len(song.split())):
            if '(' in song.split()[k] or '-' in song.split()[k]:
                song = ' '.join(song.split()[:k])
                break
        lyrics.append(genius.search_song(song, artist).lyrics)
    with open('corpus.txt', "w", encoding='utf-8') as f:
        print('\n\n***************\n\n'.join(lyrics), file=f)


songs = get_songs(50)
folder_corpus(songs)
compiled_corpus(songs)

# print(genius.search_song("Gangsta's Paradise", "Coolio").lyrics)
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


def get_songs(n, playlist_id):
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    results = sp.playlist_items(playlist_id, limit=200)
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
def compiled_corpus(songs, filename):
    lyrics = []
    found  = 0
    for artist, song in songs.items():
        for k in range(0,len(song.split())):
            if '(' in song.split()[k] or '-' in song.split()[k]:
                song = ' '.join(song.split()[:k])
                break
        try:
            lyrics.append(genius.search_song(song, artist).lyrics)
            found +=1
        except AttributeError:
            print("Lyrics NOT found")
        
    with open(filename+'.txt', "w", encoding='utf-8') as f:
        print('NUMBER OF SONGS FOUND' + str(found) + "\n", file =f)
        print('\n\n***************\n\n'.join(lyrics), file=f)
        # print('\n\n'.join(lyrics), file=f)
    return found

top50_2020 = '37i9dQZF1DXaqCgtv7ZR3L?si=69d763c84af24554'


fifties = '37i9dQZF1DWSV3Tk4GO2fq?si=f8b1ed0c4b1241f0' # 150
songs = get_songs(100, fifties)
compiled_corpus(songs, '1950')

sixties = '37i9dQZF1DXaKIA8E7WcJj?si=98b03662bfd84f1d' # 150
songs = get_songs(100, sixties)
compiled_corpus(songs, '1960')

seventies = '37i9dQZF1DWTJ7xPn4vNaz?si=f690027939054ff1' # 150
songs = get_songs(100, seventies)
compiled_corpus(songs, '1970')

eighties = '37i9dQZF1DX4UtSsGT1Sbe?si=72b043fb060d413f' # 150
songs = get_songs(100, eighties)
compiled_corpus(songs, '1980')

nineties = '37i9dQZF1DXbTxeAdrVG2l?si=48292311eb264589' # 150
songs = get_songs(100, nineties)
compiled_corpus(songs, '1990')

twothousands ='37i9dQZF1DX4o1oenSJRJd?si=6465ff05a30d459d' # 150
songs = get_songs(100, twothousands)
compiled_corpus(songs, '2000')

todays_top50 = '37i9dQZF1DXcBWIGoYBM5M?si=d7e7ee5ee8bb416b'# 50
songs = get_songs(50, todays_top50)
compiled_corpus(songs, 'current50')
# folder_corpus(songs)

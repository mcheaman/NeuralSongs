# from PyLyrics.functions import PyLyrics
import spotipy
import credentials
from spotipy.oauth2 import SpotifyOAuth
import os
import lyricsgenius as lg

# Set environment variables
credentials.setEnvironment();
corpus = open("corpus.txt", "w", encoding='utf-8')
genius = lg.Genius('D8JvvAIQsEfFTrpaKFQepQx2egIOJDTqtIXovRNmIerS-tPgE3A84vB717kbScDT', skip_non_songs=True, remove_section_headers=True)
song_count = 0

def get_songs(n, playlist_id):
    scope = "user-library-read"
    tried = 0
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    results = sp.playlist_items(playlist_id)
    tracks = results['tracks']
    track_data = results['tracks']['items']
    song_dict = {}
    for i in range(n):
        tried +=1
        song_dict[track_data[i]['track']['name']] = track_data[i]['track']['artists'][0]['name']
    print('TRIED: ' + str(tried))
    print('ACTUAL: ' + str(len(song_dict)))
    return song_dict



# Scrape lyrics from a Genius.com song URL
def folder_corpus(songs):
    # lyrics = []
    for song, artist in songs.items():
        for k in range(0,len(song.split())):
            if '(' in song.split()[k] or '-' in song.split()[k]:
                song = ' '.join(song.split()[:k])
                break
        with open('corpus/'+'_'.join(song.split())+".txt", "w", encoding='utf-8') as f:
            print(genius.search_song(song, artist).lyrics, file=f)
def compiled_corpus(songs, filename):
    lyrics = []
    found  = 0
    tried = 0
    for song, artist in songs.items():
        tried+=1
        for k in range(0,len(song.split())):
            if '(' in song.split()[k] or '-' in song.split()[k]:
                song = ' '.join(song.split()[:k])
                break
        try:
            global song_count
            lyrics.append(genius.search_song(song, artist).lyrics)
            song_count += 1
        except AttributeError:
            print("Lyrics NOT found")
        except:
            with open(filename+'.txt', "w", encoding='utf-8') as f:
                print('NUMBER OF SONGS TRIED: ' + str(tried) + '\nNUMBER OF SONGS FOUND: ' + str(found) + "\n")
                print('\n\n<|endoftext|>\n\n'.join(lyrics), file=f)

        
    with open(filename+'.txt', "w", encoding='utf-8') as f:
        print('NUMBER OF SONGS TRIED: ' + str(tried) + '\nNUMBER OF SONGS FOUND: ' + str(found) + "\n")
        print('\n\n<|endoftext|>\n\n'.join(lyrics), file=f)
        # print('\n\n'.join(lyrics), file=f)
    return found


def artistFix(artist):
    split = artist.split()
    return split[2] + " " + split[0]

def titleParser():
    songs = {}
    import csv
    with open('rock.csv', newline='') as csvfile:
        song_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in song_reader:
            artist= row[1];
            if artist.find(";") != -1:
                artist = artistFix(artist)
            songs[row[0]] = artist;
    return songs
songs = titleParser();
try:
    compiled_corpus(songs, "rock")
except:
    print("Exception")

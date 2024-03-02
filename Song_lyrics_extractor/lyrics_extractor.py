# Importing necessary libraries
from tkinter import *
import tkinter.messagebox as mb
import requests

# Function to extract lyrics
def extract_lyrics():
    global artist, song
    artist_name = str(artist.get())
    song_name = str(song.get()).lower()

    try:
        # Using the api.lyrics.ovh API
        link = f'https://api.lyrics.ovh/v1/{artist_name.replace(" ", "%20")}/{song_name.replace(" ", "%20")}'
        req = requests.get(link)
        json_data = req.json()

        # Check if lyrics are present in the response
        if 'lyrics' in json_data:
            lyrics = json_data['lyrics']
            print(lyrics)
            mb.showinfo('Lyrics printed', f'The lyrics to the song have been extracted and printed on your command terminal.')
        elif 'error' in json_data:
            raise Exception(json_data['error'])
        else:
            raise Exception('Unknown error occurred')
    except Exception as e:
        mb.showerror('Error', str(e))

# Initializing the window
root = Tk()
root.title("Song Lyrics Extractor")
root.geometry("600x200")
root.resizable(0, 0)
root.config(bg='CadetBlue')

# Placing the components
Label(root, text='Song Lyrics Extractor', font=("Comic Sans MS", 16, 'bold'), bg='CadetBlue').pack(side=TOP, fill=X)

Label(root, text='Enter the song name: ', font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=50)
song = StringVar()
Entry(root, width=40, textvariable=song, font=('Times New Roman', 14)).place(x=200, y=50)

Label(root, text='Enter the artist\'s name: ', font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=100)
artist = StringVar()
Entry(root, width=40, textvariable=artist, font=('Times New Roman', 14)).place(x=200, y=100)

Button(root, text='Extract lyrics', font=("Georgia", 10), width=15, command=extract_lyrics).place(x=220, y=150)

# Finalizing the window
root.update()
root.mainloop()

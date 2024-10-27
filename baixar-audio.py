import yt_dlp
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
clear()
        
url = input('digite a url da playlist: ')
print(' ')
print('_____________________________________')

playlist_url = url

options = {
    'format': 'bestaudio/best',
    'extractaudio': True,         
    'audioformat': 'mp3',         
    'outtmpl': 'D:\\Post-x-audio\\audio\\%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(options) as ydl:
    try:
        ydl.download([playlist_url])
        print('Download da playlist completo!')
    except Exception as e:
        print(f'Erro ao baixar a playlist: {e}')
        
clear()
print('Musicas baixadas :)')

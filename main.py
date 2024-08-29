from playsound import playsound
from last_words.lyrics import lyrics

def main():
    try:
        with open('music.mp3'):
            print('Song found. Starting...')
    except FileNotFoundError:
        print("\nSong not found. Please download the song and rename it to 'music.mp3'.\n")
        exit()
    
    playsound('music.mp3', block=False)
    lyrics()


if __name__ == "__main__":
    main()
from moviepy import editor
import time

movies = ['Armin','Shadmehr','yass','yass2','Yelawolf']

start_time = time.time()

for move in movies:

    video = editor.VideoFileClip(move + '.mp4')
    video.audio.write_audiofile(move + '_music.mp3')

end_time = time.time()

print(end_time-start_time)
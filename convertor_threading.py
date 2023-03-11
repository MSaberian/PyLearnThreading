from threading import Thread
from moviepy import editor
import time

movies = ['Armin','Shadmehr','yass','yass2','Yelawolf']

start_time = time.time()

def converting(i):
    videos[i].audio.write_audiofile(movies[i] + '_music.mp3')

threads = []
videos = []
for i in range(len(movies)):

    videos.append(editor.VideoFileClip(movies[i] + '.mp4'))
    threads.append(Thread(target=converting, args=[i]))

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = time.time()

print(end_time-start_time)
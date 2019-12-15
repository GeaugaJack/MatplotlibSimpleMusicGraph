import matplotlib.pyplot as plt

#convert the song time (song time * 60) to seconds and multiply the total number of seconds by the number of song plays to get the result
#next take the result and divide it by 3600 to get the number of hours listened

song_hours = [9.61, 5.56, 7.65, 11.74, 13.14]
song_titles = ["Fire\nThe Ohio Players", "Get The Funk Out Ma Face\nThe Brothers Johnson", "Mustang Sally\nWilson Pickett", "Atomic Dog\nGeorge Clinton", "Run To You\nBryan Adams"]
y_pos = [0, 1, 2, 3, 4]

plt.xticks(y_pos, song_titles)
plt.bar(y_pos, song_hours)
plt.legend()
plt.xlabel("Song Name")
plt.ylabel("Hours Listened")
plt.title("Most Listened Songs\nBy Number of Plays")
plt.show()

number_of_songs = [83, 339, 269, 125, 139, 170]
decade_music = ["1960s", "1970s", "1980s", "1990s", "2000s", "2010s"]
ypos1 = [0, 1, 2, 3, 4, 5]
plt.xticks(ypos1, decade_music)
plt.bar(ypos1, number_of_songs)
plt.legend()
plt.xlabel("Decade")
plt.ylabel("Number of Songs")
plt.title("Number of Songs\non My iTunes by Decade")
plt.show()
S = """my.song.mp3 11b
greatSong.flac 1000b
not3.txt 5b
video.mp4 200b
game.exe 100b
mov!e.mkv 10000b"""

strList = S.rsplit("\n")

def solution(string):
	strList = string.rsplit("\n")
	music = 0
	images = 0
	movies = 0
	other = 0
	for item in strList:
		if(item.rfind("mp3") != -1 or item.rfind("aac") != -1 or item.rfind("flac") != -1 ):
			space = item.rfind(" ")
			music = music + int(item[space + 1 : len(item) - 1])
		elif(item.rfind("jpg") != -1 or item.rfind("bmp") != -1 or item.rfind("gif") != -1):
			space = item.rfind(" ")
			images = images + int(item[space + 1 : len(item) - 1])
		elif(item.rfind("mp4") != -1 or item.rfind("avi") != -1 or item.rfind("mkv") != -1):
			space = item.rfind(" ")			
			movies = movies + int(item[space + 1 : len(item) - 1])
		elif(item.rfind("7z") != -1 or item.rfind("txt") != -1 or item.rfind("zip") != -1 or item.rfind("exe") != -1):
			space = item.rfind(" ")	
			other = other + int(item[space + 1 : len(item) - 1])

	result = "music " + str(music) + "b" + "\n" + "images " + str(images) + "b" + "\n" + "movies " + str(movies) + "b" + "\n" + "other " + str(other) + "b"
	return result

print(solution(S))	

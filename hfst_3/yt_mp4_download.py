from pytube import YouTube

# Video van een timer.
url = "https://www.youtube.com/watch?v=zU9y354XAgM"

# Maak verbinding met YTB. Foutmelding als URL niet bestaat.
yt = YouTube(url)

# Wat info over de URL.
print(f"Titel: {yt.title}\nMaker: {yt.author}\nLengte: {yt.length} seconden")

# Haal alle streams (video's) van deze URL op.
# Filter ze zodat enkel MP4 bestanden van resolutie 720p overblijven. progressive combineert audio & video.
# Indien er meerdere streams overblijven, selecteer dan de eerste.
stream = yt.streams.filter(file_extension="mp4", progressive=True, resolution="720p").first()

# Download de stream naar je toestel.
stream.download()


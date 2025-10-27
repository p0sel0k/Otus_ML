from files import VideoFile, AudioFile, PhotoFile, LocalStorage, CloudStorage

if __name__ == "__main__":
    photo = PhotoFile("otus_2025.jpg", 2048, "Anton", (1920, 1080), "MY_PERSONAL_CAM")
    audio = AudioFile("song.mp3", 5000, "Anton", 180, 320)
    video = VideoFile("movie.mp4", 200000, "Anton", (3840, 2160), 60)

    cloud = CloudStorage()
    local = LocalStorage()

    # Work with photo files
    photo.open()
    photo.save("/tmp/photos")
    print(photo.get_metadata())

    # Upload to cloud
    cloud.upload(photo)

    # Convert audio
    audio.convert("wav")

    # Extract frame
    video.extract_frame(12.5)

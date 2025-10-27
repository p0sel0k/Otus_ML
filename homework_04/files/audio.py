from file import MediaFile

class AudioFile(MediaFile):
    """Represents an audio file"""

    def __init__(self, name, size, owner, duration: float, bitrate: int):
        super().__init__(name, size, owner)
        self.duration = duration
        self.bitrate = bitrate

    def open(self):
        print(f"Playing audio {self.name}")

    def save(self, path: str):
        print(f"Saving audio {self.name} to {path}")

    def delete(self):
        print(f"Deleting audio {self.name}")

    def get_metadata(self):
        return {
            "duration": self.duration,
            "bitrate": self.bitrate
        }

    def convert(self, format: str):
        """Convert audio to another format (e.g. mp3 -> wav)."""
        print(f"Converting {self.name} to {format}")
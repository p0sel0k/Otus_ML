from file import MediaFile


class VideoFile(MediaFile):
    """Represents a video file."""

    def __init__(self, name, size, owner, resolution: tuple[int, int], fps: int):
        super().__init__(name, size, owner)
        self.resolution = resolution
        self.fps = fps

    def open(self):
        print(f"Playing video {self.name}")

    def save(self, destination: str):
        print(f"Saving video {self.name} to {destination}")

    def delete(self):
        print(f"Deleting video {self.name}")

    def get_metadata(self):
        return {
            "resolution": self.resolution,
            "fps": self.fps
        }

    def extract_frame(self, time_position: float):
        """Extract a single frame at a given time position."""
        print(f"Extracting frame at {time_position}s from {self.name}")
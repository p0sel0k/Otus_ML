from abc import ABC, abstractmethod
import datetime
from typing import Optional


class MediaFile(ABC):
    """Abstract base class for any media file (photo, audio, video)."""

    def __init__(self, name: str, size: int, owner: str, created_at: Optional[datetime] = None):
        self.name = name
        self.size = size
        self.owner = owner
        self.created_at = created_at or datetime.now()

    @abstractmethod
    def open(self):
        """Open the file for reading"""
        pass

    @abstractmethod
    def save(self, path: str):
        """Save the file to directory"""
        pass

    @abstractmethod
    def delete(self):
        """Delete the file from storage."""
        pass

    @abstractmethod
    def get_metadata(self) -> dict:
        """Return metadata specific to the media type."""
        pass
    


class AudioFile(MediaFile):
    """Represents an audio file."""

    def __init__(self, name, size, owner, duration: float, bitrate: int):
        super().__init__(name, size, owner)
        self.duration = duration
        self.bitrate = bitrate

    def open(self):
        print(f"Playing audio {self.name}")

    def save(self, destination: str):
        print(f"Saving audio {self.name} to {destination}")

    def delete(self):
        print(f"Deleting audio {self.name}")

    def get_metadata(self):
        return {
            "duration": self.duration,
            "bitrate": self.bitrate
        }

    def convert(self, format_: str):
        """Convert audio to another format (e.g. mp3 -> wav)."""
        print(f"Converting {self.name} to {format_}")


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


# ===== Storage abstraction =====

class Storage(ABC):
    """Abstract base class for file storage systems."""

    @abstractmethod
    def upload(self, media_file: MediaFile):
        pass

    @abstractmethod
    def download(self, file_name: str) -> MediaFile:
        pass

    @abstractmethod
    def delete(self, file_name: str):
        pass


class LocalStorage(Storage):
    """Local file system implementation."""

    def upload(self, media_file: MediaFile):
        print(f"Uploading {media_file.name} to local storage")

    def download(self, file_name: str):
        print(f"Downloading {file_name} from local storage")

    def delete(self, file_name: str):
        print(f"Deleting {file_name} from local storage")


class CloudStorage(Storage):
    """Cloud storage (e.g., AWS S3, Google Drive)."""

    def upload(self, media_file: MediaFile):
        print(f"Uploading {media_file.name} to cloud")

    def download(self, file_name: str):
        print(f"Downloading {file_name} from cloud")

    def delete(self, file_name: str):
        print(f"Deleting {file_name} from cloud storage")
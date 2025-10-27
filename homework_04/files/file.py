from abc import ABC, abstractmethod
from datetime import datetime
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
    
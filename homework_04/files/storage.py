from abc import ABC, abstractmethod
from file import MediaFile


class Storage(ABC):
    """Base class for file storage implemetations"""

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
    """Local file system implementation"""

    def upload(self, media_file: MediaFile):
        print(f"Uploading {media_file.name} to local storage")

    def download(self, file_name: str):
        print(f"Downloading {file_name} from local storage")

    def delete(self, file_name: str):
        print(f"Deleting {file_name} from local storage")


class CloudStorage(Storage):
    """Cloud storage"""

    def upload(self, media_file: MediaFile):
        print(f"Uploading {media_file.name} to cloud")

    def download(self, file_name: str):
        print(f"Downloading {file_name} from cloud")

    def delete(self, file_name: str):
        print(f"Deleting {file_name} from cloud storage")
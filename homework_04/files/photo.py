from file import MediaFile

class PhotoFile(MediaFile):
    """Represents an image/photo file"""

    def __init__(self, name, size, owner, resolution: tuple[int, int], camera_model: str):
        super().__init__(name, size, owner)
        self.resolution = resolution
        self.camera_model = camera_model

    def open(self):
        # open image in viewer
        print(f"Opening photo {self.name}")

    def save(self, path: str):
        # save photo to destination
        print(f"Saving photo {self.name} to {path}")

    def delete(self):
        print(f"Deleting photo {self.name}")

    def get_metadata(self):
        return {
            "resolution": self.resolution,
            "camera_model": self.camera_model,
            "owner": self.owner
        }
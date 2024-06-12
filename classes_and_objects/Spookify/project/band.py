from project.song import Song
from project.album import Album
from typing import List


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album}."

    def remove_album(self, album_name) -> str:
        try:
            album = next(filter(lambda a: a == album_name, self.albums))

        except StopIteration:
            return f"Album {album_name} is not found."

        if album.published:
            return f"Album has been published. It cannot be removed."

        self.albums.remove(album_name)
        return f"Album {album_name} has been removed."

    def details(self):
        album_details = "\n".join(a.details() for a in self.albums)
        return f"Band {self.name}\n" \
               f"{album_details}"

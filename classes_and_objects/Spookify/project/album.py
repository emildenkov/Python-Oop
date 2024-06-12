from project.song import Song
from typing import Tuple


class Album:

    def __init__(self, name: str, *songs: Tuple[Song]):
        self.name = name
        self.songs = [*songs]
        self.published = False

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)

    def remove_song(self, song_name) -> str:
        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        if self.published:
            return "Cannot remove songs. Album is published."

        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self) -> str:
        self.published = True
        return f"Album {self.name} has been published."

    def details(self) -> str:
        songs_details = "\n".join(f"== {s.get_info()}" for s in self.songs)
        return f"Album {self.name}\n" \
               f"{songs_details}"


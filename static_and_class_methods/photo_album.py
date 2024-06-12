from math import ceil
from typing import List


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    LINE_SYMBOL = "-"
    NUMBER_DASHES = 11

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < self.PHOTOS_PER_PAGE:
                slot = len(self.photos[page]) + 1
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {slot}"
        return "No more free slots"

    def display(self):
        result = [
            self.LINE_SYMBOL * self.NUMBER_DASHES,
        ]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append(self.LINE_SYMBOL * self.NUMBER_DASHES)

        return "\n".join(result)
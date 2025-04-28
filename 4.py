class Song:
    label = "Universal Music Group"
    language = "English"
    def __init__(self, name:str, author: str, genre: str, year: int, time: int) -> None:
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year
        self.time = time

    def __str__(self):
        return f"'{self.name}' by {self.author}"

    def get_time(self) -> bool:
        return 6 > self.time > 2

    def get_year(self, now_year: int) -> int:
        return now_year - self.year

    def new_name(self, n_name: str) -> None:
        self.name = n_name

    def change_label(self, label: str) -> None:
        Song.label = label


song1 = Song("Enter The Sandman", "Metallica", "Heavy metal", 1991, 5)
song2 = Song("Sonne", "Rammstein", "Industrial metal", 2001, 4)

print(song1.get_time())
print(song2.author)
song2.new_name("Mutter")
song1.change_label("Vertigo")
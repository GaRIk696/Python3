class Film:
    label = "Universal Pictures"
    language = "English"

    def __init__(self, name: str, author: str, genre: str, year: int, time: int) -> None:
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year
        self.time = time

    def __str__(self):
        return f"'{self.name}' (реж. {self.author})"

    def get_time(self) -> bool:
        return 360 > self.time > 120  # 6ч > время > 2ч

    def get_year(self, now_year: int) -> int:
        return now_year - self.year

    def new_name(self, n_name: str) -> None:
        self.name = n_name

    def change_label(self, label: str) -> None:
        Film.label = label


# Примеры использования (аналогично вашему исходному коду)
film1 = Film("Первому игроку приготовиться", "Стивен Спилберг", "Фантастика", 2018, 140)
film2 = Film("Гостья из будущего", "Павел Арсенов", "Фантастика", 1985, 137)

print(film1.get_time())
print(film2.author)

film2.new_name("Гостья из будущего")
film1.change_label("Warner Bros.")

print(film1)
print(f"Студия: {Film.label}")
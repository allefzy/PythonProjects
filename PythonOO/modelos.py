class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def give_like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return f'Name: {self.name} Likes: {self.likes}'

class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration
    
    def __str__(self):
        return f'Name: {self.name} - {self.duration} min - Likes: {self.likes}'

class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'Name: {self.name} - {self.seasons} seasons - Likes: {self.likes}'


class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    def __len__(self):
        return len(self._programs)

avengers = Movie('avengers - infinity war', 2018, 160)
atlanta = Series('atlanta', 2018, 2)
scary_movie = Movie('scary movie', 1999, 100)
daredevil = Series('daredevil', 2016, 2)

avengers.give_like()
avengers.give_like()
avengers.give_like()
atlanta.give_like()
atlanta.give_like()
scary_movie.give_like()
scary_movie.give_like()
daredevil.give_like()
daredevil.give_like()

playlist_list = [atlanta, avengers, daredevil, scary_movie]
my_playlist = Playlist('weekend', playlist_list)

for program in my_playlist:
    print(program)

print(f'Size: {len(my_playlist)}')

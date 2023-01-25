# Write your solution here:

class Series:

    def __init__(self, title: str, seasons: int, genres: list):

        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = 0
        self.rate_count = 0
        self.avg = 0

    def rate(self, rating: int):

        self.ratings += rating
        self.rate_count += 1

        self.average()

    def average(self):

        self.avg = self.ratings / self.rate_count


    def __str__(self):

        genre_string = ", ".join(self.genres)

        if self.rate_count > 0:

            return f"{self.title} ({self.seasons} seasons) \ngenres: {genre_string} \n{self.rate_count} ratings, average {self.avg:.1f} points".strip()
        else:

            return f"{self.title} ({self.seasons} seasons) \ngenres: {genre_string} \nno ratings".strip()





def minimum_grade(rating: float, series_list: list):

    
    series = []

    for serie in series_list:
        
        if serie.ratings > rating:
            series.append(serie)
    

    
    return series
        


def includes_genre(genre: str, series_list: list):
        
        genres = []

        for serie in series_list:

            if genre in serie.genres:
                genres.append(serie)

        
        return genres

if __name__ == "__main__":

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)
    
    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)


class AdvancedEvent:

    def __init__(self, title, year, image, releaseDate, runtimeStr, plot, genres, ratings, boxOffice, directors, writers, stars, keywords, similars):
        self.title = title
        self.year = year
        self.image = image
        self.releaseDate = releaseDate
        self.time= runtimeStr
        self.plot = plot
        self.genres = genres
        self.ratings = ratings
        self.boxOffice = boxOffice

        self.directors = directors
        self.writers = writers
        self.stars = stars
        self.keywords = keywords
        self.similars = similars
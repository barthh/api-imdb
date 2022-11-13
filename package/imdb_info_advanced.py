from datetime import datetime

class AdvancedEvent:

    def __init__(self, title, year, image, releaseDate, time, plot, genres, ratings, directors, writers, stars, keywords, similars, errorMessage):
        self.title = title
        self.year = year
        self.image = image

        self.releaseDate = releaseDate
        if releaseDate:
            date = datetime.strptime(releaseDate, "%Y-%m-%d")
            self.releaseDateFormatted  = datetime.strftime(date, "%d %B %Y" )
        else:
            self.releaseDateFormatted = None
        self.time= time
        self.plot = plot
        self.genres = genres
        self.directors = directors
        self.writers = writers
        self.stars = stars
        self.keywords = keywords
        self.similars = similars
        self.errorMessage = errorMessage

        if ratings:
            # Keep only ratings
            ratings = { key: ratings[key] for key in ["imDb", "metacritic", "theMovieDb", "rottenTomatoes", "filmAffinity"] }
            self.ratings = ratings

            # Convert from /10 to /100 notation (to purcentage)
            ratingsPurcentage = ratings.copy()
            elements = ["imDb", "theMovieDb", "filmAffinity"] 
            for element in elements:
                if ratingsPurcentage[element]:
                    ratingsPurcentage[element] = int(float(ratingsPurcentage[element]) * 10)
            self.ratingsPurcentage = ratingsPurcentage
        else:
            self.ratings = None
            self.ratingsPurcentage = None
    
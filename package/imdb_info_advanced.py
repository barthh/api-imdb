from datetime import datetime

class AdvancedEvent:

    def __init__(self, title, year, image, releaseDate, time, plot, genres, ratings, boxOffice, directors, writers, stars, keywords, similars, errorMessage):
        self.title = title
        self.year = year
        self.image = image

        self.releaseDate = releaseDate
        date = datetime.strptime(releaseDate, "%Y-%m-%d")
        self.releaseDateFormatted  = datetime.strftime(date, "%d %B %Y" )
        
        self.time= time
        self.plot = plot
        self.genres = genres
        self.boxOffice = boxOffice
        self.directors = directors
        self.writers = writers
        self.stars = stars
        self.keywords = keywords
        self.similars = similars
        self.errorMessage = errorMessage

        # Keep only ratings
        ratings = { key: ratings[key] for key in ["imDb", "metacritic", "theMovieDb", "rottenTomatoes", "filmAffinity"] }
        self.ratings = ratings

        # Convert /10 to /100 notation (for purcentage)
        ratingsPurcentage = ratings.copy()
        elements = ["imDb", "theMovieDb", "filmAffinity"] 
        for element in elements:
            if ratingsPurcentage[element]:
                ratingsPurcentage[element] = int(float(ratingsPurcentage[element]) * 10)
        self.ratingsPurcentage = ratingsPurcentage
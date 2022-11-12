class RatingsEvent:

    def __init__(self, title, fullTitle, rating, errorMessage):
        self.title = title
        self.fullTitle = fullTitle
        self.rating = rating
        self.errorMessage = errorMessage